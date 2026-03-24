import json
import html
import decorators

@staticmethod
class Color:
    """Klasa pomocnicza do kolorowania składni w HTML."""

    @staticmethod
    def red(text: str) -> str:
        return f'<span style="color: #E06C75;">{html.escape(text)}</span>'

    @staticmethod
    def dark_green(text: str) -> str:
        return f'<span style="color: #2E8B57;">{html.escape(text)}</span>'

    @staticmethod
    def blue(text: str) -> str:
        return f'<span style="color: #61AFEF;">{html.escape(text)}</span>'

    @staticmethod
    def light_green(text: str) -> str:
        return f'<span style="color: #98C379;">{html.escape(text)}</span>'

    @staticmethod
    def plain(text: str) -> str:
        # Dla zwykłego tekstu (np. nawiasów, spacji), który nie ma koloru, ale nadal musi być bezpieczny
        return html.escape(text)