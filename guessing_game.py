original_num = 13
num_of_trials = 5

user_guess = int(input("Guess a number between 1-20. You have 5 trials: "))
while num_of_trials != 0 and user_guess != original_num:
    num_of_trials = num_of_trials - 1

    if original_num-3 <= user_guess <= original_num+3:
        print(f"So close try again. {num_of_trials} trial(s) left")
    else:
        print(f"You are far from the true number. {num_of_trials} trial(s) left")

    user_guess = int(input("Guess a number between 1-20 "))
print("Your guess is correct")
