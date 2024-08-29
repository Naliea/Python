class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old, and I am a {self.gender}.")


# Create an instance of the Person class
person_instance = Person(name="John Doe", age=30, gender="male")

# Call the introduce method
person_instance.introduce()