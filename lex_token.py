from typing import Any
from token_enum import TokenType
from colors import Color

class Token:
    def __init__(self, token_type: TokenType, value: Any):
        self.token_type = token_type
        self.value = value

    def toHtml(self) -> str:
        """Html coloring"""
        match self.token_type:
            case TokenType.LB | TokenType.RB:
                return f"{Color.light_green(self.token_type)}"
            case TokenType.PLUS:
                return f"{Color.dark_green(self.token_type)}"
            case TokenType.MUL:
                return f"{Color.dark_green(self.token_type)}"
            case TokenType.MINUS:
                return f"{Color.dark_green(self.token_type)}"
            case TokenType.DIV:
                return f"{Color.dark_green(self.token_type)}"
            case TokenType.ID:
                return f"{Color.blue(self.token_type)}"
            case _:
                return f"{Color.plain(self.token_type)}"