import os
import psutil
import time

CPU_THRESHOLD = 75
MEMORY_THRESHOLD = 75

while True:
    cpu = psutil.cpu_percent(interval=5)
    memory = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")

    if cpu > CPU_THRESHOLD or memory > MEMORY_THRESHOLD:
        print("Threshold exceeded! Trigger scaling to GCP.")
        print("Creating new GCP VM...")
        break

    time.sleep(10)
