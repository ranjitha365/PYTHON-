is_failed = True
i = 0
while is_failed:
    i += 1
    if i % 2 != 0:
        continue # skip odd numbers
    if i >= 100:
        break # stop loop when i reaches 100
    print(f"attempt: {i}")
print("I never gave up ")

