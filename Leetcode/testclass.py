import sys

class Pointer():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def squared(self):
        return self.x ** self.y
    def getMap(self):
        string = ""
        for i in range(self.y):
            for j in range(self.x):
                string += str(i + 1) + "\t"
            string += "\n"
        return string


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    point = Pointer(x, y)
    print(point.squared())
    print(point.getMap())