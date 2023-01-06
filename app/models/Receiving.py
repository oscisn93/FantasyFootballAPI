from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class ReceivingBase(SQLModel):
    week: int
    targets: int
    rec: int
    rec_yds: int
    rec_td: int
    rec_long: int
    player_id: Optional[int] = Field(default=None, foreign_key='player.id')
    player: Optional['Player'] = Relationship(back_populates='receiving')


class ReceivingRead(ReceivingBase):
    id: int


class ReceivingCreate(ReceivingBase):
    ...


class Receiving(ReceivingBase, table=True):
    id: int = Field(primary_key=True)
