import sqlite3

def connect():
    conn = sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expense (id INTEGER PRIMARY KEY, expense text, mop text, amount integer, location text)")
    conn.commit()
    conn.close()

def insert(expense, mop, amount, location):
    conn = sqlite3.connect("expenses.db")
    cur=conn.cursor()  
    cur.execute("INSERT INTO expense VALUES (NULL,?,?,?,?)",(expense, mop, amount, location))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("expenses.db")
    cur=conn.cursor()  
    cur.execute("SElECT * FROM expense")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(expense="",mop="",amount="",location=""):
    conn = sqlite3.connect("expenses.db")
    cur=conn.cursor()  
    cur.execute("SElECT * FROM expense WHERE expense=? OR mop=? OR amount=? OR location=?",(expense,mop,amount,location))
    rows = cur.fetchall()
    conn.close() 
    return rows

    
def delete(id):
    conn = sqlite3.connect("expenses.db")
    cur=conn.cursor()  
    cur.execute("DELETE FROM expense WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,expense,mop,amount,location):
    conn = sqlite3.connect("expenses.db")
    cur=conn.cursor()  
    cur.execute("UPDATE expense SET expense=?, mop=?, amount=?, location=? WHERE id=?", (expense,mop,amount,location,id))
    conn.commit()
    conn.close()    
    

connect()



view()
    


from tkinter import *

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])    

def view_command():
    list1.delete(0,END)
    for row in view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in search(expense_text.get(),mop_text.get(), amount_text.get(), location_text.get()):
        list1.insert(END,row)

def add_command():
    insert(expense_text.get(),mop_text.get(), amount_text.get(), location_text.get())
    list1.delete(0,END)
    list1.insert(END,(expense_text.get(),mop_text.get(), amount_text.get(), location_text.get()))

def delete_command():
    delete(selected_tuple[0])
    list1.delete(0,END)
    for row in view():
        list1.insert(END, row)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_command():
    update(selected_tuple[0],expense_text.get(),mop_text.get(), amount_text.get(), location_text.get())
    list1.delete(0,END)
    for row in view():
        list1.insert(END, row)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

        
        
window= Tk()
window.wm_title("Group 5 Expense Calculator")

l1 = Label(window, text = "Expense")
l1.grid(row=0, column =0)

l1 = Label(window, text = "Method of Payment")
l1.grid(row=0, column =2)

l1 = Label(window, text = "Amount")
l1.grid(row=1, column =0)

l1 = Label(window, text = "Location")
l1.grid(row=1, column =2)

expense_text = StringVar()
e1 = Entry(window, textvariable = expense_text)
e1.grid(row = 0, column = 1)

mop_text = StringVar()
e2 = Entry(window, textvariable = mop_text)
e2.grid(row = 0, column = 3)

amount_text = StringVar()
e3 = Entry(window, textvariable = amount_text)
e3.grid(row = 1, column = 1)

location_text = StringVar()
e4 = Entry(window, textvariable = location_text)
e4.grid(row = 1, column = 3)

list1=Listbox(window, height=6, width =35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)


b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2,column = 3)
b2=Button(window, text="Search Entry", width=12, command = search_command)
b2.grid(row=3,column = 3)

b3=Button(window, text="Add Entry", width=12, command = add_command)
b3.grid(row=4,column = 3)

b4=Button(window, text="Update Selected", width=12, command = update_command)
b4.grid(row=5,column = 3)

b5=Button(window, text="Delete Selected", width=12, command = delete_command)
b5.grid(row=6,column = 3)


window.mainloop()
