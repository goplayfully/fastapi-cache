import hashlib
from typing import Callable, Optional

from starlette.requests import Request
from starlette.responses import Response


def default_key_builder(
    func: Callable,
    namespace: Optional[str] = "",
    request: Optional[Request] = None,
    response: Optional[Response] = None,
    args: Optional[tuple] = None,
    kwargs: Optional[dict] = None,
) -> str:
    from fastapi_cache import FastAPICache

    prefix = f"{FastAPICache.get_prefix()}:{namespace}:{func.__name__}:"
    cache_key = (
        prefix
        + hashlib.blake2b(f"{func.__module__}:{func.__name__}:{args}:{kwargs}".encode()).hexdigest()
    )
    return cache_key
