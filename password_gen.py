from random import randint
from tkinter import *

root = Tk()
root.title('PassGen')

#Creditos autor do icone ---> www.freepik.com" 
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='/home/david/Desktop/Python/PassGen/icone/senha.png'))

root.geometry('500x310')

root.configure(bg='black')

my_password = chr(randint(33,126))

#Gerar senha aleatoria
def new_rand():
    #Limpar Entry box
    pw_entry.delete(0,END)
    #Receber o tamanho da senha
    pw_lenght = int(my_entry.get())
    #Variavel p/ a senha
    my_password=''
    #Loop 
    for x in range(pw_lenght):
        my_password += chr(randint(33,126))
    #Mostrar senha na tela
    pw_entry.insert(0,my_password)    
# Copiar a senha
def clipper():
    #Limpar clipboard
    root.clipboard_clear()
    #Copiar para o clipboard
    root.clipboard_append(pw_entry.get())
#Label Frame
lf = LabelFrame(root,text="De quantos caracteres quer sua senha?",font='bold',bd='3px',bg='black',fg="#41A003")
lf.pack(pady=20)

#Entry Box escolher o número de caracteres

my_entry = Entry(lf, font=("Helvetica",24),fg="#41A003",bg="black")
my_entry.pack(pady=20,padx=20)

#Entry box saída

pw_entry=Entry(root,text='',font=("Helvetica",24),bd='3px',fg="#41A003",bg="black")
pw_entry.pack(pady=20)

#Frame Buttons

my_frame =Frame(root)
my_frame.pack(pady=20)

#Crear Buttons

my_button= Button(my_frame,text="Gerar senha", command=new_rand,bd='3px',bg='black',fg="#41A003", activebackground='#41A003', activeforeground='black')
my_button.grid(row=0,column=0,padx=0)

clip_button = Button(my_frame, text="Copiar senha", command=clipper,bd='3px',bg='black',fg="#41A003", activebackground='#41A003',activeforeground='black')
clip_button.grid(row=0, column=1 ,padx=0)

root.mainloop()