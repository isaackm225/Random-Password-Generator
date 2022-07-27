def ui()->tuple():
    """Returns tuple of bools for symboles,digits and an int for len of pwd"""

    while True:
        print("Please enter Y to enable any of these options.")
        print("Or leave blank to disable.")
        s=bool(input("Add symboles? "))
        d=bool(input("Add digits? "))
        l=input("Please enter the length of your password as an integer: ")
        try:
            l=int(l)
        except:
            print("Please enter a integer!!")
        if type(l) is int:
            return s,d,l
        else:
            print("Let's retry!")
            
       

    
