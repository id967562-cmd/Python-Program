try:
    x=10/0 #This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    num = int(input("Enter a number:"))
    result = 10/num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")

#Alternative using a tuple:
try:
    nums = int(input("Enter a number: "))
    result = 10 / nums
except(ZeroDivisionError,ValueError)as e:
    print(f"An error occurred: {e}")

# Using  else and finally 
try:
    #Cod that might cause an exception
    num = int(input("Enter a number: "))
    result = 100/num

except ValueError:
    print("Enter an integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:",result)
finally:
    print("Program execution attempted.")

#raise :- Used to intentionally generate an exception(error) when a condition
#         in your program is not allowed.
  
age = 15

if age < 18:
    raise ValueError("You must be 18 or older!")

print("You are allowed")

# Another example of raise
class InsufficientBalanceError(Exception):
    pass

balance = 500
withdraw = 800

if withdraw > balance:
    raise InsufficientBalanceError("Not enough money!")

#Custom Exception :- Used to intentionally generate an exception(error) when a condition in your program is not allowed.
class InsufficientBalanceError(Exception):
    pass

balance = int(input("Enter the bankBalance: "))
withdraw = int(input("Enter amount you want to withdraw: "))

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance!")

    balance -= withdraw
    print("Withdrawal successful")

except InsufficientBalanceError as e:
    print(e)

print("Program continues")