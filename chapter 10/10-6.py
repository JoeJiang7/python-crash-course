print("Give me two numbers and I will add them.")
number1 = input('Please enter a number: ')
number2 = input('Please enter a number: ')
try:
    number3 = int(number1) + int(number2)
    print(number3)
except ValueError:
    msg = 'Sorry, you need to enter a number.'
    print(msg)