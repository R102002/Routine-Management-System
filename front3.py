from tkinter import *
from tkinter import messagebox
from mysql.connector import *

# Function to get the selected row from the listbox
def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    ent_date.delete(0, END)
    ent_date.insert(0, selected_row[1])
    ent_earn.delete(0, END)
    ent_earn.insert(0, selected_row[2])
    ent_exe.delete(0, END)
    ent_exe.insert(0, selected_row[3])
    ent_study.delete(0, END)
    ent_study.insert(0, selected_row[4])
    ent_code.delete(0, END)
    ent_code.insert(0, selected_row[5])
    ent_brk.delete(0, END)
    ent_brk.insert(0, selected_row[6])

selected_row = None  # add this line

# Function to delete a record from the database

def delete_command():
    global selected_row
    if selected_row:
        delete_record(selected_row[0])
        messagebox.showinfo("Success", "Record deleted")
        selected_row = None
        view_command()
    else:
        messagebox.showerror("Error", "Please select a record to delete")


# ...


# Function to view all records from the database
def view_command():
    list.delete(0, END)
    rows = view()
    if rows is not None:
        for row in rows:
            list.insert(END, row)

# Function to search records in the database
def search_command():
    list.delete(0, END)
    search_results = search(date_text.get(), earn_text.get(), exercise_text.get(), study_text.get(), coding_text.get(), rest_text.get())
    for row in search_results:
        list.insert(END, row)

# Function to add a new record to the database
def add_command():
    # Check if date is a valid integer with underscores
    if not all(c.isdigit() or c == '-' for c in date_text.get()):
        messagebox.showerror("Error", "Date should be a valid integer with Hyphen")
        return

    # Add data to the database
    insert(date_text.get(), earn_text.get(), exercise_text.get(), study_text.get(), coding_text.get(), rest_text.get())

    # Show success message
    messagebox.showinfo("Success", "Record added successfully")

    # Show the updated database
    view_command()




# Function to connect to the database
def connect_to_db():
    connection = None
    try:
        connection = connect(host="localhost", user="root", password="abc123", database="routine")
        cursor = connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS routine_1(id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, date VARCHAR(15), earnings INT, exercise VARCHAR(25), study VARCHAR(25), coding VARCHAR(25), rest VARCHAR(25))"
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
         messagebox.showerror("Error:", e)
    finally:
        if connection is not None:
            connection.close()

# Function to insert a new record into the database
def insert(date, earnings, exercise, study, coding, rest):
    connection = None
    try:
        connection = connect(host="localhost", user="root", password="abc123", database="routine")
        cursor = connection.cursor()
        sql = "INSERT INTO routine_1 (date, earnings, exercise, study, coding, rest) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (date, earnings, exercise, study, coding, rest))
        connection.commit()
    except Exception as e:
         messagebox.showerror("Error:", e)
    finally:
        if connection is not None:
            connection.close()

# Function to retrieve all records from the database
def view():
    connection = None
    rows = None
    try:
        connection = connect(host="localhost", user="root", password="abc123", database="routine")
        cursor = connection.cursor()
        sql = "SELECT * FROM routine_1"
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.commit()
    except Exception as e:
         messagebox.showerror("Error:", e)
    finally:
        if connection is not None:
            connection.close()
        return rows


# Function to delete a

def delete_record(id):
    con=None
    try:
        con=connect(host="localhost",user="root",password="abc123",database="routine")
        cursor=con.cursor()
        sql="delete from routine_1 where id=%s"
        cursor.execute(sql, (id,))
        con.commit()
    except Exception as e:
         messagebox.showerror("issue", e)
        # con.rollback()
    finally:
        if con is not None:
            con.close()


def search(date='', earnings='', exercise='', study='', coding='', rest=''):
    con = None
    try:
        con = connect(host="localhost", user="root", password="abc123", database="routine")
        cursor = con.cursor()
        sql = "select * from routine_1 where date=%s OR earnings=%s OR exercise=%s OR study=%s OR coding=%s OR rest=%s"
        cursor.execute(sql, (date, earnings, exercise, study, coding, rest))
        rows = cursor.fetchall()
        con.commit()
    except Exception as e:
         messagebox.showerror("issue", e)
    finally:
        if con is not None:
            con.close()
        return rows

connect_to_db()

root=Tk()
root.title("MY ROUTINE DATABASE")
root.geometry("1100x600+50+50")
f=("Arial",12)

lab_date=Label(root,text="Date",font=f)
lab_date.grid(row=0,column=0, pady=10)
lab_earn=Label(root,text="Earnings",font=f)
lab_earn.grid(row=0,column=2, pady=10)
lab_exe=Label(root,text="Exercise",font=f)
lab_exe.grid(row=1,column=0, pady=10)
lab_stu=Label(root,text="Study",font=f)
lab_stu.grid(row=1,column=2, pady=10)
lab_code=Label(root,text="Coding",font=f)
lab_code.grid(row=2,column=0, pady=10)
lab_rest=Label(root,text="Rest",font=f)
lab_rest.grid(row=2,column=2, pady=10)

date_text=StringVar()
ent_date=Entry(root,width=25,textvariable=date_text,font=f)
ent_date.grid(row=0,column=1,pady=10)

earn_text=StringVar()
ent_earn=Entry(root,width=25,textvariable=earn_text,font=f)
ent_earn.grid(row=0,column=3,pady=10)

exercise_text=StringVar()
ent_exe=Entry(root,width=25,textvariable=exercise_text,font=f)
ent_exe.grid(row=1,column=1,pady=10)

study_text=StringVar()
ent_study=Entry(root,width=25,textvariable=study_text,font=f)
ent_study.grid(row=1,column=3,pady=10)

coding_text=StringVar()
ent_code=Entry(root,width=25,textvariable=coding_text,font=f)
ent_code.grid(row=2,column=1,pady=10)

rest_text=StringVar()
ent_brk=Entry(root,width=25,textvariable=rest_text,font=f)
ent_brk.grid(row=2,column=3,pady=10)


list=Listbox(root,height=15,width=60,font=f)
list.grid(row=10,column=1,rowspan=9,columnspan=2,pady=20)

sb=Scrollbar(root)
sb.grid(row=10,column=3,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(root,text="ADD",width=12,pady=5,command=add_command,font=f)
b1.grid(row=25,column=0,padx=5)
b2=Button(root,text="Search",width=12,pady=5,command=search_command,font=f)
b2.grid(row=25,column=1,padx=5)
b3=Button(root,text="Delete data",width=12,pady=5,command=delete_command,font=f)
b3.grid(row=25,column=2,padx=5)
b4=Button(root,text="View all",width=12,pady=5,command=view_command,font=f)
b4.grid(row=25,column=3,padx=5)
b5=Button(root,text="Close",width=12,pady=5,command=root.destroy,font=f)
b5.grid(row=25,column=4,padx=5)




root.mainloop()