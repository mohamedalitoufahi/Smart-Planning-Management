import tkinter
import customtkinter
from PIL import ImageTk, Image
from chaussure import chausseTous
d= []
cs = []
cMp = []
currentMonth = 0

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

def update_vals_mois(entry22, entry33, entry44):
    global cs, d, cMp
    d.append(float(entry22.get()))
    cs.append(float(entry33.get()))
    cMp.append(float(entry44.get()))


def update_vals(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10):
    global months, s0, no0, Sal, cHsup, cMp, h, H, Hmax, R, L
    months = int(entry1.get())
    s0 = int(entry8.get())  # stock initiale
    no0 = int(entry5.get())  # no ouvrier initiale
    Sal = float(entry2.get())  # salaire

    cHsup = int(entry9.get())  # cout 1h supp
    h = float(entry10.get())  # cout en heure /paire de chaussure
    H = float(entry7.get())  # volume horaire /mois pour un ouvrier
    Hmax = float(entry6.get())  # heure sup max /ouvrier /mois

    R = float(entry3.get())  # frais de recrutement
    L = float(entry4.get())  # frais de licenciemenet


def create_frame_month(root, currentMonth):
    frame1 = customtkinter.CTkFrame(master=root, width=420, height=700, corner_radius=15)
    frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l4 = customtkinter.CTkLabel(master=frame1, text=f'le Mois no {currentMonth}  ', font=('Century Gothic', 20))
    l4.place(x=50, y=80)

    entry22 = customtkinter.CTkEntry(master=frame1, width=330, placeholder_text=f'demande du mois {currentMonth}')
    entry22.place(x=50, y=110)

    entry33 = customtkinter.CTkEntry(master=frame1, width=330,
                                     placeholder_text=f'Cout de Stockage du mois {currentMonth}')
    entry33.place(x=50, y=165)

    entry44 = customtkinter.CTkEntry(master=frame1, width=330,
                                     placeholder_text="Cout de fabrication d'un paire de chaussure")
    entry44.place(x=50, y=220)

    # Create custom button
    if currentMonth == months:
        btn = "solve"
    else:
        btn = "Next Month"
    button = customtkinter.CTkButton(master=frame1, width=220, text=f'{btn}',
                                     command=lambda: button_function_and_save(frame1,entry22,entry33,entry44),
                                     corner_radius=6)
    button.place(x=100, y=265)
    root.mainloop()

def button_function_and_save(frame,entry22,entry33,entry44):
    update_vals_mois(entry22,entry33,entry44)
    button_function_month(frame)

def button_function_month(frame):
    global currentMonth
    global months
    global cs, d, cMp
    currentMonth += 1
    if currentMonth == 1:
        update_vals(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10)
        frame.destroy()
        create_frame_month(app, currentMonth)
    if currentMonth <= months:
        frame.destroy()
        create_frame_month(app, currentMonth)
    elif currentMonth > months:
        #update_vals_mois(entry22, entry33, entry44)
        chausseTous(months, s0, no0, Sal, cHsup, cMp, h, H, Hmax, R, L, cs, d)
        print("frame destroy")
        frame.destroy()


app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("800x900")
app.title('ChaussTous')

img1 = ImageTk.PhotoImage(Image.open("./assets/chaussure.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=420, height=850, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Gestion de ressources ", font=('Century Gothic', 20))
l2.place(x=50, y=25)

entry1 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' le nombre de mois ')
entry1.place(x=50, y=100)  # months
entry2 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' le salaire de base ')
entry2.place(x=50, y=170)  # sal
entry3 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' frais de rectrutement ')
entry3.place(x=50, y=240)  # r
entry4 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' frais de licenciement ')
entry4.place(x=50, y=310)  # l
entry5 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' le nombre des ouvriers initial ')
entry5.place(x=50, y=380)  # no
entry6 = customtkinter.CTkEntry(master=frame, width=330,
                                placeholder_text=' le volume horaire supplementaire Max par ouvrier ')
entry6.place(x=50, y=450)  # Hsup
entry7 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' le volume horaire nominale par ouvrier ')
entry7.place(x=50, y=520)  # H
entry8 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' le stock initial ')
entry8.place(x=50, y=590)  # s0
entry9 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=' cout heure supplementaire ')
entry9.place(x=50, y=660)  # cHsup
entry10 = customtkinter.CTkEntry(master=frame, width=330,
                                 placeholder_text=' nombre des heures necessaire/paire de chaussure ')
entry10.place(x=50, y=730)  # h

button1 = customtkinter.CTkButton(master=frame, width=220, text="Next",
                                  command=lambda: button_function_month(frame),
                                  corner_radius=6)
button1.place(x=100, y=780)

app.mainloop()
