def get_name(prompt):
    while True:
        name = input(prompt).strip()
        try:
            if name == "":
                raise ValueError("This field cannot be empty.")
            return name
        except ValueError as e:
            print(f"Error: {e}")


def get_age(prompt):
    while True:
        age = int(input(prompt))
        try:
            if age < 0:
                raise ValueError("Age cannot be negative.")
            elif age < 10 or age > 60:
                raise ValueError("Age must be between 10 - 60")
            return age
        except ValueError:
            print("Enter a valid age(number) 10 and 60")


def get_email(prompt):
    while True:
        email = input(prompt).strip()
        try:
            if "@" not in email or "." not in email:
                raise ValueError("Email must contain '@' and '.'")
            return email
        except ValueError as e:
            print(f"Error: {e}")

def get_phone(prompt):
    while True:
        phone = input(prompt).strip()
        try:
            if not phone.isdigit():
                raise ValueError("Invalid input, Enter numbers only")
            if len(phone) < 10 or len(phone) > 15:
                raise ValueError("Number must be 10 to 15 long")
            return phone
        except ValueError as e:
            print("Error: ", e)


print("=== User Registration Form ===")
try:
    name = get_name("Name: ")
    age = get_age("Age: ")
    email = get_email("Email: ")
    phone = get_phone("Phone: ")
finally:
    print("\nForm session ended.")


