from tkinter import *
from time import sleep

#Secondary Frames
#showwarning
def home():#Home Frame
    global homeframe
    
    homeframe=LabelFrame(tk,height=scrh,width=scrhw,bg='#dec06f')
    homeframe.pack()
    
    
    piclabel2=Label(homeframe,image=icon,bg='#dec06f')
    piclabel2.place(relx=0.5,rely=0.1,anchor=N)
    
    hombut1=Button(homeframe,text="Play",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=Home_to_PlayStarter)
    hombut1.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    hombut2=Button(homeframe,text="Rules",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=Home_to_Rules)
    hombut2.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    
    hombut3=Button(homeframe,text="Quit",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=lambda:tk.destroy())
    hombut3.place(relx=0.5,rely=0.6,anchor=CENTER) 

def rules():#Rule Frame
    global ruleframe
    
    ruleframe=LabelFrame(tk,height=scrh,width=scrhw,bg='#dec06f')
    ruleframe.pack()
    
    rullab1=Label(ruleframe,text="RULES OF THE GAME",bg='#dec06f',width=100,font=("garamond",80,'italic'),fg='#94ffe2')
    rullab1.place(relx=0.5,rely=0.1,anchor=N)
    
    rullab2=Label(ruleframe,text="Play Sudoku is based on the popular number-based logic puzzle in\n\
    which one must fill a 9 X 9 square with the correct digits.In order to \n\
    complete the puzzle,you must fill each cell with a number between 1 and 9, \n\
    inclusive, such that no number is repeated in any row, column or 3x3 box.\n\
    In a solved sudoku, each row, column, and 3x3 box contains all the numbers \n\
    1 through 9.There are Three levels in this game- 1:Easy, 2:Medium, 3:Hard.\n\
    Each puzzle has only one solution.",bg='#dec06f',width=100,font=("Courier",20))
    rullab2.place(relx=0.45,rely=0.4,anchor=CENTER)
    
    rulbut1=Button(ruleframe,text="Back",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=Rule_to_Home)
    rulbut1.place(relx=0.5,rely=0.8,anchor=S)

def PlayStarter():#Play Start Page
    
    def difficultiy(level):
        global lel
        lel=level
    
    global plstarframe
    
    plstarframe=LabelFrame(tk,height=scrh,width=scrhw,bg='#dec06f')
    plstarframe.pack()
    
    plstarlab=Label(plstarframe,text="Choose the Level",bg='#dec06f',width=100,font=("garamond",80,'italic'),fg='#94ffe2')
    plstarlab.place(relx=0.5,rely=0.1,anchor=N)
    
    Level=1
    
    op1=Radiobutton(plstarframe,text="Easy",value=1,variable=Level, bg="#dec06f",width=7,height=1,font=("garamond",20,'italic'),activebackground="#ffc300",command=lambda:difficultiy(1))
    op1.place(relx=0.5,rely=0.3,anchor=N)
    
    op2=Radiobutton(plstarframe,text="Medium",value=2,variable=Level, bg="#dec06f",width=7,height=1,font=("garamond",20,'italic'),activebackground="#ffc300",command=lambda:difficultiy(2))
    op2.place(relx=0.5,rely=0.5,anchor=N)
    
    op3=Radiobutton(plstarframe,text="Hard",value=3,variable= Level, bg="#dec06f",width=7,height=1,font=("garamond",20,'italic'),activebackground="#ffc300",command=lambda:difficultiy(3))
    op3.place(relx=0.5,rely=0.7,anchor=N)
    
    but8=Button(plstarframe,text="Next",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=PlayStarter_to_Play)
    but8.place(relx=0.5,rely=0.9,anchor=S)

def Play():
    import main
    
    def get(Gam):
        x=[[0 for i in range(9)]for j in range(9)]
        for i in range(9):
            for j in range(9):
                x[i][j]=int(Gam[i][j].get())
        return x
    
    def only_numbers(char):
        if char.isdigit():
            return True
        else:
            return False
    
    def cheak(event):
        for i in [A,B,C,D,E,F,G,H,I]:
            for j in i:
                j.delete(1,END)
    
    def placing(List,y,x):#(variables list,Primary y corrdinate,Primary x corrdinat)
        posy=y
        cons=0
        for i in range(3):
           posx=x
           for j in range(3):
               pos=i+j+cons
               List[pos]=Entry(PlayFrame,width=3,font=(15),validate="key", validatecommand=(validation, '%S'))
               List[pos].place(relx=posx,rely=posy,anchor=CENTER)
               List[pos].bind("<Key>",cheak)
               posx+=0.03
           else:
                posy+=0.03
           cons+=2
    
    def Cheaking():
        gvalues=get(EntryBox)
        cond=False
        for i in range(9):
            for j in range(9):
                if gvalues[i][j]!=main.Values[i][j]:
                    EntryBox[i][j].delete(0,END)
                    EntryBox[i][j].insert(0,"*")
                    cond=True
        if cond:
            messagebox.showinfo("Play Sudoko","The Entry boxes with * is wrong Try again")
        else:
            messagebox.showinfo("Play Sudoko","Congradulation !! All is correct! \n Returning to Home Screen Shortly")
            sleep(5)
            PlayFrame.destroy()
            home()
    
    def Quit():
        res=messagebox.askyesno("Play Sudoko","Do you want to quit.Note that progress will mot be saved.")
        if res:
            PlayFrame.destroy()
            home()
    
    """
    #Cheak Variables
    ca1=ca2=ca3=ca4=ca5=ca6=ca7=ca8=ca9=None
    cb1=cb2=cb3=cb4=cb5=cb6=cb7=cb8=cb9=None
    cc1=cc2=cc3=cc4=cc5=cc6=cc7=cc8=cc9=None
    cd1=cd2=cd3=cd4=cd5=cd6=cd7=cd8=cd9=None
    ce1=ce2=ce3=ce4=ce5=ce6=ce7=ce8=ce9=None
    cf1=cf2=cf3=cf4=cf5=cf6=cf7=cf8=cf9=None
    cg1=cg2=cg3=cg4=cg5=cg6=cg7=cg8=cg9=None
    ch1=ch2=ch3=ch4=ch5=ch6=ch7=ch8=ch9=None
    ci1=ci2=ci3=ci4=ci5=ci6=ci7=ci8=ci9=None
    
    cA=[ca1,ca2,ca3,ca4,ca5,ca6,ca7,ca8,ca9]
    cB=[cb1,cb2,cb3,cb4,cb5,cb6,cb7,cb8,cb9]
    cC=[cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9]
    cD=[cd1,cd2,cd3,cd4,cd5,cd6,cd7,cd8,cd9]
    cE=[ce1,ce2,ce3,ce4,ce5,ce6,ce7,ce8,ce9]
    cF=[cf1,cf2,cf3,cf4,cf5,cf6,cf7,cf8,cf9]
    cG=[cg1,cg2,cg3,cg4,cg5,cg6,cg7,cg8,cg9]
    cH=[ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9]
    cI=[ci1,ci2,ci3,ci4,ci5,ci6,ci7,ci8,ci9]
    
    CheakVar=[cA,cB,cC,cD,cE,cF,cG,cH,cI]
    """
    a1=a2=a3=a4=a5=a6=a7=a8=a9=None
    b1=b2=b3=b4=b5=b6=b7=b8=b9=None
    c1=c2=c3=c4=c5=c6=c7=c8=c9=None
    d1=d2=d3=d4=d5=d6=d7=d8=d9=None
    e1=e2=e3=e4=e5=e6=e7=e8=e9=None
    f1=f2=f3=f4=f5=f6=f7=f8=f9=None
    g1=g2=g3=g4=g5=g6=g7=g8=g9=None
    h1=h2=h3=h4=h5=h6=h7=h8=h9=None
    i1=i2=i3=i4=i5=i6=i7=i8=i9=None
    
    # Forming the Nine Blocks
    A=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
    B=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    C=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
    D=[d1,d2,d3,d4,d5,d6,d7,d8,d9]
    E=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
    F=[f1,f2,f3,f4,f5,f6,f7,f8,f9]
    G=[g1,g2,g3,g4,g5,g6,g7,g8,g9]
    H=[h1,h2,h3,h4,h5,h6,h7,h8,h9]
    I=[i1,i2,i3,i4,i5,i6,i7,i8,i9]
    
    EntryBox=[A,B,C,D,E,F,G,H,I]
    
    global PlayFrame
    PlayFrame=LabelFrame(tk,height=scrh,width=scrhw,bg='#dec06f')
    PlayFrame.pack()
    
    validation = tk.register(only_numbers)
    
    PlayLab1=Label(PlayFrame,text='GAME BEGINS!!!!',bg='#dec06f',width=50,font=("garamond",25,'italic'),fg='red')
    PlayLab1.place(relx=0.5,rely=0.1,anchor=N)
    
    #First Row
    placing(A,0.2,0.35)
    placing(B,0.2, 0.45)
    placing(C,0.2, 0.55)
    
    #Second Row
    placing(D,0.3, 0.35)
    placing(E,0.3, 0.45)
    placing(F,0.3, 0.55)
    
    #Third Row
    placing(G,0.4, 0.35)
    placing(H,0.4, 0.45)
    placing(I,0.4, 0.55)
    """
    if lel==1:
        show=10
    elif lel==2:
        show=8
    elif lel==3:
        show=5
    """
    main.mainplay(EntryBox)
    
    Playbut1=Button(PlayFrame,text="Cheak",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=Cheaking)
    Playbut1.place(relx=0.25,rely=0.9,anchor=S)
    Playbut2=Button(PlayFrame,text="Quit",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=Quit)
    Playbut2.place(relx=0.75,rely=0.9,anchor=S)
#Changing Frames

def Star_to_Home():
    starframe.destroy()
    home()

def Home_to_Rules():
    homeframe.destroy()
    rules()

def Rule_to_Home():
     ruleframe.destroy()
     home()

def Home_to_PlayStarter():
    homeframe.destroy()
    PlayStarter()

def PlayStarter_to_Play():
    plstarframe.destroy()
    Play()



#Primary Frames

tk=Tk()

tk.title("Play Sudoku")

scrh=tk.winfo_screenheight()  # Getting screen height
scrhw=tk.winfo_screenwidth() # Getting Screen width

starframe=LabelFrame(tk,height=scrh,width=scrhw,bg='#dec06f')
starframe.pack()

icon=PhotoImage(file="pic.gif")
startIcon=PhotoImage(file="pic1.gif")
startPiclabel=Label(starframe,image=startIcon,bg='#dec06f')
startPiclabel.place(relx=0.5,rely=0.1,anchor=N)

startlabel1=Label(starframe,text='Welcome To',bg='#dec06f',width=100,font=("garamond",80,'italic'),fg='red')
startlabel1.place(relx=0.5,rely=0.6,anchor=CENTER)

startlabel2=Label(starframe,text='PLAY SUDOKO',bg='#dec06f',width=100,font=("rockwell",60,'italic'),fg="red")
startlabel2.place(relx=0.5,rely=0.7,anchor=CENTER)

startbut1=Button(starframe,text="Next",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=Star_to_Home)
startbut1.place(relx=0.25,rely=0.9,anchor=S)

startbut2=Button(starframe,text="Exit",width=10,font=("Courier",25,"bold"),activebackground="#065e47",bg='#94ffe2',command=lambda:tk.destroy())
startbut2.place(relx=0.75,rely=0.9,anchor=S)

tk.mainloop()