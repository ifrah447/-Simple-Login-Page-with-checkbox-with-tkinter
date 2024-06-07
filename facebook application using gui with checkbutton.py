
from tkinter import *
import tkinter as tk
gui=tk.Tk()
gui.title('login page')
gui.geometry('600x300')
gui.configure(bg="#4267b2")
##password=IntVariable
title=Label(gui,text='facebook',font=('Segoe UI',30,'bold'),fg='white',bg='#4267b2').grid(row=0,column=1)
l1=Label(gui,text='User Name: ',font=('Ariel 12 bold'),fg='white',bg='#4267b2').grid(row=1,column=0,padx=20,sticky='w')
E1=Entry(gui,bd=5,relief=GROOVE,width=60)
E1.grid(row=1,column=1,pady=10,padx=20,sticky='e')

l2=Label(gui,text='Password: ',font=('Ariel 12 bold'),fg='white',bg='#4267b2').grid(row=2,column=0,padx=20,sticky='w')

E2=Entry(gui, show='*',bd=5,relief=GROOVE,width=60)
E2.grid(row=2,column=1,pady=10,padx=20,sticky='e')
def print_selection():
    if (var1.get() == 0):
        E2.config(show="*")
    elif (var1.get() == 1):
        E2.config(show="")
var1 = tk.IntVar()
Button1 = Checkbutton(gui, text = "show",variable = var1,onvalue = 1,offvalue = 0,height = 2,width = 10, takefocus = 0,
                      command=print_selection).grid(row=3,column=0,padx=20,sticky='w')
def save():
    text="name: "+E1.get()+"\n"+"password: "+E2.get()
    with open("History.txt",'w') as f:
        f.writelines(text)
button_ok=Button(gui,text='login',font=('Ariel 9 bold'),borderwidth=2,highlightthickness=3,highlightbackground='dark blue',relief=GROOVE,command=save)
button_ok.grid(row=4,column=1)
#quit information button
button_quit=Button(gui,text='quit',font=('Ariel 9 bold'),borderwidth=2,highlightthickness=3,highlightbackground='dark blue',relief=GROOVE,command=gui.destroy)
button_quit.grid(row=5,column=1)
gui.mainloop()
