def main():
    name = input("What's your name? ").strip().title()

    # Say hello to user
    hello(name)
    
def hello(to="world"):
    print(f"Hello, {to}!")
    
main()