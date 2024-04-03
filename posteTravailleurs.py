import tkinter
import customtkinter
from PIL import ImageTk, Image
from posteTravailleursSolve import solve
from gurobipy import *


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green






def switch_frame(frame, next_frame):
    frame.destroy()
    next_frame()
def create_frame_result(root):
    frame = customtkinter.CTkFrame(master=root, width=500, height=700, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Besion en Ressources Humaines", font=('Century Gothic', 15))
    l2.place(x=50, y=25)

    l3 = customtkinter.CTkLabel(master=frame, text=f'lundi : {result.getVars()[0].x} ', font=('Century Gothic', 15))
    l3.place(x=50, y=135)
    l4 = customtkinter.CTkLabel(master=frame,text=f'mardi : {result.getVars()[1].x} ',font=('Century Gothic', 15))
    l4.place(x=150, y=135)
    l5 = customtkinter.CTkLabel(master=frame,text=f' mercredi : {result.getVars()[2].x} ',font=('Century Gothic', 15))
    l5.place(x=250, y=135)
    l6 = customtkinter.CTkLabel(master=frame,text=f'jeudi : {result.getVars()[3].x} ',font=('Century Gothic', 15))
    l6.place(x=50, y=300)
    l7 = customtkinter.CTkLabel(master=frame,text=f'vendredi : {result.getVars()[4].x} ',font=('Century Gothic', 15))
    l7.place(x=150, y=300)
    l8 = customtkinter.CTkLabel(master=frame,text=f' samedi : {result.getVars()[5].x}  ',font=('Century Gothic', 15))
    l8.place(x=250, y=300)
    l9 = customtkinter.CTkLabel(master=frame,text=f'dimanche : {result.getVars()[6].x} ',font=('Century Gothic', 15))
    l9.place(x=150, y=465)

    lx = customtkinter.CTkLabel(master=frame, text=f'nombre Totale des employeurs requis {result.objVal}', font=('Century Gothic', 15))
    lx.place(x=50, y=630)



    root.mainloop()


def button_function_culture(frame, entry1, entry2, entry3, entry4, entry5, entry6, entry7):
        global result
        result = solve(int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), int(entry6.get()), int(entry7.get()))

        frame.destroy()
        switch_frame(frame, lambda: create_frame_result(app))



app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("800x800")
app.title('Besion en RH')

img1 = ImageTk.PhotoImage(Image.open("./assets/post.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=420, height=700, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Besion en Ressources Humaines", font=('Century Gothic', 20))
l2.place(x=50, y=25)

l3 = customtkinter.CTkLabel(master=frame, text="le nombre de travailleurs requis/jour", font=('Century Gothic', 15))
l3.place(x=50, y=80)

entry1 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Lundi')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Mardi')
entry2.place(x=50, y=165)

entry3 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Mercredi')
entry3.place(x=50, y=220)

entry4 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Jeudi')
entry4.place(x=50, y=275)

entry5 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Vendredi')
entry5.place(x=50, y=330)

entry6 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Samedi')
entry6.place(x=50, y=385)

entry7 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Dimanche')
entry7.place(x=50, y=440)

# Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Solve",
                                  command=lambda: button_function_culture(frame, entry1, entry2, entry3, entry4, entry5,
                                                                          entry6, entry7),
                                  corner_radius=6)
button1.place(x=100, y=495)

app.mainloop()
