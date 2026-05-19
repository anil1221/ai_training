import random
import time

from app.core.monitor import monitor_performance
from app.core.retry import retry
from app.core.cache import cache_result


@cache_result
@monitor_performance
@retry(max_attempts=3, delay=1)
def generate_recommendations(user_id):

    print(f"Generating recommendations for user {user_id}")

    # Simulate slow operation
    time.sleep(3)

    # Simulate random failure
    if random.choice([True, False]):
        raise Exception("Temporary database failure")

    return {
        "user_id": user_id,
        "recommendations": [
            "Laptop",
            "Phone",
            "Headphones"
        ]
    }