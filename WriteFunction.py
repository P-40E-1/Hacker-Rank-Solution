#leap year 

def main():
    year = int(input("Enter Year: "))

    if leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

#this function checks if the given year is leap year or not
def leap_year(num):
    if isinstance(num, int):
        if num % 4 == 0:
            if num % 100 == 0:
                if num % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False

if __name__=="__main__":
    main()
