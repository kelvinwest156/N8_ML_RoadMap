numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)

words = ["hi", "hello", "Gooodnight", "goodbye"]
long_words = list(filter(lambda x: len(x)>3, words))
print(long_words)