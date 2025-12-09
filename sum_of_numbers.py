def is_prime_number(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    if len(factors) == 2:
        return True
    else:
        return False


max_number = int(input("Where do you want to sum up to? "))
sum_of_nums = 0

for number in range(1, max_number + 1):
    if is_prime_number(number):
        sum_of_nums = sum_of_nums + number
print(f"The sum of all prime numbers from 1 to {max_number} is {sum_of_nums}")
