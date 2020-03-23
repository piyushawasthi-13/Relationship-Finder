from tkinter import *
import sqlite3

win=Tk()
win.title("relation khoj")
win.geometry("500x550")

def submit():
    conn=sqlite3.connect("khushi.db")
    cur=conn.cursor()
    
    n1=name1.get()
    n2=name2.get()
    n1=n1.lower()
    n2=n2.lower()
    for i in n1:
        for j in n2:
            if i==j:
                n1=n1.replace(i,"",1)
                n2=n2.replace(j,"",1)
                break 
    print(n1+n2)
    c=len(n1+n2)
    print(c)
    s=0
    if c>0:
      list=["freinds","love","affection","marriage","enemy","siblings"]
      while len(list)>1:
        s=(s+c-1)%len(list)
        l=list[:s]
        r=list[s+1:]
        list=l+r
        if s==-1:
            list=list[:len(list)-1]
    k=list[0]
    result.insert(END,k)
    try:
        cur.execute("INSERT INTO RELATION values(:first_name,:second_name,:relation)",
        {
        "first_name": name1.get(),
        "second_name": name2.get(),
        "relation": k
        }
        )
    except:
        cur.execute("""CREATE TABLE RELATION(
        first_name text,
        second_name text,
        relation text
    )""")
        cur.execute("INSERT INTO RELATION values(:first_name,:second_name,:relation)",
        {
        "first_name": name1.get(),
        "second_name": name2.get(),
        "relation": k
        }
        )

    conn.commit()
    conn.close()
def fetch_all():
    conn=sqlite3.connect("khushi.db")
    cur=conn.cursor()
    cur.execute("SELECT*,oid from RELATION")
    RECORD=cur.fetchall()
    records=''
    for rec in RECORD:
        records+= "  Name1: "+      str(rec[0])+ "   Name2: "+        str(rec[1])+ "  Relation: "+      str(rec[2])+"\n"
    
    query=Label(win,text=records)
    query.place(x=60,y=350)
    
    conn.commit()
    conn.close()
def clear_all():
    name1.delete(0,END)
    name2.delete(0,END)
    result.delete(0,END)
    name1.focus()
#create la
title=Label(win,text="RELATION KHOJ",width=35,font=("bold",30),fg="blue",)
name1=Label(win,text="first name")
name2=Label(win,text="second name")
relation=Label(win,text="Relationship")
name1.place(x=60,y=80)
name2.place(x=60,y=130)
title.place(x=-150,y=15)
relation.place(x=60,y=180)
#create textbox
name1=Entry(win,width=20)
name1.place(x=255,y=85)
name1.focus()
name2=Entry(win,width=20)
name2.place(x=255,y=135)

result=Text(win,width=15,height=1)
result.place(x=255,y=185)

#create button 

submit_btn=Button(win,text="Check Relation",width=20,fg="white",bg="brown",command=submit)
submit_btn.place(x=260,y=260)

submit_btn2=Button(win,text="Create new",width=20,fg="white",bg="brown",command=clear_all)
submit_btn2.place(x=55,y=260)
name1.focus()


btn3=Button(win,text="Show all Relation",width=50,fg="white",bg="brown",command=fetch_all)
btn3.place(x=55,y=310)
win.mainloop()
