from tkinter import *

def new_game():

    global player

    player = "X"

    message.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

def turns_left():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def current_player(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                message.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                message.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                message.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                message.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                message.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                message.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    elif turns_left() is False:
        return "Tie"

    else:
        return False



window = Tk()
window.title("Tic Tac Toe")
players = ["X","O"]
player = "X"
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

message = Label(text=player + "'s TURN", font=('Ariel',40))
message.pack(side="top")

reset_button = Button(text="RESTART", font=('Ariel',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('Ariel',40), width=5, height=2,
                                      command= lambda row=row, column=column: current_player(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()