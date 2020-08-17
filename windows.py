from tkinter import *
root = Tk()
root.title("视窗")


string = StringVar()


frame = Frame(root)
frame.pack()

e = Entry(frame, textvariable = string)
e.pack(side = LEFT)

b = Button(frame, text = "计算", bg = "red", fg = "green", command = lambda: print(eval(string.get())))
b.pack(side = RIGHT)

root.mainloop()