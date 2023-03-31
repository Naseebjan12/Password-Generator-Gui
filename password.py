from tkinter import *
import pyperclip
from tkinter import messagebox
import random
window = Tk()
# changing the color of the window
window.config(bg='light blue')

# max and min size of the screen
window.minsize(width=400,height=300)
window.maxsize(width=400,height=300)
var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()


# functio to print the password
def print_values():
    pass_length= length.get()
    character_check= var1.get()
    alphabet_check= var2.get()
    integer_check=var3.get()

    if integer_check==True and character_check==True and alphabet_check==True:
        res=''
        for i in range(1,pass_length+1):
            char =['1','2','3','4','5','6','7','8','9','!', '@', '#', '$', '%', '^', '&', '*', '(', ')','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            password=random.choice(char)
            res=res+password
        pyperclip.copy(res)
        messagebox.showinfo(message='Password Copy to Clipboard\nU can use it using win+v')
    elif alphabet_check==True and character_check==True:
        res=''
        for i in range(1,pass_length+1):
            char =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
            password=random.choice(char)
            res=res+password
        pyperclip.copy(res)
        messagebox.showinfo(message='Password Copy to Clipboard\nU can use it using win+v')
    elif alphabet_check==True and integer_check==True:
        res=''
        for i in range(1,pass_length+1):
            char =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
            password=random.choice(char)
            res=res+password
        pyperclip.copy(res)
        messagebox.showinfo(message='Password Copy to Clipboard\nU can use it using win+v')
    elif integer_check==True and character_check==True:
        res=''
        for i in range(1,pass_length+1):
            char =['1','2','3','4','5','6','7','8','9','!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
            password=random.choice(char)
            res=res+password
        pyperclip.copy(res)
        messagebox.showinfo(message='Password Copy to Clipboard\nU can use it using win+v')
    elif character_check==True:
        res=''
        for i in range(1,pass_length+1):
            char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
            password=random.choice(char)
            res=res+password
        pyperclip.copy(res)
        messagebox.showinfo(message='Password Copy to Clipboard\nU can use it using win+v')
    elif alphabet_check==True:
        res=''
        for i in range(1,pass_length+1):
            char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            password=random.choice(char)
            res=res+password
        pyperclip.copy(res)
        messagebox.showinfo(message='Password Copy to Clipboard\nU can use it using win+v')
    elif integer_check==True:
        res=''
        for i in range(1,pass_length+1):
            char =['1','2','3','4','5','6','7','8','9']
            password=random.choice(char)
            res=res+password
        pyperclip.copy(res)
        messagebox.showinfo(message='Password Copy to Clipboard\nU can use it using win+v')
 
# title of the window
window.title('Password Generator By Naseeb jan')
# false the resizebility of the window
window.resizable(False,False)



# label
text=Label(text='Random Password Generator:',bg='light blue',pady=20,font=('arial',15))
text.pack()



# lengt
text=Label(text='Select Password Length',bg='light blue')
text.pack()
# passord length
length=Scale(orient=HORIZONTAL, length=200, from_=1.0 , to=100,width=10,bg='light blue')
length.pack()
label=Label(text='',bg='light blue')
label.pack()

# special character
special_character=Checkbutton(text='Inlcude Character',font=('arial',10),bg='light blue',variable=var1)
special_character.pack()

# alphabets
alphabets=Checkbutton(text='Inlcude Alphabets',font=('arial',10),pady=2,padx=-10,bg='light blue',variable=var2)
alphabets.pack()

# include number
number=Checkbutton(text='Inlcude Number   ',font=('arial',10),bg='light blue',variable=var3)
number.pack()
label=Label(text='',bg='light blue')
label.pack()

btn=Button(text='Generate Password',bg='light blue',width=27,command=print_values)

# pssword Copy section

btn.pack()
window.mainloop()