def main():
    x = getInt("What's x? ")
    print(f"x is {x}")


def getInt(prompt):
    while True:
        try:
           x = int(input(prompt))
           return x
        except ValueError:
            pass

main()