"""module with all classes"""

class Item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name}'
    def __eq___(self, other):
        return self.name == other.name

class Street:
    def __init__(self, name, linked_streets, character=None, item=None):
        self.name = name
        self.linked_streets = linked_streets
        self.character=character
        self.item=item
    def __str__(self):
        return f'---зараз ви тут: {self.name}---'
    def choose_next(self):
        """method to choose the next street to go on"""
        for item in self.linked_streets.items():
            print(item[0], item[1])
        number = 0
        while number not in self.linked_streets.keys():
            try:
                number = int(input(">>> "))
                if number not in self.linked_streets.keys():
                    if number == 5:
                        return 5
                    else:
                        print("спробуйте ще раз, неправильний номер")
            except:
                print("спробуйте ще раз, неправильний номер")
        return self.linked_streets[number]
    def set_character(self, character):
        self.character = character
    def move(self, side):
        return self.linked_streets[side]

class People:
    def __init__(self, name, conversation=""):
        self.name = name
        self.conversation = conversation
    def __str__(self):
        return f"{self.conversation}"
    def __eq__(self, other):
        return self.name == other.name

class Friend(People):
    def __init__(self, name, conversation="", item=None):
        super().__init__(name, conversation)
        self.item = item
    def take_item(self):
        print(f"тепер у вас ще є {self.item}")
        return self.item


class Enemy(People):
    def __init__(self, name, conversation="", weakness=None):
        super().__init__(name, conversation)
        self.weakness = weakness
    def take_weakness(self):
        print(f'доведеться віддати {self.weakness}!')
        return self.weakness
