def check_number(number):
    if number < 2:
        print("Alert: The number is less than 2!")
    else:
        print("The number is 2 or greater.")

# Example usage:
number = float(input("Enter a number: "))
check_number(number)
