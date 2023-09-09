import tkinter as tk

window = tk.Tk()
window.geometry("550x400")
window.title("Writer")
window.iconbitmap("file.ico")
window["bg"] = "#ADD8E6"

def save():
    text = text_box.get("1.0", "end-1c")
    print(text)
    name = text_name.get("1.0", "end-1c")
    
    if text == '' or text == " " or name == "" or name == " ":
        save_label.config(text="Estatiti: Fichye a pa gen kontni oubyen ou pa mete non")
    else:
        with open(name, "w") as file:
            file.write(text)
        print()
        save_label.config(text="Estatiti: Tèks la anrejistre ak siksè")
msg = tk.Message(window, text="Tape kontni a nan gwo chan an epi non fiche a nan ti piti a.", width=200).pack()

text_box = tk.Text(window, height=15, width=65)
text_box.config(font=("Times new roman", 12, "bold"))
text_box.place(x=10, y=40)

text_name = tk.Text(window, height=1, width=55, font=("Times new roman", 12))
text_name.place(x=10, y=360)

save_label = tk.Label(window, text="Estati: ---")
save_label.place(x=10, y=335)

save_button = tk.Button(window, text="Anrejistre", relief="raised", command=save)
save_button.place(x=474, y=360)

window.mainloop()