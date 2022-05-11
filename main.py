import random
from tkinter import *
window = Tk()

window.minsize(500,500)
window.maxsize(500,500)

window.title('Dice Roller Simulator created by Sayam')


label = Label(window,font=('bold',200))
def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{ random.choice(number)}')
    label.pack()



heading = Label(window,text='Roll the dice', font=('bold',40) , bg='light cyan')
heading.pack(fill=X)

button = Button(window,text='Roll Dice',font=('Ink free',20,'bold'),command=lambda:roll())
button.config(bg='light cyan')
button.config(fg='black')
button.pack()



window.mainloop()

