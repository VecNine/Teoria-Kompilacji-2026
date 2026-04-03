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
    EQ = auto()

    IF = auto()
    ELSE = auto()
    WHILE = auto()
    PRINT = auto()


    EQUAL_EQUAL = auto()  # ==
    BANG_EQUAL = auto()  # !=
    LESS = auto()  # <
    EQUAL_LESS = auto()
    GREATER = auto()  # >
    EQUAL_GREATER = auto()