from functools import wraps


def memoization(func):
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return inner

