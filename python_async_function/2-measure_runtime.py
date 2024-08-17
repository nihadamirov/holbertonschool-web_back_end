#!/usr/bin/env python3
"""
2-measure_runtime.py
--------------------

This script measures the average time taken per coroutine when running
the 'wait_n' asynchronous function. It computes the total elapsed time
and divides it by the number of coroutines to find the average time per
coroutine.

Modules:
    asyncio: Provides support for asynchronous programming.
    time: Provides various time-related functions.

Functions:
    measure_time(n: int, max_delay: int) -> float:
        Asynchronously measures the average time taken per coroutine when
        running 'wait_n' with the given parameters.

Usage:
    To use this script, you need to have the 'wait_n' function
    implemented in the '1-concurrent_coroutines' module. This function
    should be an asynchronous function that waits for a random delay
    and returns the total list of delays.

    Example:
        n = 5
        max_delay = 9
        total_time = asyncio.run(measure_time(n, max_delay))
        print(total_time)
"""

import asyncio
import time


# Importing the 'wait_n' function from the '1-concurrent_coroutines' module.
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average elapsed time per coroutine when running 'wait_n'.

    This function starts a timer before calling 'wait_n' with the given
    parameters, waits for the execution of 'wait_n', and then calculates
    the total elapsed time. It returns the average time per coroutine
    by dividing the total time by the number of coroutines 'n'.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time taken per coroutine in seconds.
    """
    # Record the start time
    start_time = time.time()

    # Execution of the 'wait_n' asynchronous function
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time = time.time()

    # Calculate the total elapsed time
    total_time = end_time - start_time

    # Return the average elapsed time per coroutine
    return total_time / n
