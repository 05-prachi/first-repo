# # int(), integer
# # float(), decimal value
# # bool(), true or false
# # type()
#
# text = '''
# Hi cutie,
# Miss ya so much
# '''
#
# # indexes
# another = text[:]
# print(text[-5])
# print(text[4:10])
# print(another)
#
# first = 'John'
# last = 'Doe'
# # formatted strings
# msg = f'{first} [{last}] is a coder'
# print(msg)
#
# # counts the number of characters in a string
# print(len(msg))
#
# # is called a method, converts the text into upper or lower case, and replaces a text or a word
# # case sensitive
# print(first.upper())
# print(first.lower())
# print(last.replace('Doe', 'McDowell'))
#
# # title method capitalizes first word or every letter whereas capitalize method only capitalizes the letter at index 0 and converts the other into lower case
# print(text.title())
# print(text.capitalize())
#
# # difference between the find and the in command is that the find command gives the index of the letter or the word
# # we're trying to find while the in command is a boolean command and tell us whether the letter or the word in the given variable
# print(first.find('o'))
# print('John' in first)
#
# # arithmetic operators
# # first, + is for addition, - is for subtraction, * to multiply, and / for division when we desire a float output but // when we desire an integral output
# # secondly, % gives the remainder of a division and ** is used for exponential values
# # augmented operators, x = x + 3 can be written as x += 3
#
# # we can also round off [round()] a number or get its absolute (positive) value [abs()], kinda like mod
# import math
#
# print(math.acos(1))
#
# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a warm day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's cold outside")
#     print("Don't forget your sweaters")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
#
# price = 1000000
# good_credit = True
# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down payment: ${down_payment}')
#
# has_high_income = True
# has_good_credit = True
# criminal_record = True
# if has_good_credit and not criminal_record:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")
#
# temperature = 30
# if temperature != 30:
#     print("It's a hot day!")
# else:
#     print("It's not really a hot day")
#
# name = input("Name: ")
# if len(name) <= 3:
#     print("Name must be at least 3 characters.")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters.")
# else:
#     print("Name looks good!")
#
# weight = int(input("Weight: "))
# lbs_kgs = input("(l)bs or (k)gs: ")
# if lbs_kgs.upper() == "L":
#     converted = weight * 0.453
#     print(F'You are {converted} kilos.')
# else:
#     converted = weight * 2.204
#     print(f'You are {converted} pounds.')
#
# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print("Done")
#
# secret_number = 7
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You win!!")
#         break
# else:
#     print("Try again!!")
#
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "help":
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif command == "start":
#         if started:
#             print("The car is already started.")
#         else:
#             started = True
#             print("Car started... Ready to go!")
#     elif command == "stop":
#         if not started:
#             print("The car is already stopped.")
#         else:
#             started = False
#             print("The car is stopped :(")
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that.")
#
# names = ['Prachi', 'Mehar', 'Rashan']
# names[2] = "Venika"
# for item in names:
#     print(item)
#
# for item_1 in range(1, 11, 2):
#     print(item_1)
#
# prices = [12, 38, 56, 29, 47, 63, 46]
# max = prices[0]
# for number in prices:
#     if number > max:
#         max = number
# print(max)
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")
#
# for x in range(5):
#     for y in range(4):
#         print(f'({x}, {y})')
#
# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)
# numbers.append(4)
# numbers.insert(2, 6)
# numbers.sort()
# numbers.reverse()
# numbers.pop()
# numbers.remove(2)
# print(numbers)
# numbers.clear()
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 4
# print(matrix[0][1])
# for row in matrix:
#     print(row)
#
# list1 = [1, 2, 3, 4, 2, 2, 6, 9, 3, 1, 6, 8, 9]
# uniques = []
# for item in list1:
#     if item not in uniques:
#         uniques.append(item)
# print(uniques)
#
# # tuples are list that can't be modified
# tuple = (1, 2, 3)
# print(tuple[2])
#
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(y)
#
# # dictionary, keys are case-sensitive
# customer = {
#     "name": "John Smith",
#     "age": 20,
#     "phone number": 9876658391
# }
# customer["e-mail"] = "johnsmith@gmail.com"
# print(customer["age"])
# print(customer.get("birthdate", "Jan 1 2005"))
#
# phone = input("Phone: ")
# digits_mapping = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# output = ""
# if len(phone) == 10:
#     for ch in phone:
#         output += digits_mapping.get(ch, "!") + " "
#     print(output)
# else:
#     print("Phone number must be equal to 10 characters.")
#
#
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":(": "😞",
#         ":)": "😁",
#         "<3": "💗"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input("> ")
# print(emoji_converter(message))
#
#
# def greet_user(first_name, last_name):
#     print(f'''Hi {first_name} {last_name}!
# Welcome aboard!!''')
#
#
# # keyword arguments should always be used after positional arguments
# print("Start")
# greet_user("Prachi", last_name="Arora")
# print("Stop")
#
#
# def square(number):
#     return number ** 2
#
#
# print(square(67))
#
# # try and except statements
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(risk)
# except ValueError:
#     print("Invalid Value")
# except ZeroDivisionError:
#     print("Age cannot be 0.")

