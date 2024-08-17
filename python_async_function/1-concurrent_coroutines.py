#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
--------------------------

This module demonstrates concurrency using asyncio by running multiple
instances of an asynchronous function that waits for a random delay.

Functions:
- wait_random(max_delay: int = 10) -> float:
    Asynchronously waits for a random amount of time and returns
    the duration of the delay.
- wait_n(n: int, max_delay: int) -> List[float]:
    Runs multiple `wait_random` tasks concurrently and returns
    a list of all delays in ascending order of completion.

Usage Example:
--------------
import asyncio
from async_concurrency_example import run_multiple_tasks

async def main():
    delays = await run_multiple_tasks(5, 10)
    print(f"Delays: {delays}")

asyncio.run(main())
"""
import asyncio
from typing import List

wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs multiple `wait_random` tasks concurrently and returns
    the delays in the order they complete.

    Parameters:
    -----------
    n : int
        The number of `wait_random` tasks to run.
    max_delay : int
        The maximum delay for each `wait_random` task.

    Returns:
    --------
    List[float]
        A list of the actual durations of each delay
        in ascending order of completion.
    """
    tasks = [asyncio.create_task(wait_r(max_delay)) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
