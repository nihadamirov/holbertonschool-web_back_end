#!/usr/bin/env python3
""" write a measure_runtime coroutine that will
execute async_comprehension four times """
import asyncio
import time
import random
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    full_time = end_time - start_time
    return full_time
