class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Meoww")

    def grow_up(self):
        self.age = self.age + 1
    
    def print_age(self):
        print(f"age - {self.age}")

cat_blanch = Cat(name = "Blanch", age=4)
cat_blanch.greeting()

cat_blanch.print_age()
cat_blanch.grow_up()
cat_blanch.print_age()
