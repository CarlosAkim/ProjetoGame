from pygame.examples.moveit import HEIGHT

from code.Const import WIN_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verifyCollissionWindow(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, Player):
            if ent.rect.left >= WIN_HEIGHT:
                ent.health = 0
        pass

    @staticmethod
    def verifyCollision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verifyCollissionWindow(test_entity)

    @staticmethod
    def verifyHealth(entity_list):
        for ent in entity_list:
            if ent is not None and hasattr(ent, "health"):
                if ent.health <= 0:
                    print(f"{ent.name} foi removido!")
                    entity_list.remove(ent)
