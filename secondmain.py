1
import random
import math

def calculate_sum_of_square_roots():
    total_sum = 0
    
    for _ in range(1000):
        num = random.randint(0, 100)
        
        if num % 5 == 0 and num % 2 == 0:  # Check for even multiples of 5
            total_sum += math.sqrt(num)
    
    return total_sum

result = calculate_sum_of_square_roots()
print("Sum of square roots of even multiples of 5:", result)

2
import random
import math

def calculate_sum_of_square_roots():
    total_sum = 0
    
    for _ in range(1000):
        num = random.randint(0, 100)
        
        if num % 5 == 0 and num % 2 == 0:  # Check for even multiples of 5
            total_sum += math.sqrt(num)
    
    return total_sum

def capitalize(word):
    return word.capitalize()

sia = ["donkey", "dog", "dingo"]
capitalized_sia = list(map(capitalize, sia))

result = calculate_sum_of_square_roots()
print("Sum of square roots of even multiples of 5:", result)
print("Capitalized list:", capitalized_sia)

3
import random
import math

def calculate_sum_of_square_roots():
    total_sum = 0
    
    for _ in range(1000):
        num = random.randint(0, 100)
        
        if num % 5 == 0 and num % 2 == 0:  # Check for even multiples of 5
            total_sum += math.sqrt(num)
    
    return total_sum

def capitalize(word):
    return word.capitalize()

sia = ["donkey", "dog", "dingo"]
capitalized_sia = list(map(capitalize, sia))

grades = [["Apple", 8], ["Banna", 9],["Peach", 3]]

student_count = sum(1 for _ in grades)  # Counting elements without len()
max_grade = max(grade for _, grade in grades)

result = calculate_sum_of_square_roots()
print("Sum of square roots of even multiples of 5:", result)
print("Capitalized list:", capitalized_sia)
print("Number of students:", student_count)
print("Maximum grade:", max_grade)

4
import random

# Step 1: Create an empty list
numbers = []

# Step 2: Fill it with 100 random numeric elements (from 1 to 1000)
numbers = [random.randint(1, 1000) for _ in range(100)]

# Step 3: Separate even and odd numbers
even_numbers = tuple(num for num in numbers if num % 2 == 0)
odd_numbers = {num for num in numbers if num % 2 != 0}

# Print results
print("Even numbers (tuple):", even_numbers)
print("Odd numbers (set):", odd_numbers)

5
class List:
    def __init__(self, lst):
        self.lst = lst
        print("List:", self.lst)
        print("Sum of elements:", sum(self.lst))
        print("Minimum element:", min(self.lst))
        print("Maximum element:", max(self.lst))
    
    def chamateba(self, index, element):
        self.lst.insert(index, element)
        print("Updated List after chamateba:", self.lst)
    
    def cashla(self, element):
        if element in self.lst:
            self.lst.remove(element)
            print("Updated List after cashla:", self.lst)
        else:
            print("Element not found in list.")

# Example usage:
list_obj = List([3, 7, 2, 9, 5])
list_obj.chamateba(2, 10)
list_obj.cashla(7)

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")
    
    def get_balance(self):
        return self.balance

# Example usage:
bank_account = BankAccount("123456", "John Doe", 500)
bank_account.deposit(200)
bank_account.withdraw(100)
print("Final Balance:", bank_account.get_balance())
