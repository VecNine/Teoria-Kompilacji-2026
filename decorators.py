def staticclass(cls):
    """Decorator class."""

    def prevent_instantiation(*args, **kwargs):
        raise TypeError(f"Class {cls.__name__} is static! Do not change it!")

    cls.__new__ = prevent_instantiation
    return cls