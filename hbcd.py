# Exam Eligibility Check
# Outline:
# Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
# Project:
# https://replit.com/~
# Electricity bill
# Outline:


presentper=int(input("Enter the days he is prent percentage "))
medical=input("Enter the medical cause Y or N ")  
if medical=="Y" :
  print("OKAY ,YOU ARE ALLOWED")
else:
  if presentper>75:
    print("OKAY ,YOU ARE ALLOWED")
  else:
    print("OKAY ,YOU ARE Not ALLOWED")

# Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
# Project:
# https://replit.com/~

# Take input of number of units consumed from the user
units = int(input(" Please enter Number of Units you Consumed : "))

# Check conditions of units consumed 
# Then calculate amount and surcharge accordingly
# surcharge is the tax value

# Check for units less than 50
if(units < 50):
    amount = units * 2.60 
    surcharge = 25 

# Check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# Check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

# Check for all the cases other than mentioned 
# When units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

# Calculate and Display the total electricity bill
# total amount = amount + surcharge
total = amount + surcharge
print("\nElectricity Bill = %.2f"  %total)


