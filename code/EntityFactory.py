import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name : str, position: tuple = (0,0)):
        match entity_name:
            case 'level1Bg':
                listBackground = []
                for i in range(6):
                    listBackground.append(Background(f'level1Bg{i}', (0,0)))
                    listBackground.append(Background(f'level1Bg{i}', (WIN_HEIGHT, 0)))
                return listBackground
            case 'PlayerRunning':
                return Player('PlayerRunning1', (10, WIN_WIDTH / 2))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_HEIGHT + 10, random.randint(125, 360)))
            #case 'Enemy2':
                #return Enemy('Enem', (WIN_HEIGHT + 10, random.randint(125, 360)))

