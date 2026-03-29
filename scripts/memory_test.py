memory_list = []

print("Starting memory stress test...")

while True:
    memory_list.append("A" * 10000000)
    print(f"Current memory blocks: {len(memory_list)}")
