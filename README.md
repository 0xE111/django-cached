# Django-cached

Django-cached is a small library to add `@cache` decorator based on Django cache.

## How to use

```sh
pip install django-cached
```

```python
from cached import cache


@cache()
def foo(one, two, three):
    return one + two + three

class StatefulClass:
    @cache()
    def bar(self, one, two, three):
        return one + two + three


class StatelessClass:
    @cache(ignore_self=True)  # we don't want `self` to be in cache key
    def bar(self, one, two, three):
        return one + two + three

```
