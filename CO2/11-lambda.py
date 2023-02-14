s = int(input("Enter side of square: "))
sqr = lambda s: s * s
print(sqr(s))
print()

l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
rect = lambda l, b: l * b
print(rect(l, b))
print()

b1 = int(input("Enter base of triangle: "))
h = int(input("Enter height of triangle: "))
tri = lambda b1, h: b1 * h / 2
print(tri(b1, h))
print()
