import tkinter

app = tkinter.Tk()

# hello = tkinter.Label(app, text = "Hello World Hello World Hello World Hello World Hello World Hello World")
# hello.pack()

canvas = tkinter.Canvas(app, bg="grey", width="500", height="500")
canvas.pack()

canvas.create_oval(50, 50, 50, 50)


app.mainloop()
