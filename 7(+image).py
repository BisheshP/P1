from tkinter import*
import math,random,os
import datetime
from tkinter import messagebox
from PIL import ImageTk, Image

class main:
    def __init__(self,master):
        self.master = master
        self.master.title("Billing Software")
        self.master.geometry("1300x700+0+0")
        # self.master.config(bg="black")
        self.master.resizable(0,0)
        bg_color = "#001a60"
        T_frame = Frame(self.master)
        T_frame.pack(fill=X)
        title = Label(T_frame, text="B$B Mart", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman",30,"bold"), pady=2)
        title.pack(fill=X)
        # img1 = ImageTk.PhotoImage(Image.open("pic4.png"))
        # img_lbl = Label(title, image=img1)
        # img_lbl.place(x = 490, y=5, height=40, width=50)

        image1 = Image.open("logo.png")
        image1 = image1.resize((65, 44), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image1)

        lbl_1 = Label(T_frame,image=photo1, bd=5, relief=GROOVE, bg=bg_color)
        lbl_1.image1 = photo1
        lbl_1.place(x=460,y=12)

        image2 = Image.open("logo.png")
        image2 = image2.resize((65, 44), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)

        lbl_2 = Label(T_frame,image=photo2, bd=5, relief=GROOVE, bg="#4D006E")
        lbl_2.image2 = photo2
        lbl_2.place(x=760,y=12)
        #================ Date & Time =============================
        self.dt = datetime.date.today()
        date = Label(T_frame, text=self.dt, font="arial 20 bold", bg="#001a60", fg="white")
        date.place(x=1080, y=20)
        
        #====================================Variables========================================
        #==================== Stationary =================================
        self.g_pen = IntVar()
        self.eraser = IntVar()
        self.marker = IntVar()
        self.n_book = IntVar()
        self.g_box = IntVar()
        self.m_pencil = IntVar()
        #==================== Grocery =================================
        self.rice = IntVar()
        self.bread = IntVar()
        self.flour = IntVar()
        self.fish = IntVar()
        self.sugar = IntVar()
        self.cheese = IntVar()
        #==================== Drinks =================================
        self.fanta = IntVar()
        self.real = IntVar()
        self.limca = IntVar()
        self.tuborg = IntVar()
        self.wine = IntVar()
        self.redbull = IntVar()
        #==================== Total Product Price and Tax Variable =================================
        self.stationary_price = StringVar()
        self.grocery_price = StringVar()
        self.drink_price = StringVar()

        self.total_tax = StringVar()
        self.total_amt = StringVar()
        self.received_amt = IntVar()

        #==================== Customer =================================
        self.c_name = StringVar()
        self.c_mob = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        #==================== Check Variables ==========================

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        #================= Stationary Check_F ====================
        def chkg_pen():
            if (var1.get()==1):
                g_pen_en.configure(state = NORMAL)
                g_pen_en.focus()
                g_pen_en.delete('0',END)
                self.g_pen.set("")
            elif (var1.get()==0):
                g_pen_en.configure(state = DISABLED)
                self.g_pen.set("0")
        def chkeraser():
            if (var2.get()==1):
                eraser_en.configure(state = NORMAL)
                eraser_en.focus()
                eraser_en.delete('0',END)
                self.eraser.set("")
            elif (var2.get()==0):
                eraser_en.configure(state = DISABLED)
                self.eraser.set("0")
        def chkmarker():
            if (var3.get()==1):
                marker_en.configure(state = NORMAL)
                marker_en.focus()
                marker_en.delete('0',END)
                self.marker.set("")
            elif (var3.get()==0):
                marker_en.configure(state = DISABLED)
                self.marker.set("0")
        def chkn_book():
            if (var4.get()==1):
                n_book_en.configure(state = NORMAL)
                n_book_en.focus()
                n_book_en.delete('0',END)
                self.n_book.set("")
            elif (var4.get()==0):
                n_book_en.configure(state = DISABLED)
                self.n_book.set("0")
        def chkg_box():
            if (var5.get()==1):
                g_box_en.configure(state = NORMAL)
                g_box_en.focus()
                g_box_en.delete('0',END)
                self.g_box.set("")
            elif (var5.get()==0):
                g_box_en.configure(state = DISABLED)
                self.g_box.set("0")
        def chkm_pencil():
            if (var6.get()==1):
                m_pencil_en.configure(state = NORMAL)
                m_pencil_en.focus()
                m_pencil_en.delete('0',END)
                self.m_pencil.set("")
            elif (var6.get()==0):
                m_pencil_en.configure(state = DISABLED)
                self.m_pencil.set("0")
        #================= Grocery Check_F ====================
        def chkrice():
            if (var7.get()==1):
                rice_en.configure(state = NORMAL)
                rice_en.focus()
                rice_en.delete('0',END)
                self.rice.set("")
            elif (var7.get()==0):
                rice_en.configure(state = DISABLED)
                self.rice.set("0")
        def chkbread():
            if (var8.get()==1):
                bread_en.configure(state = NORMAL)
                bread_en.focus()
                bread_en.delete('0',END)
                self.bread.set("")
            elif (var8.get()==0):
                bread_en.configure(state = DISABLED)
                self.bread.set("0")
        def chkflour():
            if (var9.get()==1):
                flour_en.configure(state = NORMAL)
                flour_en.focus()
                flour_en.delete('0',END)
                self.flour.set("")
            elif (var9.get()==0):
                flour_en.configure(state = DISABLED)
                self.flour.set("0")
        def chkfish():
            if (var10.get()==1):
                fish_en.configure(state = NORMAL)
                fish_en.focus()
                fish_en.delete('0',END)
                self.fish.set("")
            elif (var10.get()==0):
                fish_en.configure(state = DISABLED)
                self.fish.set("0")
        def chksugar():
            if (var11.get()==1):
                sugar_en.configure(state = NORMAL)
                sugar_en.focus()
                sugar_en.delete('0',END)
                self.sugar.set("")
            elif (var11.get()==0):
                sugar_en.configure(state = DISABLED)
                self.sugar.set("0")
        def chkcheese():
            if (var12.get()==1):
                cheese_en.configure(state = NORMAL)
                cheese_en.focus()
                cheese_en.delete('0',END)
                self.cheese.set("")
            elif (var12.get()==0):
                cheese_en.configure(state = DISABLED)
                self.cheese.set("0")
        #================= Drinks Check_F ====================
        def chkfanta():
            if (var13.get()==1):
                fanta_en.configure(state = NORMAL)
                fanta_en.focus()
                fanta_en.delete('0',END)
                self.fanta.set("")
            elif (var13.get()==0):
                fanta_en.configure(state = DISABLED)
                self.fanta.set("0")
        def chkreal():
            if (var14.get()==1):
                real_en.configure(state = NORMAL)
                real_en.focus()
                real_en.delete('0',END)
                self.real.set("")
            elif (var14.get()==0):
                real_en.configure(state = DISABLED)
                self.real.set("0")
        def chklimca():
            if (var15.get()==1):
                limca_en.configure(state = NORMAL)
                limca_en.focus()
                limca_en.delete('0',END)
                self.limca.set("")
            elif (var15.get()==0):
                limca_en.configure(state = DISABLED)
                self.limca.set("0")
        def chktuborg():
            if (var16.get()==1):
                tuborg_en.configure(state = NORMAL)
                tuborg_en.focus()
                tuborg_en.delete('0',END)
                self.tuborg.set("")
            elif (var16.get()==0):
                tuborg_en.configure(state = DISABLED)
                self.tuborg.set("0")
        def chkwine():
            if (var17.get()==1):
                wine_en.configure(state = NORMAL)
                wine_en.focus()
                wine_en.delete('0',END)
                self.wine.set("")
            elif (var17.get()==0):
                wine_en.configure(state = DISABLED)
                self.wine.set("0")
        def chkredbull():
            if (var18.get()==1):
                redbull_en.configure(state = NORMAL)
                redbull_en.focus()
                redbull_en.delete('0',END)
                self.redbull.set("")
            elif (var18.get()==0):
                redbull_en.configure(state = DISABLED)
                self.redbull.set("0")
                
                

        #================== Costumer Detail Frame ====================
        F1 = LabelFrame(self.master, text="Customer Details", font=("times new roman",15,"bold"), bd=12, relief=GROOVE, fg="gold", bg="#001a60")
        F1.place(x=0, y=75, relwidth=1)

        name_l = Label(F1, text="Customer Name", bg="#001a60", fg="white", font=("cambria",18,"bold"))
        name_l.pack(fill=BOTH, expand=True, side=LEFT)
        name_en=Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN)
        name_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)
        
        phn_l = Label(F1, text="Mobile No.", bg="#001a60", fg="white", font=("times new roman",18,"bold"))
        phn_l.pack(fill=BOTH, expand=True, side=LEFT)
        phn_en = Entry(F1, width=15, textvariable=self.c_mob, font="arial 15", bd=7, relief=SUNKEN)
        phn_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)

        billno_l = Label(F1, text="Customer Bill No.", bg="#001a60", fg="white", font=("times new roman",18,"bold"))
        billno_l.pack(fill=BOTH, expand=True, side=LEFT)
        billno_en =Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN)
        billno_en.pack(fill=BOTH, expand=True, side=LEFT, pady=3)
        
        search_btn = Button(F1, text="Search", command=self.find_receipt, width=10, bd=7, font="arial 12 bold")
        search_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=12, pady=3)

        #================== Stationary Frame ===================
        F2 = LabelFrame(self.master, text="Stationary", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F2.place(x=364, y=165, width=325, height=380)

        g_pen_l = Checkbutton(F2, text="Gel Pen", font=("times new roman",16,"bold"),variable=var1, onvalue=1, offvalue=0, command=chkg_pen, bg=bg_color, fg="lightgreen")
        g_pen_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g_pen_en = Entry(F2, textvariable=self.g_pen, width=9,state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        g_pen_en.grid(row=0, column=1, padx=10, pady=10)

        eraser_l = Checkbutton(F2, text="Eraser", font=("times new roman",16,"bold"),variable=var2, onvalue=1, offvalue=0, command=chkeraser, bg=bg_color, fg="lightgreen")
        eraser_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        eraser_en = Entry(F2, width=9, textvariable=self.eraser,state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        eraser_en.grid(row=1, column=1, padx=10, pady=10)

        marker_l = Checkbutton(F2, text="Marker", font=("times new roman",16,"bold"),variable=var3, onvalue=1, offvalue=0, command=chkmarker, bg=bg_color, fg="lightgreen")
        marker_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        marker_en = Entry(F2, width=9, textvariable=self.marker, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        marker_en.grid(row=2, column=1, padx=10, pady=10)

        n_book_l = Checkbutton(F2, text="Notebook", font=("times new roman",16,"bold"),variable=var4, onvalue=1, offvalue=0, command=chkn_book, bg=bg_color, fg="lightgreen")
        n_book_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        n_book_en = Entry(F2, width=9, textvariable=self.n_book, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        n_book_en.grid(row=3, column=1, padx=10, pady=10)

        g_box_l = Checkbutton(F2, text="Geometry Box", font=("times new roman",16,"bold"),variable=var5, onvalue=1, offvalue=0, command=chkg_box, bg=bg_color, fg="lightgreen")
        g_box_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g_box_en = Entry(F2, width=9, textvariable=self.g_box, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        g_box_en.grid(row=4, column=1, padx=10, pady=10)

        m_pencil_l = Checkbutton(F2, text="Color Pencils", font=("times new roman",16,"bold"),variable=var6, onvalue=1, offvalue=0, command=chkm_pencil, bg=bg_color, fg="lightgreen")
        m_pencil_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        m_pencil_en = Entry(F2, width=9, textvariable=self.m_pencil, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        m_pencil_en.grid(row=5, column=1, padx=10, pady=10)
        


        #================== Grocery Frame =====================
        F3 = LabelFrame(self.master, text="Grocery", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F3.place(x=694, y=165, width=325, height=380)

        rice_l = Checkbutton(F3, text="Rice", font=("times new roman",16,"bold"), variable=var7, onvalue=1, offvalue=0, command=chkrice, bg=bg_color, fg="lightgreen")
        rice_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rice_en = Entry(F3, width=10, textvariable=self.rice, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        rice_en.grid(row=0, column=1, padx=10, pady=10)

        bread_l = Checkbutton(F3, text="Brown Bread", font=("times new roman",16,"bold"), variable=var8, onvalue=1, offvalue=0, command=chkbread, bg=bg_color, fg="lightgreen")
        bread_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        bread_en = Entry(F3, width=10, textvariable=self.bread, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        bread_en.grid(row=1, column=1, padx=10, pady=10)

        flour_l = Checkbutton(F3, text="Flour", font=("times new roman",16,"bold"), variable=var9, onvalue=1, offvalue=0, command=chkflour, bg=bg_color, fg="lightgreen")
        flour_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        flour_en = Entry(F3, width=10, textvariable=self.flour, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        flour_en.grid(row=2, column=1, padx=10, pady=10)

        fish_l = Checkbutton(F3, text="Fish", font=("times new roman",16,"bold"), variable=var10, onvalue=1, offvalue=0, command=chkfish, bg=bg_color, fg="lightgreen")
        fish_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        fish_en = Entry(F3, width=10, textvariable=self.fish, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        fish_en.grid(row=3, column=1, padx=10, pady=10)

        sugar_l = Checkbutton(F3, text="Sugar", font=("times new roman",16,"bold"), variable=var11, onvalue=1, offvalue=0, command=chksugar, bg=bg_color, fg="lightgreen")
        sugar_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_en = Entry(F3, width=10, textvariable=self.sugar, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        sugar_en.grid(row=4, column=1, padx=10, pady=10)

        cheese_l = Checkbutton(F3, text="Cheese", font=("times new roman",16,"bold"), variable=var12, onvalue=1, offvalue=0, command=chkcheese, bg=bg_color, fg="lightgreen")
        cheese_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        cheese_en = Entry(F3, width=10, textvariable=self.cheese, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        cheese_en.grid(row=5, column=1, padx=10, pady=10)
        

        #================== Drinks Frame ======================
        F4 = LabelFrame(self.master, text="Drinks", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F4.place(x=1024, y=165, width=275, height=380)

        fanta_l = Checkbutton(F4, text="Fanta", font=("times new roman",16,"bold"), variable=var13, onvalue=1, offvalue=0, command=chkfanta, bg=bg_color, fg="lightgreen")
        fanta_l.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        fanta_en = Entry(F4, width=10, textvariable=self.fanta, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        fanta_en.grid(row=0, column=1, padx=10, pady=10)

        real_l = Checkbutton(F4, text="Real", font=("times new roman",16,"bold"), variable=var14, onvalue=1, offvalue=0, command=chkreal, bg=bg_color, fg="lightgreen")
        real_l.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        real_en = Entry(F4, width=10, textvariable=self.real, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        real_en.grid(row=1, column=1, padx=10, pady=10)

        limca_l = Checkbutton(F4, text="Limca", font=("times new roman",16,"bold"), variable=var15, onvalue=1, offvalue=0, command=chklimca, bg=bg_color, fg="lightgreen")
        limca_l.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        limca_en = Entry(F4, width=10, textvariable=self.limca, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        limca_en.grid(row=2, column=1, padx=10, pady=10)

        tuborg_l = Checkbutton(F4, text="Tuborg", font=("times new roman",16,"bold"), variable=var16, onvalue=1, offvalue=0, command=chktuborg, bg=bg_color, fg="lightgreen")
        tuborg_l.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tuborg_en = Entry(F4, width=10, textvariable=self.tuborg, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        tuborg_en.grid(row=3, column=1, padx=10, pady=10)

        wine_l = Checkbutton(F4, text="Wine", font=("times new roman",16,"bold"), variable=var17, onvalue=1, offvalue=0, command=chkwine, bg=bg_color, fg="lightgreen")
        wine_l.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        wine_en = Entry(F4, width=10, textvariable=self.wine, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        wine_en.grid(row=4, column=1, padx=10, pady=10)

        redbull_l = Checkbutton(F4, text="Redbull", font=("times new roman",16,"bold"), variable=var18, onvalue=1, offvalue=0, command=chkredbull, bg=bg_color, fg="lightgreen")
        redbull_l.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        redbull_en = Entry(F4, width=10,textvariable=self.redbull, state=DISABLED, font=("times new roman",16,"bold"), bd=5, relief=SUNKEN)
        redbull_en.grid(row=5, column=1, padx=10, pady=10)

        #================== Receipt Area =========================
        F5 = Frame(self.master, bd=5, relief=GROOVE)
        F5.place(x=5, y=165, width=355, height=380)
        header = Label(F5, text="Receipt", font="arial 15 bold", bd=7, relief=GROOVE)
        header.pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set, bg="lightblue")
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=True)
        

        #================== Button Frame ======================
        F6 = LabelFrame(self.master, text="Bill Menu", bd=8, relief=GROOVE, font=("times new roman",15,"bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=548, relwidth=1, height=152)

        R1_l = Label(F6, text="Total Stationary Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=0, column=0, padx=10, pady=1, sticky="w")
        R1_en = Entry(F6, textvariable=self.stationary_price, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=3)

        R2_l = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=1, column=0, padx=10, pady=1, sticky="w")
        R2_en = Entry(F6, textvariable=self.grocery_price, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=3)

        R3_l = Label(F6, text="Total Drinks Price", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=2, column=0, padx=10, pady=1, sticky="w")
        R3_en = Entry(F6, textvariable=self.drink_price, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=3)
        
        R4_l = Label(F6, text="Total Tax", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=0, column=2, padx=10, pady=1, sticky="w")
        R4_en = Entry(F6, textvariable=self.total_tax, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        R5_l = Label(F6, text="Total Amount", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=1, column=2, padx=10, pady=1, sticky="w")
        R5_en = Entry(F6, textvariable=self.total_amt, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        R_l = Label(F6, text="Received Amount", bg=bg_color, fg="white", font=("times new roman",14,"bold")).grid(row=2, column=2, padx=10, pady=1, sticky="w")
        R_en = Entry(F6, textvariable=self.received_amt, width=16, font="arial 11 bold", bd=6, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=715, y=5, width=570, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=0, padx=4, pady=10)
        Gbill_btn = Button(btn_F, text="Generate Bill",command=self.receipt_area, bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=1, padx=4, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=2, padx=4, pady=5)
        Exit_btn = Button(btn_F, text="Exit",command=self.Exit_app, bg=bg_color, fg="white", pady=15, bd=2, width=10, font="arial 15 bold").grid(row=0, column=3, padx=4, pady=5)
        self.welcome_receipt()


    def total(self):
        self.s_gp_p = self.g_pen.get()*30
        self.s_e_p = self.eraser.get()*50
        self.s_m_p = self.marker.get()*50
        self.s_nb_p = self.n_book.get()*100
        self.s_gb_p = self.g_box.get()*450
        self.s_mp_p = self.m_pencil.get()*150
        self.total_stationary_price = float(
                                        self.s_gp_p+
                                        self.s_e_p+
                                        self.s_m_p+
                                        self.s_nb_p+
                                        self.s_gb_p+
                                        self.s_mp_p
                                        )
        self.stationary_price.set("Rs. "+str(self.total_stationary_price))

        self.g_r_p = self.rice.get()*2650
        self.g_b_p = self.bread.get()*80
        self.g_fl_p = self.flour.get()*350
        self.g_fi_p = self.fish.get()*500
        self.g_s_p = self.sugar.get()*72
        self.g_c_p = self.cheese.get()*200
        self.total_grocery_price = float(
                                        self.g_r_p+
                                        self.g_b_p+
                                        self.g_fl_p+
                                        self.g_fi_p+
                                        self.g_s_p+
                                        self.g_c_p
                                        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))

        self.d_f_p = self.fanta.get()*220
        self.d_r_p = self.real.get()*180
        self.d_l_p = self.limca.get()*150
        self.d_t_p = self.tuborg.get()*340
        self.d_w_p = self.wine.get()*2100
        self.d_rb_p = self.redbull.get()*110
        self.total_drink_price = float(
                                        self.d_f_p+
                                        self.d_r_p+
                                        self.d_l_p+
                                        self.d_t_p+
                                        self.d_w_p+
                                        self.d_rb_p
                                        )
        self.drink_price.set("Rs. "+str(self.total_drink_price))

        self.ttl_tax = (round(
                            ((self.total_stationary_price*0.05)+
                            (self.total_grocery_price*0.01)+
                            (self.total_drink_price*0.03)),2)
                        )
        self.total_tax.set("Rs. "+str(self.ttl_tax))

        self.ttl_amt = (round(
                            ((self.total_stationary_price)+
                            (self.total_grocery_price)+
                            (self.total_drink_price)+
                            (self.ttl_tax)),2)
                        )
        self.total_amt.set("Rs. "+str(self.ttl_amt))


    def welcome_receipt(self):
        self.datetime = datetime.datetime.today().replace(microsecond=0)
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END, "\t    B$B Mart Pvt.Ltd \n\t\tBansbari\n")
        self.txtarea.insert(END, f"\n Bill No.  : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer  : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone No. : {self.c_mob.get()}")
        self.txtarea.insert(END, f"\n P.Time    : {self.datetime}")
        self.txtarea.insert(END, f"\n----------------------------------------")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n----------------------------------------")
   
    def receipt_area(self):
        #======== calculate the amount to return =============
        self.received = self.received_amt.get()
        self.return_amt = (round(
                            (float(self.received) - 
                            self.ttl_amt),2)                    
                            )
        if self.c_name.get()=="" or self.c_mob.get()=="":
            messagebox.showerror("Error", "Customer Details are must")
        elif self.stationary_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        elif self.received_amt.get()==0:
            messagebox.showwarning("Reminder", "Please enter the received amount")
        else:

            self.welcome_receipt()

            #--------- Stationary ------------
            if self.g_pen.get() !=0:
                self.txtarea.insert(END, f"\n Gel Pen\t\t{self.g_pen.get()}\t\t{self.s_gp_p}")   
            if self.eraser.get() !=0:
                self.txtarea.insert(END, f"\n Eraser\t\t{self.eraser.get()}\t\t{self.s_e_p}")   
            if self.marker.get() !=0:
                self.txtarea.insert(END, f"\n Marker\t\t{self.marker.get()}\t\t{self.s_m_p}")   
            if self.n_book.get() !=0:
                self.txtarea.insert(END, f"\n Notebook\t\t{self.n_book.get()}\t\t{self.s_nb_p}")   
            if self.g_box.get() !=0:
                self.txtarea.insert(END, f"\n Geometry Box\t\t{self.g_box.get()}\t\t{self.s_gb_p}")   
            if self.m_pencil.get() !=0:
                self.txtarea.insert(END, f"\n Magic Pencils\t\t{self.m_pencil.get()}\t\t{self.s_mp_p}")

            #--------- Grocery ------------
            if self.rice.get() !=0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")   
            if self.bread.get() !=0:
                self.txtarea.insert(END, f"\n Bread\t\t{self.bread.get()}\t\t{self.g_b_p}")   
            if self.flour.get() !=0:
                self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_fl_p}")   
            if self.fish.get() !=0:
                self.txtarea.insert(END, f"\n Fish\t\t{self.fish.get()}\t\t{self.g_fi_p}")   
            if self.sugar.get() !=0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")   
            if self.cheese.get() !=0:
                self.txtarea.insert(END, f"\n Cheese\t\t{self.cheese.get()}\t\t{self.g_c_p}")

            #--------- Drinks ------------
            if self.fanta.get() !=0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")   
            if self.real.get() !=0:
                self.txtarea.insert(END, f"\n Real\t\t{self.real.get()}\t\t{self.d_r_p}")   
            if self.limca.get() !=0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")   
            if self.tuborg.get() !=0:
                self.txtarea.insert(END, f"\n Tuborg\t\t{self.tuborg.get()}\t\t{self.d_t_p}")   
            if self.wine.get() !=0:
                self.txtarea.insert(END, f"\n Wine\t\t{self.wine.get()}\t\t{self.d_w_p}")   
            if self.redbull.get() !=0:
                self.txtarea.insert(END, f"\n Redbull\t\t{self.redbull.get()}\t\t{self.d_rb_p}") 

            self.txtarea.insert(END, f"\n----------------------------------------")
            if self.stationary_price.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Stationary Price:\t\tRs. {self.total_stationary_price}")
            if self.grocery_price.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Price   :\t\tRs. {self.total_grocery_price}")
            if self.drink_price.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Drinks Price    :\t\tRs. {self.total_drink_price}")
            self.txtarea.insert(END, f"\n Total Tax       :\t\tRs. {self.ttl_tax}")
            self.txtarea.insert(END, f"\n----------------------------------------")
            #if !=0 then..... use garne
            self.txtarea.insert(END, f"\n Total Amount    :\t\tRs. {self.ttl_amt}")
            self.txtarea.insert(END, f"\n----------------------------------------")
            self.txtarea.insert(END, f"\n Received Amount :\t\tRs. {self.received}")
            self.txtarea.insert(END, f"\n Return Amount   :\t\tRs. {self.return_amt}")
            self.txtarea.insert(END, f"\n****************************************")
            self.txtarea.insert(END, "\n\t\tTHANK YOU!\n\t       VISIT AGAIN")
            self.txtarea.insert(END, f"\n****************************************")
            self.save_receipt()
    
    def save_receipt(self):
        op = messagebox.askyesno("Save Receipt", "Do you want to save the Bill?")
        if op>0:
            self.receipt_data = self.txtarea.get("1.0",END)
            f1 = open("bill2/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.receipt_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. {self.bill_no.get()} saved successfully")
        else:
            return

    def find_receipt(self):
        present = "no"
        for i in os.listdir("bill2/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"bill2/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            
            #==================== Stationary =================================
            self.g_pen.set(0)
            self.eraser.set(0)
            self.marker.set(0)
            self.n_book.set(0)
            self.g_box.set(0)
            self.m_pencil.set(0)
            #==================== Grocery =================================
            self.rice.set(0)
            self.bread.set(0)
            self.flour.set(0)
            self.fish.set(0)
            self.sugar.set(0)
            self.cheese.set(0)
            #==================== Drinks =================================
            self.fanta.set(0)
            self.real.set(0)
            self.limca.set(0)
            self.tuborg.set(0)
            self.wine.set(0)
            self.redbull.set(0)
            #==================== Total Product Price and Tax Variable =================================
            self.stationary_price.set("")
            self.grocery_price.set("")
            self.drink_price.set("")

            self.total_tax.set("")
            self.total_amt.set("")
            self.received_amt.set(0)

            #==================== Customer =================================
            self.c_name.set("")
            self.c_mob.set("")
            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")

            self.welcome_receipt()

    def Exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.master.destroy()




Bill_App = Tk()
obj = main(Bill_App)
Bill_App.mainloop()

