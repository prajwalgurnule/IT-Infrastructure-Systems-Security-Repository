def calculateArea(length, width):
    area = (length * width) / 2
    if length == width:
        print(f"The area of square is {area}")
    else:
        print(f"The area of rectangle is {area}")

calculateArea(2, 3)
calculateArea(4, 4)