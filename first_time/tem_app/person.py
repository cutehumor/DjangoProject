class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"我叫：{self.name};我今年{self.age}岁。"
