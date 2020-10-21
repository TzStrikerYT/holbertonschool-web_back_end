#!/usr/bin/env python3
""" Comprehension project """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        The coroutine will loop 10 times,
        each time asynchronously wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
