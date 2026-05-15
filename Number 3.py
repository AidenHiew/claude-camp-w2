#a new version of the code with a new function to get a number from the user and print it out.

def main():
    x = get_int("What's the number of X?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not a number")
        else:
            break
    return x

print("Welcome to the number program!")



if __name__ == "__main__":
    main()

