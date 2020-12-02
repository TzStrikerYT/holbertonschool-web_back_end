#!/usr/bin/env python3
""" Module to practice the previous concepts in Redis with requests """
import requests
from functools import wraps
from typing import Callable
import redis


def count(method: Callable):
    """Count the call to requests"""
    r = redis.Redis()

    @wraps(method)
    def wrapped(url):
        """EXtra behavior to function that will count"""
        r.incr(f"count:{url}")
        expiration_count = r.get(f"cached:{url}")
        if expiration_count:
            return expiration_count.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapped


@count
def get_page(url: str) -> str:
    """It uses the requests module to obtain the
    HTML content of a particular URL and returns it.
    """
    return requests.get(url).text