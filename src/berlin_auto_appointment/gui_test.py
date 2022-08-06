import tkinter
import tkinter.messagebox
from tkinter import *

#creating the main window and storing the window object in 'win'
mainwin=tkinter.Tk(screenName="berlin",  baseName=None,  useTk=1) 

#window parameter
mainwin.geometry('500x400') 
mainwin.title('ligma')

'''
def func():#function of the button
    tkinter.messagebox.showinfo("Hvordan har du det?")

btn=Button(mainwin,text="Click Me", width=10,height=5,command=func)
btn.place(x=200,y=30)

'''
'''
#canvas and shapes
can=Canvas(mainwin, width=500, height=300) #creating the canvas
oval=can.create_oval(100, 100, 200, 180,fill='green') #drawing an oval 
can.pack()
'''

'''
cb_var1 = IntVar() 
cb1=Checkbutton(mainwin, text='Python', variable=cb_var1,onvalue=1,offvalue=0,height=5,width=20).grid(row=0, sticky=W) 
cb_var2 = IntVar() 
cb2=Checkbutton(mainwin, text='C++', variable=cb_var2,onvalue=1,offvalue=0,height=5,width=20).grid(row=1, sticky=W) 
cb_var3 = IntVar() 
cb3=Checkbutton(mainwin, text='Java', variable=cb_var3,onvalue=1,offvalue=0,height=5,width=20).grid(row=2, sticky=W) 

'''

'''
Label(mainwin, text='Name').grid(row=0) 
Label(mainwin, text='Email').grid(row=1) 
ent1 = Entry(mainwin) 
ent2 = Entry(mainwin) 
ent1.grid(row=0, column=1) 
ent2.grid(row=1, column=1)
'''

'''
lb = Listbox(mainwin) 
lb.insert(1, 'Dosa') 
lb.insert(2, 'Idli') 
lb.insert(3, 'Roti') 
lb.insert(4,'Coffee')
lb.insert(5,'Tea')
lb.insert(6, 'Others') 
lb.pack() 
'''

'''
sb = Scrollbar(mainwin) 
sb.pack( side = RIGHT, fill = Y ) 
list_1 = Listbox(mainwin, yscrollcommand = sb.set ) 
for i in range(100): 
    list_1.insert(END, 'Item ' + str(i)) 
list_1.pack( side = LEFT, fill = BOTH ) 
sb.config( command = list_1.yview ) 

'''


mainwin.mainloop() #running the loop that works as a trigger