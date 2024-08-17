#!/usr/bin/env python3
"""
This module provides a function to create asyncio Tasks from a coroutine
that waits for a random delay.

Functions:
    - task_wait_random(max_delay: int) -> asyncio.Task:
      Creates an asyncio Task that runs the wait_random coroutine.

The `wait_random` coroutine is imported dynamically using the `__import__`
function from a module named '0-basic_async_syntax'.
"""

import asyncio

# Dynamically import the wait_random function from the specified module
wait_r = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay (in seconds) for the
        wait_random coroutine.

    Returns:
        asyncio.Task: An asyncio Task object that runs the
        wait_random coroutine.

    Description:
        This function uses the `asyncio.create_task()` function to
        create a task from the `wait_random` coroutine, which is
        imported from the '0-basic_async_syntax' module using the
        `__import__()` function. The task is scheduled to run
        concurrently, and the function immediately returns the Task object.

    Example:
        task = task_wait_random(5)
        # The above line creates an asyncio Task that will wait
        # for a random delay between 0 and 5 seconds.
    """
    return asyncio.create_task(wait_r(max_delay))
