#concatenation
a, b = "5", 10
txt = "@"
print((a+txt)*b)

#a//b = floor(a/b)

A = int(input("A: "))
G = input("M/F: ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")

#single line conditional statement, ternary operator
food = input("food: ")
eat = "yes" if food == "pizza" else "no"
print(eat)
print("yummy" if food == "pizza" else "not yummy")

#clever if conditional statement, ternary operator (complex) 
#<var> = (false_val, true_val)[condition]
age = int(input("age: "))
vote = ("yes", "no") [age >= 18]

sal = float(input("salary: "))
tax = sal*(0.1, 0.2) [sal<=50000]
print(tax)

#escape sequence characters
str1 = "This is a string.\nThis is a new line.\tThis is a tab."
print(str1)

marks = int(input("marks: "))
if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "D"

print(f"Your grade is {grade}.")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#immutable, strings and tuples
#mutable, lists and dictionaries
movies = []
movies.append(input("Enter a movie name: "))
movies.append(input("Enter another movie name: "))
movies.append(input("Enter one more movie name: "))
print(movies)

list = [1, 2, 3, 2, 1]
list2 = list.copy()
list2.reverse()
if list == list2:
    print("The list is a palindrome.")

#keys (unique) should be immutable
#unordered, can add new keys
null_dict = {}
dict = {
    "key" : "value" 
}

#set is mutable (unhashable)
#elements of a set = immutable (hashable), no duplicate elements
null_set = set()
set = {1, 2, 3, 3, 3, "world", "hello", "hello"}
set.add("prachi")
set.discard("words")  #does not raise an error if the element is not found
print(set)

marks = {}
marks["Subject 1: "] = int(input("Marks: "))
marks["Subject 2: "] = int(input("Marks: "))
marks.update({"Subject 3: ": int(input("Marks: "))})
print(marks)

#while loops
i = 1
while i <= 10:
    print(i ** 2)
    i += 1

heroes = ["Batman", "Superman", "WonderWoman", "Flash", "Aquaman"]
i = 0
while i < len(heroes):
    print(heroes[i]) #traversing
    i += 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0 
x = int(input("Enter a number to search in the tuple: "))
while i < len(nums):
    if nums[i] == x:
        print (f"{x} is found in the given tuple at index {i}.")
        break
    else:
        print("finding...")
    i += 1

i = 0
while i <= 5:
    if i == 3:
        print("Skipping 3")
        i += 1
        continue
    print(i)
    i += 1

n = int(input("Enter a natural number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1  
print(f"The sum of first {n} natural numbers is {sum}.")

#for loops
str = "prachiarora"
for char in str:
    print(char)

for i in range(1, 11):
    print (i ** 2)

y = int(input("Enter a number to search in the tuple: "))
idx = 0
for val in nums:
    if val == y: #linear search
        print(f"{y} is found in the given tuple at index {idx}.")
        break
    idx += 1

table = int(input("Enter a number to print its table: "))
for i in range (1, 11):
    print(table * i) 

n = int(input("Enter a number to print its factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"The factorial of {n} is {fact}.")

#functions
nums = [2, 5, 6, 4, 8, 9, 3, 5, 2, 6, 7]
def print_list(list):
    for i in list:
        print(i, end = " ")

print_list(nums)
print()

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        for i in range(1, n):
            n *= i
        print(n)
        return n

factorial(5)

def convert(usd):
    inr = usd * 82.5
    print(f"{usd} USD = {inr} INR")
    return inr

convert(10)

def num(n = 0):
    #n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")

num()

#recursive function, recursion have specific use cases
def show(n):
    if n == 0:
        return #base case, or stop condition
    else:
        print(n)
        show(n - 1)

show(5)

def factorial2(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial2(n - 1) #recurrence relation
    
print(factorial2(0))

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1) #call stack
    
print(sum(5))
    
def print_list1(list1, index = 0):
    if index == len(list1):
        return
    else:
        print(list1[index])
        print_list1(list1, index + 1)

print_list1(nums)