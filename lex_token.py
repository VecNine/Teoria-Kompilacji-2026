from typing import Any
from token_enum import TokenType

class Token:
    def __init__(self, token_type: TokenType, value: Any):
        self.token_type = token_type
        self.value = value

