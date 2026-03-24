from __future__ import annotations # Pozwala używać nazwy klasy przed jej definicją
from typing import TYPE_CHECKING
from token_enum import TokenType
import html

if TYPE_CHECKING:
    from lex_token import Token

class Color:
    """Klasa pomocnicza do kolorowania składni w HTML."""
    _token_colors = {
        TokenType.NUM: "#bd93f9",  # Fioletowy
        TokenType.ID: "#8be9fd",  # Jasnoniebieski
        TokenType.LB: "#a6e22e",  # Jasnozielony (Nawiasy)
        TokenType.RB: "#a6e22e",  # Jasnozielony (Nawiasy)
        TokenType.PLUS: "#44ad4d",  # Ciemnozielony
        TokenType.MINUS: "#44ad4d",  # Ciemnozielony
        TokenType.MUL: "#44ad4d",  # Ciemnozielony
        TokenType.DIV: "#44ad4d",  # Ciemnozielony
        TokenType.EOF: "#6272a4",  # Szary
    }

    @staticmethod
    def get_color_by_type(token_type: TokenType):
        return Color._token_colors[token_type]

    @staticmethod
    def get_color(token: Token) -> str:
        return Color._token_colors[token.token_type]

    @staticmethod
    def get_color_html(token: Token) -> str:
        """Zwraca gotowy tag <span> z kolorem inline."""
        color = Color.get_color(token)

        value = str(token.value) if token.value is not None else ""
        return f'<span style="color: {color};">{html.escape(value)}</span>'