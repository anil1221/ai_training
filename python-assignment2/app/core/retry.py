import time
import logging


def retry(max_attempts=3, delay=1):
    def decorator(func):

        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)

                except Exception as error:
                    attempts += 1

                    logging.warning(
                        f"Retry {attempts}/{max_attempts} "
                        f"for {func.__name__}: {error}"
                    )

                    time.sleep(delay)

            raise Exception(
                f"{func.__name__} failed after retries"
            )

        return wrapper

    return decorator