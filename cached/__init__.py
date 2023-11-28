from dataclasses import dataclass
from datetime import timedelta
from functools import wraps
from hashlib import md5
from typing import Callable

from django.core.cache import caches


@dataclass
class cache:

    cache_name: str = 'default'
    timeout: timedelta | None = None
    version: int | None = None
    max_key_length: int = 150
    ignore_self: bool = False

    def __call__(self, fn: Callable) -> Callable:

        def get_key(*args, **kwargs) -> str:
            module = fn.__module__.rsplit('.', maxsplit=1)[1]
            raw_key = ':'.join(
                [f'{module}.{fn.__name__}'] +
                [str(arg) for arg in args[int(self.ignore_self):]] +
                [f'{k}={v}' for k, v in kwargs.items()])

            if len(raw_key) > self.max_key_length:
                hash_ = md5(raw_key.encode('utf-8')).hexdigest()
                raw_key = raw_key[:self.max_key_length - len(hash_) - 1] + ':' + hash_
            return raw_key

        def cache_clear(*args, **kwargs):
            key = get_key(*args, **kwargs)
            cache = caches[self.cache_name]
            cache.delete(key)

        @wraps(fn)
        def wrapped(*args, **kwargs):
            key = get_key(*args, **kwargs)
            cache = caches[self.cache_name]
            return cache.get_or_set(
                key,
                lambda: fn(*args, **kwargs),
                timeout=self.timeout and int(self.timeout.total_seconds()),
                version=self.version,
            )

        wrapped.cache_clear = cache_clear
        return wrapped
