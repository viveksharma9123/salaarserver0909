from .alix_earle import alix_earle
from .angele import angele
from .ethan_ridge import ethan_ridge
from .jack_dawson import jack_dawson
from .jordan_belfort import jordan_belfort
from .luna import luna
from .makima import makima
from .sacha import sacha
from .sandra import sandra

__all__ = [
    "sacha",
    "luna",
    "angele",
    "makima",
    "sandra",
    "alix_earle",
    "jack_dawson",
    "jordan_belfort",
    "ethan_ridge",
    "get_personality"
]


def get_personality(name: str):
    try:
        return {
            "Sacha": sacha,
            "Luna": luna,
            "Angèle": angele,
            "Makima": makima,
            "Sandra": sandra,
            "Alix Earle": alix_earle,
            "Jack Dawson": jack_dawson,
            "Jordan Belfort": jordan_belfort,
            "Ethan Ridge": ethan_ridge
        }[name]
    except Exception:
        raise Exception("The personality you selected does not exist!")
