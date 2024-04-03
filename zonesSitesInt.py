import tkinter
import customtkinter
from PIL import ImageTk, Image
from zoneSiteSolve import solve

current_site_index = 0

zone_site = []


def create_frame_zone_site(root):
    global checkbox_vars
    site_frame = customtkinter.CTkFrame(master=root)
    site_frame.grid(row=0, column=0, padx=20, pady=10)
    l3 = customtkinter.CTkLabel(master=site_frame, text=f'Site {current_site_index}')
    l3.grid(row=0, column=0, padx=20, pady=10)

    checkbox_vars = []  # List to store different variables for each checkbox

    for i in range(zones):
        checkbox_var = tkinter.IntVar(value=0)
        checkbox_vars.append(checkbox_var)

        checkbox = customtkinter.CTkCheckBox(master=site_frame,
                                             variable=checkbox_var, onvalue=1, offvalue=0,
                                             text=f'Zone {i + 1}')
        checkbox.grid(row=i + 1, column=0, padx=20, pady=10)
    if current_site_index == sites:
        text_btn = "Submit"
    else:
        text_btn = "Next Site"

    submit_button = customtkinter.CTkButton(master=site_frame, text=f'{text_btn}',
                                            command=lambda: submit_values(site_frame, checkbox_vars))
    submit_button.grid(row=zones + 1, column=0, padx=20, pady=10)
    app.mainloop()


def submit_values(frame, checkbox_vars):
    global zone_site, current_site_index

    for j in range(zones):
        zone_site[current_site_index - 1][j] = checkbox_vars[j].get()
    button_function_zone_site(frame)


def button_function_zone_site(frame):
    global sites, zones, current_site_index
    current_site_index += 1
    if current_site_index == 1:
        zones = int(entry1.get())
        sites = int(entry2.get())
        for i in range(sites):
            row = []
            for j in range(zones):
                column = []
                row.append(column)
            zone_site.append(row)
        frame.destroy()
        create_frame_zone_site(app)
    elif current_site_index <= sites:
        frame.destroy()
        create_frame_zone_site(app)
    elif current_site_index > sites:
        frame.destroy()
        create_frame_weighs(app)


def create_frame_weighs(root):
    global entries
    entries=[]
    zone_frame = customtkinter.CTkFrame(master=root)
    zone_frame.grid(row=0, column=0, padx=20, pady=10)
    l3 = customtkinter.CTkLabel(master=zone_frame, text=f'Weights ')
    l3.grid(row=0, column=0, padx=20, pady=10)

    for i in range(zones):
        entry = customtkinter.CTkEntry(master=zone_frame,width=330, placeholder_text=f'Zone {i + 1}')
        entry.grid(row=i + 1, column=0, padx=20, pady=10)
        entries.append(entry)
    btn = customtkinter.CTkButton(master=zone_frame, text="Go",
                                            command=lambda: solve_pos(zone_frame, entries))
    btn.grid(row=zones + 1, column=0, padx=20, pady=10)
    app.mainloop()


def solve_pos(frame, entries):
    global zones, sites, zone_site
    global weights
    weights = [int(entries[i].get()) for i in range(zones)]
    result = solve(zone_site, sites, zones, weights)
    frame.destroy()
    create_frame_result(app,result)



def create_frame_result(root,result):
    global sites
    frame = customtkinter.CTkFrame(master=root, width=500, height=700, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l5 = customtkinter.CTkLabel(master=frame, text="Gestion des Positions d'antenne", font=('Century Gothic', 15))
    l5.place(x=50, y=25)

    for i in range(sites):
        if result.getVars()[i].x == 0:
            res = "Vide"
        else:
            res = "Antenne"
        label_text = f'Site  {i + 1} : {res}'
        label = customtkinter.CTkLabel(master=frame, text=label_text, font=('Century Gothic', 15))
        label.place(x=50, y=135 + i * 20)
        lx = customtkinter.CTkLabel(master=frame, text=f'nombre Totale des Antennes {result.objVal}',
                                    font=('Century Gothic', 15))
        lx.place(x=50, y=135 + sites * 20)

    root.mainloop()


app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("700x700")
app.title('Problème de Positionnement')

img1 = ImageTk.PhotoImage(Image.open("./assets/antenne.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.grid(row=0, column=0, padx=10, pady=10)

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=420, height=700, corner_radius=15)
frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew",
           columnspan=2)  # Use column 1 for the frame, spanning two columns

l2 = customtkinter.CTkLabel(master=frame, text="Gestion des Positions d'antennes", font=('Century Gothic', 20))
l2.grid(row=0, column=0, padx=20, pady=10, sticky="w")

entry1 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Entrez le nombre des zones à étudier')
entry1.grid(row=1, column=0, padx=20, pady=10, sticky="w")

entry2 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Entrez le nombre des sites à étudier')
entry2.grid(row=2, column=0, padx=20, pady=10, sticky="w")

# Create custom button
button1 = customtkinter.CTkButton(master=frame, width=20, text="Next",
                                  command=lambda: button_function_zone_site(frame), corner_radius=6)
button1.grid(row=3, column=0, padx=20, pady=10, sticky="w")

# Configure row and column weights to allow resizing
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

app.mainloop()


