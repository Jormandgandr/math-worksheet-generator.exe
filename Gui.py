from tkinter import *
from tkinter import ttk

#Create the window
root = Tk()
root.title("Math-worksheet-generator by januschung")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Please select which type of worksheet you wish to create.").grid(columnspan=4, row=0)
ttk.Label(frm, text="Total Questions").grid(column=0, row=1)
ttk.Label(frm, text="Highest Number").grid(column=3, row=1)

#Button Functions
def addition():
    q = int(Q.get())
    d = int(D.get())
    import run
    #Type,Digits,Questions,Output,Title
    run.main("+", d, q, "Addition.pdf", "Addition Practice")
    ttk.Label(frm, text="addition.pdf created!").grid(columnspan=4, row=7)

def Subtraction():
    q = int(Q.get())
    d = int(D.get())
    import run
    #Type,Digits,Questions,Output,Title
    run.main("-", d, q, "Subtraction.pdf", "Subtraction Practice")
    ttk.Label(frm, text="addition.pdf created!").grid(columnspan=4, row=7)

def Multiplication():
    q = int(Q.get())
    d = int(D.get())
    import run
    #Type,Digits,Questions,Output,Title
    run.main("x", d, q, "Multiplication.pdf", "Multiplication Practice")
    ttk.Label(frm, text="Multiplication.pdf created!").grid(columnspan=4, row=7)

def Division():
    q = int(Q.get())
    d = int(D.get())
    import run
    #Type,Digits,Questions,Output,Title
    run.main("/", d, q, "Division.pdf", "Division Practice")
    ttk.Label(frm, text="Division.pdf created!").grid(columnspan=4, row=7)

def Mixed():
    q = int(Q.get())
    d = int(D.get())
    import run
    #Type,Digits,Questions,Output,Title
    run.main("mix", d, q, "addition.pdf", "Addition Praceice")
    ttk.Label(frm, text="addition.pdf created!").grid(columnspan=4, row=7)

#Buttons to run functions, currently set to close the window while in dev
ttk.Button(frm, text="Addition", command=addition).grid(column=0 , row =3)
ttk.Button(frm, text="Subtraction", command=Subtraction).grid(column=3 , row =3)
ttk.Button(frm, text="Multiplication", command=Multiplication).grid(column=0 , row =4)
ttk.Button(frm, text="Division", command=Division).grid(column=3 , row =4)
ttk.Button(frm, text="Mixed", command=Mixed).grid(column=2 , row =5)

#Entery for Digits and Number of questions
Q = ttk.Entry(frm)
Q.grid(column=0,row=2)
D = ttk.Entry(frm)
D.grid(column=3, row=2)

root.mainloop()