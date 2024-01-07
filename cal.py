from customtkinter import *


app = CTk()
app.title("TIMER")
app.configure(fg_color='black')
app.geometry("330x540")

bold_font = ("Verdana", 52)

digits = ''
a = 0
s = ''
b = 0




def addition():

    global digits
    global a
    global s

    a = float(digits)
    
    s = '+'
    
    digits=''
    number.configure(text=digits)

def substraction():
    global digits
    global a
    global s

    a = float(digits)
    
    s = '-'
    
    digits=''
    number.configure(text=digits)

def multiplication():
    global digits
    global a
    global s

    a = float(digits)
    
    s = 'x'
    
    digits=''
    number.configure(text=digits)

def divition():
    global digits
    global a
    global s

    a = float(digits)
    
    s = '/'
    
    digits=''
    number.configure(text=digits)

def result():
    global digits
    global a
    global s
    global b 

    b = float(digits)

    
    if s =='+':
        final = a+b

    elif s=='-':
        final = a-b
    
    elif s=='x':
        final = a*b

    elif s=='/':
        final = a/b
    
    
    
    digits = f'{final:.2f}'
    number.configure(text=digits)

    a = 0
    b = 0
    s =''

    

def ac_():
    global digits
    digits=''
    number.configure(text='')

def decimal():
    global digits
    if len(digits) <=8 and '.' not in digits:
        
        digits +='.'
        number.configure(text=digits)

def negative():
    global digits
    convert = float(digits) * -1

    digits = f'{convert}'
    number.configure(text=digits)

def mod():
    global digits
    convert = float(digits) / 100

    digits = f'{convert}'
    number.configure(text=digits)



def one_():
    global digits
    if len(digits) <=8:
        
        digits +='1'
        number.configure(text=digits)

def two_():
    global digits
    if len(digits) <=8:
        
        digits +='2'
        number.configure(text=digits)

def three_():
    global digits
    if len(digits) <=8:   
        
        digits +='3'
        number.configure(text=digits)

def four_():
    global digits
    if len(digits) <=8:
        
        digits +='4'
        number.configure(text=digits)

def five_():
    global digits
    if len(digits) <=8:
        
        digits +='5'
        number.configure(text=digits)

def six_():
    global digits
    if len(digits) <=8:
        
        digits +='6'
        number.configure(text=digits)

def seven_():
    global digits
    if len(digits) <=8:
        
        digits +='7'
        number.configure(text=digits)

def eight_():
    global digits
    if len(digits) <=8:
        
        digits +='8'
        number.configure(text=digits)
        
def nine_():
    global digits
    if len(digits) <=8:
        
        digits +='9'
        number.configure(text=digits)


def zero_():
    global digits
    if len(digits) <=8:
        
        digits +='0'
        number.configure(text=digits)



number = CTkLabel(app, text=digits, font= bold_font, anchor='w')

smaller = ("Verdana", 48)

ac = CTkButton(app, text='C', width= 70, corner_radius=60, font= bold_font, command=ac_, fg_color='white', text_color='black', hover_color='white')
sign = CTkButton(app, text='-', width= 70, corner_radius=60, font= bold_font,  fg_color='white', text_color='black', hover_color='white', command=negative)
module = CTkButton(app, text='M', width=70, corner_radius=60, font= bold_font,  fg_color='white', text_color='black', hover_color='white', command=mod)
point = CTkButton(app, text='.', width= 70, corner_radius=60, font= bold_font,  fg_color='grey', text_color='black', hover_color='grey', command=decimal)

zero = CTkButton(app, text='0', width= 150, corner_radius=60, font= bold_font, command=zero_, fg_color='grey', text_color='black', hover_color='grey')

one = CTkButton(app, text='1', width= 70, corner_radius=60, font= bold_font, command=one_, fg_color='grey', text_color='black', hover_color='grey')
two = CTkButton(app, text='2', width= 70, corner_radius=60, font= bold_font, command=two_, fg_color='grey', text_color='black', hover_color='grey')
three = CTkButton(app, text='3', width= 70, corner_radius=60, font= bold_font, command=three_, fg_color='grey', text_color='black', hover_color='grey')

four = CTkButton(app, text='4', width= 70, corner_radius=60, font= bold_font, command=four_, fg_color='grey', text_color='black', hover_color='grey')
five = CTkButton(app, text='5', width= 70, corner_radius=60, font= bold_font, command=five_, fg_color='grey', text_color='black', hover_color='grey')
six = CTkButton(app, text='6', width= 70, corner_radius=60, font= bold_font, command=six_, fg_color='grey', text_color='black', hover_color='grey')

seven = CTkButton(app, text='7', width= 70, corner_radius=60, font= bold_font, command=seven_, fg_color='grey', text_color='black', hover_color='grey')
eight = CTkButton(app, text='8', width= 70, corner_radius=60, font= bold_font, command=eight_, fg_color='grey', text_color='black', hover_color='grey')
nine = CTkButton(app, text='9', width= 70, corner_radius=60, font= bold_font, command=nine_, fg_color='grey', text_color='black', hover_color='grey')


plus = CTkButton(app, text='+', width= 70, corner_radius=80, font= bold_font,  fg_color='orange', text_color='white', hover_color='orange', command=addition)
minus = CTkButton(app, text='-', width= 70, corner_radius=60, font= bold_font,  fg_color='orange', text_color='white', hover_color='orange', command=substraction)
times = CTkButton(app, text='x', width= 70, corner_radius=60, font= bold_font,  fg_color='orange', text_color='white', hover_color='orange', command=multiplication)
divide = CTkButton(app, text='/', width= 70, corner_radius=60, font= bold_font,  fg_color='orange', text_color='white', hover_color='orange',command=divition)

equal = CTkButton(app, text='=', width= 70,  corner_radius=90, font= bold_font,  fg_color='orange', text_color='white', hover_color='orange', command=result)






#app.bind('<1>', lambda event:one_())


app.bind('<+>', lambda event:addition())
app.bind('-', lambda event:substraction())
app.bind('<*>', lambda event:multiplication())
app.bind('</>', lambda event:divition())
app.bind('<Escape>', lambda event:ac_())
app.bind('.', lambda event:decimal())




app.bind('1', lambda event:one_())
app.bind('2', lambda event:two_())
app.bind('3', lambda event:three_())
app.bind('4', lambda event:four_())
app.bind('5', lambda event:five_())
app.bind('6', lambda event:six_())
app.bind('7', lambda event:seven_())
app.bind('8', lambda event:eight_())
app.bind('9', lambda event:nine_())
app.bind('0', lambda event:zero_())


app.bind('<Return>', lambda event:result())




number.place(x=10, y=70)

ac.place(x=10,y=140)
sign.place(x=90,y=140)
module.place(x=170,y=140)
divide.place(x=250, y = 140 )

seven.place(x=10,y=220)
eight.place(x=90,y=220)
nine.place(x=170,y=220)

times.place(x=250, y=220)

four.place(x=10, y = 300)
five.place(x=90, y = 300 )
six.place(x=170, y = 300 )
minus.place(x=250,y=300)


one.place(x=10, y = 380)
two.place(x=90, y = 380 )
three.place(x=170, y = 380 )
plus.place(x=250, y = 380 )

zero.place(x=10, y=460)
point.place(x=170, y = 460)
equal.place(x=250, y=460)



app.mainloop()