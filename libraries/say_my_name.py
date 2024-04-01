import sys

from sayings import goodbye, hello


def main():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        
        hello(name)
        goodbye(name)
    
main()