# division by zero error
try:
    result=10/0
except ZeroDivisionError as e:
    print(f"Error:{e}")

#Name error
try:
    print(vriable_not_found)
except NameError as e:
    print(f"Error:{e}")

#Type error
try:
    sum01="Hello"+4
except TypeError as e:
    print(f"Error:{e}")

#ValueError
try:
    number=int("abc")
except ValueError as e:
    print(f"Error:{e}")

#File not found error
try:
    with open("nonexistent_file.txt","r")as file:
        content=file.read()
except FileNotFoundError as e:
    print(f"Error:{e}")

#user defined exception
class AgeBelow18(Exception):
    def __init__(self,message="Not eligible to apply for this program"):
        self.message=message
        super().__init__(self.message)

def process_age(age):
    if age<=18:
        raise AgeBelow18()
    else:
        print("You are eligible to apply for the program")

try:
    user_age=int(input("Enter your age:"))
    process_age(user_age)
except AgeBelow18 as e:
    print(f"{e}")
except ValueError as e:
    print("Invalid input.Please enter a valid integer for age.")


