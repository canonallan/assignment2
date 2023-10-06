#SCT211-0019/2020
#Chikombe Canon Allan


from datetime import datetime


current_date = datetime.now()


year_of_birth = int(input("Enter your year of birth: "))


age = current_date.year - year_of_birth

birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

if birth_month > current_date.month or (birth_month == current_date.month and birth_day > current_date.day):
    age -= 1

print(f"You are {age} years old.")
