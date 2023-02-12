class rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.area = self.__length * self.__width

    def __lt__(self, other):
        return self.area < other.area

r1 = rectangle(30, 25)
r2 = rectangle(65, 39)

print(r1 < r2)