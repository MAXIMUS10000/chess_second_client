import time
from tkinter import *
x=[]
figure = '123'
def show():
    global figure
    def choose(x1):
        global figure
        figure=x1
        win.destroy()
    win = Toplevel()
    win.geometry('200x50')
    queenimg =PhotoImage(file='figures/bq.png').subsample(3)
    knightimg =PhotoImage(file='figures/bn.png').subsample(3)
    bishopimg =PhotoImage(file='figures/bb.png').subsample(3)
    rookimg =PhotoImage(file='figures/br.png').subsample(3)
    imagelist=[queenimg,knightimg,bishopimg,rookimg]
    for m in range(0,4):
        b=Button(win,bg='white',fg='Blue')
        b.configure(command=lambda x1=m: choose(x1),image=imagelist[m])
        b.place(x=50*m,y=0,width=50,height=50)
        x.append(b)

    while figure=='123':
        win.update()
        time.sleep(0.01)
    print('Chosen:',figure)
    a=figure
    figure='123'
    return a