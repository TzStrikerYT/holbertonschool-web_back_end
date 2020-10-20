#!/usr/bin/env python3
""" async proyect """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """ Return a list of delays in asc order """
    delays: List[float] = []
    toReturn = []

    for _ in range(n):
        delays.append(wait_random(max_delay))

    return [await process for process in asyncio.as_completed(delays)]
