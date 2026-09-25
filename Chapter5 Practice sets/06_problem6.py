marks = int(input("Enter your total marks: "))


if ((marks>=90) and (marks<=100)):
    print("You obtained Ex grade with", marks)
elif((marks>=80) and (marks<90)):
    print("You obtained A grade with", marks)
elif((marks>=70) and (marks<80)):
    print("You obtained B grade with", marks)
elif((marks>=60) and (marks<70)):
    print("You obtained C grade with", marks)
elif((marks>=50) and (marks<60)):
    print("You obtained D grade with", marks)
elif((marks>=40) and (marks<50)):
    print("You obtained F grade with", marks)
else:
    print("Invalid marks")
    
    