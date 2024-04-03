import tkinter
import customtkinter
from PIL import ImageTk, Image
from reseau import *
#from zonerouteursolve import solve

current_noeud_index = 0

edges = []
edges_tuples=[]

def create_frame_routeurs_link(root):
    global checkbox_vars, routeurs
    routeur_frame = customtkinter.CTkFrame(master=root)
    routeur_frame.grid(row=0, column=0, padx=20, pady=10)
    l3 = customtkinter.CTkLabel(master=routeur_frame, text=f'Routeur no: {current_noeud_index}')
    l3.grid(row=0, column=0, padx=20, pady=10)

    checkbox_vars = []  # List to store different variables for each checkbox

    for i in range(routeurs):
        checkbox_var = tkinter.IntVar(value=0)
        checkbox_vars.append(checkbox_var)

        checkbox = customtkinter.CTkCheckBox(master=routeur_frame,
                                             variable=checkbox_var, onvalue=1, offvalue=0,
                                             text=f'Routeur {i + 1}')
        checkbox.grid(row=i + 1, column=0, padx=20, pady=10)
    if current_noeud_index == routeurs:
        text_btn = "Submit"
    else:
        text_btn = "Next Router"

    submit_button = customtkinter.CTkButton(master=routeur_frame, text=f'{text_btn}',
                                            command=lambda: submit_values(routeur_frame, checkbox_vars))
    submit_button.grid(row=routeurs + 1, column=0, padx=20, pady=10)
    app.mainloop()


def submit_values(frame, checkbox_vars):
    global edges, current_noeud_index, routeurs,edges_tuples
# edges    [1,0,1,0...],[0,1,0,1...] (1=currentindex, j=edges[current_index][k]  if j==1
    for j in range(routeurs):
        edges[current_noeud_index - 1][j] = checkbox_vars[j].get()
    for k in range(routeurs):
        if(edges[current_noeud_index - 1][k]==1):
            edges_tuples.append(tuple([current_noeud_index-1, k]))
        print(edges_tuples)
    button_function_route(frame)


def button_function_route(frame):
    global routeurs, current_noeud_index
    current_noeud_index += 1
    if current_noeud_index == 1:
        routeurs = int(entry1.get())
        for i in range(routeurs):
            row = []
            for j in range(routeurs):
                column = []
                row.append(column)
            edges.append(row)
        frame.destroy()
        create_frame_routeurs_link(app)
    elif current_noeud_index <= routeurs:
        frame.destroy()
        create_frame_routeurs_link(app)
    elif current_noeud_index > routeurs:
        frame.destroy()
        create_frame_weighs(app)


def create_frame_weighs(root):
    global entries
    entries = []
    weight_frame = customtkinter.CTkFrame(master=root)
    weight_frame.grid(row=0, column=0, padx=20, pady=10)
    l3 = customtkinter.CTkLabel(master=weight_frame, text=f'Path Cost ')
    l3.grid(row=0, column=0, padx=20, pady=10)

    for i in range(len(edges_tuples)):
        entry = customtkinter.CTkEntry(master=weight_frame,width=330, placeholder_text=f'link {edges_tuples[i] }')
        entry.grid(row=i + 1, column=0, padx=20, pady=10)
        entries.append(entry)
    btn = customtkinter.CTkButton(master=weight_frame, text="Go",
                                            command=lambda: solve_pos(weight_frame, entries))
    btn.grid(row=len(edges_tuples) + 1, column=0, padx=20, pady=10)
    app.mainloop()


def solve_pos(frame, entries):
    global routeurs, edges_tuples,edges_costs
    global weights
    weights = [int(entries[i].get()) for i in range(len(edges_tuples))]
    edges_costs = {tup: value for tup, value in zip(edges_tuples, weights)}
    print(edges_costs)
    result = solve_network_flow(edges_costs, routeurs)
    print(result)
    frame.destroy()
    create_frame_result(app, result)



def create_frame_result(root,result):
    global routeurs
    frame = customtkinter.CTkFrame(master=root, width=500, height=700, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l5 = customtkinter.CTkLabel(master=frame, text="Gestion des Positions d'antenne", font=('Century Gothic', 15))
    l5.place(x=50, y=25)
    res=""
    for i in range(len(edges_costs)):
        if result.getVars()[i].x == 1:
            res = "admis"
        else:
            res = "pas admis"
        label_text = f'link  {edges_tuples[i]} : {res}'
        label = customtkinter.CTkLabel(master=frame, text=label_text, font=('Century Gothic', 15))
        label.place(x=50, y=135 + i * 20)
        lx = customtkinter.CTkLabel(master=frame, text=f'Cout Totale du chemin{result.objVal}',
                                    font=('Century Gothic', 15))
        lx.place(x=50, y=135 + len(edges_costs) * 20)

    root.mainloop()

















app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("700x700")
app.title('Problème de Routage')

img1 = ImageTk.PhotoImage(Image.open("./assets/antenne.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.grid(row=0, column=0, padx=10, pady=10)

# creating custom frame
frame = customtkinter.CTkFrame(master=l1, width=420, height=700, corner_radius=15)
frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew",
           columnspan=2)  # Use column 1 for the frame, spanning two columns

l2 = customtkinter.CTkLabel(master=frame, text="Gestion de Routage IP", font=('Century Gothic', 20))
l2.grid(row=0, column=0, padx=20, pady=10, sticky="w")



entry1 = customtkinter.CTkEntry(master=frame, width=330, placeholder_text='Entrez le nombre des routeurs à étudier')
entry1.grid(row=2, column=0, padx=20, pady=10, sticky="w")

# Create custom button
button1 = customtkinter.CTkButton(master=frame, width=20, text="Next",
                                  command=lambda: button_function_route(frame), corner_radius=6)
button1.grid(row=3, column=0, padx=20, pady=10, sticky="w")

# Configure row and column weights to allow resizing
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

app.mainloop()


