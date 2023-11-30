class User:

    def __init__(self, first_name, last_name, age, course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course

    def describe_user(self):
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course.title()}")

    def greet_user(self):
        print(f"\nHello, {self.first_name.title()}")


user_one = User('rein', 'solis', age=20, course='information technology')
user_two = User('kian', 'padilla', age=20, course='language and literature')
user_three = User('rhanniel', 'villanueva', age=20, course='nursing')

user_one.describe_user()
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()

user_three.describe_user()
user_three.greet_user()
