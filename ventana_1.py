from os import*
from tkinter import * 
from tkinter import ttk
from main_1 import *            #importa las demas ventanas

#from ventana_2 import *

class frame1(Frame):

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()


    def create_widgets(self):

        self.img = PhotoImage(file="help.png")

        f1=Frame(self, width=1920, height=10, highlightbackground="black", highlightthickness=1)

        f2=Frame(self, width=2000, bg="white")

        self.btn1=Button(self,text="Revisar estado", command=lambda: self.master.switch_frame(frame2), 
                        font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black" )

        self.btn2=Button(self,text="Inciar nueva germinación", command=lambda: self.master.switch_frame(frame4),
                         font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")

        self.btn3=Button(self,text="Terminar germinación", command=lambda: self.master.switch_frame(frame5),
                         font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")

        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")

        self.btn5= Button(f2, text="apagar", command=self.master.quit, font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")

        self.btn6= Button(f2, text="ayuda y acerca de nosotros", 
                        command=lambda: self.master.switch_frame(frame7), font=("Comic Sans MS", 10),bg="white",  #frane7
                        highlightbackground="black")
        
        self.icono1=Label(f2, image=self.img, bg="white")

        self.lbl2 = Label(self,text="alertas \n \n \n \n", 
                        borderwidth = 3, relief="raised", width=30, height=10,
                        font=("Comic Sans MS", 12 ),bg="white", highlightbackground="black",
                         )


        self.btn1.pack(pady=50) 
        self.btn2.pack(pady=50)
        self.btn3.pack(pady=50) 
        self.lbl2.pack(pady=50)
        f2.pack(fill="both", pady=5)  
        f1.pack(fill="both") 
        self.lb1.pack()
        self.btn5.pack(side="left", padx=10)
        self.icono1.pack(side="right")
        self.btn6.pack(side="right", padx=10)
