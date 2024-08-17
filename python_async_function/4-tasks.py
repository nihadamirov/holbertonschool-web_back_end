#!/usr/bin/env python3
"""
4-tasks.py
----------

This module demonstrates concurrency using asyncio by running multiple
instances of an asynchronous function that waits for a random delay.

Functions:
- task_wait_random(max_delay: int) -> asyncio.Task:
    Returns an asyncio Task that runs the `wait_random` coroutine.

- task_wait_n(n: int, max_delay: int) -> list[float]:
    Runs multiple `wait_random` tasks concurrently and returns
    a list of all delays in ascending order of completion.

Usage Example:
--------------
import asyncio
from 4-tasks import task_wait_n

async def main():
    delays = await task_wait_n(5, 6)
    print(f"Delays: {delays}")

asyncio.run(main())
"""

import asyncio
from typing import List

# Importing task_wait_random from 3-tasks
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
    list[float]
        A list of the actual durations of each delay
        in ascending order of completion.

    Description:
    ------------
    This function creates and schedules `n` tasks using `task_wait_random`,
    which itself is based on the `wait_random` coroutine. The tasks are run
    concurrently, and as each task completes, its delay duration is captured
    and appended to the `delays` list. The list is built in the order of
    task completion, ensuring it reflects the sequence in which tasks finished.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
