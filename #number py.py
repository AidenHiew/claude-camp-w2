#number py
while True:
    try:
        x = int(input("what's X?"))
        y = int(input("what's Y?"))
    except ValueError:
        print("x or y is not a number")
    else:
        print(f"x is {x}, y is {y}")
        break 
