#_______________________________________________________________________________________________________________________________

#                                                    Day of the Week Calculator
#-------------------------------------------------------------------------------------------------------------------------------
# Python 3
# Gautam D - 2018
# Formula taken from the book 'Murderous Maths : The Perfect Sausage' by Kjartan Poskitt, published by Scholastic
#-------------------------------------------------------------------------------------------------------------------------------

def dayofweek(date, month, year):
    
    a = (14 - month) // 12
    b = year - a
    c = month + 12*a - 2
    day = (date + b + (31*c // 12) + (b//4) - (b//100) + (b//400)) % 7

    return day


    
if __name__ == '__main__' :

    print("_______________________________________________________________\n")
    print("                 Day of the week calculator                    ")
    print("_______________________________________________________________\n")
    print("Find the day of the week for any given date since 1 Jan 0000 AD")
    print("[Press Ctrl + C to exit]")
    print("---------------------------------------------------------------")
    while True :
        # Another loop inside this to show an input prompt again even when it is exited using break
        while True :
            try : 
                date = int(input("Enter date (1-31) : "))
                month = int(input("Enter month (1-12) : "))
                year = int(input("Enter year (4-digit) : "))
            except ValueError :
                print("Error - Please enter valid numbers for date, month and year")
                print("---------------------------------------------------------------")
                break
            if date < 1 or date > 31 or month < 1 or month > 12 or year < 0 :
                print("Error - Please enter valid numbers for date, month and year")
                print("---------------------------------------------------------------")
                break
                
            print("    Calculating...\n")
            
            day = dayofweek(date, month, year)
            days = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
            print("%d-%d-%d is a %s" % (date, month, year, days[day]) )   
            print("---------------------------------------------------------------")
#_______________________________________________________________________________________________________________________________
