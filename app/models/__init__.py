from typing import Optional
from sqlmodel import SQLModel, Field


class PlayerBase(SQLModel):
    name: str = Field(index=True)
    age: Optional[int] = Field(default=None, index=True)


class PlayerCreate(PlayerBase):
    ...


class PlayerRead(PlayerBase):
    id: int


class Player(PlayerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

