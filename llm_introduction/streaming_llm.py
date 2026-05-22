import sys
import time

# Simulated LLM response
response = """
Large Language Models can stream tokens
incrementally instead of waiting for the
entire response to finish generation.
This improves perceived responsiveness
and user experience.
"""

words = response.split()

print("Starting LLM streaming...\n")

start_time = time.time()

first_token_time = None

for index, word in enumerate(words):

    # Simulate token generation delay
    time.sleep(0.2)

    # Measure TTFT
    if index == 0:
        first_token_time = time.time()

        ttft = (
            first_token_time - start_time
        )

        print(
            f"\nTTFT (Time To First Token): "
            f"{ttft:.3f} seconds\n"
        )

    # Stream token output
    sys.stdout.write(word + " ")

    # Force immediate display
    sys.stdout.flush()

print("\n\nStreaming complete.")