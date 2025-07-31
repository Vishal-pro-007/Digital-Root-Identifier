while True:
    try:
        n = int(input("Enter a number(or type 0 to exit): "))
        if n == 0:
            print("Ok, exiting....")
            break

    except ValueError:
        print("Invalid entry, please try again")

    while n >= 10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total

    print(f"Digital root of this number is: {n}






            
