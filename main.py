import tkinter as tk
from tkinter import messagebox
from subprocess import call
import json


# ---------------------------- Searching saved data ------------------------------- #
def serach():
    web=webent.get()
    if len(web)==0:
        messagebox.showwarning(title="Ooops", message="Please Provide a website name first!")
    else:
        try:
            with open("data.json", 'r') as fle:
                data=json.load(fle)
                messagebox.showinfo(title=web, message=f"Usename: {data[web]['username']}\nPassword: {data[web]['password']}")
        except FileNotFoundError:
            messagebox.showwarning(title='Ooops', message="First please save some data")
        except KeyError:
            messagebox.showwarning(title="Ooops", message=f"No data available related to {web}")

# ---------------------------- Showing saved data ------------------------------- #
def show_data():
    
    call("notepad details.txt")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    #Password Generator Project
    op=None
    passwo=None

    def passw():
        global op
        global passwo
        import random
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        
        nr_letters= letent.get()
        nr_symbols = syment.get()
        nr_numbers = nument.get()
        
        if len(letent.get())==0 or len(syment.get())==0 or len(nument.get())==0 or len(str(op))==0:
            messagebox.showwarning(title='Oops', message="please don't leave any fields empty!")
            scr2.attributes('-topmost', True)
        
        

        else:
            try:
                S=int(op)
                if S==1:
                #Eazy Level - Order not randomised:
                #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
                    passwordstr=''
                    for i in range(0,int(nr_letters)):
                        x=random.randint(0,25)
                        passwordstr+=letters[x]

                    for j in range(1,int(nr_symbols)+1):
                        y=random.randint(0,9)
                        passwordstr+=numbers[y]

                    for k in range(1,int(nr_symbols)+1):
                        z=random.randint(0,8)
                        passwordstr+=symbols[z]

                    passwo=passwordstr

            #Hard Level - Order of characters randomised:
            #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
                else:
                    password_list=[]

                    for i in range(0,int(nr_letters)):
                        password_list+=random.choice(letters)
                    for j in range(0,int(nr_numbers)):
                        password_list+=random.choice(numbers)
                    for k in range(0,int(nr_symbols)):
                        password_list+=random.choice(symbols)

                    random.shuffle(password_list)

                    password=""
                    for char in password_list:
                        password+=char

                    passwo=password

                condition1=messagebox.askokcancel(title='⚠️⚠️⚠️⚠️', message=f"password generated: {passwo}\nDo you want to use it ?")

                if condition1:
                    pasent.insert(1, passwo)
                    scr2.destroy()
                else:
                    scr2.attributes('-topmost', True)
            except:
                messagebox.showwarning(title="Oops", message="Only integer values please!")
                scr2.attributes('-topmost', True)
    
    scr2=tk.Toplevel()
    scr2.title("Password Generator")
    scr2.config(padx=10,pady=10)
    scr2.minsize(width=600,height=300)
    scr2.maxsize(width=600,height=300)

    scr2.grid_columnconfigure(0, weight=1)
    scr2.grid_columnconfigure(1, weight=1)
    scr2.grid_columnconfigure(2, weight=1)
    scr2.grid_rowconfigure(0, weight=1)
    scr2.grid_rowconfigure(1, weight=1)
    scr2.grid_rowconfigure(2, weight=1)
    scr2.grid_rowconfigure(3, weight=1)
    scr2.grid_rowconfigure(4, weight=1)
    scr2.grid_rowconfigure(5, weight=1)
    scr2.grid_rowconfigure(6, weight=1)
    scr2.grid_rowconfigure(7, weight=1)


    # can2=tk.Canvas(scr2,width=200,height=200,bg="#f0f0f0")
    # pic2=tk.PhotoImage(file='images-removebg-preview.png')
    # can2.create_image(100,100,image=pic2)
    # can2.grid(column=2,row=0)

    can3=tk.Canvas(scr2,width=338,height=78,bg="#f0f0f0")
    pic3=tk.PhotoImage(file='password.png')
    can3.create_image(169,39,image=pic3)
    can3.grid(column=0,row=0,columnspan=2)

    can4=tk.Canvas(scr2,width=338,height=84,bg="#f0f0f0")
    pic4=tk.PhotoImage(file='generate.png')
    can4.create_image(169,42,image=pic4)
    can4.grid(column=1,row=1,columnspan=2)

    def used_button():
        global op
        op=radio_state.get()
        # print(op)

    #labels
    letlab=tk.Label(scr2, text="Nummber of letter in password:",font=("Courier",10,"bold"))
    letlab.grid(column=0,row=2,sticky='w')
    
    symlab=tk.Label(scr2, text="Number of symbols in password:",font=("Courier",10,"bold"))
    symlab.grid(column=0,row=4,sticky='w')

    numlab=tk.Label(scr2, text="Number of digits in password:",font=("Courier",10,"bold"))
    numlab.grid(column=0,row=6,sticky='w')

    strenlab=tk.Label(scr2, text='Choose the strength of password',font=("Courier",10,"bold"))
    strenlab.grid(column=1,row=3,columnspan=2)

    #buttons
    radio_state = tk.IntVar()
    radiobutton1 = tk.Radiobutton(scr2,text="Moderate", value=1, variable=radio_state, command=used_button)
    radiobutton1.grid(column=2,row=4,sticky='w')
    radiobutton2 = tk.Radiobutton(scr2,text="Strong", value=2, variable=radio_state, command=used_button)
    radiobutton2.grid(column=2,row=5,sticky='w')

    genbut2=tk.Button(scr2, text='Generate password',font=("Courier",10,"bold"), bg='#89CFF0',command=passw)
    genbut2.grid(column=1,row=7,columnspan=2)


    #entries

    letent=tk.Entry(scr2)
    letent.grid(column=0,row=3,sticky='w')

    syment=tk.Entry(scr2)
    syment.grid(column=0,row=5,sticky='w')

    nument=tk.Entry(scr2)
    nument.grid(column=0,row=7,sticky='w')



    scr2.mainloop()
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    password=pasent.get()
    username=userent.get()
    website=webent.get()
    new_data={website:{
        "username":username,
        "password":password
    }}

    if len(password)==0 or len(username)==0 or len(website)==0:
        messagebox.showwarning(title='Oops', message="please don't leave any fields empty!")
    
    else:
        condition=messagebox.askokcancel(title=website, message=f"These are the details entered:\n Username/Email: {username}\n Password: {password}")

        if condition:
            try:
                with open("data.json", 'r') as fle:
                    data=json.load(fle)
                    data.update(new_data)
                with open("data.json", 'w') as fle:
                    json.dump(data, fle, indent=4)
            except:
                with open("data.json", 'w') as fle:
                    json.dump(new_data, fle, indent=4)
            finally:
                with open("details.txt", 'a') as fil:
                    fil.write(f"website:{website} || username/email:{username} || password:{password}\n\n")
                pasent.delete(0, 'end')
                userent.delete(0, 'end')
                webent.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #
scr=tk.Tk()
scr.title("Password Manager")
scr.minsize(width=700,height=500)
scr.maxsize(width=700,height=500)
scr.config(padx=20,pady=20)


scr.grid_columnconfigure(0, weight=1)
scr.grid_columnconfigure(1, weight=1)
scr.grid_columnconfigure(2, weight=1)
scr.grid_rowconfigure(0, weight=1)
scr.grid_rowconfigure(1, weight=1)
scr.grid_rowconfigure(2, weight=1)
scr.grid_rowconfigure(3, weight=1)
scr.grid_rowconfigure(4, weight=1)

can=tk.Canvas(width=300 , height=300)
pic=tk.PhotoImage(file="logo.png")
can.create_image(150,150,image=pic)
can.grid(row=0, column=1)


#labels
website=tk.Label(text="Website:", font=("Courier",12,"bold"))
website.grid(column=0,row=1)

userlab=tk.Label(text="Email/Username:",font=("Courier",12,"bold"))
userlab.grid(column=0,row=2)

paslab=tk.Label(text="Password:",font=("Courier",12,"bold"))
paslab.grid(column=0,row=3)

#entries
webent=tk.Entry(width=49)
webent.focus()
webent.grid(column=1,row=1,columnspan=2,sticky="W")

userent=tk.Entry(width=49)
userent.grid(column=1,row=2,columnspan=2,sticky="W")

pasent=tk.Entry(width=30)
pasent.grid(column=1,row=3,sticky="W")

#buttons
genbut=tk.Button(text="Generate Passwod",width=20,font=("Courier",9,"bold"), command=generate)
genbut.grid(column=2,row=3,sticky="W")

adbut=tk.Button(text="Add",width=36,font=("Courier",10,"bold"), command=save_details)
adbut.grid(column=1,row=4,columnspan=3,sticky="W")

filebut=tk.Button(text="Show saved data",font=("Courier",10,"bold"), command=show_data )
filebut.grid(column=0,row=0,sticky='nw')

serchbut=tk.Button(text="Search",font=("Courier",10,"bold"),width=17, command=serach)
serchbut.grid(column=2,row=1)

scr.mainloop()