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

if __name__ == "__main__":
    main()
