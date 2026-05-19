import time
import logging

logging.basicConfig(level=logging.INFO)


def monitor_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        logging.info(
            f"{func.__name__} executed in "
            f"{execution_time:.4f} seconds"
        )

        if execution_time > 2:
            logging.warning(
                f"Performance bottleneck detected in "
                f"{func.__name__}"
            )

        return result

    return wrapper