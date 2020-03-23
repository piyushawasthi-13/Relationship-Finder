from tkinter import * 
import sqlite3

win = Tk()
win.title("Relation Finder")
win.geometry("500x550")



# Create table
'''
c.execute("""CREATE TABLE details (
        first_name text,
        second_name text,
        relation text
        )""")
'''

#create submit btn function

def submit():

    # Create a database
    conn = sqlite3.connect("name_details.db")
    # Create Cursor
    cur = conn.cursor()

    #CAlculate relation
    n1=f_name.get()
    n2=s_name.get()
    n1 = n1.lower()
    n2 = n2.lower()
    for i in n1:
        for j in n2:
            if i==j:
                n1=n1.replace(i,"",1)
                n2=n2.replace(j,"",1)
                break 
    s=0
    c=len(n1+n2)
    if c>0:
        list=["freinds","love","affection","marriage","enemy","siblings"]
        while len(list)>1:
            s=(s+c-1)%len(list)
            l=list[:s]
            r=list[s+1:]
            list=l+r
            if s==-1:
                list=list[:len(list)-1]
    result = list[0]

    result_box.insert(END, result)

    #Insert IN DAtabase

    cur.execute("INSERT INTO details VALUES (:f_name, :s_name, :relation)",
            {
                'f_name': f_name.get(),
                's_name': s_name.get(),
                'relation': result
            })

    conn.commit()
    conn.close()
    f_name.delete(0,END)
    s_name.delete(0,END)

def fetch():
    # Create a database
    conn = sqlite3.connect("name_details.db")
    # Create Cursor
    cur = conn.cursor()
    
    cur.execute(" SELECT *,oid FROM details")
    records = cur.fetchall()

    print_records = ''
    for record in records:
        print_records += "Name1 :" + str(record[0]) + "Name2 :" +str(record[1]) + "relation" + str(record[2])+ "\n"

    query_label = Label(win, text=print_records)
    query_label.place(x =70, y = 380)
    
    conn.commit()
    conn.close()

#create textboxes labels
Title = Label(win, text = "Relationship Finder", width = 20, font= ("bold",20))
Title.place(x = 90, y = 53)
f_name_label = Label(win, text= "First Name")
f_name_label.place(x = 80, y = 130)

s_name_label = Label(win, text= "Second Name")
s_name_label.place(x = 68, y = 180)

Relation = Label(win, text= "Relation Status")
Relation.place(x = 70, y = 230)


#cREATE TEXTBOXES
f_name = Entry(win, width= 30)
f_name.place(x = 240, y = 130)

s_name = Entry(win, width= 30)
s_name.place(x = 240, y = 180)

result_box = Text(win, width = 30, height = 1)
result_box.place(x =240, y = 230)

# Create button

submit_btn = Button(win, text = "Check Relation", width=50, bg='brown', fg='white', command = submit)
submit_btn.place(x =70, y = 280)

fetch_btn = Button(win, text = "Show All Queries", width=50, bg='brown', fg='white', command = fetch)
fetch_btn.place(x =70, y = 330)
if val=="+":
win.mainloop()
