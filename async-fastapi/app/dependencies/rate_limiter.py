import time

from fastapi import HTTPException

request_tracker = {}

RATE_LIMIT = 5
WINDOW_SIZE = 60


async def rate_limiter(token: str):

    current_time = time.time()

    if token not in request_tracker:
        request_tracker[token] = []

    request_times = request_tracker[token]

    request_tracker[token] = [
        req_time
        for req_time in request_times
        if current_time - req_time < WINDOW_SIZE
    ]

    if len(request_tracker[token]) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    request_tracker[token].append(current_time)