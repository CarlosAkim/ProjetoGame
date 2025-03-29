from code.Background import Background
from code.Const import WIN_HEIGHT


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
