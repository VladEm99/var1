from tkinter import *
window=Tk()
res=0
def arvutamine(event):
    global res 
    res=int(ent1.get())+int(ent2.get())
    lbl1.configure(text=res)



window.title("Решение квадратного уравнения")
window.geometry("1920x1080")
btn=Button(window,text="Решить",font="Arial 20",fg="green",bg="red",width=20,height=3)
ent1=Entry(window,fg="blue",width=20,font="Arial 20")
ent2=Entry(window,fg="blue",width=20,font="Arial 20")
lbl=Label(window,text="Решение квадратного уравнения",font="Arial 28",fg="green",bg="white",width=28,height=1)
lbl1=Label(window,text="решение:",font="Arial 28",fg="green",bg="white",width=28,height=1)
lbl2=Label(window,text="x**2",font="Arial 20",fg="white",bg="green",width=4,height=1)
lbl3=Label(window,text="x+",font="Arial 20",fg="white",bg="green",width=4,height=1)


btn.bind("<Button-1>",arvutamine)

lbl.pack()
ent2.pack()
lbl2.pack()
ent1.pack()
lbl3.pack()
btn.pack()
lbl1.pack()
window.mainloop()
