# Question 1
def add_numbers(num1:int, num2:int):
    return num1 + num2
print(add_numbers(1, 6))

#Question 2

def is_even(number):
    return number % 2 == 0
print(is_even(8))

#Question 3

def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))

#Question 4

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)
print(count_vowels("joy"))

#Question 5

def calculate_factorial(n):
    if n == 0: 
        return 1
    return n * calculate_factorial(n - 1)

print(calculate_factorial(4))

#Question 6

def apply_decorator(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

@apply_decorator
def my_function():
    print("Original Function Called")

my_function()

#Question 7

def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

people = [("Joy",12), ("John", 55), ("Charles", 32)]
print(sort_by_age(people)) 

#Question 8

def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {'a': 6, 'b': 12}
dict2 = {'b': 4, 'c': 8}

merged = merge_dicts(dict1, dict2)
print(merged)

#Question 9

class Movie:
    def __init__(self, title, producer, year_released):
        self.title = title
        self.producer = producer
        self.year_released = year_released

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Producer: {self.producer}")
        print(f"Year Released: {self.year_released}")


my_movie = Movie("DeadPool 2", "Marvel Studio", 2024)


my_movie.display_info()



  
