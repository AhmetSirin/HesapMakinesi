import tkinter
from tkinter import *

def butonclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def butonallclear():
    global operator
    operator = ""
    text_input.set("")

def buttonesittir():
    global operator
    sum = str(eval((operator)))
    text_input.set(sum)
    operator = ""

calculator = Tk()
calculator.title("Hesap Makinesi")
operator = ""
text_input = StringVar()
txtDisplay = Entry(calculator,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg='powder blue',justify='right').grid(columnspan=4)

button7 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="7",bg='powder blue',command=lambda:butonclick(7)).grid(row=1,column=1)
button8 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="8",bg='powder blue',command=lambda:butonclick(8)).grid(row=1,column=2)
button9 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="9",bg='powder blue',command=lambda:butonclick(9)).grid(row=1,column=3)
UsAlma = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="^",bg='powder blue',command=lambda:butonclick('**')).grid(row=1,column=4)
allClear = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="AC",bg='powder blue',command=butonallclear).grid(row=1,column=5)

button4 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="4",bg='powder blue',command=lambda:butonclick(4)).grid(row=2,column=1)
button5 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="5",bg='powder blue',command=lambda:butonclick(5)).grid(row=2,column=2)
button6 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="6",bg='powder blue',command=lambda:butonclick(6)).grid(row=2,column=3)
carpma = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="x",bg='powder blue',command=lambda:butonclick("*")).grid(row=2,column=4)
Bolme = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="/",bg='powder blue',command=lambda:butonclick("/")).grid(row=2,column=5)

button1 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="1",bg='powder blue',command=lambda:butonclick(1)).grid(row=3,column=1)
button2 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="2",bg='powder blue',command=lambda:butonclick(2)).grid(row=3,column=2)
button3 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="3",bg='powder blue',command=lambda:butonclick(3)).grid(row=3,column=3)
Toplama = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="+",bg='powder blue',command=lambda:butonclick("+")).grid(row=3,column=4)
cikarma = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="-",bg='powder blue',command=lambda:butonclick("-")).grid(row=3,column=5)

button0 = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="0",bg='powder blue',command=lambda:butonclick(0)).grid(row=4,column=1)
virgul = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text=".",bg='powder blue',command=lambda:butonclick(".")).grid(row=4,column=2)
esittir = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="=",bg='powder blue',command=buttonesittir).grid(row=4,column=3)
solparantez = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text="(",bg='powder blue',command=lambda:butonclick("(")).grid(row=4,column=4)
sagparantez = Button(calculator,padx=16,bd=8,fg='black',font=('arial',20),text=")",bg='powder blue',command=lambda:butonclick(")")).grid(row=4,column=5)
calculator.mainloop()
