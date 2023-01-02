from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Player, PlayerCreate, PlayerRead

router = APIRouter()


@router.post('/players/', response_model=PlayerRead)
async def create_player(player: PlayerCreate, session: AsyncSession = Depends(get_session)):
    player = Player.from_orm(player)
    session.add(player)
    await session.commit()
    await session.refresh(player)
    return player

# async def create_player(player: PlayerCreate):
#     with Session(engine) as session:
#         db_player = await Player.from_orm(player)
#         session.add(db_player)
#         session.commit()
#         session.refresh(db_player)
#         return db_player


@router.get('/players/', response_model=List[PlayerRead])
async def get_players(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Player))
    players: List[Player] = result.scalars().all()
    return players

# async def read_heroes() -> List[PlayerRead]:
#     with Session(engine) as session:
#         players = await session.exec(select(Player)).all()
#         return players


@router.get('/players/{player_id}', response_model=PlayerRead)
async def get_player(player_id: int, session: AsyncSession = Depends(get_session)):
    player = await session.get(Player, player_id)
    if not player:
        raise HTTPException(status_code=404, detail='Player not found')
    return player

# async def read_player(player_id: int):
#     with Session(engine) as session:
#         player = await session.get(Player, player_id)
#         if not player:
#             raise HTTPException(status_code=404, detail="Player not found")
#         return player
