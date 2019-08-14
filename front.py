from tkinter import *
import backend

def get_selected_row(event):
    try:
         global selected_tuple
         index=list1.curselection()[0]
         selected_tuple=list1.get(index)
         e1.delete(0,END)
         e1.insert(END,selected_tuple[0])
         e2.delete(0,END)
         e2.insert(END,selected_tuple[1])
         e3.delete(0,END)
         e3.insert(END,selected_tuple[2])
         e4.delete(0,END)
         e4.insert(END,selected_tuple[3])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for things in backend.view():
        list1.insert(END,things)

def search_command():
    list1.delete(0,END)
    for things in backend.search(e1.get(),e2.get(),e3.get(),e4.get()):
        list1.insert(END,things)

def add_command():
    backend.insert(e1.get(),e2.get(),e3.get(),e4.get())
    list1.delete(0,END)
    list1.insert(END,(e1.get(),e2.get(),e3.get(),e4.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],e2.get(),e3.get(),e4.get())


window=Tk()
window.wm_title("Inventory Manager software")

Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)

l1=Label(window,text= "Product Id")
l1.grid(row=0,column=0,sticky=N+S+E+W)

l2=Label(window,text="Product name")
l2.grid(row=0,column=2,sticky=N+S+E+W)

l3=Label(window,text="Price")
l3.grid(row=1,column=0,sticky=N+S+E+W)

l4=Label(window,text="quant")
l4.grid(row=1,column=2,sticky=N+S+E+W)

productid=StringVar()
e1=Entry(window,textvariable="productid")
e1.grid(row=0,column=1,sticky=N+S+E+W)

Pname=StringVar()
e2=Entry(window,textvariable="Pname")
e2.grid(row=0,column=3,sticky=N+S+E+W)

cost=StringVar()
e3=Entry(window,textvariable="cost")
e3.grid(row=1,column=1,sticky=N+S+E+W)

quant=StringVar()
e4=Entry(window,textvariable="quant")
e4.grid(row=1,column=3,sticky=N+S+E+W)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2,sticky=N+S+E+W)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,sticky=N+S+E+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b2=Button(window,text="view products",width=12,command=view_command)
b2.grid(row=2,column=3,sticky=N+S+E+W)

b3=Button(window,text="search product",width=12,command=search_command)
b3.grid(row=3,column=3,sticky=N+S+E+W)

b4=Button(window,text="Add new",width=12,command=add_command)
b4.grid(row=4,column=3,sticky=N+S+E+W)

b5=Button(window,text="update list",width=12,command=update_command)
b5.grid(row=5,column=3,sticky=N+S+E+W)

b6=Button(window,text="delete selected",width=12,command=delete_command)
b6.grid(row=6,column=3,sticky=N+S+E+W)

b7=Button(window,text="close manager",width=12,command=window.destroy)
b7.grid(row=7,column=3,sticky=N+S+E+W)

window.mainloop()
