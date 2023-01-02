from typing import Optional
from sqlmodel import SQLModel, Field


class KickerBase(SQLModel):
    name: str = Field(index=True)
    team: str = Field(index=True)
    position: str = Field(index=True)
    xpm: int = Field(index=True)
    xpa: int = Field(index=True)
    fgm: int = Field(index=True)
    fga: int = Field(index=True)

class KickerRead(KickerBase):
    id: int


class KickerCreate(KickerBase):
    ...


class Kicker(KickerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
