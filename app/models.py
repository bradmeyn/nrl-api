from sqlmodel import Field, Relationship, SQLModel
from enum import Enum

class Team(SQLModel, table=True):
    __tablename__ = "teams"

    id: int | None = Field(default=None, primary_key=True)
    name: str

    players: list["Player"] = Relationship(back_populates="team")


class Position(str, Enum):
    FLB = "FLB"   # Fullback
    CTW = "CTW"   # Centre/Wing
    HFB = "HFB"   # Halfback
    FIVE_EIGHTH = "5/8"   # Five-eighth
    HOK = "HOK"   # Hooker
    FRF = "FRF"   # Front-row forward
    TWO_RF = "2RF"   # Second-row forward

class Player(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    first_name: str
    last_name: str

    position: Position
    second_position: Position| None

    team_id: int | None = Field(default=None, foreign_key="teams.id")

