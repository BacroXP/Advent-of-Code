import re
from typing import Callable, Iterable, List, Any, Optional


def file(f: Optional[Callable[[str], Any]] = None, path: str = "input.txt") -> List[Any]:
    """Read lines from `path`. If `f` is provided, apply f to each line and
    return the transformed list.

    Examples:
      file() -> list[str]
      file(int) -> list[int]
    """
    with open(path, "r") as fh:
        # keep behavior similar to previous implementation: strip outer
        # whitespace then split on newlines
        text = fh.read().strip()
        if text == "":
            lines: List[str] = []
        else:
            lines = text.split("\n")

    if f is None or f is str:
        return lines  # type: ignore[return-value]
    return [f(line) for line in lines]

def word_file() -> list[list[str]]:
    return [line.split() for line in file()]


def grid() -> list[list[str]]:
    return [[char for char in line] for line in file()]


def sub_grid() -> list[list[list[str]]]:
    return [[[char for char in line] for line in grid.split("\n")] for grid in open("input.txt").read().strip().split("\n\n")]


def nums(lines: list[str], sort: bool = False) -> list[list[int]]:
    return [sorted([int(x) for x in re.findall(r'-?\d+', line)]) if sort else [int(x) for x in re.findall(r'-?\d+', line)] for line in lines]


def pairs(array: list[any]) -> list[tuple[any, any]]:
    length = len(array)
    _ret = []
    
    for i in range(length - 1):
        _ret.append((array[i], array[i + 1]))
    
    return _ret


def triples(array: list[any]) -> list[tuple[any, any, any]]:
    length = len(array)
    _ret = []
    
    for i in range(length - 2):
        _ret.append((array[i], array[i + 1], array[i + 2]))
    
    return _ret

def groups(array: list[any], n: int) -> list[tuple[Any, ...]]:
    length = len(array)
    _ret = []
    
    for i in range(length - n + 1):
        _ret.append(tuple(array[i + j] for j in range(n)))
    
    return _ret
