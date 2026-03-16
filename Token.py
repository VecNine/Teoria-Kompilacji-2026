from enum import StrEnum, auto
from typing import Any


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

class Token:
    def __init__(self, token_type: TokenType, value: Any):
        self.token_type = token_type
        self.value = value

class Scanner:
    tokens: list[Token]

    def __init__(self, source: str):
        self.source = source
        self.start = 0
        self.tokens = []
        self.current = 0

    def scan(self) -> list[Token]:
        """Proces skanowania"""
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, None))
        return self.tokens


    def is_at_end(self) -> bool:
        """Czy koniec wyrażenia."""
        return self.current >= len(self.source)

    def advance(self) -> str:
        """Przechodzi do następnego znaku"""
        c = self.source[self.current]
        self.current += 1
        return c

    def peek(self) -> str:
        """Pobiera obecny znak"""
        if self.is_at_end():
            return ""
        return self.source[self.current]


    def peek_next(self) -> str:
        """Pobiera następny znak"""
        if self.current + 1 > len(self.source):
            return ""
        return self.source[self.current + 1]


    def scan_token(self) -> None:
        """
        Proces skanowania tokenu.

        isdigit() - sprawdzanie czy jest cyfrą
        isalpha() - sprawdzanie czy jest literą
        """
        c = self.advance()
        match c:
            case "(":
                self.tokens.append(Token(TokenType.LB, c))
            case ")":
                self.tokens.append(Token(TokenType.RB, c))
            case "+":
                self.tokens.append(Token(TokenType.PLUS, c))
            case "-":
                self.tokens.append(Token(TokenType.MINUS, c))
            case "*":
                self.tokens.append(Token(TokenType.MUL, c))
            case "/":
                self.tokens.append(Token(TokenType.DIV, c))
            case " ":
                pass
            case _ if c.isdigit():
                self.number()
            case _ if c.isalpha():
                self.indentifier()
            case _:
                raise Exception(f"Błąd leksykalny w kolumnie {self.start + 1}: Nieoczekiwany znak {c}")
