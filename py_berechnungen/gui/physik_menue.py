import tkinter as tk
from tkinter import messagebox
from physik.konstanten import G
from physik.formeln import (
    berechne_kraft,
    berechne_geschwindigkeit,
    berechne_gewichtskraft
)
#rechnungen importieren

def starte_physik(parent):
    window = tk.Toplevel(parent)
    window.title("Physik")

    tk.Label(window, text="Masse: kg").pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    tk.Label(window, text="Beschleunigung:  m/s²").pack()
    entry2 = tk.Entry(window)
    entry2.pack()

    def push_kraft():
        try:
            masse = float(entry1.get())
            a = float(entry2.get())
            f = berechne_kraft(masse, a)
            messagebox.showinfo("Ergebnis", f"Kraft: {f:.2f} N")
        except ValueError:
            messagebox.showerror("Fehler", "Ungültige Eingabe")

    button_kraft = tk.Button(window, text="F = m * a berechnen", command=push_kraft)
    button_kraft.pack(pady=10)

    tk.Label(window, text="Weg:  m").pack()
    entry3 = tk.Entry(window)
    entry3.pack()

    tk.Label(window, text="Zeit:  s").pack()
    entry4 = tk.Entry(window)
    entry4.pack()

    def push_geschwindigkeit():
        try:
            s = float(entry3.get())
            t = float(entry4.get())
            v = berechne_geschwindigkeit(s,t)
            messagebox.showinfo("Ergebnis", f"Geschwindigkeit: {v} m/s")
        except ValueError as e:
            messagebox.showerror("Fehler", str(e))

    button_gesch = tk.Button(window, text="v = s/t", command=push_geschwindigkeit)
    button_gesch.pack(pady=10)

    tk.Label(window, text="Masse:  kg").pack()
    entry5 = tk.Entry(window)
    entry5.pack()

    def push_gewichtskraft():
        try:
            masse = float(entry5.get())
            fg = berechne_gewichtskraft(masse,G)
            messagebox.showinfo("Ergebnis", f"Gewichtskraft: {fg} N")
        except ValueError as e:
            messagebox.showerror("Fehler", str(e))

    button_fg = tk.Button(window, text="Fg = m*G", command=push_gewichtskraft)
    button_fg.pack(pady=10)


