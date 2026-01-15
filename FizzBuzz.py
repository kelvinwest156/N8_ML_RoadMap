def is_multiple_3(num):
    if num % 3 == 0:
        return True
    else:
        return False


def is_multiple_5(num):
    if num % 5 == 0:
        return True
    else:
        return False

print("******FIZZBUZZ CHALLENGE******")

num = int(input("Enter any number. Multiple digits recommended: "))

for count in range(1, num + 1):
    if is_multiple_3(count) and is_multiple_5(count):
        print("FizzBuzz")
    elif is_multiple_3(count):
        print("Fizz")
    elif is_multiple_5(count):
        print("Buzz")
    else:
        print(count)
