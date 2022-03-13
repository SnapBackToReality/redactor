from tkinter import *
brush_size = 20
color = "white"

def redactor (event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1= event.y - brush_size
    y2= event.y + brush_size
    w.create_oval(x1, y1, x2, y2,
                  fill=color, outline=color)

def brish_size_change (new_size):
    global brush_size
    brush_size = new_size

def color_change (new_color):
    global color
    color = new_color
root = Tk()
root.title("redactor")


w = Canvas(root,
           width=1920,
           height=1080,
           bg="white")
w.bind("<B1-Motion>", redactor)

black_btn = Button (text="Ниггер момент", width=15,
                  command=lambda: color_change("black"))

red_btn = Button (text="ты индеец", width=15,
                  command=lambda: color_change("red"))

green_btn = Button (text="Блевотина", width=15,
                  command=lambda: color_change("green"))


w.grid(row=2, column=0,
       columnspan=7, padx=5,
       pady=5, sticky=EW+S+N)
w.columnconfigure(4, weight=1)
w.rowconfigure(2, weight=1)
red_btn.grid(row=1, column=2)
black_btn.grid(row=1, column=1)
green_btn.grid(row=0, column=1)
root.mainloop()
