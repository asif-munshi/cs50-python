def main():
    number = getNumber()
    meow(number)
    
def getNumber():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")
        
main()