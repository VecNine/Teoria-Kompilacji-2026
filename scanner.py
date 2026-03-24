from lex_token import Token
from token_enum import TokenType
from config import Config

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
        if self.current + 1 >= len(self.source):
            return ""
        return self.source[self.current + 1]

    def number(self, first_char: str) -> str:
        """Skanowanie numeru"""
        buffer: list = [first_char]
        while self.peek().isdigit():
            buffer.append(self.advance())
        return "".join(buffer)


    def identifier(self, first_char: str) -> str:
        buffer = [first_char]
        while self.peek().isalpha():
            char = self.advance()
            buffer.append(char)
        value_string = "".join(buffer)
        return value_string

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
                self.tokens.append(Token(TokenType.NUM, self.number(c)))
            case _ if c.isalpha():
                self.tokens.append(Token(TokenType.ID, self.identifier(c)))
            case _:
                raise Exception(f"Błąd leksykalny w kolumnie {self.start + 1}: Nieoczekiwany znak {c}")

    def __str__(self):
        buffer: list = [f"[{t.token_type.name}] " for t in self.tokens]

        return "".join(buffer)

    def details(self) -> str:
        """Wyświetlanie detali"""
        buffer: list = [f"[{t.token_type.name}, {t.value}] " for t in self.tokens]

        return "".join(buffer)

    def to_html(self, path: str) -> None:
        """
        Generuje kompletny plik HTML i zapisuje go pod wskazaną ścieżką.

        Args:
            path (str): Ścieżka do pliku wynikowego (np. 'output.html').
        """
        header = Config.get_full_header()

        open_tags = Config.get("open_tags")

        tokens_content = "".join([t.get_color_html() for t in self.tokens])

        close_tags = Config.get("close_tags")

        final_html = f"{header}{open_tags}{tokens_content}{close_tags}"

        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(final_html)
            print(f"Sukces: Plik został zapisany w {path}")
        except Exception as e:
            print(f"Błąd podczas zapisywania pliku: {e}")

        return None