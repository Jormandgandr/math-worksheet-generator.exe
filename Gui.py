from tkinter import *
from tkinter import ttk

# Colour codes
S1 = "#F7E6C4"
S2 ="#E89F6E"
S3 ="#6D324F"
S4 = "#1C1E3A"

#Create the window
root = Tk()
root.title("Math-worksheet-generator by januschung")
root.minsize(width=400, height=300)
root.configure(background=S1)

#Style
style = ttk.Style(root)
style.configure("TFrame", background=S1)
style.configure("TLabel", background= S1, foreground=S4, font=("Segoe UI",10))
style.configure("TButton", padding=(14, 9), background=S1, foregound="S2", bordercolor="S3", font=("Segoe UI Semibold", 10))
style.configure("TEntry", padding=(14, 9), background=S1, foregound="S2", bordercolor="S3", font=("Segoe UI Semibold", 10))
style.map("TButton",background=[("active", S2), ("pressed", S3)],relief=[("pressed", "sunken")],)

#Container
frm = ttk.Frame(root, padding=10,style="TFrame")
frm.grid()

#Window Text
ttk.Label(frm, text="Please select which type of worksheet you wish to create.", style="TLabel").grid(columnspan=4, row=0)
ttk.Label(frm, text="Total Questions", style="TLabel").grid(column=0, row=1)
ttk.Label(frm, text="Highest Number", style="TLabel").grid(column=3, row=1)

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
Run = ttk.Frame(root)
Run.grid(column=0, row=1, pady=10,sticky="ew")
ttk.Button(Run, text="Addition", command=addition, style="TButton").grid(column=0 , row =3, sticky="ew")
ttk.Button(Run, text="Subtraction", command=Subtraction, style="TButton").grid(column=3 , row =3, sticky="ew")
ttk.Button(Run, text="Multiplication", command=Multiplication, style="TButton").grid(column=0 , row =4, sticky="ew")
ttk.Button(Run, text="Division", command=Division, style="TButton").grid(column=3 , row =4, sticky="ew")
ttk.Button(Run, text="Mixed", command=Mixed, style="TButton").grid(column=2 , row =5, sticky="ew")

#Entery for Digits and Number of questions
Q = ttk.Entry(frm, style="TEntry")
Q.grid(column=0,row=2)
Q.insert(0,"80")
D = ttk.Entry(frm, style="TEntry")
D.grid(column=3, row=2)
D.insert(0, "100")

root.mainloop()