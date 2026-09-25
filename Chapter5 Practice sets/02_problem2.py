science = int(input("Enter the marks obtained in science: "))
maths = int(input("Enter marks obtained in maths: "))
health = int(input("Enter the marks obtained in health: "))

# check total percentage
total_percentage = (100*(science + maths + health)) / 300

if (total_percentage>=40 and science>=33 and maths>=33 and health>=33):
    print("You are passeed your total percentage is", total_percentage)
else:
    print("Student has failed the exam, Try again next year")


