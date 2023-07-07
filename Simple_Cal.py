from tkinter import *
from tkinter.messagebox import *
import keyboard

calculation = ""

def press(symbol):
	global calculation
	calculation += str(symbol)
	text_field.delete(1.0,"end")
	text_field.insert(1.0,calculation)
def evaluation():
	global calculation
	try:
		calculation = str(eval(calculation))
		text_field.delete(1.0,"end")
		text_field.insert(1.0,calculation)
	except:
		clear()
		text_field.delete(1.0,"end")
		showerror("ERROR","INVALID INPUT")
def clear():
	global calculation
	calculation = ""
	text_field.delete(1.0,"end")
def sign_change():
    global calculation
    if calculation[0]=='-':
        temp = calculation[1:]
    else:
        temp = '-'+calculation
    calculation = temp
    text_field.delete(1.0,"end")
    text_field.insert(1.0,calculation)
    
def percent():
    global calculation
    calculation = str(eval(calculation+'/100'))
    text_field.delete(1.0,"end")
    text_field.insert(1.0,calculation)
	

root = Tk()
root.geometry("300x310")
root.title("Simple Calculator")
root.iconbitmap("Cal.ico")
text_field = StringVar()
text_field = Text(root,height=2,width=16,font=("Arial",24))
text_field.grid(columnspan=5)

btn_1 = Button(root,text="1",command = lambda: press(1),width=5,font=("Arial",14))
btn_1.grid(row=2,column=1)

btn_2 = Button(root,text="2",command = lambda: press(2),width=5,font=("Arial",14))
btn_2.grid(row=2,column=2)

btn_3 = Button(root,text="3",command = lambda: press(3),width=5,font=("Arial",14))
btn_3.grid(row=2,column=3)

btn_4 = Button(root,text="4",command = lambda: press(4),width=5,font=("Arial",14))
btn_4.grid(row=3,column=1)

btn_5 = Button(root,text="5",command = lambda: press(5),width=5,font=("Arial",14))
btn_5.grid(row=3,column=2)

btn_6 = Button(root,text="6",command = lambda: press(6),width=5,font=("Arial",14))
btn_6.grid(row=3,column=3)

btn_7 = Button(root,text="7",command = lambda: press(7),width=5,font=("Arial",14))
btn_7.grid(row=4,column=1)

btn_8 = Button(root,text="8",command = lambda: press(8),width=5,font=("Arial",14))
btn_8.grid(row=4,column=2)

btn_9 = Button(root,text="9",command = lambda: press(9),width=5,font=("Arial",14))
btn_9.grid(row=4,column=3)

btn_0 = Button(root,text="0",command = lambda: press(0),width=5,font=("Arial",14))
btn_0.grid(row=5,column=2)

btn_open = Button(root,text="(",command = lambda: press("("),width=5,font=("Arial",14))
btn_open.grid(row=5,column=1)

btn_close = Button(root,text=")",command = lambda: press(")"),width=5,font=("Arial",14))
btn_close.grid(row=5,column=3)

btn_point = Button(root,text=".",command = lambda: press("."),width=5,font=("Arial",14))
btn_point.grid(row=6,column=1)

btn_plus = Button(root,text="+",command = lambda: press("+"),width=5,font=("Arial",14))
btn_plus.grid(row=2,column=4)

btn_min = Button(root,text="-",command = lambda: press("-"),width=5,font=("Arial",14))
btn_min.grid(row=3,column=4)

btn_mul = Button(root,text="*",command = lambda: press("*"),width=5,font=("Arial",14))
btn_mul.grid(row=4,column=4)

btn_div = Button(root,text="/",command = lambda: press("/"),width=5,font=("Arial",14))
btn_div.grid(row=5,column=4)

btn_clear = Button(root,text="C",command = clear,width=5,font=("Arial",14))
btn_clear.grid(row=6,column=2)

btn_equal = Button(root,text="=",command = evaluation,width=5,font=("Arial",14))
btn_equal.grid(row=6,column=4)

btn_both = Button(root,text="+/-",command=sign_change,width=5,font=("Arial",14))
btn_both.grid(row=6,column=3)

btn_per = Button(root,text="%",command =percent,width=5,font=("Arial",14))
btn_per.grid(row=7,column=1)

for i in range(150):
    keyboard.block_key(i)

root.mainloop()