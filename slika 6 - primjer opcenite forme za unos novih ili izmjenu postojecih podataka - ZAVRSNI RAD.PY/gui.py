import ctypes
import tkinter as tk
from tkinter import messagebox
from crud import get_all_users
from datetime_utils import *
from weather_api import WeatherForecast
from main import session

root = tk.Tk()
root.title("Algebra | PyPosuda")
root.configure(bg="#282828") # tamno siva pozadina

root.geometry('600x400')


frame = tk.LabelFrame (root, width=700, height=500, text= 'Naziv forme',bg='#282828',fg='white', font='Arial') 
frame.grid(column=0, row=0, padx=10, pady=10)

frame1 = tk.Label (frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=1) 
frame1 =tk.Entry(frame)
frame1.grid(column=1, row=1, padx=10, pady=10)

frame2 = tk.Label(frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=2)
frame2 =tk.Entry(frame)
frame2.grid(column=1, row=2, padx=10, pady=10)

frame3 = tk.Label(frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=3)
frame3 =tk.Entry(frame)
frame3.grid(column=1, row=3, padx=10, pady=10)

frame4 = tk.Label(frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=4)
frame4 =tk.Entry(frame)
frame4.grid(column=1, row=4, padx=10, pady=10)

frame5 = tk.Label(frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=5)
frame5 =tk.Entry(frame)
frame5.grid(column=1, row=5, padx=10, pady=10)

frame6 = tk.Label(frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=6)
frame6 =tk.Entry(frame)
frame6.grid(column=1, row=6, padx=10, pady=10)

frame7 = tk.Label(frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=7)
frame7 =tk.Entry(frame)
frame7.grid(column=1, row=7, padx=10, pady=10)

frame8 = tk.Label(frame, text= 'Naziv polja za unos',bg='#282828',fg='white',font='Arial').grid(row=8)
frame8 =tk.Entry(frame)
frame8.grid(column=1, row=8, padx=10, pady=10)

profil_image = tk.Button(root, text='Profil',bg='#282828', fg='white',font=('Arial', 10))
profil_image.grid(column=6, row=1, padx=5, pady=5)

next_image = tk.Button(root, text='Next image',bg='#282828', fg='white',font=('Arial', 10))
next_image.grid(column=4, row=0, padx=5, pady=5)

sync_image = tk.Button(root, text='Sync' ,bg='#282828', fg='white',font=('Arial', 10))
sync_image.grid(column=5, row=0, padx=5, pady=5)

pohrani_image = tk.Button(root, text='Pohrani' ,bg='#282828', fg='white',font=('Arial', 10))
pohrani_image.grid(column=4, row=1, padx=5, pady=5)

odustani_image = tk.Button(root, text='Odustani' ,bg='#282828', fg='white',font=('Arial', 10))
odustani_image.grid(column=5, row=1, padx=5, pady=5)





root.mainloop()



