print("********GRADE CLASSIFIER*********")

grade = int(input("Enter our grade: "))

if 80 <= grade <= 100:
    print("You got A")
elif 70 <= grade < 80:
    print("You got B")
elif 60 <= grade < 70:
    print("You got C")
elif 50 <= grade < 60:
    print("D")
elif 0 <= grade < 50:
    print("You failed. ou got F")
else:
    print("Invalid input.")

