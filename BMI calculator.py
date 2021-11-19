import time
your_weight=float(input("Weight in kilogram:"))
yourheightinch=float(input("Height in inch:"))
yourheight=yourheightinch/ 39.37
your_height=yourheight ** 2
your_bmi=your_weight / your_height
print("Calculating....")
time.sleep(3)
print("Your BMI is"," ",your_bmi,)
if your_bmi<18.5:
    print("Your weight is too low")
elif your_bmi<24.9:
    print("Your weight is normal")
elif your_bmi<29.9:
    print("Your weight is overweight")
elif your_bmi<34.9:
    print("You are in the first level of fat")
elif your_bmi<39.9:
    print("You are in the second level of fat")
else:
    print("Your life is in danger")
print("[Program Finished.]")
while True:
    choice = int(input("Press 0 to exit:"))
    if choice == 0:
        break
