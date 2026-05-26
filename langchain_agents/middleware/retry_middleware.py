import time


def retry_tool( tool_function, *args, retries=3):
    for attempt in range(retries):
        try:
            return tool_function(*args)
        except Exception as error:
            print(f"Retry {attempt + 1}: {error}")
            time.sleep(1)

    return "Tool failed after retries"