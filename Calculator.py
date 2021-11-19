import math

def add():#1st option
    times = int(input("Sum:\nHow many number do you want to sum:"))
    nums = []
    for i in range(times):
        num = float(input("Enter your number:"))
        nums.append(num)
    result = sum(nums)
    return result

def subtraction():#2nd option
    times = int(input("Subtraction\nHow many number do you want to add for subtraction:"))
    nums = []
    for i in range(times):
        num = float(input("Enter your number:"))
        nums.append(num)
    result = nums[0]
    nums.remove(result)
    for i in nums:
        result -= i
    return result

def multiplication():#3rd option
    times = int(input("Multiplication:\nHow many number do you want to add for multiplication:"))
    nums = []
    for i in range(times):
        num = float(input("Enter your number:"))
        nums.append(num)
        result = 1
    for i in nums:
        result *= i
    return result

def division():#4th option
    print("Division:")
    divisible = float(input("Enter the divisible:"))
    divisor = float(input("Enter the divisor:"))
    result = divisible / divisor
    result1 = int(divisible // divisor)
    result2 = int(divisible % divisor)
    print("Quotient =",result1,",Remainder =",result2,end = ",")
    return result

def power():#5th option
    print("Power based math")
    base = float(input("Enter the base:"))
    power = float(input("Enter the power:"))
    result = math.pow(base,power)
    return result

options = "This is a calculator program.\n1)Press 1:Addition\n2)Press 2:Subtraction\n3)Press 3:Multiplication\n4)Press 4:Division\n5)Press 5:Power based math"
print(options)

while True:
    choice = input("Enter your choice:")
    try:
        choice = int(choice)
        break
    except:
        print("Invaild choice!")
        break

if choice == 1:
    result = add()

elif choice == 2:
    result = subtraction()

elif choice == 3:
    result = multiplication()

elif choice == 4:
    result = division()

elif choice == 5:
    result = power()

try:
    print("Your result is ", result)
except:
    print("An error occured!")
print("[Program finished]")
