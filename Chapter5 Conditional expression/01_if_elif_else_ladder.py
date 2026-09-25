Age = int(input("Enter your age: "))

# if, elif, else ladder 

if (Age>= 18):
    print("You are eligible to vote.\nGood for you.")

elif (Age<0):
    print("Invalid negative age entered.")

elif(Age==0):
    print("You entered 0, You are not eligible to vote.")

else:
    print("You are not eligible to vote.")

print("End of the program.")