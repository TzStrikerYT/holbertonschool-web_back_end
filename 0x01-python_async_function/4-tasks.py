#!/usr/bin/env python3
""" async proyect """

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Return a list of delays in asc order """
    delays: List[float] = []

    for _ in range(n):
        delays.append(task_wait_random(max_delay))

    return [await process for process in asyncio.as_completed(delays)]
