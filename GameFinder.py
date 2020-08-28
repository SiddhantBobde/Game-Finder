from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

window=Tk()
window.geometry("800x800")
window.title("GAME FINDER")

def insert():
    name=e_Gname.get()
    Category=e_GCategory.get()
    release=e_release_date.get()

    if(name=="" or Category=="" or release==""):
        MessageBox.showinfo("ALL Fields are Compulsory")
    else:
        con=mysql.connect(host="localhost",user="root",password="",database="python-tkinter")
        cursor=con.cursor()
        cursor.execute("insert into games values('"+ name +"','"+ Category +"','"+ release +"')")
        cursor.execute("commit")

        e_Gname.delete(0,'end')
        e_GCategory.delete(0,'end')
        e_release_date.delete(0,'end')
        show()
        MessageBox.showinfo("Insert Status","Inserted Successfully")
        con.close()

def delete():
    if(e_Gname.get()== " "):
        MessageBox.showinfo("Delete Status","Name is compulsory for delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("delete from games where Gname='"+ e_Gname.get() +"'")
        cursor.execute("commit")

        e_Gname.delete(0,'end')
        e_GCategory.delete(0,'end')
        e_release_date.delete(0,'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

def update():
    name = e_Gname.get()
    Category = e_GCategory.get()
    release = e_release_date.get()

    if (name == "" or Category == "" or release == ""):
        MessageBox.showinfo("Update status","All fields are compulsory")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("update games set GCategory='" + Category + "',releasedate='" + release + "' where Gname='" + name + "' ")
        cursor.execute("commit")

        e_Gname.delete(0, 'end')
        e_GCategory.delete(0, 'end')
        e_release_date.delete(0, 'end')
        show()
        MessageBox.showinfo("Updated Status", "Updated Successfully")
        con.close()

def get():
    if (e_Gname.get() == " "):
        MessageBox.showinfo("Fetch Status", "Name is compulsory for delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("select * from games where Gname='" + e_Gname.get() + "'")
        rows=cursor.fetchall()

        for row in rows:
            e_GCategory.insert(0,row[1])
            e_release_date.insert(0,row[2])

        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
    cursor = con.cursor()
    cursor.execute("select * from games")
    rows = cursor.fetchall()
    list.delete(0,list.size())
    for row in rows:
        insertData= str(row[0])+'      '+str(row[1])
        list.insert(list.size()+1,insertData)

    con.close()

Gname = Label(window,text='Enter Game Name:',font=('bold',10))
Gname.place(x=20,y=30)

GCategory=Label(window,text='Enter Game Category:',font=('bold',10))
GCategory.place(x=20,y=60)

release_date=Label(window,text='Enter Release Date:',font=('bold',10))
release_date.place(x=20,y=90)

e_Gname=Entry()
e_Gname.place(x=160,y=30)

e_GCategory=Entry()
e_GCategory.place(x=160,y=60)

e_release_date=Entry()
e_release_date.place(x=160,y=90)

insert=Button(window,text='Insert',font=('italic',10),bg='white',command=insert)
insert.place(x=20,y=140)

delete=Button(window,text='Delete',font=('italic',10),bg='white',command=delete)
delete.place(x=70,y=140)

update=Button(window,text='Update',font=('italic',10),bg='white',command=update)
update.place(x=130,y=140)

get=Button(window,text='Get',font=('italic',10),bg='white',command=get)
get.place(x=190,y=140)

list = Listbox(window)
list.place(x=310,y=30)

show()

window.mainloop()
