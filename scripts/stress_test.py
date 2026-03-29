import os
import time

print("Starting CPU stress test...")

while True:
    for i in range(10000000):
        x = i * i
    print("CPU load running...")
    time.sleep(1)
