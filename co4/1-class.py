class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)

    def perimeter(self):
        return (2 * (self.length + self.breadth))


rect1 = rectangle(23, 40)
rect2 = rectangle(78, 94)

area1 = rectangle.area(rect1)
area2 = rectangle.area(rect2)

pm1 = rectangle.perimeter(rect1)
pm2 = rectangle.perimeter(rect2)

print("\nArea of rectangle 1:", area1)
print("Perimeter of rectangle 1:", pm1, "\n")
print("Area of rectangle 2:", area2)
print("Perimeter of rectangle 2:", pm2, "\n")

if (area1 > area2):
    print("Rectangle 1 is larger.\n")
elif (area2 > area1):
    print("Rectangle 2 is larger.\n")
else:
    print("Both rectangles are equal in area.\n")
