import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]: #slicing
    print("my anme is ", arg)
    
#python has packages to have access of different libraries3
#pypi.org let you access them
#APIs stands for application programming interface third party services
#json java script object notation
# __name__ == "__main__ "