#import tkinter as tk
from itertools import count
from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile 

import tkinter
import requests
import json
import mysql.connector

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")

        #self.bg = PhotoImage(file="background-login-page.jpg")

        #lbl_bg = Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="#D1D1D1")
        frame.place(x=610,y=170,width=340,height=450)

        get_str=Label(frame,text="Welcome, Admin", font=("Calibri",20,"bold"),fg="black",bg="#D1D1D1")
        get_str.place(x=60,y=60)

        #label
        label_username=lbl=Label(frame,text="Username:", font=("Calibri",15),fg="black",bg="#D1D1D1")
        label_username.place(x=40,y=140)

        self.txtuser=ttk.Entry(frame,font=("Calibri",13))
        self.txtuser.place(x=40,y=170,width=260)

        label_password=lbl=Label(frame,text="Password:", font=("Calibri",15),fg="black",bg="#D1D1D1")
        label_password.place(x=40,y=200)

        self.txtpass=ttk.Entry(frame,font=("Calibri",13), show = '*')
        self.txtpass.place(x=40,y=230,width=260)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login", font=("Calibri",15),bd=3,relief=RAISED,fg="white",bg="#008A31")
        loginbtn.place(x=110,y=350,width=120,height=35)
    
    def login(self):

        IDAdmin = self.txtuser.get()
        Password_Admin = self.txtpass.get()

        if IDAdmin=="" or Password_Admin=="":
            messagebox.showerror("Error","all field required")
        elif IDAdmin=="sabrina" and Password_Admin=="Admin123":
            #messagebox.showinfo("Success","Welcome to Admin Page")
            self.new_window=Toplevel(self.root)
            self.app=adminpage_window(self.new_window)
        else:
            messagebox.showerror("Invalid","Invalid username or password")
            """conn=mysql.connector.connect(host="localhost",user="root",password="Admin123_",database="databaseadm")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from data admin where nama_admin=%s and password_admin=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                            ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                self.new_window=Toplevel(self.new_window)
                self.app=adminpage_window(self.new_window)
            
            conn.commit()
            conn.close()"""

class adminpage_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Page")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root,text="Admin Page",fg="black",font=("Calibri",30,"bold"))
        lbltitle.grid(row=0,column=0, sticky=W, columnspan=2, padx=10, pady=10)

        #frame untuk logo
        logo1_frame = Frame(self.root, bg="#D1D1D1")
        logo1_frame.place(x=275,y=200,width=400,height=400)

        logo2_frame = Frame(self.root, bg="#D1D1D1")
        logo2_frame.place(x=875,y=200,width=400,height=400)
        
        #logo untuk button
        image1 = Image.open("books.png")
        resize_image = image1.resize((150,150))
        self.image_book = ImageTk.PhotoImage(resize_image)
        image_book_label = Label(logo1_frame, image=self.image_book, bg="#D1D1D1")
        image_book_label.place(x=125, y=80)

        image2 = Image.open("pay.png")
        resize_image2 = image2.resize((150,150))
        self.image_pay = ImageTk.PhotoImage(resize_image2)
        image_pay_label = Label(logo2_frame, image=self.image_pay, bg="#D1D1D1")
        image_pay_label.place(x=125, y=80)

        #button
        book_btn=Button(logo1_frame,command=self.book, text="Data Buku", font=("Calibri",15),bd=3,fg="black")
        book_btn.place(x=125,y=290,width=150,height=50)

        customer_btn=Button(logo2_frame,text="Data Pembayaran", font=("Calibri",15),bd=3,fg="black")
        customer_btn.place(x=100,y=290,width=200,height=50)

    def book(self):
        self.new_window=Toplevel(self.root)
        self.app=databuku_window(self.new_window)

class databuku_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Data Buku")
        self.root.geometry("1550x800+0+0")

        '''self.id_buku=StringVar()
        self.nama_buku=StringVar()
        self.pengarang_buku=StringVar()
        self.penerbit_buku=StringVar()
        self.kategori_buku=StringVar()
        self.bahasa_buku=StringVar()
        self.harga_buku=StringVar()
        self.stok_buku=StringVar()'''


        #lbltitle = Label(self.root,text="Data Buku",fg="black",font=("Calibri",30,"bold"))
        #lbltitle.grid(row=0,column=0, sticky=W, columnspan=2, padx=10, pady=10)

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
        tabel_frame.place(x=10, y=30, width=755, height=500)

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
        self.my_tabel['column'] = ("IDBuku","Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku", "Stok Buku")
        
        #headings
        self.my_tabel.heading("#0", text="", anchor=W)
        self.my_tabel.heading("IDBuku", text="ID Buku")
        self.my_tabel.heading("Nama Buku", text="Nama Buku")
        self.my_tabel.heading("Pengarang Buku", text="Pengarang Buku")
        self.my_tabel.heading("Penerbit Buku", text="Penerbit Buku")
        self.my_tabel.heading("Kategori Buku", text="Kategori Buku")
        self.my_tabel.heading("Bahasa Buku", text="Bahasa Buku")
        self.my_tabel.heading("Harga Buku", text="Harga Buku")
        self.my_tabel.heading("Stok Buku", text="Stok Buku")

        self.my_tabel["show"]="headings"

        #format columns
        self.my_tabel.column("#0", width=0, stretch=NO)
        self.my_tabel.column("IDBuku", width=100)
        self.my_tabel.column("Nama Buku", width=100)
        self.my_tabel.column("Pengarang Buku", width=100)
        self.my_tabel.column("Penerbit Buku", width=100)
        self.my_tabel.column("Kategori Buku", width=100)
        self.my_tabel.column("Bahasa Buku", width=100)
        self.my_tabel.column("Harga Buku", width=100)
        self.my_tabel.column("Stok Buku", width=100)

        self.my_tabel.pack(fill=BOTH,expand=1)

        #data dummy
        data = [
            [1, "Bibi Gill", "Tere Liye", "PENERBIT SABAK GRIP", "Fiksi Ilmiah", "Indonesia", 89000, 50],
            [2, "Spy X Family 03", "Endo Tatsuya", "Elex Media Komputindo", "Manga", "Indonesia", 36000, 50],
            [3, "Laut Bercerita", "Leila S. Chudori", "Kepustakaan Populer Gramedia", "Fiksi Ilmiah", "Indonesia", 70000, 50],
            [4, "Sebuah Seni untuk Bersikap Bodo Amat", "Nark Manson", "Gramedia Widiasarana Indonesia", "Pengembangan Diri", "Indonesia", 54600, 50],
            [5, "Hai, Miko! 34 - Premium", "Ono Eriko", "m&c!", "Manga", "Indonesia", 42000, 50],
            [6, "Home Sweet Loan", "Almira Bastari", "Gramedia Pustaka Utama", "Novel", "Indonesia", 66500, 50],
            [7, "Jujutsu Kaisen 05", "Gege Akutami", "Elex Media Komputindo", "Manga", "Indonesia", 32000, 50],
            [8, "Sagaras", "Tere Liye", "PENERBIT SABAK GRIP", "Fiksi Ilmiah", "Indonesia", 89000, 50],
            [9, "Merawat Luka Batin", "Dr Jiemi Ardian", "Gramedia Pustaka Utama", "Pengembangan Diri", "Indonesia", 78400, 50],
            [10, "Heartbreak Motel", "Ika Natassa", "Gramedia Pustaka Utama", "Romance", "Indonesia", 69300, 50],
            [11, "Anak Bajang Mengayun Bulan", "Sindhunata", "Gramedia Pustaka Utama", "Novel", "Indonesia", 170800, 50],
            [12, "Pachinko", "Min Jin Lee", "Gramedia Pustaka Utama", "Romance", "Indonesia", 95200, 50],
            [13, "Cr: The Sweetest Hours", "Cathryn Parry", "Elex Media Komputindo", "Romance", "Indonesia", 72000, 50],
            [14, "Membasmi Frustasi Fotografer", "Edwin Effendi", "Elex Media Komputindo", "Seni Desain", "Indonesia", 72000, 50],
            [15, "Panduan Praktis Seminar Edisi Ketiga", "Indra Yuzal", "Pt Rajagrafindo Persada", "Pendidikan", "Indonesia", 69000, 50],
            [16, "Cake Kekinian Favorit", "Meida Felici", "Gramedia Pustaka Utama", "Buku Masakan", "Indonesia", 78400, 50],
            [17, "Yuk Belajar Nabung Saham", "Ryan Filbert Wijaya, S.Sn, ME.", "Elex Media Komputindo", "Finansial", "Indonesia", 63000, 50],
            [18, "Siap-Siap Jadi Orangtua", "Najelaa Shihab", "Buah Hati", "Buku Parenting", "Indonesia", 120000, 50],
            [19, "Violet", "Kyung Sook Shin", "Gramedia Pustaka Utama", "Sastra", "Indonesia", 61600, 50],
            [20, "35 Fabel Anak", "Any Hidayati", "Anak Hebat Indonesia", "Buku Anak", "Indonesia", 55500, 50]
        ]

        #create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lemonchiffon3")

        #add our data to the screen
        global count
        count = 0

        for record in data:
            if count % 2 == 0:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))
        
            #increment count
            count += 1
        
        
        #add entry boxes
        #frame
        viewdata_frame = LabelFrame(self.root, text="Details")
        viewdata_frame.place(x=785, y=30, width=735, height=750)

        #form input data
        label_id_buku=Label(viewdata_frame,text="ID Buku :", fg="black")
        label_id_buku.place(x=10,y=30)
        label_nama_buku=Label(viewdata_frame,text="Nama Buku :", fg="black")
        label_nama_buku.place(x=10,y=60)
        label_pengarang_buku=Label(viewdata_frame,text="Pengarang Buku :", fg="black")
        label_pengarang_buku.place(x=10,y=90)
        label_penerbit_buku=Label(viewdata_frame,text="Penerbit Buku :", fg="black")
        label_penerbit_buku.place(x=10,y=120)
        label_kategori_buku=Label(viewdata_frame,text="Kategori Buku :", fg="black")
        label_kategori_buku.place(x=10,y=150)
        label_bahasa_buku=Label(viewdata_frame,text="Bahasa Buku :", fg="black")
        label_bahasa_buku.place(x=10,y=180)
        label_harga_buku=Label(viewdata_frame,text="Harga Buku :", fg="black")
        label_harga_buku.place(x=10,y=210)
        label_stok_buku=Label(viewdata_frame,text="Stok Buku :", fg="black")
        label_stok_buku.place(x=10,y=240)
        label_deskripsi_buku=Label(viewdata_frame,text="Deskripsi Buku :", fg="black")
        label_deskripsi_buku.place(x=10,y=270)

        #entry boxes
        self.txt_idbuku=ttk.Entry(viewdata_frame)
        self.txt_idbuku.place(x=135,y=30,width=550)
        self.txt_namabuku=ttk.Entry(viewdata_frame)
        self.txt_namabuku.place(x=135,y=60,width=550)
        self.txt_pengarangbuku=ttk.Entry(viewdata_frame)
        self.txt_pengarangbuku.place(x=135,y=90,width=550)
        self.txt_penerbitbuku=ttk.Entry(viewdata_frame)
        self.txt_penerbitbuku.place(x=135,y=120,width=550)
        self.txt_kategoribuku=ttk.Entry(viewdata_frame)
        self.txt_kategoribuku.place(x=135,y=150,width=550)
        self.txt_bahasabuku=ttk.Entry(viewdata_frame)
        self.txt_bahasabuku.place(x=135,y=180,width=550)
        self.txt_hargabuku=ttk.Entry(viewdata_frame)
        self.txt_hargabuku.place(x=135,y=210,width=550)
        self.txt_stokbuku=ttk.Entry(viewdata_frame)
        self.txt_stokbuku.place(x=135,y=240,width=550)
        self.txt_deskripsibuku = Text(viewdata_frame)
        self.txt_deskripsibuku.place(x=135, y=270, width=550, height=185)

        def open_file():
            global img
            
            f_types = [('JPG Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            #print(filename)
            img = Image.open(filename)
            print(filename)
            resize_image = img.resize((150,200))
            image1 = ImageTk.PhotoImage(resize_image)

            label1 = tkinter.Label(viewdata_frame, image=image1)
            label1.image = image1

            #position image
            label1.place(x=150, y=480)

        label_upld_foto = Label(viewdata_frame, text='Cover buku (jpg):')
        label_upld_foto.place(x=10, y=480)

        upld_foto_btn = Button(viewdata_frame, text='Choose File', command = lambda:open_file())
        upld_foto_btn.place(x=10, y=510)


        #add buttons
        #button tambah buku
        add_new_book_btn=Button(self.root, text="clear", command=self.clear, font=("Calibri",12),bd=3,fg="black")
        add_new_book_btn.place(x=10,y=550,width=120,height=35)

        delete_book_btn=Button(self.root, text="tambah", command=self.tambah_buku, font=("Calibri",12),bd=3,fg="black")
        delete_book_btn.place(x=130,y=550,width=120,height=35)

        viewall_book_btn=Button(self.root, text="lihat detail", command=self.lihat_detail, font=("Calibri",12),bd=3,fg="black")
        viewall_book_btn.place(x=250,y=550,width=180,height=35)

        edit_book_btn=Button(self.root, text="edit", font=("Calibri",12),bd=3,fg="black")
        edit_book_btn.place(x=430,y=550,width=120,height=35)

        #self.my_tabel.bind("<ButtonRelease-1>", self.lihat_detail)
        
    def clear(self):
        #clear entry boxes
        self.txt_idbuku.configure(state=NORMAL)
        self.txt_idbuku.delete(0, END)
        self.txt_idbuku.configure(state=DISABLED)
        self.txt_namabuku.delete(0, END)
        self.txt_pengarangbuku.delete(0, END)
        self.txt_penerbitbuku.delete(0, END)
        self.txt_kategoribuku.delete(0, END)
        self.txt_bahasabuku.delete(0, END)
        self.txt_hargabuku.delete(0, END)
        self.txt_stokbuku.delete(0, END)
        #self.txt_deskripsibuku.delete(0, END)


    def tambah_buku(self):
        Nama_Buku = self.txt_namabuku.get()
        Pengarang_Buku = self.txt_pengarangbuku.get()
        Penerbit_Buku = self.txt_penerbitbuku.get()
        Kategori_Buku = self.txt_kategoribuku.get()
        Bahasa_Buku = self.txt_bahasabuku.get()
        Harga_Buku = self.txt_hargabuku.get()
        Stok_Buku = self.txt_stokbuku.get()
        Deskripsi_Buku = self.txt_deskripsibuku.get(1.0, END)

        #creating dictionary
        data_tambah_buku = {}
        data_tambah_buku['Nama_Buku'] = Nama_Buku
        data_tambah_buku['Pengarang_Buku'] = Pengarang_Buku
        data_tambah_buku['Penerbit_Buku'] = Penerbit_Buku
        data_tambah_buku['Kategori_Buku'] = Kategori_Buku
        data_tambah_buku['Bahasa_Buku'] = Bahasa_Buku
        data_tambah_buku['Harga_Buku'] = Harga_Buku
        data_tambah_buku['Stok_Buku'] = Stok_Buku
        data_tambah_buku['Deskripsi_Buku'] = Deskripsi_Buku

        out_file = open("data_tambah_buku.json", "w")
        json.dump(data_tambah_buku,out_file)
        print(data_tambah_buku)

    def lihat_detail(self):
        #clear entry boxes
        self.txt_idbuku.configure(state=NORMAL)
        self.txt_idbuku.delete(0, END)
        self.txt_namabuku.delete(0, END)
        self.txt_pengarangbuku.delete(0, END)
        self.txt_penerbitbuku.delete(0, END)
        self.txt_kategoribuku.delete(0, END)
        self.txt_bahasabuku.delete(0, END)
        self.txt_hargabuku.delete(0, END)
        self.txt_stokbuku.delete(0, END)
        #self.txt_deskripsibuku.delete(0, END)

        #grab record number
        selected = self.my_tabel.focus()

        #grab record values
        values = self.my_tabel.item(selected, 'values')

        #output to entry boxes
        self.txt_idbuku.insert(0, values[0])
        self.txt_idbuku.configure(state=DISABLED)
        self.txt_namabuku.insert(0, values[1])
        self.txt_pengarangbuku.insert(0, values[2])
        self.txt_penerbitbuku.insert(0, values[3])
        self.txt_kategoribuku.insert(0, values[4])
        self.txt_bahasabuku.insert(0, values[5])
        self.txt_hargabuku.insert(0, values[6])
        self.txt_stokbuku.insert(0, values[7])

    '''def add_new_book(self):
        self.new_window=Toplevel(self.root)
        self.app=tambahbuku_window(self.new_window)'''


class tambahbuku_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Tambah Buku")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root,text="Tambah Buku",fg="black",font=("Calibri",30,"bold"))
        lbltitle.grid(row=0,column=0, sticky=W, columnspan=2, padx=10, pady=10)

        #frame input data
        inputdatabukuframe = Frame(self.root, bg="#D1D1D1")
        inputdatabukuframe.place(x=50,y=80,width=1440,height=680)

        #form input data
        label_nama_buku=Label(inputdatabukuframe,text="Nama Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_nama_buku.place(x=40,y=40)
        label_pengarang_buku=Label(inputdatabukuframe,text="Pengarang Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_pengarang_buku.place(x=40,y=120)
        label_penerbit_buku=Label(inputdatabukuframe,text="Penerbit Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_penerbit_buku.place(x=40,y=200)
        label_kategori_buku=Label(inputdatabukuframe,text="Kategori Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_kategori_buku.place(x=40,y=280)
        label_bahasa_buku=Label(inputdatabukuframe,text="Bahasa Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_bahasa_buku.place(x=720,y=40)
        label_harga_buku=Label(inputdatabukuframe,text="Harga Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_harga_buku.place(x=720,y=120)
        label_stok_buku=Label(inputdatabukuframe,text="Stok Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_stok_buku.place(x=720,y=200)
        label_deskripsi_buku=Label(inputdatabukuframe,text="Deskripsi Buku :", font=("Calibri",15),fg="black", bg="#D1D1D1")
        label_deskripsi_buku.place(x=40,y=360)
        
        
        #entri boxes
        self.txt_namabuku=ttk.Entry(inputdatabukuframe,font=("Calibri",13))
        self.txt_namabuku.place(x=40,y=80,width=640)
        self.txt_pengarangbuku=ttk.Entry(inputdatabukuframe,font=("Calibri",13))
        self.txt_pengarangbuku.place(x=40,y=160,width=640)
        self.txt_penerbitbuku=ttk.Entry(inputdatabukuframe,font=("Calibri",13))
        self.txt_penerbitbuku.place(x=40,y=240,width=640)
        self.txt_kategoribuku=ttk.Entry(inputdatabukuframe,font=("Calibri",13))
        self.txt_kategoribuku.place(x=40,y=320,width=640)
        self.txt_bahasabuku=ttk.Entry(inputdatabukuframe,font=("Calibri",13))
        self.txt_bahasabuku.place(x=720,y=80,width=640)
        self.txt_hargabuku=ttk.Entry(inputdatabukuframe,font=("Calibri",13))
        self.txt_hargabuku.place(x=720,y=160,width=640)
        self.txt_stokbuku=ttk.Entry(inputdatabukuframe,font=("Calibri",13))
        self.txt_stokbuku.place(x=720,y=240,width=640)
        self.txt_deskripsibuku = Text(inputdatabukuframe,font=("Calibri",13))
        self.txt_deskripsibuku.place(x=40, y=400, width=1360, height=185)

        #button tambah buku
        tambahbuku_btn=Button(inputdatabukuframe,command=self.tambahbuku, text="Tambah Buku", font=("Calibri",15),bd=3,fg="black")
        tambahbuku_btn.place(x=40,y=625,width=200,height=35)

    def tambahbuku(self):
        Nama_Buku = self.txt_namabuku.get()
        Pengarang_Buku = self.txt_pengarangbuku.get()
        Penerbit_Buku = self.txt_penerbitbuku.get()
        Kategori_Buku = self.txt_kategoribuku.get()
        Bahasa_Buku = self.txt_bahasabuku.get()
        Harga_Buku = self.txt_hargabuku.get()
        Stok_Buku = self.txt_stokbuku.get()
        Deskripsi_Buku = self.txt_deskripsibuku.get(1.0, END)

        #creating dictionary
        data_tambah_buku = {}
        data_tambah_buku['Nama_Buku'] = Nama_Buku
        data_tambah_buku['Pengarang_Buku'] = Pengarang_Buku
        data_tambah_buku['Penerbit_Buku'] = Penerbit_Buku
        data_tambah_buku['Kategori_Buku'] = Kategori_Buku
        data_tambah_buku['Bahasa_Buku'] = Bahasa_Buku
        data_tambah_buku['Harga_Buku'] = Harga_Buku
        data_tambah_buku['Stok_Buku'] = Stok_Buku
        data_tambah_buku['Deskripsi_Buku'] = Deskripsi_Buku

        #print(idbuku," ", namabuku," ", pengarangbuku," ",kategoribuku," ",hargabuku," ",stokbuku)
        #data_tambahbuku = '''{ 'Nama_Buku': '%s', 'Pengarang_Buku': '%s', 'Penerbit_Buku': '%s', 'Kategori_Buku': '%s', 'Bahasa_Buku': '%s', 'Harga_Buku': %s, 'Stok_Buku': %s, 'Deskripsi_Buku': %s}''' %(Nama_Buku, Pengarang_Buku, Penerbit_Buku, Kategori_Buku, Bahasa_Buku, Harga_Buku, Stok_Buku, Deskripsi_Buku)
        #print(data_tambahbuku)
        out_file = open("data_tambah_buku.json", "w")
        json.dump(data_tambah_buku,out_file)
        print(data_tambah_buku)

        #convert string to object
        #json_object = json.loads(data_tambahbuku)

        #print untuk ngecek
        #print(type(json_object))

        #json_object = json.dumps(data_tambahbuku, indent = 4)
        #print(json_object)
        #with open("datatambahbuku.json","w") as outfile:
        #    outfile.write(json_object)


if __name__ == "__main__":
    main()