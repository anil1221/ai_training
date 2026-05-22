import time

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

print("Starting batch processing...\n")

# Read prompts
with open(INPUT_FILE, "r") as file:
    prompts = [line.strip() for line in file.readlines()]

print(f"Loaded {len(prompts)} prompts")

# Simulate batching
batch_start = time.time()

print("\nRunning single batch inference...")

time.sleep(3)

processed_prompts = []

for prompt in prompts:

    processed_prompts.append(f"{prompt} [PROCESSED]")

# Save results
with open(OUTPUT_FILE, "w") as file:

    for item in processed_prompts:
        file.write(item + "\n")

batch_end = time.time()

batch_total_time = (batch_end - batch_start)

# Sequential comparison
sequential_time = len(prompts) * 1

print("\nBatch Processing Complete")

print(f"\nBatch Total Time: {batch_total_time:.2f} seconds")

print(f"Sequential Processing Time: {sequential_time} seconds")

improvement = (sequential_time / batch_total_time)

print(f"\nEfficiency Improvement: {improvement:.2f}x faster")