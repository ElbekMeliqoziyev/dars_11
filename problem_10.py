"""User klassi va undan meros olgan AdminUser
 va RegularUser klasslarini yarating. """

class User:
    def __init__(self, name):
        self.name = name

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
    