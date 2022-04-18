from tkinter import *
from tkinter import ttk,messagebox,PhotoImage
from tkinter.ttk import Progressbar
from textwrap import fill
from itertools import cycle
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk, Image
from gnews import GNews
import sqlite3,datetime,webbrowser,pygame
from time import strftime

def splash_screen() :
    # splash screen
    global bg_splash,progress,ttk_style,start_root,splash_root
    splash_root = Tk()

    w_splash = 427
    h_splash = 250
    screen_width = splash_root.winfo_screenwidth()/2 - w_splash/2
    screen_height = splash_root.winfo_screenheight()/2 - h_splash/2
    
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
    # mainwindow
    global root,userinfo,pwdinfo,regis_first,regis_last,regis_username,regis_pwd,regis_cfpwd,w,h,cereal_login,login_bg,regis_btn1,login_btn1,regis_bg
    global add_act_btn,del_act_btn,date_ent_spy,act_name_ent_spy,descript_ent_spy,color_ent_spy,menu_bg,home_bg,login_btn,regis_btn
    global profile_bg,chgpwd_btn,back_btn,confirm_btn,chgpwd_bg,confirm_chgpwd,music_bg,second_act_bg
    global red_act,pink_act,green_act,blue_act,purple_act,calendar_bg,freetime,act_bg,dis_pre_page_btn,dis_next_page_btn
    global home_ico,calendar_ico,act_ico,music_ico,timer_ico,del_namecombo_spy,del_date_ent_spy,next_page_btn,pre_page_btn
    global play_song_btn,volumn_down_btn,volumn_up_btn,pause_btn,song_spy,lofi_1,lofi_2,guitar_1,guitar_2,chill_1,kpop_1
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
    root.iconbitmap("img/light_theme/element/icon.ico")
    home_ico = PhotoImage(file="img/light_theme/element/home_ico.png")
    calendar_ico = PhotoImage(file="img/light_theme/element/calendar_ico.png")
    act_ico = PhotoImage(file="img/light_theme/element/act_ico.png")
    music_ico = PhotoImage(file="img/light_theme/element/music_ico.png")
    timer_ico = PhotoImage(file="img/light_theme/element/timer_ico.png")
    
    # LIGHT THEME
    menu_bg = PhotoImage(file="img/light_theme/bg/menu_bg.png")
    home_bg = PhotoImage(file="img/light_theme/bg/home_bg.png")
    login_bg = PhotoImage(file="img/light_theme/bg/login_bg.png")
    regis_bg = PhotoImage(file="img/light_theme/bg/regis_bg.png")
    profile_bg = PhotoImage(file="img/light_theme/bg/profile_bg.png")
    calendar_bg = PhotoImage(file="img/light_theme/bg/calendar_bg.png")
    chgpwd_bg = PhotoImage(file="img/light_theme/bg/chgpwd_bg.png")
    act_bg = PhotoImage(file="img/light_theme/bg/act_bg.png")
    music_bg = PhotoImage(file="img/light_theme/bg/music_bg.png")
    second_act_bg = PhotoImage(file="img/light_theme/bg/second_act_bg.png")

    cereal_login = PhotoImage(file="img/light_theme/element/cereal_login.png")
    add_act_btn = PhotoImage(file="img/light_theme/element/add_act_btn.png")
    del_act_btn = PhotoImage(file="img/light_theme/element/del_act_btn.png")
    login_btn = PhotoImage(file="img/light_theme/element/login_btn.png")
    regis_btn = PhotoImage(file="img/light_theme/element/regis_btn.png")
    regis_btn1 = PhotoImage(file="img/light_theme/element/regis_btn1.png")
    login_btn1 = PhotoImage(file="img/light_theme/element/login_btn1.png")
    chgpwd_btn = PhotoImage(file="img/light_theme/element/chgpwd_btn.png")
    back_btn = PhotoImage(file="img/light_theme/element/back_btn.png")
    confirm_btn = PhotoImage(file="img/light_theme/element/confirm_btn.png")
    lofi_1 = PhotoImage(file="img/light_theme/element/lofi_1.png")
    lofi_2 = PhotoImage(file="img/light_theme/element/lofi_2.png")
    guitar_1 = PhotoImage(file="img/light_theme/element/guitar_1.png")
    guitar_2 = PhotoImage(file="img/light_theme/element/guitar_2.png")
    chill_1 = PhotoImage(file="img/light_theme/element/chill_1.png")
    kpop_1 = PhotoImage(file="img/light_theme/element/kpop_1.png")
    pre_page_btn = PhotoImage(file="img/light_theme/element/pre_page_btn.png")
    next_page_btn = PhotoImage(file="img/light_theme/element/next_page_btn.png")
    dis_pre_page_btn = PhotoImage(file="img/light_theme/element/dis_pre_page_btn.png")
    dis_next_page_btn = PhotoImage(file="img/light_theme/element/dis_next_page_btn.png")
    confirm_chgpwd = PhotoImage(file="img/light_theme/element/confirm_chgpwd.png")
    play_song_btn = PhotoImage(file="img/light_theme/element/play_song.png")
    volumn_down_btn = PhotoImage(file="img/light_theme/element/volumn_down.png")
    volumn_up_btn = PhotoImage(file="img/light_theme/element/volumn_up.png")
    pause_btn = PhotoImage(file="img/light_theme/element/pause_song.png")

    red_act = PhotoImage(file="img/light_theme/element/red_act.png")
    pink_act = PhotoImage(file="img/light_theme/element/pink_act.png")
    green_act = PhotoImage(file="img/light_theme/element/green_act.png")
    blue_act = PhotoImage(file="img/light_theme/element/blue_act.png")
    purple_act = PhotoImage(file="img/light_theme/element/purple_act.png")
    freetime = PhotoImage(file="img/light_theme/element/freetime.png")

    # DARK THEME
    global menu_bg_dark,home_bg_dark,login_bg_dark,regis_bg_dark,profile_bg_dark,calendar_bg_dark,chgpwd_bg_dark,act_bg_dark,music_bg_dark,second_act_bg_dark
    global home_ico_dark,calendar_ico_dark,act_ico_dark,music_ico_dark,timer_ico_darka
    home_ico_dark = PhotoImage(file="img/dark_theme/element/home_ico.png")
    calendar_ico_dark = PhotoImage(file="img/dark_theme/element/calendar_ico.png")
    act_ico_dark = PhotoImage(file="img/dark_theme/element/act_ico.png")
    music_ico_dark = PhotoImage(file="img/dark_theme/element/music_ico.png")
    timer_ico_dark = PhotoImage(file="img/dark_theme/element/timer_ico.png")

    menu_bg_dark = PhotoImage(file="img/dark_theme/bg/menu_bg.png")
    home_bg_dark = PhotoImage(file="img/dark_theme/bg/home_bg.png")
    login_bg_dark = PhotoImage(file="img/dark_theme/bg/login_bg.png")
    regis_bg_dark = PhotoImage(file="img/dark_theme/bg/regis_bg.png")
    profile_bg_dark = PhotoImage(file="img/dark_theme/bg/profile_bg.png")
    calendar_bg_dark = PhotoImage(file="img/dark_theme/bg/calendar_bg.png")
    chgpwd_bg_dark = PhotoImage(file="img/dark_theme/bg/chgpwd_bg.png")
    act_bg_dark = PhotoImage(file="img/dark_theme/bg/act_bg.png")
    music_bg_dark = PhotoImage(file="img/dark_theme/bg/music_bg.png")
    second_act_bg_dark = PhotoImage(file="img/dark_theme/bg/second_act_bg.png")

    global cereal_login_dark,add_act_btn_dark,del_act_btn_dark,login_btn_dark,regis_btn_dark,regis_btn1_dark,login_btn1_dark,chgpwd_btn_dark,back_btn_dark,confirm_btn_dark
    global lofi_1_dark, lofi_2_dark, guitar_1_dark, guitar_2_dark, chill_1_dark, kpop_1_dark, pre_page_btn_dark, next_page_btn_dark, dis_pre_page_btn_dark, dis_next_page_btn_dark
    global confirm_chgpwd_dark,play_song_btn_dark,volumn_down_btn_dark,volumn_up_btn_dark,pause_btn_dark,freetime_dark
    cereal_login_dark = PhotoImage(file="img/dark_theme/element/cereal_login.png")
    add_act_btn_dark = PhotoImage(file="img/dark_theme/element/add_act_btn.png")
    del_act_btn_dark = PhotoImage(file="img/dark_theme/element/del_act_btn.png")
    login_btn_dark = PhotoImage(file="img/dark_theme/element/login_btn.png")
    regis_btn_dark = PhotoImage(file="img/dark_theme/element/regis_btn.png")
    regis_btn1_dark = PhotoImage(file="img/dark_theme/element/regis_btn1.png")
    login_btn1_dark = PhotoImage(file="img/dark_theme/element/login_btn1.png")
    chgpwd_btn_dark = PhotoImage(file="img/dark_theme/element/chgpwd_btn.png")
    back_btn_dark = PhotoImage(file="img/dark_theme/element/back_btn.png")
    confirm_btn_dark = PhotoImage(file="img/dark_theme/element/confirm_btn.png")
    lofi_1_dark = PhotoImage(file="img/dark_theme/element/lofi_1.png")
    lofi_2_dark = PhotoImage(file="img/dark_theme/element/lofi_2.png")
    guitar_1_dark = PhotoImage(file="img/dark_theme/element/guitar_1.png")
    guitar_2_dark = PhotoImage(file="img/dark_theme/element/guitar_2.png")
    chill_1_dark = PhotoImage(file="img/dark_theme/element/chill_1.png")
    kpop_1_dark = PhotoImage(file="img/dark_theme/element/kpop_1.png")
    pre_page_btn_dark = PhotoImage(file="img/dark_theme/element/pre_page_btn.png")
    next_page_btn_dark = PhotoImage(file="img/dark_theme/element/next_page_btn.png")
    dis_pre_page_btn_dark = PhotoImage(file="img/dark_theme/element/dis_pre_page_btn.png")
    dis_next_page_btn_dark = PhotoImage(file="img/dark_theme/element/dis_next_page_btn.png")
    confirm_chgpwd_dark = PhotoImage(file="img/dark_theme/element/confirm_chgpwd.png")
    play_song_btn_dark = PhotoImage(file="img/dark_theme/element/play_song.png")
    volumn_down_btn_dark = PhotoImage(file="img/dark_theme/element/volumn_down.png")
    volumn_up_btn_dark = PhotoImage(file="img/dark_theme/element/volumn_up.png")
    pause_btn_dark = PhotoImage(file="img/dark_theme/element/pause_song.png")

    freetime_dark = PhotoImage(file="img/dark_theme/element/freetime.png")

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
    song_spy = StringVar()
    
    login_page(root)
    #root.mainloop()

# slide show
images = ["img/light_theme/news/news1.png","img/light_theme/news/news2.png","img/light_theme/news/news3.png"]
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)

def slideShow() :
    img = next(photos)
    photo_frm.config(image=img)
    root.after(5500, slideShow)


def login_page(root) :
    global login_frm,userentry,pwdentry,photo_frm,bg_login,login_logo,username_label,password_label,btn_login,btn_regis
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

    bg_login = Label(login_frm,image=login_bg,bg="#FEEDED")
    bg_login.place(x=0,y=0,width=480,height=700)

    login_logo = Label(login_frm,image=cereal_login,bg="#FEEDED")
    login_logo.place(x=69,y=73,width=358,height=50)

    username_label = Label(login_frm,text="Username",bg="#FEEDED",fg="#8F8B8F",font="Calibri 16")
    username_label.place(x=92,y=213)
    userentry = Entry(login_frm,textvariable=userinfo,font="Arial 12",relief=FLAT,bd=0)
    userentry.place(x=94,y=247,width=304,height=28)
    userentry.focus_force()

    password_label = Label(login_frm,text="Password",bg="#FEEDED",fg="#8F8B8F",font="Calibri 16")
    password_label.place(x=92,y=305)
    pwdentry = Entry(login_frm,textvariable=pwdinfo,show="●",font="Arial 12",relief=FLAT,bd=0)
    pwdentry.place(x=94,y=339,width=304,height=28)

    btn_login = Button(login_frm,activebackground="#FEEDED",image=login_btn,bg="#FEEDED",relief=FLAT,width=10,command=loginclick,bd=0, cursor="hand2")
    btn_login.place(x=116,y=485,width=255,height=60)
    btn_regis = Button(login_frm,activebackground="#FEEDED",image=regis_btn,bg="#FEEDED",relief=FLAT,width=10,command=regiswindow,bd=0, cursor="hand2")
    btn_regis.place(x=160,y=568,width=168,height=39)


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
    Label(menu_frm,image=menu_bg_dark,bg="#161E58").place(x=0,y=0,width=215,height=h)
    
    options = [" Home"," Calendar", " Activity", " Music", " Timer"," Profile"]
    command_list = [home_page,calendar_page,activity_page,music_page,timer_page,profile_page]

    
    home_menu = Button(menu_frm,text=options[0],bg="#161E58",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[0],activebackground="#575F96",activeforeground="#FFFFFF", cursor="hand2")
    home_menu.place(x=0,y=138,width=215,height=60)
    cal_menu = Button(menu_frm,text=options[1],bg="#161E58",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[1],activebackground="#575F96",activeforeground="#FFFFFF", cursor="hand2")
    cal_menu.place(x=0,y=198,width=215,height=60)
    act_menu = Button(menu_frm,text=options[2],bg="#161E58",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[2],activebackground="#575F96",activeforeground="#FFFFFF", cursor="hand2")
    act_menu.place(x=0,y=258,width=215,height=60)
    music_menu = Button(menu_frm,text=options[3],bg="#161E58",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[3],activebackground="#575F96",activeforeground="#FFFFFF", cursor="hand2")
    music_menu.place(x=0,y=318,width=215,height=60)
    timer_menu = Button(menu_frm,text=options[4],bg="#161E58",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[4],activebackground="#575F96",activeforeground="#FFFFFF", cursor="hand2")
    timer_menu.place(x=0,y=378,width=215,height=60)
    profile_menu = Button(menu_frm,text=options[5],bg="#161E58",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 15 bold",command=command_list[5],activebackground="#575F96",activeforeground="#FFFFFF", cursor="hand2")
    profile_menu.place(x=0,y=438,width=215,height=60)
    Button(menu_frm,text="Logout",bg="#161E58",fg="#FFFFFF",relief=FLAT,bd=0,font="Nunito 12",command=logoutClick,activebackground="#161E58",activeforeground="#FFFFFF", cursor="hand2").place(x=80,y=618)
    menu_frm.place(x=0,y=0,width=215,height=h)
    home_page()

def home_page() :
    global home_frm,username,date,today
    login_frm.destroy()
    home_menu["bg"] = "#575F96"
    home_menu["fg"] = "#FFFFFF"
    home_menu["activebackground"] = "#575F96"
    home_menu["activeforeground"] = "#FFFFFF"
    cal_menu["bg"] = "#161E58"
    cal_menu["fg"] = "#FFFFFF"
    cal_menu["activebackground"] = "#161E58"
    cal_menu["activeforeground"] = "#FFFFFF"
    act_menu["bg"] = "#161E58"
    act_menu["fg"] = "#FFFFFF"
    act_menu["activebackground"] = "#161E58"
    act_menu["activeforeground"] = "#FFFFFF"
    music_menu["bg"] = "#161E58"
    music_menu["fg"] = "#FFFFFF"
    music_menu["activebackground"] = "#161E58"
    music_menu["activeforeground"] = "#FFFFFF"
    timer_menu["bg"] = "#161E58"
    timer_menu["fg"] = "#FFFFFF"
    timer_menu["activebackground"] = "#161E58"
    timer_menu["activeforeground"] = "#FFFFFF"
    home_menu["image"] = home_ico_dark
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
    Label(home_frm,image=home_bg_dark,bg="#EBECFA").place(x=0,y=0,width=985,height=h)
    # real time clock
    def time():
        string = strftime('%H:%M:%S %p')
        real_time.config(text = string)
        real_time.after(1000, time)

    real_time = Label(home_frm, font = "BahnschriftLight 18",background = '#0A1471',foreground = '#7B6079')
    real_time.place(x=740,y=40)
    time()
    #date
    get_today = datetime.date.today()
    today = str(get_today)
    date = Label(home_frm,text=today,bg="#0A1471", fg="#D8D5D8", font="BahnschriftLight 16")
    date.place(x=760,y=73)
    
    Label(home_frm,text=news[0]['title'],bg="#333333", fg="#FFFFFF", font="Tahoma 12" ,wraplength=460,justify='left').place(x=109,y=228)
    Label(home_frm,text=news[0]['published date'],bg="#333333", fg="#FFFFFF", font="BahnschriftLight 8" ).place(x=109,y=275)
    Button(home_frm, text="Read More...",command=lambda:opennews(0), font="Kalinga 10 bold", bg="#333333", fg="#FFFFFF", activebackground="#333333", activeforeground="#1B1C22", bd=0,relief=FLAT, cursor="hand2").place(x=480,y=288)
    
    Label(home_frm,text=news[1]['title'],bg="#333333", fg="#FFFFFF", font="Tahoma 12" ,wraplength=460,justify='left').place(x=109,y=331)
    Label(home_frm,text=news[1]['published date'],bg="#333333", fg="#FFFFFF", font="BahnschriftLight 8" ).place(x=109,y=378)
    Button(home_frm, text="Read More...",command=lambda:opennews(1), font="Kalinga 10 bold", bg="#333333", fg="#FFFFFF", activebackground="#333333", activeforeground="#1B1C22", bd=0,relief=FLAT, cursor="hand2").place(x=480,y=391)
    
    Label(home_frm,text=news[2]['title'],bg="#333333", fg="#FFFFFF", font="Tahoma 12" ,wraplength=460,justify='left').place(x=109,y=434)
    Label(home_frm,text=news[2]['published date'],bg="#333333", fg="#FFFFFF", font="BahnschriftLight 8" ).place(x=109,y=481)
    Button(home_frm, text="Read More...",command=lambda:opennews(2), font="Kalinga 10 bold", bg="#333333", fg="#FFFFFF", activebackground="#333333", activeforeground="#1B1C22", bd=0,relief=FLAT, cursor="hand2").place(x=480,y=494)

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

    daily_act_frm =Frame(home_frm,bg="#333333")
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
            Label(daily_act_frm,text=result_daily[i][1],bg="#333333",font="Nunito 12 bold",fg="#1B1C22").grid(row=i+1,column=1,sticky="nw",padx=20)
            Label(daily_act_frm,image=color_act,bg="#333333",font="Nunito 12 bold",fg="#1B1C22").grid(row=i+1,column=0,sticky="nw",padx=20,pady=6)
    else :
        Label(daily_act_frm,image=freetime_dark,bg="#333333").place(x=42,y=59,width=177,height=200)

def opennews(n) :
    url = news[n]['url']
    webbrowser.open(url,new=1)


def logoutClick() :
    pygame.mixer.init()
    pygame.mixer.music.stop()
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
    
    date_ent = Entry(act_frm,textvariable=date_ent_spy,font="Nunito 12",relief=FLAT,bd=0,state=DISABLED,disabledbackground="#FFFFFF",disabledforeground="#000000",cursor="arrow")
    date_ent.grid(row=1,column=1,sticky="nw",padx=10,pady=5)
    act_name_ent = Entry(act_frm,textvariable=act_name_ent_spy,font="Nunito 12",relief=FLAT,bd=0,bg="#FFDFDF")
    act_name_ent.grid(row=2,column=1,sticky="nw",padx=10,pady=5)
    descript_ent = Entry(act_frm,textvariable=descript_ent_spy,font="Nunito 12",relief=FLAT,bd=0,bg="#FFDFDF")
    descript_ent.grid(row=3,column=1,sticky="nw",padx=10,pady=5)


    color_ent = ttk.Combobox(act_frm,textvariable=color_ent_spy,width=18,state="readonly")
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
    del_date_ent = Entry(del_frm,textvariable=del_date_ent_spy,font="Nunito 12",relief=FLAT,bd=0,state=DISABLED,disabledbackground="#FFFFFF",disabledforeground="#000000",cursor="arrow")
    del_date_ent.grid(row=1,column=1,sticky="nw",padx=10,pady=5)
    del_date_ent_spy.set(cal.selection_get())

    del_name = Label(del_frm,text="Activity Name :",font="Nunito 12",bg="#FFFFFF",fg="#1B1C22")
    del_name.grid(row=2,column=0,sticky="ne",padx=15,pady=5)
    
    del_name_combo = ttk.Combobox(del_frm,textvariable=del_namecombo_spy,width=18,state="readonly")
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
            sql = """
            select act_name from Activity where username=? and date=?
            """
            cursor.execute(sql,[username,del_date_ent.get()])
            result = cursor.fetchall()
            result_lst = []
            for i in range (len(result)) :
                result_lst.append(result[i][0])
            del_name_combo["values"] = result_lst
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

    activity_frm = Frame(root,bg="#FEEDED")
    activity_frm.place(x=215,y=0,width=985,height=h)

    first_act_page()
    

def first_act_page() :
    first_actpage_frm = Frame(activity_frm,bg="#FEEDED")
    first_actpage_frm.place(x=0,y=0,width=985,height=h)

    Label(first_actpage_frm,image=act_bg,bg="#FFEDED").place(x=0,y=0,width=985,height=700)

    pre_page_act = Button(first_actpage_frm, image=dis_pre_page_btn,bg="#FFBABA",activebackground="#FFBABA",relief=FLAT,bd=0, command=None, cursor="hand2")
    pre_page_act.place(x=384,y=634)

    Label(first_actpage_frm,text="1/2",bg="#FBEBFF",font="Nunito 12",fg="#5C5B5B").place(x=479,y=645)

    next_page_act = Button(first_actpage_frm, image=next_page_btn,bg="#FBEBFF",activebackground="#FBEBFF",relief=FLAT,bd=0, command=second_act_page, cursor="hand2")
    next_page_act.place(x=560,y=634)


def second_act_page() :
    second_actpage_frm = Frame(activity_frm,bg="#FEEDED")
    second_actpage_frm.place(x=0,y=0,width=985,height=h)

    Label(second_actpage_frm,image=second_act_bg,bg="#FFEDED").place(x=0,y=0,width=985,height=700)

    pre_page_act = Button(second_actpage_frm, image=pre_page_btn,bg="#FBEBFF",activebackground="#FBEBFF",relief=FLAT,bd=0, command=first_act_page, cursor="hand2")
    pre_page_act.place(x=384,y=634)

    Label(second_actpage_frm,text="2/2",bg="#FBEBFF",font="Nunito 12",fg="#5C5B5B").place(x=479,y=645)

    next_page_act = Button(second_actpage_frm, image=dis_next_page_btn,bg="#FFBABA",activebackground="#FFBABA",relief=FLAT,bd=0, command=None, cursor="hand2")
    next_page_act.place(x=560,y=634)


song_state = False
def music_page() :
    global music_frm,play_song,song_ent,volumn
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

    music_frm = Frame(root,bg="#FEEDED")
    music_frm.place(x=215,y=0,width=985,height=h)
    pygame.mixer.init()
    volumn = 0.15
    pygame.mixer.music.set_volume(volumn)
    Label(music_frm,image=music_bg,bg="#EBECFA").place(x=0,y=0,width=985,height=h)

    song_ent = Entry(music_frm,textvariable=song_spy,relief=FLAT,bd=0,state=DISABLED,cursor="arrow",justify=CENTER,font="Arial 12",disabledbackground="#FFFFFF",disabledforeground="#000000")
    song_ent.place(x=376,y=529,width=234,height=24)
    play_song = Button(music_frm, image=play_song_btn,bg="#FFFFFF",activebackground="#FFFFFF",relief=FLAT,bd=0, command=play)
    play_song.place(x=470,y=573,width=49,height=49)
    Button(music_frm, image=volumn_down_btn,bg="#FFFFFF",activebackground="#FFFFFF",relief=FLAT,bd=0, command=volumn_down).place(x=350,y=573,width=49,height=49)
    Button(music_frm,image=volumn_up_btn,bg="#FFFFFF",activebackground="#FFFFFF",relief=FLAT,bd=0, command=volumn_up).place(x=590,y=573,width=49,height=49)

    Button(music_frm, image=lofi_1,bg="#FFBABA",activebackground="#FFBABA",relief=FLAT,bd=0, command=lambda:song_spy.set("Lofi Pack 1"),cursor="hand2").place(x=36,y=149,width=240,height=88)
    Button(music_frm,image=lofi_2,bg="#FFBABA",activebackground="#FFBABA",relief=FLAT,bd=0, command=lambda:song_spy.set("Lofi Pack 2"),cursor="hand2").place(x=36,y=243,width=240,height=88)
    Button(music_frm, image=guitar_1,bg="#FFBABA",activebackground="#FFBABA",relief=FLAT,bd=0, command=lambda:song_spy.set("Guitar Pack 1"),cursor="hand2").place(x=374,y=149,width=240,height=88)
    Button(music_frm,image=guitar_2,bg="#FFBABA",activebackground="#FFBABA",relief=FLAT,bd=0, command=lambda:song_spy.set("Guitar Pack 2"),cursor="hand2").place(x=374,y=243,width=240,height=88)
    Button(music_frm, image=chill_1,bg="#FFCFEC",activebackground="#FFCFEC",relief=FLAT,bd=0, command=lambda:song_spy.set("Chill Pack 1"),cursor="hand2").place(x=711,y=149,width=240,height=88)
    Button(music_frm,image=kpop_1,bg="#FFCFEC",activebackground="#FFCFEC",relief=FLAT,bd=0, command=lambda:song_spy.set("K-POP Pack 1"),cursor="hand2").place(x=711,y=243,width=240,height=88)
    if song_state == True :
        play_song["command"] = stop
        play_song["image"] = pause_btn
    elif song_state == False :
        play_song["command"] = play
        play_song["image"] = play_song_btn
def play():
    global song_state
    song_pack = song_ent.get()
    if song_pack == "Lofi Pack 1" :
        pygame.mixer.music.load("song/lofi_pack1.mp3")
        pygame.mixer.music.play(loops=0)
    elif song_pack == "Lofi Pack 2" :
        pygame.mixer.music.load("song/lofi_pack2.mp3")
        pygame.mixer.music.play(loops=0)
    elif song_pack == "Guitar Pack 1" :
        pygame.mixer.music.load("song/guitar_pack1.mp3")
        pygame.mixer.music.play(loops=0)
    elif song_pack == "Guitar Pack 2" :
        pygame.mixer.music.load("song/guitar_pack2.mp3")
        pygame.mixer.music.play(loops=0)
    elif song_pack == "Chill Pack 1" :
        pygame.mixer.music.load("song/chillsong_pack1.mp3")
        pygame.mixer.music.play(loops=0)
    elif song_pack == "K-POP Pack 1" :
        pygame.mixer.music.load("song/kpop_pack1.mp3")
        pygame.mixer.music.play(loops=0)
    else :
        pygame.mixer.music.load("song/lofi_pack1.mp3")
        pygame.mixer.music.play(loops=0)
        song_spy.set("Lofi Pack 1")
    song_state = True
    play_song["command"] = stop
    play_song["image"] = pause_btn
def volumn_down() :
    pygame.mixer.music.set_volume(0.05)
def stop() :
    global song_state
    song_state = False
    pygame.mixer.music.stop()
    play_song["command"] = play
    play_song["image"] = play_song_btn
def volumn_up() :
    pygame.mixer.music.set_volume(0.3)

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
    profile_top.geometry("%dx%d+200+200"%(pro_w,pro_h))
    profile_top.config(bg='#FFDDDD')
    profile_top.option_add('*font',"Calibri 24 bold")
    profile_top.iconbitmap("img/light_theme/element/pro_icon.ico")
    profile_top.resizable(0,0)
    profile_top.rowconfigure((0,1,2,3,4),weight=1)
    profile_top.columnconfigure((0,1),weight=1)

    Label(profile_top,image=profile_bg,bg="#FFFFFF").place(x=0,y=0,width=363,height=466)

    Label(profile_top,text="First name :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=92,y=202)
    Label(profile_top,text=result[0],bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=202)

    Label(profile_top,text="Last name :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=92,y=236)
    Label(profile_top,text=result[1],bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=236)

    Label(profile_top,text="Registration date :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=42,y=270)
    Label(profile_top,text=result[2],bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=270)

    Label(profile_top,text="Username :",bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=92,y=304)
    Label(profile_top,text=username,bg="#FFFFFF",font="Nunito 12 bold",fg="#826B6B").place(x=200,y=304)

    Button(profile_top,activebackground="#FFFFFF",image=chgpwd_btn,bg="#FFFFFF",relief=FLAT,width=10,command=chg_password,bd=0, cursor="hand2").place(x=27,y=391,width=173,height=49)
    Button(profile_top,activebackground="#FFFFFF",image=back_btn,bg="#FFFFFF",relief=FLAT,width=10,command=profile_back,bd=0, cursor="hand2").place(x=248,y=391,width=86,height=49)
    

    profile_top.mainloop()

def profile_back() :
    profile_top.grab_release()
    profile_top.destroy()

def chg_password() :
    global chgpwd_top,chgpwd,cf_chgpwd,curpwd_ent,newpwd_ent
    
    chgpwd_top = Toplevel()
    chgpwd_top.grab_set()
    chgpwd_w = 363
    chgpwd_h = 200
    chgpwd_top.title("Change Password")
    #chgpwd_top.geometry("%dx%d+%d+%d"%(chgpwd_w,chgpwd_h,chgpwd_x,chgpwd_y))
    chgpwd_top.geometry("%dx%d+600+400"%(chgpwd_w,chgpwd_h))
    chgpwd_top.config(bg='#FFEDED')
    chgpwd_top.option_add('*font',"Calibri 24 bold")
    chgpwd_top.iconbitmap("img/light_theme/element/pro_icon.ico")
    chgpwd_top.rowconfigure((0,1,2,3),weight=1)
    chgpwd_top.columnconfigure((0,1,2),weight=1)
    chgpwd = StringVar()
    cf_chgpwd = StringVar()
    Label(chgpwd_top,image=chgpwd_bg,bg="#FFEDED").place(x=0,y=0,width=363,height=200)

    Label(chgpwd_top,text="Change Account Password",bg="#FFEDED",font="Nunito 15 bold",fg="#4D484C").place(x=80,y=14)

    Label(chgpwd_top,text="Current Password",bg="#FFEDED",font="Nunito 12",fg="#5C5B5B").place(x=23,y=58)
    curpwd_ent = Entry(chgpwd_top,textvariable=chgpwd,show="●",font="Arial 12",relief=FLAT,bd=0,bg="#CFC2FF")
    curpwd_ent.place(x=173,y=58,width=168,height=24)

    Label(chgpwd_top,text="New Password",bg="#FFEDED",font="Nunito 12",fg="#5C5B5B").place(x=43,y=100)
    newpwd_ent = Entry(chgpwd_top,textvariable=cf_chgpwd,show="●",font="Arial 12",relief=FLAT,bd=0,bg="#CFC2FF")
    newpwd_ent.grid(row=2,column=1,sticky="n",padx=8,pady=7,columnspan=3)
    newpwd_ent.place(x=173,y=100,width=168,height=24)

    Button(chgpwd_top,image=confirm_chgpwd,bg="#FFEDED",relief=FLAT,bd=0,command=confirm_chg,activebackground="#FFEDED", cursor="hand2").place(x=133,y=156)

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
        chgpwd_top.grab_release()
        profile_top.grab_set()
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

conn.close()