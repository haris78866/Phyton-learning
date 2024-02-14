# Large Python Code Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}, and I'm {self.age} years old.")

def calculate_square(num):
    return num ** 2

def main():
    # Creating a list of persons
    people = [
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 22)
    ]

    # Greeting each person
    for person in people:
        person.greet()

    # Calculating squares of numbers
    for i in range(1, 11):
        square = calculate_square(i)
        print(f"The square of {i} is {square}")

if __name__ == "__main__":
    main()
