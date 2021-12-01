from classModule import *

def main():
    Running = True
    board = Board(Team_init(), First_realize())
    Board_view_decorate(board.update())

if __name__ == '__main__':
    main()