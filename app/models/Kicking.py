from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class KickingBase(SQLModel):
    week: int
    xpm: int
    xpa: int
    fgm: int
    fga: int
    player_id: Optional[int] = Field(default=None, foreign_key='player.id')
    player: Optional['Player'] = Relationship(back_populates='kicking')


class KickingRead(KickingBase):
    id: int


class KickingCreate(KickingBase):
    ...


class Kicking(KickingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
