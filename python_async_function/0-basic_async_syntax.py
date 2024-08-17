#!/usr/bin/env python3
"""
0-basic_async_syntax.py
-----------------------

This module provides an asynchronous function that waits
for a random delay and then returns the duration of that delay.

Functions:
- wait_random(max_delay: int = 10) -> float:
    Asynchronously waits for a random amount of time and
    returns the duration of the delay.

Usage Example:
--------------
import asyncio
from 0-basic_async_syntax import wait_random

async def main():
    delay = await wait_random(5)
    print(f"Waited for {delay} seconds")

asyncio.run(main())
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time between 0
    and max_delay seconds.

    Parameters:
    -----------
    max_delay : int, optional
        The maximum number of seconds to wait (default is 10).

    Returns:
    --------
    float
        The actual duration of the delay in seconds.
    """
    sleep_time = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
