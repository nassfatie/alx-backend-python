#!/usr/bin/env python3

import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    bt = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - bt
    return total_time
