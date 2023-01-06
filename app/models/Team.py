from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class TeamBase(SQLModel):
    players: Optional[List['Player']] = Relationship(back_populates='team')


class TeamRead(TeamBase):
    name: str


class TeamCreate(TeamBase):
    ...


class Team(TeamBase, table=True):
    name: str = Field(primary_key=True)