class MyClass:
    zahl = 42
    string = "zeichenkette"
    list = []

    def __init__(self, buchstabeneu='a'):
        self.buchstabe = buchstabeneu
        self.list = []

    def do_something(self, neuezahl):
        self.zahl = neuezahl
        self.list.append(neuezahl)

instanz = MyClass('Z')
instanz2 = MyClass('b')
instanz.do_something(1337)
print(instanz.list)

