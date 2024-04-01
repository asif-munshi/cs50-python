import sys


def main():
    # Check for errors
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    
    # Print name tags
    for arg in sys.argv[1:]:
        print("Hello, my name is", arg)
    
main()