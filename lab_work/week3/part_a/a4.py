def grading_calculator():
    marks = int(input("Enter your marks: "))

    if marks in range(70, 101):
        print("First Class")
        grading_calculator()
    elif marks in range (60, 70):
        print("Upper Second")
        grading_calculator()
    elif marks in range (50, 60):
        print("Lower Second")
        grading_calculator()
    elif marks in range(40, 50):
        print("Pass")
        grading_calculator()
    elif marks in range(0, 40):
        print("Fail")
        grading_calculator()
    else:
        print("Invalid marks entered (must be positive integer 0-100)")
        grading_calculator()


grading_calculator()