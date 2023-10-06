#SCT211-0019/2020
#Chikombe Canon Allan



weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))


bmi = weight / (height ** 2)


if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "normal weight"
else:
    category = "overweight"


print(f"Your BMI is {bmi:.2f}, which is considered {category}.")
