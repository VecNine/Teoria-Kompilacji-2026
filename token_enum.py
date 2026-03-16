from enum import StrEnum, auto

class TokenType(StrEnum):
    NUM = auto()
    ID = auto()
    LB = auto()
    RB = auto()
    MUL = auto()
    DIV = auto()
    PLUS = auto()
    MINUS = auto()
    EOF = auto()