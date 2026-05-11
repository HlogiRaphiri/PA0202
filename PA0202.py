#PA0202 - Percentage

#1.1 Write a Python program that asks the user to enter the original price of an item and the discount percentage. The program must calculate the discount amount and the final price after applying the discount, then display both results. simple code

original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_amount = (discount_percentage / 100) * original_price
final_price = original_price - discount_amount

print(f"Discount amount: {discount_amount:.2f}")
print(f"Final price after discount: {final_price:.2f}")

#1.2 Write a Python program that asks the user to enter the marks obtained and the total marks. The program must calculate the percentage and display it. Based on the percentage, print the grade as follows: 75% and above is Distinction, 60%–74% is Merit, 50%–59% is Pass, and below 50% is Fail.

marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))
percentage = (marks_obtained / total_marks) * 100

print(f"Your percentage is: {percentage:.2f}%")

if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: Merit")
elif percentage >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail") 

#1.3 Write a Python program that asks the user to enter their current salary and the percentage increase. The program must calculate the increase amount and the new salary after the increase, then display both values.

current_salary = float(input("Enter your current salary: "))
percentage_increase = float(input("Enter the percentage increase (%): "))
# Calculations
increase_amount = current_salary * (percentage_increase / 100)
new_salary = current_salary + increase_amount

print("\n" + "="*45)
print("SALARY INCREASE CALCULATION (ZAR)")
print("="*45)
print(f"Current Salary      : R {current_salary:,.2f}")
print(f"Percentage Increase : {percentage_increase}%")
print(f"Increase Amount     : R {increase_amount:,.2f}")
print(f"New Salary          : R {new_salary:,.2f}")
print("="*45)


#1.4 Write a Python program that asks the user to enter the cost price and the selling price of an item. The program must calculate the profit or loss and then calculate the percentage using the formula: Profit % = (Profit ÷ Cost Price) × 100. The program should display whether it is a profit or a loss and show the percentage.

cost_price = float(input("Enter the cost price (R): "))
selling_price = float(input("Enter the selling price (R): "))

difference = selling_price - cost_price

if difference > 0:
    percentage = (difference / cost_price) * 100
    print(f"Profit amount: R{difference:.2f}")
    print(f"Profit percentage: {percentage:.2f}%")
elif difference < 0:
    loss = abs(difference)
    percentage = (loss / cost_price) * 100
    print(f"Loss amount: R{loss:.2f}")
    print(f"Loss percentage: {percentage:.2f}%")
else:
    print("No profit and no loss. You broke even.")