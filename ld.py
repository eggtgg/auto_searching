class Person:
    """ Ví dụ về class nguoi
    tên người và tuổi """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print("happy birthday you were", self.age)
        self.age +=1
        print('you are now', self.age)


if __name__ == '__main__':
    tri = Person('tri', 9)
    tri.birthday()
    print(tri)