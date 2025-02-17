 1

    import random


    def multiplication():
        tp = tuple(random.randint(1, 100) for _ in range(5000))
        ans = 1
        for num in tp:
            if num % 17 == 0 and num % 2 == 0:
                ans *= num ** (1 / 3)

        return ans


    print(multiplication())


 2

 def fib(num, memo=None):
     if memo is None:
         memo = {}
     if num in memo:
         return memo[num]
     if num == 0:
         return 0
     elif num == 1:
         return 1
     else:
         memo[num] = fib(num - 1, memo) + fib(num - 2, memo)
         return memo[num]


 lst = [15, 3, 21, 32]
 ans = map(fib, lst)
 print(list(ans))

 3

 def products(ls):
     return sum([product[1] for product in ls])


 pr = [['apple', 8], ['banana', 4], ['orange', 6]]
 print(products(pr))


 def students(ls):
     max_point = 0
     ans = 0
     for student in ls:
         if student[1] > max_point:
             max_point = student[1]

         ans += 1

     return f"Max Point is: {max_point} and the total number of students is {ans}"


 pr = [['peter', 8], ['gela', 4], ['romani', 6]]
 print(students(pr))

 4
 import random


 def list_tuple_set():
     lst = [random.randint(1, 100) for _ in range(100)]
     tp = ()
     st = set()
     for num in lst:
         if num % 2 == 0:
             tp += (num,)
         else:
             st.add(num)

     return f"list: {lst}\nTuple: {tp}\nSet: {st}"


 print(list_tuple_set())

 5


 class List:

     def __init__(self, lst):
         self.lst = lst
         print(self.lst)

     def calculate_sum_min_max(self):
         print(f'Sum: {sum(self.lst)}')
         print(f'Min: {min(self.lst)}')
         print(f'Max: {max(self.lst)}')

     def chamateba(self, index, element):
         self.lst.insert(index, element)
         print("Element added")

     def cashla(self, element):
         if element in self.lst:
             self.lst.remove(element)
         else:
             print("Element not found")


 my_list = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
 my_list.calculate_sum_min_max()
 my_list.chamateba(3, 100)
 my_list.cashla(10)
 my_list.calculate_sum_min_max()


 6


class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Amount {amount} deposited successfully. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Amount {amount} withdrawn successfully. Current balance: {self.balance}"


account = BankAccount(123456, 'Romani', 1000)
print(account.deposit(500))
print(account.withdraw(2000))
print(account.withdraw(500))
