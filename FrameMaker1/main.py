from tkinter import *
from tkinter.colorchooser import askcolor
class App:
    def __init__(self,master):
        self.master=master
        self.master.title("welcome")
        self.master.geometry("500x400")
        self.master.config(bg="lightgreen")
        self.createwidgets()

    def createwidgets(self):
        self.btn1=Button(self.master,bg="#045D5D",fg="white",text="Print",width=10,font=20,command=self.show)
        self.btn1.place(relx=0.25,rely=0.6)
        self.width_label=Label(self.master,bg="#045D5D",fg="white",text="width",font=20)
        self.width_label.place(relx=0.65,rely=0.2)
        self.width_entry=Entry(self.master,width=20,font=20)
        self.width_entry.place(relx=0.15,rely=0.2)

        self.height_label=Label(self.master,bg="#045D5D",fg="white",text="Height",font=20)
        self.height_label.place(relx=0.65,rely=0.35)
        self.height_entry=Entry(self.master,width=20,font=20)
        self.height_entry.place(relx=0.15,rely=0.35)

        self.color_btn=Button(self.master,text="choose color",command=self.choose_color)

        self.color_btn.place(relx=0.25,rely=0.5)

        self.selected_color="#FFFFFF"

        self.lbl=Label(self.master,bg="#045D5D",fg="white",width=20)
        self.lbl.place(relx=0.25,rely=0.7)

    def choose_color(self):
        color=askcolor()[1]
        if color:
            self.selected_color=color

    def show(self):
        width=self.width_entry.get()
        height=self.height_entry.get()
        if not width.isdigit() or not height.isdigit():
            return
        width=int(width)
        height=int(height)

        new_window=Toplevel(self.master)
        new_window.geometry(f"{width}x{height}")
        new_window.config(bg=self.selected_color)

        message_label=Label(new_window,bg=self.selected_color,fg="white",font=20,text="Hello")
        message_label.pack(pady=20)

if __name__=="__main__":
    screen=Tk()
    screen.title("welcome")
    screen.geometry("500x400")
    screen.config(bg="lightgreen")
    app=App(screen)
    screen.mainloop()