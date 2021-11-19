name = input("Name:")
gender = input("Gender:")
gender = gender.capitalize()
age = int(input("Age(Year):"))
weight = int(float(input("Weight(kilogram):")))
height = int(float(input("Height(inch)(If you want to give your height in centimetre,press 0):")))
if height == 0:
    height = int(input("Heigh(Centimetre):"))
else:
    height = height * 2.54
if gender == "Male":
    bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
elif gender == "Female":
    bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
print("Name:",name)
print("Gender:",gender)
print("Age:",age)
print("Weight:",weight,"kg")
print("Height:",height,"cm")
print("BMR:",bmr)
exit = int(input("Do you want to exit?,press 0 to exit:"))
while True:
    if exit == 0:
        break
print("[Program finished]")