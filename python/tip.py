#SCT211-0019/2020
#Chikombe Canon Allan

bill_amount = float(input("Enter the bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))


tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount


amount_per_person = total_amount / num_people


print(f"Each person should pay: ${amount_per_person:.2f}")
