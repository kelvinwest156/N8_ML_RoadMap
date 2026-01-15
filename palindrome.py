def is_palindrome(word):
    # create a reversed list
    reverse_word = []
    for letter in original_word:
            if len(reverse_word) == 0:
                reverse_word.append(letter)
            else:
                reverse_word.insert(0, letter)

    # check for palindrome
    if original_word_list == reverse_word:
        return True
    else:
        return False


print("Enter your word below: ")
input_word = input(str(">>> "))
original_word = "".join(input_word.split())
original_word_list = []

for i in original_word:
    original_word_list.append(i)

if is_palindrome(original_word):
    print(f"{input_word} is a palindrome")
else:
    print(f"{input_word} is not a palindrome")
