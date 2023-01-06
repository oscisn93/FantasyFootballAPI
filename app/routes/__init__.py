from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models.Kicking import Kicking
from models.Player import Player
from models.Passing import Passing
from models.Receiving import Receiving
from models.Rushing import Rushing

router = APIRouter()


# @router.post('/players/', response_model=PlayerRead)
# async def create_player(player: PlayerCreate, session: AsyncSession = Depends(get_session)):
#     player = Player.from_orm(player)
#     session.add(player)
#     await session.commit()
#     await session.refresh(player)
#     return player

# @router.post('/kickers/', response_model=KickerRead)
# async def create_kicker(kicker: KickerCreate, session: AsyncSession = Depends(get_session)):
#     player = Kicker.from_orm(kicker)
#     session.add(player)
#     await session.commit()
#     await session.refresh(player)
#     return player

@router.get('/players/', response_model=List[Player])
async def get_players(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Player))
    players: List[Player] = result.scalars().all()
    return players


@router.get('/kickers/', response_model=List[Kicking])
async def get_players(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Kicking))
    players: List[Kicking] = result.scalars().all()
    return players

# @router.get('/players/{player_id}', response_model=PlayerRead)
# async def get_player(player_id: int, session: AsyncSession = Depends(get_session)):
#     player = await session.get(Player, player_id)
#     if not player:
#         raise HTTPException(status_code=404, detail='Player not found')
#     return player

# @router.get('/kickers/{kicker_id}', response_model=KickerRead)
# async def get_player(kicker_id: int, session: AsyncSession = Depends(get_session)):
#     player = await session.get(Kicker, kicker_id)
#     if not player:
#         raise HTTPException(status_code=404, detail='Player not found')
#     return player

