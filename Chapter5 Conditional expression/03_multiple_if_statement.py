Age = int(input("Enter your age: "))

# multiple if statement
# If statement number 1
if (Age%2 == 0):
    print("The number is even.")

# End of if statement number 1

# If statement number 2
if (Age>= 18):
    print("You are eligible to vote.\nGood for you.")

elif (Age<0):
    print("Invalid negative age entered.")

elif(Age==0):
    print("You entered 0, You are not eligible to vote.")

else:
    print("You are not eligible to vote.")

# End of if sattement number 2

print("End of the program.")

