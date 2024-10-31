import tkinter

GRAY = "#0f0f0f"
BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"

current_player = "X"
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def restart_game():
    print("RESTART")

def tile_clicked(r, c):

    global current_player

    print("Tile Clicked: " + str(r) + " " + str(c))
    board[r][c] = current_player

window = tkinter.Tk()
window.title("Tic Tac Toe Game")
window.resizable(False,False)

frame = tkinter.Frame(window, width=500, height=500)
frame.grid_propagate(True)
frame.pack()

message = tkinter.Label(frame, text=current_player+"'s turn", font=("Arial", 30))
message.grid(row=0,column=1)

for row in range(3):
    for col in range(3):
        board[row][col] = tkinter.Button(frame, text="", font=("Arial", 50, "bold"), bg=GRAY, fg=BLUE,
                width=3, height=1, name=str(row)+","+str(col), command=lambda r=row, c=col: tile_clicked(r,c))
        board[row][col].grid(row=row+1, column = col)

restart = tkinter.Button(frame, text="Restart", font=("Arial", 20, "bold"), command=lambda : restart_game())
restart.grid(row=4, column=1)



window.update()
window.mainloop()