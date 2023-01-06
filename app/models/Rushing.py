from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class RushingBase(SQLModel):
    week: int
    rush_att: int
    rush_yds: int
    rush_td: int
    rush_long: int
    fumbles: int
    fumbles_lost: int
    player_id: Optional[int] = Field(default=None, foreign_key='player.id')
    player: Optional['Player'] = Relationship(back_populates='rushing')


class RushingRead(RushingBase):
    id: int


class RushingCreate(RushingBase):
    ...

class Rushing(RushingBase, table=True):
    id: int = Field(primary_key=True)
