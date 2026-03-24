from token_enum import TokenType
from colors import Color # Zakładając, że klasa Color jest w pliku colors.py


class Config:
    """
    Plik konfiguracyjny generatora HTML.
    Pobiera dane o kolorach bezpośrednio z klasy Color.
    """

    _config = {
        "preamble": "<div class=\"code-header\"><span>Python Scanner</span><button class=\"copy-btn\" onclick=\"copyCode()\">Kopiuj</button></div>",
        "open_tags": "<pre id=\"code-output\" class=\"language-python\"><code class=\"language-python\">",
        "close_tags": "</code></pre>"
    }

    @classmethod
    def generate_css(cls) -> str:
        """Automatycznie tworzy style CSS, pobierając kolory z klasy Color."""
        css_lines = [
            "<style>",
            "body { background: #282a36; padding: 20px; font-family: 'Consolas', monospace; }",
            ".code-header { background: #44475a; color: #f8f8f2; padding: 10px 15px; border-radius: 8px 8px 0 0; display: flex; justify-content: space-between; align-items: center; border: 1px solid #6272a4; border-bottom: none; }",
            ".copy-btn { cursor: pointer; background: #6272a4; border: none; color: white; padding: 4px 10px; border-radius: 4px; font-size: 12px; transition: 0.2s; }",
            ".copy-btn:hover { background: #bd93f9; }",
            "pre { background: #1e1e1e; padding: 15px; border-radius: 0 0 8px 8px; margin: 0; border: 1px solid #6272a4; overflow-x: auto; white-space: pre; }",
            ".token { font-weight: bold; }",
            "</style>"
        ]

        # Automatyczna iteracja po wszystkich typach tokenów z Enum
        for token_type in TokenType:
            # Wywołanie statycznej metody z klasy Color
            color = Color.get_color_by_type(token_type)
            css_lines.insert(-1, f".{token_type.name} {{ color: {color}; }}")

        return "\n".join(css_lines)

    @classmethod
    def get(cls, key: str) -> str:
        """Pobiera konkretną linię konfiguracji."""
        return cls._config.get(key, "")

    @classmethod
    def get_full_header(cls) -> str:
        """Łączy dynamiczny CSS z preambułą."""
        return f"{cls.generate_css()}\n{cls.get('preamble')}"