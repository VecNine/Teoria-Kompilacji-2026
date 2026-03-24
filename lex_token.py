from typing import Any
from token_enum import TokenType
from colors import Color

class Token:
    def __init__(self, token_type: TokenType, value: Any):
        self.token_type = token_type
        self.value = value

    def get_color(self) -> str:
        """Hex coloring"""
        return Color.get_color(self)

    def get_color_html(self) -> str:
        """Html coloring"""
        return Color.get_color_html(self)