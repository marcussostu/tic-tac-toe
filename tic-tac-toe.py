choice_board = ['1', '2', '3',
                '4', '5', '6',
                '7', '8', '9']

def print_choice():
    print("Choice Board")
    print(choice_board[0]+"  "+choice_board[1]+"  "+choice_board[2])
    print(choice_board[3]+"  "+choice_board[4]+"  "+choice_board[5])
    print(choice_board[6]+"  "+choice_board[7]+"  "+choice_board[8])

board = ['.', '.', '.',
         '.', '.', '.',
         '.', '.', '.']

def print_board():
    print("Tic Tac Toe Board")
    print(board[0]+"  "+board[1]+"  "+board[2])
    print(board[3]+"  "+board[4]+"  "+board[5])
    print(board[6]+"  "+board[7]+"  "+board[8])

turn_counter = 0

def x_turn():
    global turn_counter
    turn_counter = turn_counter + 1
    print()
    print_choice()
    choice = input("Enter a number to place your X: ")
    
    if board[int(choice) - 1] == 'X':
        print("This spot has already been taken. Enter a different number.")
        

    elif choice == '1':
        board [0] = 'X'
        choice_board [0] = 'X'
    elif choice == '2':
        board [1] = 'X'
        choice_board [1] = 'X'
    elif choice == '3':
        board [2] = 'X'
        choice_board [2] = 'X'
    elif choice == '4':
        board [3] = 'X'
        choice_board [3] = 'X'
    elif choice == '5':
        board [4] = 'X'
        choice_board [4] = 'X'
    elif choice == '6':
        board [5] = 'X'
        choice_board [5] = 'X'
    elif choice == '7':
        board [6] = 'X'
        choice_board [6] = 'X'
    elif choice == '8':
        board [7] = 'X'
        choice_board [7] = 'X'
    elif choice == '9':
        board [8] = 'X'
        choice_board [8] = 'X'

    # board[int(choice) - 1] = 'O'
    # choice_board[int(choice) - 1] = 'O'

def o_turn():
    global turn_counter 
    turn_counter = turn_counter + 1
    print()
    print_choice()
    choice = input("Enter a number to place your O: ")
    
    if board[int(choice) - 1] == 'O':
        print("This spot has already been taken. Enter a different number.")

    elif choice == '1':
        board [0] = 'O'
        choice_board [0] = 'O'
    elif choice == '2':
        board [1] = 'O'
        choice_board [1] = 'O'
    elif choice == '3':
        board [2] = 'O'
        choice_board [2] = 'O'
    elif choice == '4':
        board [3] = 'O'
        choice_board [3] = 'O'
    elif choice == '5':
        board [4] = 'O'
        choice_board [4] = 'O'
    elif choice == '6':
        board [5] = 'O'
        choice_board [5] = 'O'
    elif choice == '7':
        board [6] = 'O'
        choice_board [6] = 'O'
    elif choice == '8':
        board [7] = 'O'
        choice_board [7] = 'O'
    elif choice == '9':
        board [8] = 'O'
        choice_board [8] = 'O'

def check_winner():
    global turn_counter
        
    # CHECK TIE
    if turn_counter == 9:
        return False
    
    # CHECK X
    # Horizontal
    elif board[0] == board[1] == board[2] == 'X':
        return 'X'
    elif board[3] == board[4] == board[5] == 'X':
        return 'X'
    elif board[6] == board[7] == board[8] == 'X':
        return 'X'
    # Verticle
    elif board[0] == board[3] == board[6] == 'X':
        return 'X'
    elif board[1] == board[4] == board[7] == 'X':
        return 'X'
    elif board[2] == board[5] == board[8] == 'X':
        return 'X'
    # Diagonal
    elif board[0] == board[4] == board[8] == 'X':
        return 'X'
    elif board[6] == board[4] == board[2] == 'X':
        return 'X'
    
    # CHECK O
    # Horizontal
    if board[0] == board[1] == board[2] == 'O':
        return 'O'
    elif board[3] == board[4] == board[5] == 'O':
        return 'O'
    elif board[6] == board[7] == board[8] == 'O':
        return 'O'
    # Verticle
    elif board[0] == board[3] == board[6] == 'O':
        return 'O'
    elif board[1] == board[4] == board[7] == 'O':
        return 'O'
    elif board[2] == board[5] == board[8] == 'O':
        return 'O'
    # Diagonal
    elif board[0] == board[4] == board[8] == 'O':
        return 'O'
    elif board[6] == board[4] == board[2] == 'O':
        return 'O'

# def print_instructions()

# MAIN PROGRAM ----------------------
# print_instructions()

while True:
    print_board()
    # if no winner then repeat
    x_turn()
    print_board()
    if check_winner() == 'X':
        print("X WINS!")
        break
    elif check_winner() == False:
        print("TIE!")
        break
    o_turn()
    print_board()
    if check_winner() == 'O':
        print("O WINS!")
        break
    elif check_winner() == False:
        print("TIE!")
        break
print("GAME OVER")