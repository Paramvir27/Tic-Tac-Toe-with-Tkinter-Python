from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import Menu


window=Tk()
window.geometry('590x600')
window.resizable(0,0)
window.configure(background='grey')
a="X"

def empty():
       btn1['text']=""
       btn2['text']=""
       btn3['text']=""
       btn4['text']=""
       btn5['text']=""
       btn6['text']=""
       btn7['text']=""
       btn8['text']=""
       btn9['text']=""

       btn1['bg']="black"
       btn2['bg']="black"
       btn3['bg']="black"
       btn4['bg']="black"
       btn5['bg']="black"
       btn6['bg']="black"
       btn7['bg']="black"
       btn8['bg']="black"
       btn9['bg']="black"

       btn1['fg']="lime"
       btn2['fg']="lime"
       btn3['fg']="lime"
       btn4['fg']="lime"
       btn5['fg']="lime"
       btn6['fg']="lime"
       btn7['fg']="lime"
       btn8['fg']="lime"
       btn9['fg']="lime"

def check():
       c1=btn1['text']
       c2=btn2['text']
       c3=btn3['text']
       c4=btn4['text']
       c5=btn5['text']
       c6=btn6['text']
       c7=btn7['text']
       c8=btn8['text']
       c9=btn9['text']

       #HORIZONTAL CONDITIONS
       
       #Condition 1
       if((c1=="X")and(c2=="X")and(c3=="X")):
              btn1['bg']="lime"
              btn1['fg']="black"
              btn2['bg']="lime"
              btn2['fg']="black"
              btn3['bg']="lime"
              btn3['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
              
       if((c1=="O")and(c2=="O")and(c3=="O")):
              btn1['bg']="lime"
              btn1['fg']="black"
              btn2['bg']="lime"
              btn2['fg']="black"
              btn3['bg']="lime"
              btn3['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()

       #Condition 2
       if((c4=="X")and(c5=="X")and(c6=="X")):
              btn4['bg']="lime"
              btn4['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn6['bg']="lime"
              btn6['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
       if((c4=="O")and(c5=="O")and(c6=="O")):
              btn4['bg']="lime"
              btn4['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn6['bg']="lime"
              btn6['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()

       #Condition 3
       if((c7=="X")and(c8=="X")and(c9=="X")):
              btn7['bg']="lime"
              btn7['fg']="black"
              btn8['bg']="lime"
              btn8['fg']="black"
              btn9['bg']="lime"
              btn9['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
       if((c7=="O")and(c8=="O")and(c9=="O")):
              btn7['bg']="lime"
              btn7['fg']="black"
              btn8['bg']="lime"
              btn8['fg']="black"
              btn9['bg']="lime"
              btn9['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()


       #VERTICAL CONDITIONS
       
       #Condition 1
       if((c1=="X")and(c4=="X")and(c7=="X")):
              btn1['bg']="lime"
              btn1['fg']="black"
              btn4['bg']="lime"
              btn4['fg']="black"
              btn7['bg']="lime"
              btn7['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
       if((c1=="O")and(c4=="O")and(c7=="O")):
              btn1['bg']="lime"
              btn1['fg']="black"
              btn4['bg']="lime"
              btn4['fg']="black"
              btn7['bg']="lime"
              btn7['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()

       #Condition 2
       if((c2=="X")and(c5=="X")and(c8=="X")):
              btn2['bg']="lime"
              btn2['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn8['bg']="lime"
              btn8['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
       if((c2=="O")and(c5=="O")and(c8=="O")):
              btn2['bg']="lime"
              btn2['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn8['bg']="lime"
              btn8['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()

       #Condition 3
              
       if((c3=="X")and(c6=="X")and(c9=="X")):
              btn3['bg']="lime"
              btn3['fg']="black"
              btn6['bg']="lime"
              btn6['fg']="black"
              btn9['bg']="lime"
              btn9['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
       if((c3=="O")and(c6=="O")and(c9=="O")):
              btn3['bg']="lime"
              btn3['fg']="black"
              btn6['bg']="lime"
              btn6['fg']="black"
              btn9['bg']="lime"
              btn9['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()

       #INCLINE CONDITIONS
              
       #Condition 1
       if((c1=="X")and(c5=="X")and(c9=="X")):
              btn1['bg']="lime"
              btn1['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn9['bg']="lime"
              btn9['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
       if((c1=="O")and(c5=="O")and(c9=="O")):
              btn1['bg']="lime"
              btn1['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn9['bg']="lime"
              btn9['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()

       #Condition 2
       if((c3=="X")and(c5=="X")and(c7=="X")):
              btn3['bg']="lime"
              btn3['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn7['bg']="lime"
              btn7['fg']="black"
              messagebox.showinfo("WON"," X Player WON ")
              empty()
       if((c3=="O")and(c5=="O")and(c7=="O")):
              btn3['bg']="lime"
              btn3['fg']="black"
              btn5['bg']="lime"
              btn5['fg']="black"
              btn7['bg']="lime"
              btn7['fg']="black"
              messagebox.showinfo("WON"," O Player WON ")
              empty()
              
       #FULLY FILLED CONDTITION
       if((not(c1==""))and(not(c2==""))and(not(c3==""))and(not(c4==""))
       and(not(c5==""))and(not(c6==""))and(not(c7==""))and(not(c8==""))
       and(not(c9==""))):
              a=messagebox.askyesno("Play Again","Do you want to Play Again ? ")
              if(a==True):
                     empty()
              else:
                     window.destroy()
                                                            


def exe():

       global a
       b=btn1['text']
       if(b==""):
              if(a=="X"):
                     btn1['text']=a
                     a="O"
              else:
                     btn1['text']=a
                     a="X"
       check()
       

def exe2():
       b=btn2['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn2['text']=a
                     a="O"
              else:
                     btn2['text']=a
                     a="X"
       check()

       

def exe3():
       b=btn3['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn3['text']=a
                     a="O"
              else:
                     btn3['text']=a
                     a="X"
       check()
              


def exe4():
       b=btn4['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn4['text']=a
                     a="O"
              else:
                     btn4['text']=a
                     a="X"
       check()


def exe5():
       b=btn5['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn5['text']=a
                     a="O"
              else:
                     btn5['text']=a
                     a="X"
       check()



def exe6():
       b=btn6['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn6['text']=a
                     a="O"
              else:
                     btn6['text']=a
                     a="X"
       check()


def exe7():
       b=btn7['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn7['text']=a
                     a="O"
              else:
                     btn7['text']=a
                     a="X"
       check()


def exe8():
       b=btn8['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn8['text']=a
                     a="O"
              else:
                     btn8['text']=a
                     a="X"
       check()



def exe9():
       b=btn9['text']
       if(b==""):
              global a
              if(a=="X"):
                     btn9['text']=a
                     a="O"
              else:
                     btn9['text']=a
                     a="X"
       check()

btn1=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe, bg="black", fg="lime")
btn1.place(x=30, y=20)

btn2=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe2, bg="black", fg="lime")
btn2.place(x=210, y=20)

btn3=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe3, bg="black", fg="lime")
btn3.place(x=390, y=20)

btn4=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe4, bg="black", fg="lime")
btn4.place(x=30, y=210)

btn5=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe5, bg="black", fg="lime")
btn5.place(x=210, y=210)

btn6=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe6, bg="black", fg="lime")
btn6.place(x=390, y=210)

btn7=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe7, bg="black", fg="lime")
btn7.place(x=30, y=400)

btn8=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe8, bg="black", fg="lime")
btn8.place(x=210, y=400)

btn9=Button(window, width=8, font=(("arial Bold"),25), text="", height=4,
            command=exe9, bg="black", fg="lime")
btn9.place(x=390, y=400)



