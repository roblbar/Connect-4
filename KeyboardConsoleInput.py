
class KeyboardConsoleInput:
    @staticmethod
    def read_spacing():
        return int(input())

    @staticmethod
    def read_move():
        move = input()
        coordinates = move.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        return (x,y)