from tkinter import *
import os
from shut import * 


st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="green")


r_buttom=Button(st,text="Restart",font=("Time New Roman",30,"bold"),
                relief=RAISED,cursor="plus",command=restart)
r_buttom.place(x=150,y=20,height=60,width=200)


rt_buttom=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),
                 relief=RAISED,cursor="plus",command=restart_time)
rt_buttom.place(x=150,y=170,height=50,width=200)


lg_buttom=Button(st,text="LOG-OUT",font=("Time New Roman",17,"bold"),
                 relief=RAISED,cursor="plus",command=logout)
lg_buttom.place(x=150,y=270,height=50,width=200)


st_buttom=Button(st,text="ShutDown",font=("Time New Roman",17,"bold"),
                 relief=RAISED,cursor="plus",command=shutdown)
st_buttom.place(x=150,y=370,height=60,width=200)












st.mainloop()
