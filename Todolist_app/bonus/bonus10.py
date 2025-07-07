try:
    length = float(input("Enter the length of rectangle:"))
    breadth = float(input("Enter the breadth of rectangle:"))
    if breadth == length:
        exit("That is a square")

    area = length * breadth
    print(area)
except ValueError:
    print("Please enter a number.")
    
