#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ("Welcome to the tip calculator.")

while True:
    try:    
        total_bill = float(input("What was the total bill? $"))
        # to get the bill
    except ValueError:
        print("Invalid input. Please enter a numeric value for the bill amount.")
        break  # Continue to the next iteration of the loop

    try:    
        percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
        # to get the percentage tip
    except ValueError:
        print("Invalid input. Please enter a numeric value for the tip percentage.")
        continue  # Continue to the next iteration of the loop

    is_splitting = input("Are you splitting the bill? ")

    if is_splitting == "Yes" or is_splitting == "yes":
    
        people_splitting = int(input ("How many people are to split the bill? "))

        to_get_bill = ((percentage_tip / 100) * total_bill) + total_bill

        ind_bill = to_get_bill / people_splitting 

        final_ind_bill = round (ind_bill, 2)

        print (f"Each person should pay: ${final_ind_bill}")
        break
    
    elif is_splitting == "No" or is_splitting == "no":
    
        to_get_bill = ((percentage_tip / 100) * total_bill) + total_bill
    
        final_ind_bill = round (to_get_bill, 2)
    
        print (f"Your final bill is {final_ind_bill }")
        break
        
    else:
        print ("Invalid input. Try again.")
        break 
        

print ("Thank you for using the tip calculator")

