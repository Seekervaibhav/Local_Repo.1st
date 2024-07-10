from tkinter import *
import tkinter
window= tkinter.Tk()
window.geometry('400x400')
window.title('Store Management App')

#Label For Name 
var =StringVar()
l1=Label(window, text='Name :', bg='lightBlue', font=("Arial", 16, "bold"),cursor="hand2")
l1.pack()
t1= Text(window, bg='lightGray',fg='black', font=("Courier", 14), height=2, width=15)
t1.pack()

#Label For Course Name 
l2=Label(window, text='Course Name :', bg='LightBlue', fg='White', font=("Arial", 16, "bold"),cursor="hand2")
l2.pack()
t2=Text(window, bg='lightgray', fg='black', font=("Courier", 14), height=2, width=45)
t2.pack()

        
Button(window, text='Enter', bg='lightGreen', command=t2).pack()

#Label For Another Courses
l3=Label(window, text='Other Courses', bg='LightBlue', fg='White', font=("Arial", 16, "bold"),cursor="hand2")
l3.pack()
var=IntVar()
r1=Radiobutton(window, text='Python FullStack',variable=var, value=1)
r1.pack()
r2=Radiobutton(window, text='Python DataScience',variable=var, value=2)
r2.pack()
r3=Radiobutton(window, text='Machine Learning',variable=var, value=3)
r3.pack()
r4=Radiobutton(window, text='Java FullStack',variable=var, value=4)
r4.pack()
r5=Radiobutton(window, text='Data Analysis',variable=var, value=5)
r5.pack()
r6=Radiobutton(window, text='PHP FullStack',variable=var, value=6)
r6.pack()


def GetData():
    if var.get()==1:
        print('Python FullStack')
    elif var.get()==2:
        print('Python DataScience')
    elif var.get()==3:
        print('Machine Learning')
    elif var.get()==4:
        print('Java FullStack')
    elif var.get()==5:
        print('Data Analysis ')
    else:
           print('PHP FullStack')
    
Button(window, text='Enter', bg='lightGreen', command=GetData).pack()

#Use Options
Locations= ['Noida','Gaziyabad', 'Delhi', 'Gurgaon', 'Greater Noida' ]


#Variable Declaration
value = StringVar(window) 
value.set("Select a Location")

Location = tkinter.OptionMenu(window, value, *Locations) 
Location.pack() 

def GetData():
    print(value.get())


Button(window, text='Enter', bg='lightGreen', command=GetData).pack()
#Entry 

window.mainloop()
