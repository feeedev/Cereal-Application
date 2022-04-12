from tkinter import *
from tkinter import ttk,messagebox,PhotoImage
from tkinter.ttk import Progressbar
from textwrap import fill
from itertools import cycle
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk, Image
from gnews import GNews
import sqlite3,datetime,webbrowser
from time import strftime

def splash_screen() :
    global bg_splash,progress,ttk_style,start_root,splash_root
    splash_root = Tk()

    w_splash = 427
    h_splash = 250
    screen_width = splash_root.winfo_screenwidth()/2 - w_splash/2
    screen_height = splash_root.winfo_screenheight()/2 - h_splash/2
    #x_coordinate = (screen_width/2)-(w_splash/2)
    #y_coordinate = (screen_height/2)-(h_splash/2)
    splash_root.geometry("%dx%d+%d+%d" %(w_splash,h_splash,screen_width,screen_height))
    splash_root.overrideredirect(1)
    
    ttk_style = ttk.Style()
    ttk_style.theme_use('clam')
    ttk_style.configure("red.Horizontal.TProgressbar", foreground='red', background='#F86E6E')
    progress = Progressbar(splash_root,orient=HORIZONTAL,length=500,mode='determinate',style="red.Horizontal.TProgressbar")
    progress.place(x=-10,y=235)
    bg_splash = '#FEEDED'
    Frame(splash_root,width=427,height=241,bg=bg_splash).place(x=0,y=0)
    
    splash_root.after(100,bar)
    
    cereal_title = Label(splash_root,text='CEREAL',fg='#7B6079',bg=bg_splash)
    title_font = ('Calibri (Body)',18,'bold')
    cereal_title.config(font=title_font)
    cereal_title.place(x=50,y=80)

    sub_title = Label(splash_root,text='DIGITAL PLANNER',fg='#7B6079',bg=bg_splash)
    sub_font = ('Calibri (Body)',13)
    sub_title.config(font=sub_font)
    sub_title.place(x=50,y=110)
    
    return splash_root
    
def bar():
    loading_lab =Label(splash_root,text='Loading...',fg='#4E494E',bg=bg_splash)
    loading_font = ('Calibri (Body)',10)
    loading_lab.config(font=loading_font)
    loading_lab.place(x=18,y=210)
    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        splash_root.update_idletasks()
        time.sleep(0.000001)
        r=r+1
    splash_root.destroy()
    mainwindow()

def createconnection() :
    global conn, cursor
    conn = sqlite3.connect('db/cereal_database.db')
    cursor = conn.cursor()

def mainwindow():
    global root,userinfo,pwdinfo,regis_first,regis_last,regis_username,regis_pwd,regis_cfpwd,w,h,cereal_login,login_bg,regis_btn1,login_btn1,regis_bg
    global add_act_btn,del_act_btn,cycle_act,date_ent_spy,act_name_ent_spy,descript_ent_spy,color_ent_spy,menu_bg,home_bg,login_btn,regis_btn
    global profile_bg,chgpwd_btn,back_btn,confirm_btn
    global red_act,pink_act,green_act,blue_act,purple_act,calendar_bg,freetime
    global home_ico,calendar_ico,act_ico,music_ico,timer_ico,del_namecombo_spy,del_date_ent_spy
    root = Tk()
    w = 1200
    h = 700
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='black')
    root.title("Cereal Digital Planner")
    root.option_add('*font',"Calibri 12")
    root.rowconfigure((0,1,2,3,4),weight=1)
    root.columnconfigure((0,1,2,3,4),weight=1)
    root.resizable(0,0)
    root.overrideredirect(0)
    root.iconbitmap("img/icon.ico")
    add_act_btn = PhotoImage(file="img/add_act_btn.png")
    del_act_btn = PhotoImage(file="img/del_act_btn.png")
    cycle_act = PhotoImage(file="img/cycle_act.png").subsample(3,3)
    cereal_login = PhotoImage(file="img/cereal_login.png")
    menu_bg = PhotoImage(file="img/menu_bg.png")
    home_bg = PhotoImage(file="img/home_bg.png")
    login_btn = PhotoImage(file="img/login_btn.png")
    regis_btn = PhotoImage(file="img/regis_btn.png")
    login_bg = PhotoImage(file="img/login_bg.png")
    regis_btn1 = PhotoImage(file="img/regis_btn1.png")
    login_btn1 = PhotoImage(file="img/login_btn1.png")
    regis_bg = PhotoImage(file="img/regis_bg.png")
    profile_bg = PhotoImage(file="img/profile_bg.png")
    chgpwd_btn = PhotoImage(file="img/chgpwd_btn.png")
    back_btn = PhotoImage(file="img/back_btn.png")
    confirm_btn = PhotoImage(file="img/confirm_btn.png")
    red_act = PhotoImage(file="img/red_act.png")
    pink_act = PhotoImage(file="img/pink_act.png")
    green_act = PhotoImage(file="img/green_act.png")
    blue_act = PhotoImage(file="img/blue_act.png")
    purple_act = PhotoImage(file="img/purple_act.png")
    home_ico = PhotoImage(file="img/home_ico.png")
    calendar_ico = PhotoImage(file="img/calendar_ico.png")
    act_ico = PhotoImage(file="img/act_ico.png")
    music_ico = PhotoImage(file="img/music_ico.png")
    timer_ico = PhotoImage(file="img/timer_ico.png")
    calendar_bg = PhotoImage(file="img/calendar_bg.png")
    freetime = PhotoImage(file="img/freetime.png")
    userinfo = StringVar()
    pwdinfo = StringVar()
    regis_first = StringVar()
    regis_last = StringVar()
    regis_username = StringVar()
    regis_pwd = StringVar()
    regis_cfpwd = StringVar()
    date_ent_spy = StringVar()
    act_name_ent_spy = StringVar()
    descript_ent_spy = StringVar()
    color_ent_spy = StringVar()
    del_namecombo_spy = StringVar()
    del_date_ent_spy = StringVar()
    login_page(root)
    #root.mainloop()

images = ["img/news1.png","img/news2.png","img/news3.png"]
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)

def slideShow() :
    img = next(photos)
    photo_frm.config(image=img)
    root.after(5500, slideShow)


def login_page(root) :
    global login_frm,userentry,pwdentry,photo_frm
    # Photo slide
    photo_frm = Label(root)
    root.after(10,lambda:slideShow())
    photo_frm.place(x=0,y=0,width=720,height=700)
    # log in zone
    login_frm = Frame(root,bg="#FEEDED")
    login_frm.rowconfigure((1,2,3,4,5,6,7),weight=1)
    login_frm.rowconfigure((0,8),weight=2)
    login_frm.columnconfigure((0,1),weight=1)
    login_frm.place(x=720,y=0,width=480,height=700)

    Label(login_frm,image=login_bg,bg="#FEEDED").place(x=0,y=0,width=480,height=700)
    Label(login_frm,image=cereal_login,bg="#FEEDED").place(x=69,y=73,width=358,height=50)

    Label(login_frm,text="Username",bg="#FEEDED",fg="#8F8B8F",font="Calibri 16").place(x=92,y=213)
    userentry = Entry(login_frm,textvariable=userinfo,font="Arial 12",relief=FLAT,bd=0)
    userentry.place(x=94,y=247,width=304,height=28)
    userentry.focus_force()
    Label(login_frm,text="Password",bg="#FEEDED",fg="#8F8B8F",font="Calibri 16").place(x=92,y=305)
    pwdentry = Entry(login_frm,textvariable=pwdinfo,show="●",font="Arial 12",relief=FLAT,bd=0)
    pwdentry.place(x=94,y=339,width=304,height=28)

    Button(login_frm,activebackground="#FEEDED",image=login_btn,bg="#FEEDED",relief=FLAT,width=10,command=loginclick,bd=0, cursor="hand2").place(x=116,y=485,width=255,height=60)
    Button(login_frm,activebackground="#FEEDED",image=regis_btn,bg="#FEEDED",relief=FLAT,width=10,command=regiswindow,bd=0, cursor="hand2").place(x=160,y=568,width=168,height=39)
    #Button(login_frm,activebackground="#FEEDED",text="Login",bg="#FEEDED",fg="#7B6079",font="Aparajita 24 bold",relief=FLAT,width=10,command=loginclick,bd=0).grid(row=6,column=0,columnspan=2,pady=20,ipady=15,sticky='s',padx=20)
    #Button(login_frm,activebackground="#FEEDED",text="Register",bg="#FEEDED",fg="#7B6079",font="Aparajita 24 bold",relief=FLAT,width=10,command=regiswindow,bd=0).grid(row=7,column=0,columnspan=2,pady=20,ipady=15,sticky='n',padx=20)

def loginclick() :
    global user
    user = userentry.get()
    pwd = pwdentry.get()
    
    if user == "" :
        messagebox.showwarning("Cereal", "Please Enter Username")
        userentry.focus_force()
    else :
        sql = "SELECT * FROM Member WHERE username=?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Cereal", "Please enter password")
                pwdentry.focus_force()
            else :
                sql = "SELECT * FROM Member WHERE username=? and password=? "
                cursor.execute(sql, [user, pwd])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Cereal", "Login Successfully")
                    menu_bar()
                else :
                    messagebox.showwarning("Cereal", "Incorrect Password")
                    pwdentry.select_range(0, END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Cereal", "Username not found\n Please register before Login")
            userentry.focus_force()

def menu_bar() :
    global username,menu_frm,home_menu,cal_menu,act_menu,music_menu,timer_menu,profile_menu
    username = userentry.get()
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    menu_frm = Frame(root,bg="#FFD4D4")
    Label(menu_frm,image=menu_bg,bg="#EBECFA").place(x=0,y=0,width=215,height=h)
    
    options = [" Home"," Calendar", " Activity", " Music", " Timer"," Profile"]
    command_list = [home_page,calendar_page,activity_page,music_page,timer_page,profile_page]

    
    home_menu = Button(menu_frm,text=options[0],bg="#FF5454",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[0],activebackground="#FF5454",activeforeground="#FFFFFF", cursor="hand2")
    home_menu.place(x=0,y=138,width=215,height=60)
    cal_menu = Button(menu_frm,text=options[1],bg="#FF5454",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[1],activebackground="#FF5454",activeforeground="#FFFFFF", cursor="hand2")
    cal_menu.place(x=0,y=198,width=215,height=60)
    act_menu = Button(menu_frm,text=options[2],bg="#FF5454",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[2],activebackground="#FF5454",activeforeground="#FFFFFF", cursor="hand2")
    act_menu.place(x=0,y=258,width=215,height=60)
    music_menu = Button(menu_frm,text=options[3],bg="#FF5454",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[3],activebackground="#FF5454",activeforeground="#FFFFFF", cursor="hand2")
    music_menu.place(x=0,y=318,width=215,height=60)
    timer_menu = Button(menu_frm,text=options[4],bg="#FF5454",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[4],activebackground="#FF5454",activeforeground="#FFFFFF", cursor="hand2")
    timer_menu.place(x=0,y=378,width=215,height=60)
    profile_menu = Button(menu_frm,text=options[5],bg="#FF5454",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[5],activebackground="#FF5454",activeforeground="#FFFFFF", cursor="hand2")
    profile_menu.place(x=0,y=438,width=215,height=60)
    Button(menu_frm,text="Logout",bg="#FF5454",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 12",command=logoutClick,activebackground="#FF5454",activeforeground="#FFFFFF", cursor="hand2").place(x=80,y=618)
    menu_frm.place(x=0,y=0,width=215,height=h)
    home_page()

def home_page() :
    global home_frm,username,date,today
    login_frm.destroy()
    home_menu["bg"] = "#FFBABA"
    home_menu["fg"] = "#FF3030"
    home_menu["activebackground"] = "#FFBABA"
    home_menu["activeforeground"] = "#FF3030"
    cal_menu["bg"] = "#FF5454"
    cal_menu["fg"] = "#FFFFFF"
    cal_menu["activebackground"] = "#FF5454"
    cal_menu["activeforeground"] = "#FFFFFF"
    act_menu["bg"] = "#FF5454"
    act_menu["fg"] = "#FFFFFF"
    act_menu["activebackground"] = "#FF5454"
    act_menu["activeforeground"] = "#FFFFFF"
    music_menu["bg"] = "#FF5454"
    music_menu["fg"] = "#FFFFFF"
    music_menu["activebackground"] = "#FF5454"
    music_menu["activeforeground"] = "#FFFFFF"
    timer_menu["bg"] = "#FF5454"
    timer_menu["fg"] = "#FFFFFF"
    timer_menu["activebackground"] = "#FF5454"
    timer_menu["activeforeground"] = "#FFFFFF"
    home_menu["image"] = home_ico
    home_menu["compound"] = LEFT
    cal_menu["image"] = ""
    cal_menu["compound"] = LEFT
    act_menu["image"] = ""
    act_menu["compound"] = LEFT
    music_menu["image"] = ""
    music_menu["compound"] = LEFT
    timer_menu["image"] = ""
    timer_menu["compound"] = LEFT


    home_frm = Frame(root,bg="#FEEDED")
    Label(home_frm,image=home_bg,bg="#EBECFA").place(x=0,y=0,width=985,height=h)

    def time():
        string = strftime('%H:%M:%S %p')
        real_time.config(text = string)
        real_time.after(1000, time)

    real_time = Label(home_frm, font = "BahnschriftLight 18",background = '#FFEDED',foreground = '#7B6079')
    real_time.place(x=740,y=40)
    time()

    get_today = datetime.date.today()
    today = str(get_today)
    date = Label(home_frm,text=today,bg="#FFEDED", fg="#7B6079", font="BahnschriftLight 16")
    date.place(x=760,y=73)
    
    Label(home_frm,text=news[0]['title'],bg="#FFFFFF", fg="#1B1C22", font="Tahoma 12" ,wraplength=460,justify='left').place(x=109,y=228)
    Label(home_frm,text=news[0]['published date'],bg="#FFFFFF", fg="#7B6079", font="BahnschriftLight 8" ).place(x=109,y=275)
    Button(home_frm, text="Read More...",command=lambda:opennews(0), font="Kalinga 10 bold", bg="#FFFFFF", fg="#1B1C22", activebackground="#FFFFFF", activeforeground="#1B1C22", bd=0,relief=FLAT, cursor="hand2").place(x=480,y=288)
    
    Label(home_frm,text=news[1]['title'],bg="#FFFFFF", fg="#1B1C22", font="Tahoma 12" ,wraplength=460,justify='left').place(x=109,y=331)
    Label(home_frm,text=news[1]['published date'],bg="#FFFFFF", fg="#7B6079", font="BahnschriftLight 8" ).place(x=109,y=378)
    Button(home_frm, text="Read More...",command=lambda:opennews(1), font="Kalinga 10 bold", bg="#FFFFFF", fg="#1B1C22", activebackground="#FFFFFF", activeforeground="#1B1C22", bd=0,relief=FLAT, cursor="hand2").place(x=480,y=391)
    
    Label(home_frm,text=news[2]['title'],bg="#FFFFFF", fg="#1B1C22", font="Tahoma 12" ,wraplength=460,justify='left').place(x=109,y=434)
    Label(home_frm,text=news[2]['published date'],bg="#FFFFFF", fg="#7B6079", font="BahnschriftLight 8" ).place(x=109,y=481)
    Button(home_frm, text="Read More...",command=lambda:opennews(2), font="Kalinga 10 bold", bg="#FFFFFF", fg="#1B1C22", activebackground="#FFFFFF", activeforeground="#1B1C22", bd=0,relief=FLAT, cursor="hand2").place(x=480,y=494)

    daily_act()
    home_frm.place(x=215,y=0,width=985,height=h)

def daily_act() :
    global daily_act_frm
    sql = """
            select date,act_name,color from Activity where username=? and date=?
    """
    cursor.execute(sql,[username,today])
    result = cursor.fetchall()

    result_daily = result
    if (len(result)) > 7 :
        result_daily = result[0:7]

    daily_act_frm =Frame(home_frm,bg="#FFFFFF")
    daily_act_frm.place(x=618,y=211,width=262,height=317)
    daily_act_frm.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    daily_act_frm.columnconfigure((0,1),weight=1)
    
    if result_daily != [] :
        for i in range (len(result_daily)) :
            if result_daily[i][2] == "Red" :
                color_act = red_act
            elif result_daily[i][2] == "Pink" :
                color_act = pink_act
            elif result_daily[i][2] == "Green" :
                color_act = green_act
            elif result_daily[i][2] == "Blue" :
                color_act = blue_act
            elif result_daily[i][2] == "Purple" :
                color_act = purple_act
            Label(daily_act_frm,text=result_daily[i][1],bg="#FFFFFF",font="Nunito 12 bold",fg="#1B1C22").grid(row=i+1,column=1,sticky="nw",padx=20)
            Label(daily_act_frm,image=color_act,bg="#FFFFFF",font="Nunito 12 bold",fg="#1B1C22").grid(row=i+1,column=0,sticky="nw",padx=20,pady=6)
    else :
        Label(daily_act_frm,image=freetime,bg="#FFFFFF").place(x=42,y=59,width=177,height=200)

def opennews(n) :
    url = news[n]['url']
    webbrowser.open(url,new=1)


def logoutClick() :
    
    login_page(root)

def calendar_page() :
    global calendar_frm,cal
    home_menu["bg"] = "#FF5454"
    home_menu["fg"] = "#FFFFFF"
    home_menu["activebackground"] = "#FF5454"
    home_menu["activeforeground"] = "#FFFFFF"
    cal_menu["bg"] = "#FFBABA"
    cal_menu["fg"] = "#FF3030"
    cal_menu["activebackground"] = "#FFBABA"
    cal_menu["activeforeground"] = "#FF3030"
    act_menu["bg"] = "#FF5454"
    act_menu["fg"] = "#FFFFFF"
    act_menu["activebackground"] = "#FF5454"
    act_menu["activeforeground"] = "#FFFFFF"
    music_menu["bg"] = "#FF5454"
    music_menu["fg"] = "#FFFFFF"
    music_menu["activebackground"] = "#FF5454"
    music_menu["activeforeground"] = "#FFFFFF"
    timer_menu["bg"] = "#FF5454"
    timer_menu["fg"] = "#FFFFFF"
    timer_menu["activebackground"] = "#FF5454"
    timer_menu["activeforeground"] = "#FFFFFF"
    home_menu["image"] = ""
    home_menu["compound"] = LEFT
    cal_menu["image"] = calendar_ico
    cal_menu["compound"] = LEFT
    act_menu["image"] = ""
    act_menu["compound"] = LEFT
    music_menu["image"] = ""
    music_menu["compound"] = LEFT
    timer_menu["image"] = ""
    timer_menu["compound"] = LEFT

    home_frm.destroy()
    calendar_frm = Frame(root,bg="#FEEDED")
    Label(calendar_frm,image=calendar_bg,bg="#EBECFA").place(x=0,y=0,width=985,height=h)
    cal = Calendar(calendar_frm, font="Arial 12", selectmode='day', locale='en_US',showweeknumbers=False,firstweekday="sunday",background="#FF7171",weekendforeground="#FF7171")
    cal.place(x=155,y=63,width=390,height=287)
    
    Button(calendar_frm,text="",image=add_act_btn,compound=CENTER,bg="#FEEDED",fg="#1B1C22", activebackground="#FEEDED", activeforeground="#1B1C22", bd=0,relief=FLAT,command=add_activity, cursor="hand2").place(x=637,y=275,width=175,height=47)
    Button(calendar_frm,text="",image=del_act_btn,compound=CENTER,bg="#FEEDED",fg="#1B1C22", activebackground="#FEEDED", activeforeground="#1B1C22", bd=0,relief=FLAT,command=del_activity, cursor="hand2").place(x=637,y=330,width=175,height=47)
    
    add_activity()

    calendar_frm.place(x=215,y=0,width=985,height=h)

def add_activity() :
    global act_name_ent,descript_ent,color_ent,date_ent,act_frm
    act_frm = Frame(calendar_frm,bg="#FFFFFF")
    act_frm.place(x=172,y=425,width=645,height=205)
    act_frm.rowconfigure((0,1,2,3,4),weight=1)
    act_frm.columnconfigure((0,1),weight=1)
    Label(act_frm,text="Add Activity",font="Nunito 18 bold",bg="#FFFFFF",fg="#1B1C22",height=1).grid(row=0,column=0,columnspan=2,sticky="nwe",pady=2)
    date = Label(act_frm,text="Date :",font="Nunito 12",bg="#FFFFFF",fg="#1B1C22")
    date.grid(row=1,column=0,sticky="ne",padx=15,pady=5)
    act_name = Label(act_frm,text="Activity Name :",font="Nunito 12",bg="#FFFFFF",fg="#1B1C22")
    act_name.grid(row=2,column=0,sticky="ne",padx=15,pady=5)
    descript = Label(act_frm,text="Description :",font="Nunito 12",bg="#FFFFFF",fg="#1B1C22")
    descript.grid(row=3,column=0,sticky="ne",padx=15,pady=5)
    color = Label(act_frm,text="Color :",font="Nunito 12",bg="#FFFFFF",fg="#1B1C22")
    color.grid(row=4,column=0,sticky="ne",padx=15,pady=5)
    
    date_ent = Entry(act_frm,textvariable=date_ent_spy,font="Nunito 12",relief=FLAT,bd=0)
    date_ent.grid(row=1,column=1,sticky="nw",padx=10,pady=5)
    act_name_ent = Entry(act_frm,textvariable=act_name_ent_spy,font="Nunito 12",relief=FLAT,bd=0,bg="#FFDFDF")
    act_name_ent.grid(row=2,column=1,sticky="nw",padx=10,pady=5)
    descript_ent = Entry(act_frm,textvariable=descript_ent_spy,font="Nunito 12",relief=FLAT,bd=0,bg="#FFDFDF")
    descript_ent.grid(row=3,column=1,sticky="nw",padx=10,pady=5)

    style = ttk.Style()
    style.configure('TCombobox',background= "red")

    color_ent = ttk.Combobox(act_frm,textvariable=color_ent_spy,width=18,font="Arial 12",state="readonly",style="TCombobox")
    color_ent.grid(row=4,column=1,sticky="nw",padx=15,pady=5)
    color_ent["values"] = ["Red","Pink","Green","Blue","Purple"]
    color_ent.set("Blue")
    date_ent_spy.set(cal.selection_get())
    Button(act_frm,image=confirm_btn,command=cf_add_act,bg="#FFFFFF",bd=0,relief=FLAT,activebackground="#FFFFFF", cursor="hand2").place(x=509,y=169,width=133,height=31)
    
def cf_add_act() :
    date = date_ent.get()
    act_name = act_name_ent.get()
    descript = descript_ent.get()
    color = color_ent.get()
    if act_name_ent.get() == "" :
        messagebox.showwarning("Cereal","Please enter your Activity Name.")
    else :
        sql = """
                insert into Activity
                values (?,?,?,?,?)
        """
        cursor.execute(sql, [username,date,act_name,descript,color])
        conn.commit()
        messagebox.showinfo("Cereal","Add Activity successfully.")
    act_name_ent.delete(0,END)
    descript_ent.delete(0,END)
    color_ent.set("Blue")
    act_name_ent.focus_force()

def del_activity() :
    global del_frm,del_date,del_date_ent,del_name,del_name_combo
    
    del_frm = Frame(calendar_frm,bg="#FFFFFF")
    del_frm.place(x=172,y=425,width=645,height=205)
    del_frm.rowconfigure((0,1,2,3,4),weight=1)
    del_frm.columnconfigure((0,1),weight=1)

    Label(del_frm,text="Delete Activity",font="Nunito 18 bold",bg="#FFFFFF",fg="#1B1C22",height=2).grid(row=0,column=0,columnspan=2,sticky="nwe",pady=2)
    del_date = Label(del_frm,text="Date :",font="Nunito 12",bg="#FFFFFF",fg="#1B1C22")
    del_date.grid(row=1,column=0,sticky="ne",padx=15,pady=5)
    del_date_ent = Entry(del_frm,textvariable=del_date_ent_spy,font="Nunito 12",relief=FLAT,bd=0)
    del_date_ent.grid(row=1,column=1,sticky="nw",padx=10,pady=5)
    del_date_ent_spy.set(cal.selection_get())

    del_name = Label(del_frm,text="Activity Name :",font="Nunito 12",bg="#FFFFFF",fg="#1B1C22")
    del_name.grid(row=2,column=0,sticky="ne",padx=15,pady=5)
    style = ttk.Style()
    style.configure('TCombobox',background= "red")
    del_name_combo = ttk.Combobox(del_frm,textvariable=del_namecombo_spy,width=18,font="Arial 12",state="readonly",style="TCombobox")
    del_name_combo.grid(row=2,column=1,sticky="nw",padx=10,pady=5)
    sql = """
            select act_name from Activity where username=? and date=?
          """
    cursor.execute(sql,[username,cal.selection_get()])
    result = cursor.fetchall()
    result_lst = []
    for i in range (len(result)) :
        result_lst.append(result[i][0])
    del_name_combo["values"] = result_lst
    del_namecombo_spy.set("Choose Activities")
    Button(del_frm,image=confirm_btn,command=del_confirm,bg="#FFFFFF",bd=0,relief=FLAT,activebackground="#FFFFFF", cursor="hand2").place(x=509,y=169,width=133,height=31)

def del_confirm() :
    if del_name_combo.get() == "Choose Activities" :
        messagebox.showwarning("Cereal","Please choose your activities first.")
    else :
        confirm_box = messagebox.askquestion("Delete activities","Are you sure to delete this activity in this day ?")
        if confirm_box == "yes" :
            sql = ''' delete from Activity where username=? and date=? and act_name=? '''
            cursor.execute(sql,[username,del_date_ent.get(),del_name_combo.get()])
            conn.commit()
            messagebox.showinfo("Cereal","Your Activity has been deleted.")
            del_namecombo_spy.set("Choose Activities")
        else:
            del_namecombo_spy.set("Choose Activities")

def activity_page() :
    global activity_frm
    home_menu["bg"] = "#FF5454"
    home_menu["fg"] = "#FFFFFF"
    home_menu["activebackground"] = "#FF5454"
    home_menu["activeforeground"] = "#FFFFFF"
    cal_menu["bg"] = "#FF5454"
    cal_menu["fg"] = "#FFFFFF"
    cal_menu["activebackground"] = "#FF5454"
    cal_menu["activeforeground"] = "#FFFFFF"
    act_menu["bg"] = "#FFBABA"
    act_menu["fg"] = "#FF3030"
    act_menu["activebackground"] = "#FFBABA"
    act_menu["activeforeground"] = "#FF3030"
    music_menu["bg"] = "#FF5454"
    music_menu["fg"] = "#FFFFFF"
    music_menu["activebackground"] = "#FF5454"
    music_menu["activeforeground"] = "#FFFFFF"
    timer_menu["bg"] = "#FF5454"
    timer_menu["fg"] = "#FFFFFF"
    timer_menu["activebackground"] = "#FF5454"
    timer_menu["activeforeground"] = "#FFFFFF"
    home_menu["image"] = ""
    home_menu["compound"] = LEFT
    cal_menu["image"] = ""
    cal_menu["compound"] = LEFT
    act_menu["image"] = act_ico
    act_menu["compound"] = LEFT
    music_menu["image"] = ""
    music_menu["compound"] = LEFT
    timer_menu["image"] = ""
    timer_menu["compound"] = LEFT

    home_frm.destroy()
    activity_frm = Frame(root,bg="#FEEDED")
    activity_frm.place(x=215,y=0,width=985,height=h)

def music_page() :
    global music_frm
    home_menu["bg"] = "#FF5454"
    home_menu["fg"] = "#FFFFFF"
    home_menu["activebackground"] = "#FF5454"
    home_menu["activeforeground"] = "#FFFFFF"
    cal_menu["bg"] = "#FF5454"
    cal_menu["fg"] = "#FFFFFF"
    cal_menu["activebackground"] = "#FF5454"
    cal_menu["activeforeground"] = "#FFFFFF"
    act_menu["bg"] = "#FF5454"
    act_menu["fg"] = "#FFFFFF"
    act_menu["activebackground"] = "#FF5454"
    act_menu["activeforeground"] = "#FFFFFF"
    music_menu["bg"] = "#FFBABA"
    music_menu["fg"] = "#FF3030"
    music_menu["activebackground"] = "#FFBABA"
    music_menu["activeforeground"] = "#FF3030"
    timer_menu["bg"] = "#FF5454"
    timer_menu["fg"] = "#FFFFFF"
    timer_menu["activebackground"] = "#FF5454"
    timer_menu["activeforeground"] = "#FFFFFF"
    home_menu["image"] = ""
    home_menu["compound"] = LEFT
    cal_menu["image"] = ""
    cal_menu["compound"] = LEFT
    act_menu["image"] = ""
    act_menu["compound"] = LEFT
    music_menu["image"] = music_ico
    music_menu["compound"] = LEFT
    timer_menu["image"] = ""
    timer_menu["compound"] = LEFT

    home_frm.destroy()
    music_frm = Frame(root,bg="#FEEDED")
    music_frm.place(x=215,y=0,width=985,height=h)

def timer_page() :
    home_menu["bg"] = "#FF5454"
    home_menu["fg"] = "#FFFFFF"
    home_menu["activebackground"] = "#FF5454"
    home_menu["activeforeground"] = "#FFFFFF"
    cal_menu["bg"] = "#FF5454"
    cal_menu["fg"] = "#FFFFFF"
    cal_menu["activebackground"] = "#FF5454"
    cal_menu["activeforeground"] = "#FFFFFF"
    act_menu["bg"] = "#FF5454"
    act_menu["fg"] = "#FFFFFF"
    act_menu["activebackground"] = "#FF5454"
    act_menu["activeforeground"] = "#FFFFFF"
    music_menu["bg"] = "#FF5454"
    music_menu["fg"] = "#FFFFFF"
    music_menu["activebackground"] = "#FF5454"
    music_menu["activeforeground"] = "#FFFFFF"
    timer_menu["bg"] = "#FFBABA"
    timer_menu["fg"] = "#FF3030"
    timer_menu["activebackground"] = "#FFBABA"
    timer_menu["activeforeground"] = "#FF3030"
    home_menu["image"] = ""
    home_menu["compound"] = LEFT
    cal_menu["image"] = ""
    cal_menu["compound"] = LEFT
    act_menu["image"] = ""
    act_menu["compound"] = LEFT
    music_menu["image"] = ""
    music_menu["compound"] = LEFT
    timer_menu["image"] = timer_ico
    timer_menu["compound"] = LEFT

    home_frm.destroy()
    timer_frm = Frame(root,bg="#FEEDED")
    timer_frm.place(x=215,y=0,width=985,height=h)

def profile_page() :
    global profile_top
    sql = "select first_name,last_name,regis_date from Member where username=?"
    cursor.execute(sql,[username])
    result = cursor.fetchone()
    profile_top = Toplevel()
    profile_top.grab_set()
    pro_w = 363
    pro_h = 466
    profile_top.title("Cereal Profile")
    pro_x = profile_top.winfo_screenwidth()/2 - pro_w/2
    pro_y = profile_top.winfo_screenheight()/2 - pro_h/2
    #profile_top.geometry("%dx%d+%d+%d"%(pro_w,pro_h,pro_x,pro_y))
    profile_top.geometry("%dx%d"%(pro_w,pro_h))
    profile_top.config(bg='#FFDDDD')
    profile_top.option_add('*font',"Calibri 24 bold")
    profile_top.iconbitmap("img/pro_icon.ico")
    profile_top.resizable(0,0)
    profile_top.rowconfigure((0,1,2,3,4),weight=1)
    profile_top.columnconfigure((0,1),weight=1)

    Label(profile_top,image=profile_bg,bg="#FFFFFF").place(x=0,y=0,width=363,height=466)

    Label(profile_top,text="First name :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=92,y=162)
    Label(profile_top,text=result[0],bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=162)

    Label(profile_top,text="Last name :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=92,y=196)
    Label(profile_top,text=result[1],bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=196)

    Label(profile_top,text="Registration date :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=42,y=230)
    Label(profile_top,text=result[2],bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=230)

    Label(profile_top,text="Username :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=92,y=264)
    Label(profile_top,text=username,bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=264)

    Button(profile_top,activebackground="#FFFFFF",image=chgpwd_btn,bg="#FFFFFF",relief=FLAT,width=10,command=chg_password,bd=0, cursor="hand2").place(x=27,y=391,width=173,height=49)
    Button(profile_top,activebackground="#FFFFFF",image=back_btn,bg="#FFFFFF",relief=FLAT,width=10,command=profile_top.destroy,bd=0, cursor="hand2").place(x=248,y=391,width=86,height=49)
    

    profile_top.mainloop()


def chg_password() :
    global chgpwd_top,chgpwd,cf_chgpwd,curpwd_ent,newpwd_ent
    
    chgpwd_top = Toplevel()
    chgpwd_top.grab_set()
    chgpwd_w = 363
    chgpwd_h = 200
    chgpwd_top.title("Change Password")
    chgpwd_x = chgpwd_top.winfo_screenwidth()/2 - chgpwd_w/2
    chgpwd_y = chgpwd_top.winfo_screenheight()/2 - chgpwd_h/2
    #chgpwd_top.geometry("%dx%d+%d+%d"%(chgpwd_w,chgpwd_h,chgpwd_x,chgpwd_y))
    chgpwd_top.geometry("%dx%d"%(chgpwd_w,chgpwd_h))
    chgpwd_top.config(bg='#FFDDDD')
    chgpwd_top.option_add('*font',"Calibri 24 bold")
    chgpwd_top.iconbitmap("img/pro_icon.ico")
    chgpwd_top.rowconfigure((0,1,2,3),weight=1)
    chgpwd_top.columnconfigure((0,1,2),weight=1)
    chgpwd = StringVar()
    cf_chgpwd = StringVar()

    Label(chgpwd_top,text="Change Account Password",bg="#FFDDDD",font="Calibri 18",fg="#7B6079").grid(row=0,column=0,padx=2,pady=5,columnspan=3,sticky="news")
    
    Label(chgpwd_top,text="Current Password",bg="#FFDDDD",font="Calibri 12",fg="#7B6079").grid(row=1,column=0,padx=2,pady=5,sticky="ne")
    curpwd_ent = Entry(chgpwd_top,textvariable=chgpwd,show="●",font="Arial 12",relief=FLAT,bd=0,width=25)
    curpwd_ent.grid(row=1,column=1,sticky="n",padx=8,pady=7,columnspan=3)

    Label(chgpwd_top,text="New Password",bg="#FFDDDD",font="Calibri 12",fg="#7B6079").grid(row=2,column=0,padx=2,pady=5,sticky="ne")
    newpwd_ent = Entry(chgpwd_top,textvariable=cf_chgpwd,show="●",font="Arial 12",relief=FLAT,bd=0,width=25)
    newpwd_ent.grid(row=2,column=1,sticky="n",padx=8,pady=7,columnspan=3)

    Button(chgpwd_top,image=confirm_btn,bg="#FFDDDD",relief=FLAT,bd=0,command=confirm_chg,activebackground="#FFDDDD", cursor="hand2").grid(row=3,column=0,sticky="news",columnspan=3)

    chgpwd_top.mainloop()


def confirm_chg() :
    sql = """
            select password
            from Member
            where username=?"""
    cursor.execute(sql,[username])
    cur_pwd = cursor.fetchone()
    if curpwd_ent.get() == "" :
        messagebox.showerror("Cereal","Please Enter Current Password",parent=chgpwd_top)
        curpwd_ent.focus_force()
    elif newpwd_ent.get() == "" :
        messagebox.showerror("Cereal","Please Enter New Password",parent=chgpwd_top)
        newpwd_ent.focus_force()
    elif cur_pwd[0] == curpwd_ent.get() :
        sql = """
                update Member
                set password=?
                where username=?"""
        cursor.execute(sql,[newpwd_ent.get(),username])
        conn.commit()
        messagebox.showinfo("Cereal","Change Password Successfully",parent=chgpwd_top)
        chgpwd_top.destroy()
    else :
        messagebox.showerror("Cereal","Password Incorrect!",parent=chgpwd_top)
        curpwd_ent.focus_force()
        curpwd_ent.select_range(0,END)

def regiswindow() :
    global regis_frm,userentry,pwdentry,photo_frm,regis_first_ent,regis_last_ent,regis_username_ent,regis_pwd_ent,regis_cfpwd_ent

    #login_frm.destroy()

    # regis in zone
    regis_frm = Frame(root,bg="#FFDDDD")
    regis_frm.rowconfigure((1,2,3,4,5,6,7,8,9,10,11),weight=1)
    regis_frm.rowconfigure((0,12),weight=2)
    regis_frm.columnconfigure((0,1),weight=1)
    regis_frm.place(x=720,y=0,width=480,height=700)

    Label(regis_frm,image=regis_bg,bg="#FEEDED").place(x=0,y=0,width=480,height=700)

    #Label(regis_frm,text="Register for Cereal",bg="#FFDDDD",fg="#7B6079",width=25).grid(row=1,column=0,columnspan=2,sticky="news",pady=20)

    Label(regis_frm,text="First name *",bg="#FF9494",fg="#EEEDED",font="Calibri 13").place(x=20,y=340)
    regis_first_ent = Entry(regis_frm,textvariable=regis_first,width=12,font="Arial 12",relief=FLAT,bd=1)
    regis_first_ent.place(x=23,y=365,width=186,height=28)

    Label(regis_frm,text="Last name *",bg="#FF9494",fg="#EEEDED",font="Calibri 13").place(x=268,y=340)
    regis_last_ent = Entry(regis_frm,textvariable=regis_last,width=12,font="Arial 12",relief=FLAT,bd=1)
    regis_last_ent.place(x=271,y=365,width=186,height=28)

    Label(regis_frm,text="Username *",bg="#FF9494",fg="#EEEDED",font="Calibri 13").place(x=20,y=412)
    regis_username_ent = Entry(regis_frm,textvariable=regis_username,width=25,font="Arial 12",relief=FLAT,bd=1)
    regis_username_ent.place(x=23,y=436,width=434,height=28)

    Label(regis_frm,text="Password *",bg="#FF9494",fg="#EEEDED",font="Calibri 13").place(x=20,y=478)
    regis_pwd_ent = Entry(regis_frm,textvariable=regis_pwd,width=25,show="●",font="Arial 12",relief=FLAT,bd=1)
    regis_pwd_ent.place(x=23,y=502,width=186,height=28)

    Label(regis_frm,text="Confirm Password *",bg="#FF9494",fg="#EEEDED",font="Calibri 13").place(x=268,y=478)
    regis_cfpwd_ent = Entry(regis_frm,textvariable=regis_cfpwd,width=25,show="●",font="Arial 12",relief=FLAT,bd=1)
    regis_cfpwd_ent.place(x=271,y=502,width=186,height=28)

    Button(regis_frm,activebackground="#FF9494",image=regis_btn1,bg="#FF9494",relief=FLAT,width=10,command=registration,bd=0, cursor="hand2").place(x=116,y=569,width=255,height=60)
    Button(regis_frm,activebackground="#FF9494",image=login_btn1,bg="#FF9494",relief=FLAT,width=10,command=exitRegis,bd=0, cursor="hand2").place(x=169,y=639,width=148,height=35)

def registration() :
    first = regis_first_ent.get().capitalize()
    last = regis_last_ent.get().capitalize()
    username = regis_username_ent.get()
    password = regis_pwd_ent.get()
    cfpassword = regis_cfpwd_ent.get()
# if all of register is blank
    if first == "":
        messagebox.showwarning("Cereal","Please enter your First name.")
        regis_first_ent.focus_force()
    elif last == "":
        messagebox.showwarning("Cereal","Please enter your Last name.")
        regis_last_ent.focus_force()
    elif username == "":
        messagebox.showwarning("Cereal","Please enter your Username.")
        regis_username_ent.focus_force()
    elif password == "":
        messagebox.showwarning("Cereal","Please enter your Password.")
        regis_pwd_ent.focus_force()
    elif cfpassword == "":
        messagebox.showwarning("Cereal","Please enter your Confirm Password.")
        regis_pwd_ent.focus_force()
    elif password != cfpassword :
        messagebox.showwarning("Cereal","This password dosn't match.")
        regis_cfpwd_ent.focus_force()
    else : 
        get_today = datetime.date.today()
        sql = "SELECT username FROM Member WHERE username=?"
        cursor.execute(sql,[username])
        result = cursor.fetchone()
        if result == None :
            sql = """
                    insert into Member
                    values (?,?,?,?,?)
            """
            cursor.execute(sql,[username,cfpassword,first,last,get_today])
            conn.commit()
            messagebox.showinfo("Cereal","Register successfully")
            regis_first_ent.delete(0,END)
            regis_last_ent.delete(0,END)
            regis_username_ent.delete(0,END)
            regis_pwd_ent.delete(0,END)
            regis_cfpwd_ent.delete(0,END)
            login_page(root)
        else :
            messagebox.showwarning("Cereal","This Email was already exist")
            regis_username_ent.focus_force()
            regis_username_ent.select_range(0,END)

def exitRegis() :
    regis_frm.destroy()
    

createconnection()

google_news = GNews()
google_news = GNews(language='th', country='thai', period='1d', max_results=10, exclude_websites=['google.com', 'bbc.com/thai'])
news = google_news.get_news('covid')

start_root = splash_screen()
start_root.mainloop()