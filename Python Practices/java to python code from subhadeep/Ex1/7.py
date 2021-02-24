print("Choose the options")
print("1.To convert to fahrenheit from Celsius")
print("2.To convert to Celsius from fahrenheit")
while True:
    n = int(input())
    if n not in (1,2):
        print("Enter the correct option")
    elif n ==1:
        c = int(input("Enter the celsius value"))
        print(f"The Value is {1.8*c+32}F")
    elif n == 2:
        f = int(input("Enter the farenheit value"))
        print(f"The value is {5/9*(f-32)}C")
