from itertools import count
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile 

import json
import tkinter
import requests
import mysql.connector
#import webbrowser

class databayar_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Data Bayar")
        self.root.geometry("1550x800+0+0")

       #style
        style = ttk.Style()

        #theme
        style.theme_use('default')

        #configure the treeview colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="white")

        #change selected color
        style.map('Treeview', background=[('selected', "lemonchiffon4")])

        #frame tabel
        tabel_frame = Frame(self.root)
        tabel_frame.place(x=10, y=30, width=1500, height=500)

        #scrollbar
        tabel_scroll_y = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        tabel_scroll_x = ttk.Scrollbar(tabel_frame, orient=HORIZONTAL)
        tabel_scroll_y.pack(side=RIGHT, fill=Y)
        tabel_scroll_x.pack(side=BOTTOM, fill=X)

        #create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, xscrollcommand=tabel_scroll_x.set, yscrollcommand=tabel_scroll_y.set)
        self.my_tabel.pack()

        #configure our columns
        #tabel_scroll_y=ttk.Scrollbar(command=self.my_tabel.yview)
        #tabel_scroll_x=ttk.Scrollbar(command=self.my_tabel.xview)
        tabel_scroll_y.config(command=self.my_tabel.yview)
        tabel_scroll_x.config(command=self.my_tabel.xview)

        #define columns
        self.my_tabel['column'] = ("IDKonsumen","IDBuku", "Jumlah Buku Dipesan", "Total Harga", "Status Pembayaran", "File Pembayaran", "Waktu Pesan", "Batas Waktu Pembayaran")
        
        #headings
        self.my_tabel.heading("#0", text="", anchor=W)
        self.my_tabel.heading("IDKonsumen", text="ID Konsumen")
        self.my_tabel.heading("IDBuku", text="ID Buku")
        self.my_tabel.heading("Jumlah Buku Dipesan", text="Jumlah Buku Dipesan")
        self.my_tabel.heading("Total Harga", text="Total Harga")
        self.my_tabel.heading("Status Pembayaran", text="Status Pembayaran")
        self.my_tabel.heading("File Pembayaran", text="File Pembayaran")
        self.my_tabel.heading("Waktu Pesan", text="Waktu Pesan")
        self.my_tabel.heading("Batas Waktu Pembayaran", text="Batas Waktu Pembayaran")

        self.my_tabel["show"]="headings"

        #format columns
        self.my_tabel.column("#0", width=0, stretch=NO)
        self.my_tabel.column("IDKonsumen", width=100)
        self.my_tabel.column("IDBuku", width=100)
        self.my_tabel.column("Jumlah Buku Dipesan", width=100)
        self.my_tabel.column("Total Harga", width=100)
        self.my_tabel.column("Status Pembayaran", width=100)
        self.my_tabel.column("File Pembayaran", width=100)
        self.my_tabel.column("Waktu Pesan", width=100)
        self.my_tabel.column("Batas Waktu Pembayaran", width=100)

        self.my_tabel.pack(fill=BOTH,expand=1)



if __name__ == "__main__":
    root=Tk()
    app = databayar_window(root)
    root.mainloop()       