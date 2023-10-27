# Dollars to Euros
## This code will convert dollars to euros.
### Made by Beckett Anderson
dollars = float(input("Enter dollar amount to be converted: "))
euros = dollars * .94540
print("Euros: " + str(euros))
user_input=input("Would you like to convert dollars to euros? (y/n)")
while user_input == "y":
      dollars = float(input("Enter dollar amount to be converted: ")) 
      euros = dollars * .94540
      print("Euros: " + str(euros))
      user_input=input("Would you like to convert dollars to euros? (y/n)")
##Program has ended
