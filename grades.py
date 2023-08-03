print("Enter your grade here as a whole number:")
grade = float(input())
if grade >= 90:
    print("Great job! You've received an 'A'.")
elif grade >= 80:
    print("You've received a 'B', nice work!")
elif grade >= 70:
    print("You've received a 'C'. Not bad")
elif grade >= 60:
    print("You've received a 'D'. okay, try a little harder next time")
else:
    print("You have failed the course, better luck next time.")
