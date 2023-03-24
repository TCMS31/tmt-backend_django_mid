
from decimal import Decimal
from pydantic import BaseModel


class InventoryMetaData(BaseModel):
    year: int
    actors: list[str]
    imdb_rating: Decimal
    rotten_tomatoes_rating: int