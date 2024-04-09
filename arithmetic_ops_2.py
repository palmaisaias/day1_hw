#TASK 2 will attempt to calculate interest accumulated

# b_a = 140,000
# i_r = 5

# total = (i_r / b_a) * 100

# ^this was my FIRST attempt. Did't work due to operation type error and what is obviously bad math

# bank_account = 140000  #decided to be more clear with variable names
# interest_rate = .05  #5% as a decimal

# interest_earned = interest_rate * bank_account

# print(interest_earned)

# ^SECOND attempt. Forgot formula to add the original bank account amount. Also, print result could be cleaner.

bank_account = 140000
interest_rate = .05

interest_earned = interest_rate * bank_account

end_of_year = interest_earned + bank_account

print('End of year total is $', end_of_year)  

#would like to get the double zeros after the decimal on the float. Don't know how.