from colorama import Fore, Style

def draw_board(board):
    # создание игрового поля
    for i in range(3):
        row = []
        for cell in board[i]:
            if cell == "X":
                row.append(Fore.GREEN + cell)
            elif cell == "O":
                row.append(Fore.BLUE + cell)
            else:
                row.append(Fore.WHITE + cell)
        print('|'.join(row))
        print('------')

def reset_color():
    print(Style.RESET_ALL)
    #сброс текущего цвета


def ask_and_make_move(player, board):
    # выбор координат для хода
    x, y = input(f"{player}, введите координаты X Y, через проблел: ").strip().split()
    x, y = int(x), int(y)
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        board[x][y] = player
    else:
        print("Эта ячейка уже занята. Попробуйте снова.")


def make_move(player, board, x, y):
    # проверика на возможность хода
    if board[x][y] != " ":
        print("Клетка занята")
        return False
    # если клетка свободна, записать ход
    board[x][y] = player
    return True


def check_win(player, board):
    # проверка на совпаления ходов
    for i in range(3):
        # в строках
        if board[i] == [player, player, player]:
            return True
        #  в столбцах
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # проверка совпадений значений по диагонали
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def tic_tac_toe():
    # цикл вызова игры
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "X"
        while True:
            # отрисовка поля
            draw_board(board)
            # запрос хода
            ask_and_make_move(player, board)
            # проверка на победу
            if check_win(player, board):
                print(f"{player} выиграл!")
                break
            # проверка на  ничью
            tie_game = False
            for row in board:
                for cell in row:
                    if cell == " ":
                        tie_game = True
            # завершение цикла в случае ничьей
            if not tie_game:
                break
            player = "O" if player == "X" else "X"
        restart = input("Сыграть еще раз? (y/n) ")
        if restart.lower() != "y":
            break
tic_tac_toe()