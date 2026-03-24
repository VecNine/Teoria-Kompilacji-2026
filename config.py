@staticmethod
class Config:
    _config = {
        "preamble": "<div class=\"code-header\"><span>Python</span><button class=\"copy-btn\">Kopiuj</button></div>",
        "open_tags": "<pre class=\"language-python\"><code class=\"language-python\">",
        "close_tags": "</code></pre>"
    }

    @classmethod
    def load_custom(cls, conf: dict):
        """Custom configuration."""
        cls._config = conf

    @classmethod
    def get(cls, key: str) -> str:
        """Loads specific configuration line."""
        return cls._config.get(key, "")

    @classmethod
    def get_all(cls) -> dict:
        """Returns whole dict of configurations."""
        return cls._config

