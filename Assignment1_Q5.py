def function1(science,maths,history):
    print(f"Marks in science: {science}")
    print(f"Marks in Math: {maths}")
    print(f"Marks in History: {history}")
    avg = (science + maths + history)/3
    print(f"Average = {avg}")
    if avg >= 90 and avg <= 100:
        print(f"Passed with A grade")
    elif avg >= 80 and avg <= 89:
        print(f"Passed with B grade")
    elif avg >= 70 and avg <= 79:
        print(f"Passed with C grade")
    elif avg >= 60 and avg <= 69:
        print(f"Passed with D grade")
    elif avg >= 0 and avg <= 59:
        print(f"F grade Poor performance")
    else:
        print(f"Invalid result")

function1(90,92,99)                           
