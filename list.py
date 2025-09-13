n = [i + 1 for i in range(10)]

# for i in range (10):
#     n.append(i + 1)

print(f"Original list: {n}")
first_five = n[:5]
print(f"Extract first five elements: {first_five}")
first_five.reverse()
print(f"Extract and reverse first five elements: {first_five}")

