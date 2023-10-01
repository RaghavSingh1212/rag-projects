# Author Name - Raghav Singh
# Date - 05/12/2023
# file - calculatorGUI.py
# description -calculatorGUI which is a visual form of calculator, where there are different button foe wrting expression.
# create a GUI calculator using tkinter
from tkinter import *
from calculator import calculate
def calculator(gui):   
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,= 
    b0 = addButton(gui,entrybox,'0')
    b1 = addButton(gui,entrybox,'1')
    b2 = addButton(gui,entrybox,'2')
    b3 = addButton(gui,entrybox,'3')
    b4 = addButton(gui,entrybox,'4')
    b5 = addButton(gui,entrybox,'5')
    b6 = addButton(gui,entrybox,'6')
    b7 = addButton(gui,entrybox,'7')
    b8 = addButton(gui,entrybox,'8')
    b9 = addButton(gui,entrybox,'9')
    b_add = addButton(gui,entrybox,'+')
    b_sub = addButton(gui,entrybox,'-')
    b_mult = addButton(gui,entrybox,'*')
    b_div = addButton(gui,entrybox,'/')
    b_clr = addButton(gui,entrybox,'c')
    b_eq = addButton(gui,entrybox,'=')
    b_dec = addButton(gui,entrybox,'.')
    b_paren1 = addButton(gui, entrybox, '(')
    b_paren2 = addButton(gui, entrybox, ')')
    b_pow = addButton(gui, entrybox, '^')

    # add buttons to the grid
    buttons =[ b7,      b8,   b9,      b_clr,
               b4,      b5,   b6,      b_sub,
               b1,      b2,   b3,      b_add, 
               b_mult,  b0,   b_div,   b_pow,
               b_paren1,b_dec,b_paren2,b_eq,]
    k = 5         
    for i in range(k):
        for j in range(4):
            buttons[i*4+j].grid(row=i+1, column=j, columnspan=1)

def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value))

def clickButton(entrybox, value):
    # get the current expression entered by the user
    current = entrybox.get()
    
    # clear the entry box if the user presses the clear button
    if value == 'c':
        entrybox.delete(0, END)
    # evaluate the expression and display the result if the user presses the equal button
    elif value == '=':
        try:
            result = calculate(current)
            entrybox.delete(0, END)
            entrybox.insert(0, result)
        except Exception as e:
            entrybox.delete(0, END)
            entrybox.insert(0, "Error")
    # add the clicked button to the expression
    else:
        
            # check if there is already a decimal in the current number
        if '.' not in current:
                entrybox.delete(0, END)
                entrybox.insert(0, current + value)
        else:
            entrybox.delete(0, END)
            entrybox.insert(0, current + value)
    
# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()



