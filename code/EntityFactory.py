from code.Background import Background


class EntityFactory:

    def get_entity(entity_name : str, position: tuple = (0,0)):
        match entity_name:
            case 'level1bg':
                listBackground = []
                for i in range(7):
                    listBackground.append(Background(f'level1Bg{i}', position))

                    # Finalizamos no minuto 57:20