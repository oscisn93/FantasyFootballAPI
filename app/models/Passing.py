from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class PassingBase(SQLModel):
    week: int
    pass_cmp: int
    pass_att: int
    pass_yds: int
    pass_td: int
    pass_int: int
    pass_sacked: int
    pass_sacked_yds: int
    pass_long: int
    pass_rating: float
    player_id: Optional[int] = Field(default=None, foreign_key='player.id')
    player: Optional['Player'] = Relationship(back_populates='passing')


class PassingRead(PassingBase):
    id: int


class PassingCreate(PassingBase):
    ...


class Passing(PassingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
