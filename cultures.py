import tkinter
import customtkinter
from PIL import ImageTk, Image
from cultureSolve import solve

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

current_culture_index = 0


rendement_values = []
prix_values = []
mo_ouvriers_values = []
temps_machine_values = []
eau_values = []
salaire_values = []
frais_fixe_values = []

water_value = None
workers_value = None
hour_value = None


def update_lists(rendement, prix, mo_ouvriers, temps_machine, eau, salaire, frais_fixe):
    global rendement_values, prix_values, mo_ouvriers_values, temps_machine_values, eau_values, salaire_values, frais_fixe_values
    rendement_values.append(float(rendement.get()))
    prix_values.append(float(prix.get()))
    mo_ouvriers_values.append(float(mo_ouvriers.get()))
    temps_machine_values.append(float(temps_machine.get()))
    eau_values.append(float(eau.get()))
    salaire_values.append(float(salaire.get()))
    frais_fixe_values.append(float(frais_fixe.get()))


def switch_frame(frame, next_frame):
    frame.destroy()
    next_frame()


def create_frame_culture(root, cultureIndex):
    frame = customtkinter.CTkFrame(master=root, width=420, height=700, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Gestion optimale d'une zone agricode", font=('Century Gothic', 20))
    l2.place(x=50, y=25)

    l3 = customtkinter.CTkLabel(master=frame, text=f'culture {cultureIndex}', font=('Century Gothic', 20))
    l3.place(x=50, y=80)

    entry11 = customtkinter.CTkEntry(master=frame, width=330,
                                     placeholder_text=f'Rendement Q/ha [culture {cultureIndex}]')
    entry11.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=330,
                                    placeholder_text=f'PrixVente UM/Q [culture {cultureIndex}]')
    entry2.place(x=50, y=165)

    entry3 = customtkinter.CTkEntry(master=frame, width=330,
                                    placeholder_text=f'M.O.Ouvriers/ha [culture {cultureIndex}]')
    entry3.place(x=50, y=220)

    entry4 = customtkinter.CTkEntry(master=frame, width=330,
                                    placeholder_text=f'TempsMachineH/ha [culture {cultureIndex}]')
    entry4.place(x=50, y=275)

    entry5 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=f'Eau m3/ha [culture {cultureIndex}]')
    entry5.place(x=50, y=330)

    entry6 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text=f'SalaireAn/Ouv [culture {cultureIndex}]')
    entry6.place(x=50, y=385)

    entry7 = customtkinter.CTkEntry(master=frame, width=330,
                                    placeholder_text=f'FraisFixe de Gest [culture {cultureIndex}]')
    entry7.place(x=50, y=440)

    # Create custom button
    button1 = customtkinter.CTkButton(master=frame, width=220, text="Next Culture",
                                      command=lambda: button_function_save(frame, entry11, entry2, entry3, entry4,
                                                                           entry5, entry6, entry7),
                                      corner_radius=6)
    button1.place(x=100, y=495)

    root.mainloop()


def button_function_save(frame, entry1, entry2, entry3, entry4, entry5, entry6, entry7):
    update_lists(entry1, entry2, entry3, entry4, entry5, entry6, entry7)
    button_function_culture(frame)


def create_frame_general(root):
    global water_value, workers_value, hour_value

    frame = customtkinter.CTkFrame(master=root, width=420, height=700, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Gestion optimale d'une zone agricode", font=('Century Gothic', 20))
    l2.place(x=50, y=25)

    l3 = customtkinter.CTkLabel(master=frame, text="Disponibilité", font=('Century Gothic', 20))
    l3.place(x=50, y=80)

    water = customtkinter.CTkEntry(master=frame, width=330, placeholder_text="Disponibilité Eau (m3)")
    water.place(x=50, y=110)

    hour = customtkinter.CTkEntry(master=frame, width=330, placeholder_text="HeureMachineH (ha)")
    hour.place(x=50, y=165)

    workers = customtkinter.CTkEntry(master=frame, width=330, placeholder_text="Main d'oeuvre (ha)")
    workers.place(x=50, y=220)

    button1 = customtkinter.CTkButton(master=frame, width=220, text="Solve",
                                      command=lambda: save_general_values(frame, water, hour, workers),
                                      corner_radius=6)
    button1.place(x=100, y=275)

    root.mainloop()


def save_general_values(frame, water_entry, hour_entry, workers_entry):
    global water_value, workers_value, hour_value, result
    water_value = float(water_entry.get())
    hour_value = float(hour_entry.get())
    workers_value = float(workers_entry.get())
    result = solve(rendement_values, prix_values, mo_ouvriers_values, temps_machine_values, eau_values, salaire_values,
                   frais_fixe_values, water_value, workers_value, hour_value, number_of_cultures,zoneT)

    frame.destroy()
    switch_frame(frame, lambda: create_frame_result(app))


def create_frame_result(root):
    frame = customtkinter.CTkFrame(master=root, width=500, height=700, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Gestion optimale d'une zone agricole", font=('Century Gothic', 15))
    l2.place(x=50, y=25)

    # Create labels for each month dynamically
    for i in range(number_of_cultures):
        label_text = f'Zone Confiée au Culture  {i + 1} : {result.getVars()[i].x}'
        label = customtkinter.CTkLabel(master=frame, text=label_text, font=('Century Gothic', 15))
        label.place(x=50, y=135 + i * 30)

    root.mainloop()


def button_function_culture(frame):
    global current_culture_index
    global number_of_cultures
    global zoneT

    current_culture_index += 1

    if current_culture_index == 1:
        number_of_cultures = int(entry1.get())
        zoneT = float(entry20.get())


        frame.destroy()
        create_frame_culture(app, current_culture_index)

    elif current_culture_index == (number_of_cultures + 1):
        switch_frame(frame, lambda: create_frame_general(app))
    else:
        frame.destroy()
        create_frame_culture(app, current_culture_index)


app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("800x800")
app.title('Agriculture')

img1 = ImageTk.PhotoImage(Image.open("./assets/agriculture.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=420, height=700, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Gestion optimale d'une zone agricole", font=('Century Gothic', 20))
l2.place(x=50, y=25)

l3 = customtkinter.CTkLabel(master=frame, text="Nombre de Cultures Proposées", font=('Century Gothic', 20))
l3.place(x=50, y=80)

entry1 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Entrez le nombre des cultures proposées')
entry1.place(x=50, y=110)
entry20 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Entrez la superficie de zone Agricole ')
entry20.place(x=50, y=140)


button1 = customtkinter.CTkButton(master=frame, width=220, text="Next Culture",
                                  command=lambda: button_function_culture(frame), corner_radius=6)
button1.place(x=100, y=170)

app.mainloop()
