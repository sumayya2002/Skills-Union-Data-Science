#############Task 1##############

# Integers

my_int = 3
print('My integer is ' + str(my_int) +'.')
# Floats

my_flt = 3.4
print('My float is ' + str(my_flt) +'.')

# Strings
my_str = 'Hello World'
print(my_str)

# Boolean
my_bool = True
print(my_str)

# Lists

my_list = ['Apple', 'Banana', 'Orange', 'Watermelon', 'Peach']
print(my_list)


# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Dictionaries

my_dict = {'Apple':1, 'Banana':2, 'Orange':3, 'Watermelon':4, 'Peach':5}
print(my_dict)


#################Task 2############

def count_and_return_vowels(text):
    
    vowels = "AaEeIiOoUu"
    vowel_count = 0
    vowel_list = []

    for i in text:
        if i in vowels:
            vowel_count += 1
            vowel_list.append(i)
    return vowel_count, vowel_list
 



print(count_and_return_vowels("Hello World")) # output: (3, ['e', 'o', 'o'])
print(count_and_return_vowels("Programming")) # output: (3, ['o', 'a', 'i'])
print(count_and_return_vowels("OpenAI")) # output: (2, ['O', 'e', 'A', 'I'])


def sum_of_even_numbers(limit):
    total = 0

    for i in range(1,limit+1):
        if i % 2 == 0:
            total += i
            
    return total
    


print(sum_of_even_numbers(10)) # output: 30
print(sum_of_even_numbers(5)) # output: 6
print(sum_of_even_numbers(1)) # output: 0


class BankAccount:
    """
    Create a BankAccount class with:
    - Constructor that sets initial balance
    - deposit() method that adds money
    - withdraw() method that removes money if sufficient funds exist
    - get_balance() method that returns current balance
    """
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, deposit_value):
        
        self.balance += deposit_value

    def withdraw(self, wd_amount):
        if wd_amount <= self.balance:
            self.balance -= wd_amount
        else:
            print("Insufficient Funds")
        
    def get_balance(self):
        return self.balance




account = BankAccount(100)
print(account.get_balance())  # output: 100
account.deposit(50)
print(account.get_balance())  # output: 150
account.withdraw(30)
print(account.get_balance())  # output: 120
account.withdraw(200)  # Should print: "Insufficient funds"
print(account.get_balance())  # output: 120