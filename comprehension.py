squares = [x for x in range(5) if x%2 == 0]

print(squares)

diction = {x: x**2 for x in range(5) if x%2 == 0}
print(diction)

unique_val = {len(word) for word in ["cat", "dog", "Horse", "ox"]}
print(unique_val)
