from tkinter import *
window=Tk()
res=0
def arvutamine(event):
    if (ent1.get()).isdigit() and (ent2.get()).isdigit() and (ent3.get()).isdigit():
        global res 
        res=int(ent2.get())**2-4*int(ent1.get())*int(ent3.get())
        if res>0:
            x1=-((int(ent2.get()))+res**0.5)/2*(int(ent1.get()))
            x2=-((int(ent2.get()))-res**0.5)/2*(int(ent1.get()))
            lbl1.configure(text=("D=",res,"x1=",x1,"x2=",x2),height=1,width=50)
        elif res==0:
            x=-(int(ent2.get()))/2*(int(ent2.get()))
            lbl1.configure(text=("D=",res,"x=",x),height=1,width=50)
        elif res<0:
            lbl1.configure(text=("D=",res,"Не имеет квадратного корня"),height=1,width=50)
    else:
        if (ent1.get()).isdigit():
            pass
            if (ent2.get()).isdigit():
                ent3.configure(bg="red")
                lbl1.configure(text="Введены не все данные")
            else:
                ent2.configure(bg="red")
                lbl1.configure(text="Введены не все данные")
        else:
            ent1.configure(bg="red")
            lbl1.configure(text="Введены не все данные")
    return

window.title("Решение квадратного уравнения")
window.geometry("1920x1080")
btn=Button(window,text="Решить",font="Arial 20",fg="green",bg="red",width=20,height=3)
ent1=Entry(window,fg="blue",width=5,font="Arial 20")
ent2=Entry(window,fg="blue",width=5,font="Arial 20")
ent3=Entry(window,fg="blue",width=5,font="Arial 20")
lbl=Label(window,text="Решение квадратного уравнения",font="Arial 28",fg="green",bg="white",width=28,height=1)
lbl1=Label(window,text="решение",font="Arial 28",fg="green",bg="white",width=28,height=1)
lbl2=Label(window,text="x**2",font="Arial 20",fg="white",bg="green",width=4,height=1)
lbl3=Label(window,text="x+",font="Arial 20",fg="white",bg="green",width=4,height=1)


btn.bind("<Button-1>",arvutamine)

lbl.pack()
ent1.pack()
lbl2.pack()
ent2.pack()
lbl3.pack()
ent3.pack()
btn.pack()
lbl1.pack()
window.mainloop()
