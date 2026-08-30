numbers = input("Anna numero:")
if numbers != "":
    maxi = int(numbers)
    mini = int(numbers)

while True:
    numbers = input("Anna numero:")
    if numbers != "":
        numbers = int(numbers)
        if int(numbers) >= maxi:
            maxi = numbers
        elif numbers <= mini:
            mini = numbers
        else:
            break

print(f"maksiimi {maxi}")
print(f"minimi {mini}")