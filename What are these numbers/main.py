#Daniel Blanco, What are these numbers?

num = input("What is a number you like? ")
num = int(num)

num_thousands = "Your number placed in the thousands is {:,} "
print(num_thousands.format(num))

num_Float = "Your favorite number as a float is {:f} "
print(num_Float.format(num))

num_percentage = "Your favorite number as a percentage is {:%} "
print(num_percentage.format(num))

num_dollar = "Your favorite number as a dollar value is {:.2f} "
print(num_dollar.format(num))