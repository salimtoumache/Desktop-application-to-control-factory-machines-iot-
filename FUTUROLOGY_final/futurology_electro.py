from tkinter.ttk import Progressbar
from tkinter import *
from pyrebase import *
from tkinter import messagebox as m
import socket
global sld
w = Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
w.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
w.overrideredirect(1)
progress = Progressbar(w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate', )
firebaseConfig = {
        "apiKey": "AIzaSyB5mep5tda2oSVHESTK194UOV2FshCmnQU",
        "authDomain": "futurology-bdd34.firebaseapp.com",
        "databaseURL": "https://futurology-bdd34-default-rtdb.firebaseio.com",
        "projectId": "futurology-bdd34",
        "storageBucket": "futurology-bdd34.appspot.com",
        "messagingSenderId": "820850128428",
        "appId": "1:820850128428:web:6c4c351c0531ffe6020389",
        "measurementId": "G-58P59QLPZ5"
    }
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
is_on = True
def new_win():
    def window_manueal():
        window3 = Tk()
        window3.geometry("1500x998")
        window3.title("Manual")
        window3.resizable(False, False)
        c = Canvas(window3, bg="gray16", height=200, width=200)
        filename = PhotoImage(file="img/man_finale_page.png")
        background_label = Label(window3, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l_stopped = Label(text="STOPPED", font=('boldface', 40), fg="#eb0707", bg='#e0e0e0', width=8).place(x=607,y=452)
        l_ccw = Label(text="Counter Clockwise", font=('boldface', 40), fg="#1288bd", bg='#e0e0e0', width=15).place(x=490,y=770)
        def ccw():
            l_ccw = Label(text="Counter Clockwise", font=('boldface', 40), fg="#1288bd", bg='#e0e0e0', width=15).place(x=490,y=770)
            db.update({"direction": -1})
        def cw():
            l_ccw = Label(text="Clockwise", font=('boldface', 40), fg="#1288bd", bg='#e0e0e0', width=15).place(x=490,y=770)
            db.update({"direction": 1})
        image_ccw = PhotoImage(file='img/ccw2.png')
        image_cw = PhotoImage(file='img/cw22.png')
        button_ccw = Button(image=image_ccw, command=ccw)
        button_ccw.place(x=236, y=761)
        button_cw = Button(image=image_cw, command=cw)
        button_cw.place(x=998, y=761)
        def on():
            l_stopped = Label(text="STARTED", font=('boldface', 40), fg="#36ee3e", bg='#e0e0e0', width=8).place(x=607,y=452)
            db.update({"machine": 1})
        def off():
            l_ccw = Label(text="STOPPED", font=('boldface', 40), fg="#eb0707", bg='#e0e0e0', width=8).place(x=607,y=452)
            db.update({"machine": 0})
        image_off = PhotoImage(file="img/stop.png")
        image_on = PhotoImage(file="img/start.png")
        button_off = Button(image=image_off, command=off)
        button_off.place(x=240, y=435)
        button_on = Button(image=image_on, command=on)
        button_on.place(x=996, y=435)
        image_b_home = PhotoImage(file="img/home_r.png")
        b_home = Button(image=image_b_home, command=lambda: [window3.destroy(), home()]).place(x=700, y=874)
        c.pack()
        window3.mainloop()
    is_on = True
    def window_auto():
        window2 = Tk()
        window2.geometry("1501x998")
        window2.title("Automatic")
        window2.resizable(False, False)
        c = Canvas(window2, bg="gray16", height=200, width=200)
        filename = PhotoImage(file="img/autopagr.png")
        background_label = Label(window2, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        sld = Scale(window2, from_=0, to=100, length=600, font=('Consolas', 20), tickinterval=20, showvalue=True,
                    resolution=1,
                    troughcolor="blue",
                    fg="black",
                    bg="#e5f4f5", orient=HORIZONTAL, relief=FLAT)
        is_on = True
        def switch():
            global is_on
            if is_on:
                on_button.config(image=off)
                is_on = False
                db.update({"stat": 0})
            else:
                on_button.config(image=on)
                is_on = True
                db.update({"stat": 1})
        off = PhotoImage(file="img/image5.png")
        on = PhotoImage(file="img/image6.png")
        on_button = Button(window2, image=off, bd=0, command=switch, fg="#677d8b", bg="#e5f4f5", background='#e5f4f5',
                           activeforeground='#677d8b', activebackground='#e5f4f5')
        on_button.place(x=750, y=290)
        def quantity():
            quantity_c = db.child("quantity").get()
            b = quantity_c.val()
            b = str(b)
            if b < "10":
                Quantity = Label(text=b + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=5)
                Quantity.place(x=573, y=409)
                window2.after(2000, quantity)
            elif b == "100":
                Quantity = Label(text=b + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=5)
                Quantity.place(x=573, y=409)
                window2.after(2000, quantity)
            else:
                Quantity = Label(text=b + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=5)
                Quantity.place(x=573, y=409)
                window2.after(2000, quantity)
        quantity()
        def readdta():
            quantity_c = db.child("speed").get()
            b = quantity_c.val()
            window2.after(100, sld.set(int(b)))
            b = str(b)
            if b < "10":
                Quantity = Label(text=b + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=5)
                Quantity.place(x=460, y=538)
                window2.after(2000, readdta)
            elif b == "100":
                Quantity = Label(text=b + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=5)
                Quantity.place(x=460, y=538)
                window2.after(2000, readdta)
            else:
                Quantity = Label(text=b + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=5)
                Quantity.place(x=460, y=538)
                window2.after(2000, readdta)
        readdta()
        def ctk(event):
            var = sld.get()
            db.update({"speed": var})
            var = var
            if var < 10:
                speed_label = Label(text=str(var) + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=5)
                speed_label.place(x=460, y=538)
                window2.after(100, ctk)
            elif var == 100:
                speed_label = Label(text=str(var) + "  ", font=('underline', 40), fg="black", bg='#e5f4f5', width=6)
                speed_label.place(x=460, y=538)
                window2.after(100, ctk)
            else:
                speed_label = Label(text=str(var) + "    ", font=('underline', 40), fg="black", bg='#e5f4f5')
                speed_label.place(x=480, y=538)
                window2.after(100, ctk)
        sld.bind("<ButtonRelease-1>", ctk)
        sld.place(x=218, y=630)
        image_b_home = PhotoImage(file="img/home_r.png")
        b_home = Button(image=image_b_home, command=lambda: [window2.destroy(),home()]).place(x=690, y=881)
        c.pack()
        window2.mainloop()
    def home():
        home = Tk()
        home.geometry("1500x997")
        home.title("home")
        home.resizable(False, False)
        c = Canvas(home, bg="gray16", height=200, width=200)
        filename = PhotoImage(file="img/final_home.png")
        background_label = Label(home, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        def message():
            m.showerror(title="ERROR", message="NO INTERNET ACCESS !")
        image_auto = PhotoImage(file="img/automatic_photo.png")
        auto_btn = Button(image=image_auto, command=lambda: [home.destroy(), window_auto()])
        def test_connection():
            try:
                socket.create_connection(('Google.com', 80))
                return True
            except OSError:
                return False
        a = test_connection()
        if a == False:
            auto_btn.config(command=message)
        else:
            auto_btn.config(command=lambda: [home.destroy(), window_auto()])
        auto_btn.place(x=265, y=668)
        image_manue = PhotoImage(file="img/manual_photo.png")
        manue_btn = Button(image=image_manue, command=lambda: [home.destroy(), window_manueal])
        if a == False:
            manue_btn.config(command=message)
        else:
            manue_btn.config(command=lambda: [home.destroy(), window_manueal()])
        manue_btn.place(x=945, y=668)
        c.pack()
        home.mainloop()
    home()
def bar():
    import time
    l4 = Label(w, text='Loading...', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=210)
    r = 0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r = r + 1
    w.destroy()
    new_win()
progress.place(x=-10, y=235)
a = '#249794'
Frame(w, width=427, height=241, bg=a).place(x=0, y=0) 
b1 = Button(w, width=10, height=1, text='Get Started', command=bar, border=0, fg=a, bg='white')
b1.place(x=170, y=200)
l1 = Label(w, text='FUTUROLOGY  ', fg='white', bg=a)
lst1 = ('Calibri (Body)', 18, 'bold')
l1.config(font=lst1)
l1.place(x=50, y=80)
l3 = Label(w, text='Electro club', fg='white', bg=a)
lst3 = ('Calibri (Body)', 13)
l3.config(font=lst3)
l3.place(x=50, y=110)
w.mainloop()
