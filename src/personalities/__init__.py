# from .luna import luna
# from .sacha import sacha
# from .angele import angele
from .papola import papola

__all__ = [ "papola"]


def get_personality(name: str):
    try:
        return {"papola":papola}[name]
    except Exception:
        raise Exception("The personality you selected does not exist!")
