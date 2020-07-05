import sys
import tkinter

def handleButton(event):
    global en
    global e
    e['text'] = eval (en.get())


top = tkinter.Tk()

header = tkinter.Label(top,text="### Taschenrechner ###")
header.pack()

info_text = tkinter.Label(top,text="Wichtig: Eingabe immer nach den Amerikanischen Regeln!")
info_text.pack()


en = tkinter.Entry(top)
en.pack()

e = tkinter.Label(top,text='Press "Berechnen" ')
e.pack()

b = tkinter.Button(top,text="Berechnen")
b.pack()


b.bind('<Button-1>', handleButton)

info_text_2 = tkinter.Label(top,text="by Robieo")
info_text_2.pack()

top.mainloop()