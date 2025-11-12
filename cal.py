def main():
    x = int(input("whats a x?"))
    if is_even(x):
        print("even")

    else:
        print("odd")
    
def is_even(x):
    if x % 2 == 0: #you can minimize   these line of codes ny writing instead // return True if  n% 2 == 0 else False
        return True # iminmize further write // return (n% 2 == 0) since this itslef is a bool
    
    else:
        return False
    
main()