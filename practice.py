class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        print("Person initialized")


class Student(Person):
    def __init__(self, name, height, status, adjective):
        super().__init__(name, height)
        self.status = status
        self.adjective = adjective
        print("Student initialized")


Yahya = Student("Yahya", 173, "extremely high", "Fearless")

print(f"{Yahya.name} is {Yahya.height} cm tall, {Yahya.status} status and is {Yahya.adjective}.")