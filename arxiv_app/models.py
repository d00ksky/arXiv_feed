from dataclasses import dataclass

@dataclass
class Paper:
    title: str
    year: int
    citations: int
    authors: list[str]