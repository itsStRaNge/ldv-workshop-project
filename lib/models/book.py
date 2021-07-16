from dataclasses import dataclass


@dataclass
class Book:
    id: str
    name: str
    price: float
    quantity: int