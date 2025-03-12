def check_num(number):
    if 100 <= number <= 999:
        firstnumber = number // 100
        lastnumber = number % 10
        if firstnumber == lastnumber:
            print("True")
        else:
            print("False")
    else:
        print("Enter a number between 100 and 999")

number = int(input("Enter a number: "))
check_num(number)
