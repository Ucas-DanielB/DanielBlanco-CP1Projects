#Daniel Blanco, ProficiencyTest: Personal Information Converter
#Write a short survey that asks for users name, age, height in meters, and favorite number.
#Convert the age and favorite number to integers and height to a float and print out all the information showing both the original input and the converted values! 


name = input("What is your name? ")
age = input("How old are you? ")
height = input("How tall are you in meters? ")
favoriteNumber = input("What is your favorite number? ")

convert_age = int(age)
convert_favoriteNumber = int(favoriteNumber)
convert_height = float(height)

print(name, age, height, favoriteNumber,
       
      convert_age, 
      convert_favoriteNumber, 
      convert_height)