import os
import time

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

print("\t\t\t*LEAP IT*", flush= False)
time.sleep(1)
print("\nI will help you check if your given year is a leap year or not.")

while True:
    try:
        time.sleep(2)
        year = int(input("\nEnter the year: "))
        
    except ValueError:
        time.sleep(1)
        print("\nInvalid Input please try again.")
        continue
    
    x = str(year)
    length = len(x)
    
    if length < 4:
        time.sleep(1)
        print("\nThis is not a year.\nThis a number.")
        time.sleep(1.5)
        print("\nPlease try again.")
        time.sleep(1)
        continue
        
    else:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    time.sleep(1)
                    print("\n{0} is a leap year".format(year))
                else:
                    time.sleep(1)
                    print("\n{0} is not a leap year".format(year))
            else:
                time.sleep(1)
                print("\n{0} is a leap year".format(year))
        else:
            time.sleep(1)
            print("\n{0} is not a leap year".format(year))
    
    time.sleep(1)
    try:
        Again = input("\nTo Check again, Please Enter 'yes' else enter 'no': ")
        
    except:
        print("\nInvalid Input. Please try again later.")
        break
    
    if Again == "yes":
        continue
    
    elif Again == "no":
        print("\nThank You.")
        break
    
    else:
        print("\nInvalid Input please try again later.")
        break