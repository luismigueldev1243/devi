from tkinter import *


j = Tk()
num1 = int(Entry(j,width=20))
num1.grid(column=1,row=1)
num1.get()

num2 = int(Entry(j,width=20))
num2.grid(column=1,row=3)
num2.get()

soma = num1 + num2



bot1 = Button(j,text="+",command=soma)








j.mainloop()


