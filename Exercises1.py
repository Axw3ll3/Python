
#Exercise 1
my_name = "Axel";

my_age = 12;

Str = f"My name is  {my_name} and I am {my_age} years old.";
print(Str);


#Exercise 2
original_string = "Python is an amazing progamming language";

first_word = original_string.split()[0]

uppercase_string = original_string.upper()

modified_string = original_string.replace('a', '@')
print ("First word: ", first_word)
print ("Uppercase word: ", uppercase_string)
print ("Modified string: ", modified_string)

#Exercise 3
favourite_foods = ["Pizza", "Sushi", "Ice Cream"]

favourite_foods.append("Burger")

favourite_foods.pop(0)

middle_index = len(favourite_foods)//2

middle_item = favourite_foods[middle_index]

print("Middle item: ", middle_item)

food_starting_with_p = [food for food in favourite_foods if food.lower().startswith('p')]

print("Updated list:", favourite_foods)
print("Foods starting with p:", food_starting_with_p)

#Exercise 4
numbers = list(range(1, 11))

even_numbers = [num for num in numbers if num % 2 == 0]

squared_numbers = [num ** 2 for num in numbers]

divisible_by_2_and_3 = [num for num in numbers if num % 2 == 0 and num % 3 == 0]

print("Even numbers: ", even_numbers)
print("Squared numbers: ", squared_numbers)
print("Divisible by 2 & 3: ", divisible_by_2_and_3)

#Exercise 5
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

student_scores["David"] = 88

student_scores["Alice"] = 95

students_above_90 = [name for name, score in student_scores.items() if score > 90]
print ("Students wit scores above 90: ", students_above_90)

average_score = sum(student_scores.values()) / len(student_scores)
print ("Average score: ", average_score)

#Exercise 6
squares = {num: num**2 for num in range (1,6)}

string_representations = {num: str(num) for num in range (1,6)}

odd_numbers = {num: num for num in numbers in range(1, 6) if num % 2 != 0}

print ("Squares:", squares)
print ("String representations:", string_representations)
print ("Odd numbers:", odd_numbers)

#Exercise 7
def grade_calculator(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print (grade_calculator(85))


#Exercise 8
def calculate_total(price, tax_rate, discout):
    if price < 0 or tax_rate < 0 or discout < 0:
        return "Error: All parameters must be a positive number."

    final_price = price * (price * tax_rate) - discount
    return f"{final_price:.2f}"


#Exercise 9
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def calculate_age(self, current_year):
        return current_year - self.year

    def get_info(self):
        return f"'{self.title}', by '{self.author} {(self.year)}'"

    my_book = Book("1984", "George Orwell", 1949)
    print (my_book.get_info())
    print ("Book age:", my_book.calculate_age(2025))

#Exercise 10
class Car:
    def move(self):
        return "The car is driving"

class Bicycle:
    def move(self):
        return "The bicycle is pedaling."

def test_movement(vehicle):
    print (vehicle.move())

car = Car()
bike = Bicycle()
test_movement(car)
test_movement(bike)

#Exercise 11
global_variable = 10

def modify_local():
    global_variable = 20
    print("Inside modify_local", global_variable)

def modify_global():
    global global_variable
    global_variable = 30
    print("Inside modify_global", global_variable)

print("Before modification:", global_variable)
modify_local()
print("After modify_local", global_variable)
modify_global()
print("After modify_global:", global_variable)

#Exercise 12
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers.")
        return None
    return result

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))