# --------------------- Project ------------------------------
# Tip Calculator
# ------------------------------------------------------------

# --------------------- Objectives ---------------------------
# Understanding data types and how to manipulate strings
# ------------------------------------------------------------

print("Welcome to the tip calculator !")

bill = float(input("What was the total bill ? RM "))
tip = int(input("What was the percentage tip would you like to give ?\n10, 12, 15 ? "))
people = int(input("How many people to split the bill ? "))

tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay RM {final_amount}")
