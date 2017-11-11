import mysql.connector
from tkinter import *
import tkinter.messagebox as m

root=Tk();
db=mysql.connector.connect(user="root",password="",host="localhost",database="python");
def display():
   
	rollno1=s1.get();
	name1=s2.get();
	address1=s3.get();
	city1=s4.get();
	cursor=db.cursor();
	

	try:
		cursor.execute("SELECT * from ajay WHERE rollno='"+rollno1+"' and city='"+city1+"'");
		row=cursor.fetchone();
		#for row in results:
		rollno=row[0];
		name=row[1];
		address=row[2];
		city=row[3];
			#m.showinfo("name",name);
		if((rollno1==rollno) & (city1==city)):
			m.showinfo("login success");
		else:
			m.showinfo("invalid");

		db.commit();
		

	except:
		db.rollback();






l1=Label(root,text="Enter the rollno");
l1.grid(row=0);

s1=StringVar();
e1=Entry(root,textvariable=s1);
e1.grid(row=0,column=1);

l2=Label(root,text="Enter the Name");
l2.grid(row=1);

s2=StringVar();
e2=Entry(root,textvariable=s2);
e2.grid(row=1,column=1);


l3=Label(root,text="Enter the address");
l3.grid(row=2);

s3=StringVar();
e3=Entry(root,textvariable=s3);
e3.grid(row=2,column=1);


l4=Label(root,text="Enter the class");
l4.grid(row=3);

s4=StringVar();
e4=Entry(root,textvariable=s4);
e4.grid(row=3,column=1);

b4=Button(root,text="show",command=display);
b4.grid(row=5,column=1);

root.mainloop();
