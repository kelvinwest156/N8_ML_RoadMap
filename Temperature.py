def to_fahrenheit(temperature):
    fahrenheit = (temperature * (9/5)) + 32
    return fahrenheit


def to_celsius(temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius

print("*******Temperature Convertor*******")

print("What Temperature do you want to convert? ")
print("1. Celsius - Fahrenheit")
print("2. Fahrenheit - Celsius")
task = int(input(">>> "))

if task == 1:
    temperature = int(input("Enter Temperature in Celsius >>> "))
    print(f"{temperature}C is {to_fahrenheit(temperature)}F")
elif task == 2:
    temperature = int(input("Enter Temperature in Fahrenheit >>> "))
    print(f"{temperature}C is {to_celsius(temperature)}C")
