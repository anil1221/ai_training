from functools import lru_cache


def cache_result(func):
    cached_function = lru_cache(maxsize=128)(func)

    return cached_function