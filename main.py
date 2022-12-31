""" Main Module for fastapi application """
import uvicorn
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

# base model
class PlayerBase(SQLModel):
    name: str = Field(index=True)
    age: Optional[int] = Field(default=None, index=True)

#  data models
class PlayerCreate(PlayerBase):
    ...


class PlayerRead(PlayerBase):
    id: int

#  table model
class Player(PlayerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# mysql_uri = "mysql+mysqlconnector://root:yzuiKJCjVGYzWsTrHnmb@containers-us-west-47.railway.app:6875/railway"
sqlite_uri = 'sqlite:///database.sqlite'
engine = create_engine(url=sqlite_uri, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event('startup')
def on_startup():
    create_db_and_tables()


@app.post('/players/', response_model=PlayerRead)
async def create_player(player: PlayerCreate):
    with Session(engine) as session:
        db_player = Player.from_orm(player)
        session.add(db_player)
        session.commit()
        session.refresh(db_player)
        return db_player


@app.get('/players/', response_model=List[PlayerRead])
async def read_heroes() -> List[PlayerRead]:
    with Session(engine) as session:
        players = session.exec(select(Player)).all()
        return players


@app.get('/players/{player_id}', response_model=PlayerRead)
async def read_player(player_id: int):
    with Session(engine) as session:
        player = session.get(Player, player_id)
        if not player:
            raise HTTPException(status_code=404, detail="Player not found")
        return player


if __name__ == '__main__':
    uvicorn.run(app)
