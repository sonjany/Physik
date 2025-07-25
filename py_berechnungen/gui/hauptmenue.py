import tkinter as tk
from tkinter import messagebox
from gui.physik_menue import starte_physik
from gui.astrophysik_menue import starte_astrophysik


def beenden(root):
    if messagebox.askokcancel("Beenden"):
        root.destroy()


def starte_menue():
    root = tk.Tk()
    root.title("Physik- und Astrophysikrechner")
    root.geometry("800x500")

    info_label = tk.Label(
        master=root, 
        text="Berechnung auswählen", 
        fg="black",
        bg="orange",
        font=("Arial", 18, "bold")
    )
    info_label.pack(pady=20)

    button_p = tk.Button(root, text="Physik", command=lambda: starte_physik(root), font=("Arial",18))
    button_p.pack(pady=10)
    button_ap = tk.Button(root, text="Astrophysik", command=lambda: starte_astrophysik(root), font=("Arial",18))
    button_ap.pack(pady=10)

    button_destroy = tk.Button(root, text="Beenden", width=50, command=lambda: beenden(root))
    button_destroy.pack(pady=60)

    root.mainloop()

#starte_menue()