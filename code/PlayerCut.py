from code.Entity import Entity


class PlayerCut(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pass