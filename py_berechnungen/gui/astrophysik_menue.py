import tkinter as tk
from tkinter import messagebox
from astrophysik.formeln import (
	berechne_lichtjahr_skm, 
	berechne_lichtjahr_pc,
	berechne_lichtjahr_km,
	quatsch_spass_mit_saturn
)

#rechnungen importieren

def starte_astrophysik(parent):
	window = tk.Toplevel(parent)
	window.title("Astrophysik")
	

	def push_ly_skm():
		wert = berechne_lichtjahr_skm()
		messagebox.showinfo("Lichtjahr (s/km)", f"{wert:.3e} Sekunden pro Kilometer")
		
	def push_ly_pc():
		wert = berechne_lichtjahr_pc()
		messagebox.showinfo("Lichtjahr in parsec", f"{wert:.3f} pc")
		
	def push_ly_km():
		wert = berechne_lichtjahr_km()
		messagebox.showinfo("Lichtjahr in km", f"{wert:.3e} km")
		
	def push_saturn():
		eingabe = entry_mass.get()
		try:
			masse = float(eingabe)
			ergebnis = quatsch_spass_mit_saturn(masse)
			messagebox.showinfo("Saturn-Fun", f"Ergebnis: {ergebnis}")
		except ValueError:
			messagebox.showerror("Fehler", "Bitte eine gültige Masse eingeben.")
		

	button_skm = tk.Button(window, text="Lichtjahr in s/km", command=push_ly_skm)
	button_skm.pack(pady=10)
	button_pc = tk.Button(window, text="Lichtjahr in parsec", command=push_ly_pc)
	button_pc.pack(pady=10)
	button_km = tk.Button(window, text="Lichtjahr in km", command=push_ly_km)
	button_km.pack(pady=10)

	tk.Label(window, text="Masse für Saturn-Test (kg):").pack()
	entry_mass = tk.Entry(window)
	entry_mass.pack()

	button_saturn = tk.Button(window, text="Saturn-Test starten", command=push_saturn)
	button_saturn.pack(pady=10)
