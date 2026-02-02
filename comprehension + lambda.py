numbers = [12, 7, 19, 3, 25, 8, 14, 30, 6, 21]

# Challenge 1: Get numbers divisible by both 2 and 3
div_by_2_and_3 = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(div_by_2_and_3)  # [12, 30, 6]

# Challenge 2: Square numbers less than 10, cube numbers >= 10
transformed = [x**2 if x < 10 else x**3 for x in numbers]
print(transformed)  # [1728, 49, 6859, 9, 15625, 64, 2744, 27000, 36, 9261]

# Challenge 3: Get average of numbers greater than 15
greater_than_15 = [x for x in numbers if x > 15]
average = sum(greater_than_15) / len(greater_than_15)
print(average)  # 23.75 (19 + 25 + 30 + 21 = 95, then 95/4)

# Challenge 4: Create dict mapping each number to "even" or "odd"
even_odd_dict = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print(even_odd_dict)
# {12: 'even', 7: 'odd', 19: 'odd', 3: 'odd', 25: 'odd', 8: 'even', 14: 'even', 30: 'even', 6: 'even', 21: 'odd'}

# Challenge 5: Remove numbers between 10 and 20 (exclusive)
filtered = [x for x in numbers if not (10 < x < 20)]
print(filtered)

# Alternative: keep numbers <= 10 or >= 20
filtered_alt = [x for x in numbers if x <= 10 or x >= 20]
print(filtered_alt)