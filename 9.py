items = ["apple", "banana", "orange", "apple", "mango"]

unique_iteam = set()

for item in items:
    if item in unique_iteam:
        print("Duplicate:",item)
        break
    unique_iteam.add(item)

print(unique_iteam)