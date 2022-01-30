import sys
from math import pi
from tkinter import *

root = Tk()
root.title('FigACalc')
root.geometry('500x400')
root.resizable(0, 0)
root.iconphoto(False, PhotoImage(file='icon.png'))


class Figure:
    def __init__(self, a, b=0, c=0):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def s_rectangle(self):
        if self.a <= 0 or self.b <= 0:
            return 'Incorrect input'
        else:
            canvas.delete('all')
            canvas.create_rectangle(150, 100, int(self.a) + 150, int(self.b) + 100, fill='white')
            return f'The area of the rectangle is {self.a * self.b}'

    def s_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 'Incorrect input'
        elif (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            return 'Calculation not possible'
        else:
            p = (self.a + self.b + self.c) / 2
            answer = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)
            canvas.delete('all')
            canvas.create_polygon(0, 0, 0, self.a, self.b, self.c, fill='white')
            return f'The area of the triangle is {answer}'

    def s_circle(self):
        if self.a <= 0:
            return 'Incorrect input'
        else:
            canvas.delete('all')
            canvas.create_oval(150, 100, int(self.a) + 150, int(self.a) + 100, fill='white')
            return f'The area of the circle is {pi * self.a ** 2}'


def return_to_ans(value):
    ans.delete(0, END)
    ans.insert(0, value)


def value_s_return():
    a = enter_a.get()
    b = enter_b.get()
    c = enter_c.get()
    n = var_n.get()
    try:
        if n == 1:
            return_to_ans(Figure(a, b).s_rectangle())
        elif n == 2:
            return_to_ans(Figure(a, b, c).s_triangle())
        elif n == 3:
            return_to_ans(Figure(a).s_circle())
        else:
            return_to_ans('Select a figure')
    except ValueError:
        return_to_ans('Missing Numeric Values')


def about_image():
    canvas.delete('all')
    canvas.create_text((150, 100), text='This program allows you to calculate\n the area of basic geometric shapes,\n '
                                        'select one of the shapes and fill \n in the given data, then click on the \n'
                                        '"Calculate area" button.\n\n©RageBots company', font=('Roboto', 12),
                       fill='#A7FC00')


canvas = Canvas(root, height=200, width=300, bg='grey')
canvas.place(x=180, y=180)

Label(root, text='Figures').place(x=50, y=20)
Label(root, text='Figure Options').place(x=250, y=20)
Label(root, text='a or radius').place(x=240, y=50)
Label(root, text='b').place(x=260, y=75)
Label(root, text='c').place(x=260, y=100)

enter_a = Entry(root, width=8)
enter_b = Entry(root, width=8)
enter_c = Entry(root, width=8)
enter_a.place(x=300, y=50)
enter_b.place(x=300, y=75)
enter_c.place(x=300, y=100)

var_n = IntVar()
Radiobutton(root, text='Rectangle', value=1, variable=var_n).place(x=20, y=50)
Radiobutton(root, text='Triangle', value=2, variable=var_n).place(x=20, y=75)
Radiobutton(root, text='Circle', value=3, variable=var_n).place(x=20, y=100)

Button(root, text='Calculate area', command=value_s_return).place(x=20, y=150)
Button(root, text='Exit', command=lambda: sys.exit()).place(x=20, y=350)
Button(root, text='About', command=about_image).place(x=20, y=185)

ans = Entry(root, width=45)
ans.place(x=200, y=150)

root.mainloop()
