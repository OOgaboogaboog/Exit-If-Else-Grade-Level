def main():
    #write your code below this line, do not delete any of the other lines
    grade=int(input("Please enter grade number:"))
    if grade <= 100 and grade >= 0:
        if grade <= 100 and grade>= 80:
            print ('4')
        elif grade <= 79 and grade >=70:
            print("3\n")
        elif grade <=69 and grade >= 60: 
            print("2\n")
        elif grade <=59 and grade >=50:
            print("1\n")
        elif grade<=49 and grade >= 0:
            print("0\n")
    elif grade>100 or grade <=-1:
        print("Invalid input!")
if __name__ == '__main__':
    main()
