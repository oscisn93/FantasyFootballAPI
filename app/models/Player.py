from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from models.Team import Team


class PlayerBase(SQLModel):
    name: str
    position: str
    team_name: Optional[str] = Field(default=None, foreign_key='team.name')
    team: Optional['Team'] = Relationship(back_populates='players')
    kicking: Optional[List['Kicking']] = Relationship(back_populates='player')
    receiving: Optional[List['Receiving']] = Relationship(back_populates='player')
    rushing: Optional[List['Rushing']] = Relationship(back_populates='player')
    passing: Optional[List['Passing']] = Relationship(back_populates='player')


class PlayerRead(PlayerBase):
    id: int


class PlayerCreate(PlayerBase):
    ...


class Player(PlayerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
