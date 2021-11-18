#from os import *
from tkinter import *
from tkinter import ttk
import ventana_1
import mcp3008
from control import *
#import ventana_3     #archivo donde esta la clase frame1
#from ventana_2 import *
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib as plt
import threading
from random import randint
import numpy as np
import time
import cv2
import imutils
from PIL import Image
from PIL import ImageTk
from datetime import datetime
x=0

def hello():
    print("hello, Timer")

    t = threading.Timer(3.0, hello)
    t.start()


# class frame1(Frame):

#     def __init__(self, master=None):
#         super().__init__(master, bg="white")
#         self.master = master
#         self.pack(fill=BOTH)
#         self.create_widgets()


#     def create_widgets(self):

#         self.img = PhotoImage(file="help.png")

#         f1=Frame(self, width=1920, height=10, highlightbackground="black", highlightthickness=1)

#         f2=Frame(self, width=2000, bg="white")

#         self.btn1=Button(self,text="Revisar estado", command=lambda: self.master.switch_frame(frame2),
#                         font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black" )

#         self.btn2=Button(self,text="Inciar nueva germinación", command=lambda: self.master.switch_frame(frame4),
#                          font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")

#         self.btn3=Button(self,text="Terminar germinación", command=lambda: self.master.switch_frame(frame6),
#                          font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")

#         self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")

#         self.btn5= Button(f2, text="apagar", command=self.master.quit, font=("Comic Sans MS", 10 ),
#                          bg="white", highlightbackground="black")

#         self.btn6= Button(f2, text="ayuda y acerca de nosotros",
#                         command=lambda: self.master.switch_frame(frame7), font=("Comic Sans MS", 10),bg="white",
#                         highlightbackground="black")

#         self.icono1=Label(f2, image=self.img, bg="white")

#         self.lbl2 = Label(self,text="alertas \n \n \n \n",
#                         borderwidth = 3, relief="raised", width=30, height=10,
#                         font=("Comic Sans MS", 12 ),bg="white", highlightbackground="black",
#                          )


#         self.btn1.pack(pady=50)
#         self.btn2.pack(pady=50)
#         self.btn3.pack(pady=50)
#         self.lbl2.pack(pady=50)
#         f2.pack(fill="both")
#         f1.pack(fill="both")
#         self.lb1.pack()
#         self.btn5.pack(side="left", padx=10)
#         self.icono1.pack(side="right")
#         self.btn6.pack(side="right", padx=10)


class frame2(Frame):           #revisar estado inicial

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill="both")
        self.create_widgets()




    def create_widgets(self):

        self.comboExample = ttk.Combobox(self,
                            values=["1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7"],
                                    state="readonly")

        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        f3=Frame(self, bg="red")
        self.lb2= Label (self, text="Seleccione una bandeja", bg="white").pack(pady=30)
        self.lb3= Label (f2, text="Por favor seleccione una bandeja", bg="white")
        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")
        self.btn2= Button(self, text="revisar", command=lambda:self.master.check_1(self.comboExample), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")
        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")


        self.comboExample.pack(pady=10)
        self.btn2.pack()
        #self.comboExample.bind("<<ComboboxSelected>>", callbackFunc)


        f2.pack(fill="both", pady=5)
        f1.pack(fill="both")

        self.lb3.pack(side="top", pady=300)
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.lb1.pack()


#def callbackFunc(event):
    print("box")
    #print(event)


class frame3(Frame):          #no esta en uso la bandeja

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()


    def create_widgets(self):

        self.comboExample = ttk.Combobox(self,
                            values=["1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7"],
                                    state="readonly")

        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white", pady=5)

        f3=Frame(self, bg="red")
        self.lb2= Label (self, text="Seleccione una bandeja", bg="white").pack(pady=30)
        self.lb3= Label (f2, text="La presenta bandeja no se esta usando, por favor vuelva e inicie una germinación", bg="white")
        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")
        self.btn2= Button(f2, text="revisar", command=lambda:self.master.check_1(self.comboExample), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")
        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")


        self.comboExample.pack(pady=10)
        self.btn2.pack()

        #f3.pack(pady=310)
        f2.pack(fill="both")
        f1.pack(fill="both")

        self.lb3.pack(side="top", pady=300)
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.lb1.pack()


class frame4(Frame):          #inicar germinación

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()


    def create_widgets(self):

        self.comboExample = ttk.Combobox(self,
                            values=["1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7"])

        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        f3=Frame(self, bg="red")
        self.lb2= Label (self, text="Seleccione una bandeja", bg="white").pack(pady=30)
        self.lb3= Label (f2, text="Por favor seleccione una bandeja", bg="white")
        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")
        self.btn1= Button(self, text="Iniciar", command=lambda:self.master.check_2(self.comboExample),
                        font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")
        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")


        self.comboExample.pack(pady=10)
        self.btn1.pack()

        f2.pack(fill="both")
        f1.pack(fill="both")

        self.lb3.pack(side="top", pady=300)
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.lb1.pack()


class frame6(Frame):          #La bandeja seleccionada se encuentra en uso

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()


    def create_widgets(self):

        self.comboExample = ttk.Combobox(self,
                            values=["1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7"])

        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        f3=Frame(self, bg="red")
        self.lb2= Label (self, text="Seleccione una bandeja", bg="white").pack(pady=30)
        self.lb3= Label (f2, text="La bandeja seleccionada se encuentra en uso, por favor regrese y termine la germinación", bg="white")
        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")
        self.btn1= Button(self, text="Iniciar", command=lambda:self.master.check_2(self.comboExample),
                        font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")
        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")


        self.comboExample.pack(pady=10)
        self.btn1.pack()

        f2.pack(fill="both")
        f1.pack(fill="both")

        self.lb3.pack(side="top", pady=300)
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.lb1.pack()


class frame5(Frame):          #terminar germinación

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):

        self.comboExample = ttk.Combobox(self,
                            values=["1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7"])

        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        f3=Frame(self, bg="red")
        self.lb2= Label (self, text="Seleccione una bandeja", bg="white").pack(pady=30)
        self.lb3= Label (f2, text="Por favor seleccione una bandeja", bg="white")
        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")
        self.btn1= Button(self, text="Terminar", command=lambda:self.master.check_3(self.comboExample),
                        font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")
        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")


        self.comboExample.pack(pady=10)
        self.btn1.pack()

        f2.pack(fill="both")
        f1.pack(fill="both")

        self.lb3.pack(side="top", pady=300)
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.lb1.pack()


class frame9(Frame):          #La bandeja seleccionada no se encuentra en uso

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):

        self.comboExample = ttk.Combobox(self,
                            values=["1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7"])

        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        f3=Frame(self, bg="red")
        self.lb2= Label (self, text="Seleccione una bandeja", bg="white").pack(pady=30)
        self.lb3= Label (f2, text="La bandeja seleccionada no se encuentra en uso", bg="white")
        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")
        self.btn1= Button(self, text="Terminar", command=lambda:self.master.check_3(self.comboExample),
                        font=("Comic Sans MS", 10 ), bg="white", highlightbackground="black")
        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")


        self.comboExample.pack(pady=10)
        self.btn1.pack()

        f2.pack(fill="both")
        f1.pack(fill="both")

        self.lb3.pack(side="top", pady=300)
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.lb1.pack()




    # def visualizar(self):
    #     video="C:/Users/Acer/Downloads/cee-bsdx-ihy (2021-04-28 at 20 14 GMT-7).mp4"
    #     cap = cv2.VideoCapture(video)
    #     if cap is not None:
    #         ret, frame = cap.read()
    #         if ret == True:
    #             frame = imutils.resize(frame, width=640)
    #             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #             im = Image.fromarray(frame)
    #             img = ImageTk.PhotoImage(image=im)

    #             self.lblVideo.configure(image=img)
    #             self.lblVideo.image = img
    #             self.lblVideo.after(10, self.visualizar)
    #         else:
    #             self.lblVideo.image = ""
    #             cap.release()


class frame7(Frame):         #información

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()


    def create_widgets(self):


        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        f3=Frame(self, bg="red")
        self.lb3= Label (self, text="""
        Somos Juan Olarte y Gustavo Bermudez los responsables de este proyecto, entendemos que algunas cosas no salen como se quieren y si llega a tener alguno problema con el uso del dispositivo siga los siguientes pasos:

                1. Desconecte el dispositivo de la red eléctrica

                2. Infórmele al encargado del hogar o a la persona capacitada que se encuentra dentro del hogar.

                3. Si el encargado sabe cómo solucionarlo, deje que él lo encienda.

                4. Si el encargado no sabe solucionarlo o no pudo, comuníquese lo más pronto mediante mensajes al siguiente número #######, haremos lo posible para ayudarlo

                """, bg="white").pack(pady=20)

        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")

        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")



        self.icono1=Label(f2, image=self.img, bg="white")

        f3.pack(pady=270)
        f2.pack(fill="both")
        f1.pack(fill="both")

        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.lb1.pack()


class frame8(Frame):         #grafica

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill="both")
        self.create_widgets()
        self.i=0
        self.t=0
        self.dpts= []
        self.dpts2= []
        self.time= []
        #self.graficar()



    def create_widgets(self):

        self.comboExample = ttk.Combobox(self,
                            values=["1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7"],
                                    state="readonly")

        self.img = PhotoImage(file="back.png")
        f1=Frame(self,  highlightbackground="black", highlightthickness=1)
        f2=Frame(self, bg="white")
        self.btn2= Button(self, text="revisar", command=lambda:self.master.check_1(self.comboExample), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")
        lab = Label(self, text="grafica en tiempo real", bg = 'white').pack( pady=20)

        self.comboExample.pack(pady=10)
        self.btn2.pack()

        lab2 = Label(self, text="zanahoria", bg = 'white').pack()

        fig = Figure()
        self.ay = fig.add_subplot(121)
        self.ay.set_xlabel("hora")
        self.ay.set_ylabel("humedad")
        self.ay.grid()
        self.ax = fig.add_subplot(122)
        self.ax.set_xlabel("hora")
        self.ax.set_ylabel("temperatura")
        self.ax.grid()
        self.graph2 = FigureCanvasTkAgg(fig, self)
        self.graph2.get_tk_widget().pack(fill='both', pady=20)
        self.graph2.draw()
        self.b=Button(self , text="Start", command=self.graficar, bg="white")

        self.b.pack()

        lab2 = Label(self, text="progreso", bg = 'white').pack(pady=20)
        f2.pack(fill="both", pady=5)
        self.icono1=Label(f2, image=self.img, bg="white").pack(side="left", padx=10)
        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(ventana_1.frame1), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black").pack(side="left")
        f1.pack(fill="both")
        lb= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque").pack(side="bottom")

    def graficar(self):
        now = datetime.now()
        self.time.append(now)
        self.dpts2.append(sensores(0,x-1))
        self.dpts.append(sensores(1,x-1))
        self.ax.plot(self.time, self.dpts, marker='o', color='orange')
        self.ay.plot(self.time, self.dpts2, marker='o', color='orange')
        self.i=1+self.i
        self.graph2.draw()
        print(self.i)
        self.after(1000, self.graficar)


class frame10(Frame):         #ha iniciado un ciclo

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()
        self.video="video.mp4"
        self.cap = cv2.VideoCapture(self.video)


    def create_widgets(self):



        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")

        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(frame5), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")

        self.btn2= Button(f2, text="continuar", command=self.alert, font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")

        self.btn1= Button(self, text="ver", command=self.visualizar, font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")



        self.lblVideo=Label(self, text="Oprima ver para visualizar el video guia")

        self.lblVideo.pack(pady=20)
        self.btn1.pack()
        f2.pack(fill="both")
        f1.pack(fill="both")
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.btn2.pack(side="right", pady=10)
        self.lb1.pack()

    def alert(self):
        r=messagebox.askyesno(message="""Por favor asegurese de que realizo todos los pasos mostrados, es su responsabilidad que esto sea así sino podria dañar el dispositivo
                                    ¿Desea continuar?
                                    """, title="Alerta")
        if(r):
            r2=messagebox.showinfo(message="Ha iniciado un ciclo de germinación, si piensa que hizo algun paso mal, puede finalizar de inmediato al volver al inicio", title="Felicitaciones")
            if(r2=="ok"):
                lambda:self.master.check_4()
                self.master.switch_frame(ventana_1.frame1)




    def visualizar(self):
        # video="C:/Users/Acer/Downloads/cee-bsdx-ihy (2021-04-28 at 20 14 GMT-7).mp4"
        # cap = cv2.VideoCapture(video)
        ret, d = self.cap.read()
      #  d = imutils.resize(d, width=800)
        d = cv2.cvtColor(d, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(d)
        img = ImageTk.PhotoImage(image=im)

        self.lblVideo.configure(image=img)
        self.lblVideo.image = img
        self.lblVideo.after(10, self.visualizar)


class frame11(Frame):         #ha terminado un ciclo

    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=BOTH)
        self.create_widgets()
        self.video="video.mp4"
        self.cap = cv2.VideoCapture(self.video)


    def create_widgets(self):



        self.img = PhotoImage(file="back.png")

        f1=Frame(self,  highlightbackground="black", highlightthickness=1)

        f2=Frame(self, bg="white")

        self.lb1= Label(f1, text= "Hecho con <3 por estudiantes de la universidad el Bosque")

        self.btn5= Button(f2, text="volver", command=lambda: self.master.switch_frame(frame5), font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")

        self.btn2= Button(f2, text="continuar", command=self.alert, font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")

        self.btn1= Button(self, text="ver", command=self.visualizar, font=("Comic Sans MS", 10 ),
                         bg="white", highlightbackground="black")


        self.icono1=Label(f2, image=self.img, bg="white")



        self.lblVideo=Label(self, text="Oprima ver para visualizar el video guia")

        self.lblVideo.pack(pady=20)
        self.btn1.pack()
        f2.pack(fill="both")
        f1.pack(fill="both")
        self.icono1.pack(side="left", padx=10)
        self.btn5.pack(side="left")
        self.btn2.pack(side="right", pady=10)
        self.lb1.pack()

    def alert(self):
        r=messagebox.askyesno(message="""Por favor asegurese de que realizo todos los pasos mostrados, es su responsabilidad que esto sea así sino podria dañar el dispositivo

                                    ¿Desea continuar?
                                    """, title="Alerta")
        if(r):
            r2=messagebox.showinfo(message="Ha terminado un ciclo de germinación, si piensa que hizo algun paso mal o aún no era momento de terminarlo, puede inicia el ciclo de nuevo al volver al inicio", title="Felicitaciones")
            if(r2=="ok"):
                lambda:self.master.check_5()
                self.master.switch_frame(ventana_1.frame1)




    def visualizar(self):
        ret, d = self.cap.read()
        d = cv2.cvtColor(d, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(d)
        img = ImageTk.PhotoImage(image=im)

        self.lblVideo.configure(image=img)
        self.lblVideo.image = img
        self.lblVideo.after(10, self.visualizar)




#class window():

#     def __init__(self):
#         root = Tk()
#         root.geometry('1920x1080')
#         root.attributes('-fullscreen', True)
#         root.wm_title("Sistema de germinación")
#         app = frame1(root)
#         app.mainloop()

class window(Tk):                               #clase para iniciar la interfaz grafica e ir cambiando de ventana



    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.geometry("800x480")
        self.title("Sistema de germinación")
        self._frame = None
        self.switch_frame(ventana_1.frame1)
        self.dpts=[]
        self.i=0
        self.t=0

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def check_1(self, combo):
        print("box")
        print(combo.get())
        global x
        x=int(combo.get())
        #bandejas[4].estado=1
        if bandejas[x-1].estado:
            self.switch_frame(frame8)   #8
        else:
            self.switch_frame(frame3)

    def check_2(self, combo):

        print("box")
        print(combo.get())
        global x
        x=int(combo.get())
        if bandejas[x-1].estado:
            self.switch_frame(frame6)
        else:
            self.switch_frame(frame10)

    def check_3(self, combo):
        print("check3")
        print(combo.get())
        global x
        x=int(combo.get())
        if bandejas[x-1].estado:
            self.switch_frame(frame11)
        else:
            self.switch_frame(frame9)


    def check_4(self):
        global x
        bandejas[x-1].estado=1

    def check_5(self):
        global x
        bandejas[x-1].estado=0


def data_points(t):
        f = open("data.txt", 'w')
        for i in range(1):
            f.write(str(np.sin(t))+'\n')
        f.close()

        f = open("data.txt", "r")
        data = f.readlines()
        f.close()

        l = []
        for i in range(len(data)):
            l.append(float(data[i].rstrip("\n")))
        #print("devuelve")
        return l


def sensores(j,i):

    if j==0:
        return (bandejas[0].humedad())
    elif j==1:
        return (bandejas[0].temperatura())



if __name__=="__main__":
    #hello()
    control()
    app=window()
    app.mainloop()
