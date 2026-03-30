# algorithms package
from .fifo import simulate as fifo_simulate
from .lru import simulate as lru_simulate
from .mru import simulate as mru_simulate
from .optimal import simulate as optimal_simulate
from .second_chance import simulate as second_chance_simulate

__all__ = [
    "fifo_simulate",
    "lru_simulate",
    "mru_simulate",
    "optimal_simulate",
    "second_chance_simulate",
]
