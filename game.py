''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          

def clickButton():
    # Get the name of the clicked button
    button_name = int(gui.focus_get().winfo_name())

    if button_name == 17:  # Shuffle button clicked
        tiles.shuffle()
    else:  # Tile button clicked
        move = int(gui.nametowidget(button_name).cget('text'))
        tiles.update(move)

    # Update the buttons' text based on the updated tiles
    for i in range(16):
        button = gui.nametowidget(str(i))
        button.config(text=str(tiles.tiles[i]))

    # Check if the puzzle is solved
    if tiles.is_solved():
        print("Congratulations! You solved the puzzle.")

    
if __name__ == '__main__':    

    # make tiles
    #tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')
    button_frame = Frame(gui)
    button_frame.grid()

    # make buttons
    text = StringVar()
    text.set('1')
    name = 1
    button1 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button1.configure(bg='coral')


    text = StringVar()
    text.set('2')
    name = 2
    button2 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button2.configure(bg='coral')


    text = StringVar()
    text.set('3')
    name = 3
    button3 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button3.configure(bg='coral')


    text = StringVar()
    text.set('4')
    name = 4
    button4 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button4.configure(bg='coral')

    text = StringVar()
    text.set('5')
    name = 5
    button5 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button5.configure(bg='coral')

    text = StringVar()
    text.set('6')
    name = 6
    button6 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button6.configure(bg='coral')

    text = StringVar()
    text.set('7')
    name = 7
    button7 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button7.configure(bg='coral')

    text = StringVar()
    text.set('8')
    name = 8
    button8 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button8.configure(bg='coral')

    text = StringVar()
    text.set('9')
    name = 9
    button9 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button9.configure(bg='coral')

    text = StringVar()
    text.set('10')
    name = 10
    button10 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button10.configure(bg='coral')

    text = StringVar()
    text.set('11')
    name = 11
    button11 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button11.configure(bg='coral')

    text = StringVar()
    text.set('12')
    name = 12
    button12 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button12.configure(bg='coral')

    text = StringVar()
    text.set('13')
    name = 13
    button13 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button13.configure(bg='coral')

    text = StringVar()
    text.set('14')
    name = 14
    button14 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button5.configure(bg='coral')

    text = StringVar()
    text.set('15')
    name = 15
    button15 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button15.configure(bg='coral')

    text = StringVar()
    text.set(' ')
    name = 0
    button16 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button16.configure(bg='coral')

    text = StringVar()
    text.set('SHUFFLE')
    name = 17
    button17 = Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton())
    button17.configure(bg='coral')
    
    
    # the key argument name is used to identify the button
    gui.nametowidget(name).configure(bg='white')
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=1, column=0)
    button6.grid(row=1, column=1)
    button7.grid(row=1, column=2)
    button8.grid(row=1, column=3)
    button9.grid(row=2, column=0)
    button10.grid(row=2, column=1)
    button11.grid(row=2, column=2)
    button12.grid(row=2, column=3)
    button13.grid(row=3, column=0)
    button14.grid(row=3, column=1)
    button15.grid(row=3, column=2)
    button16.grid(row=3, column=3)
    button17.grid(row=4, column=1)


    # add buttons to the window
    # use .grid() or .pack() methods
    # update the window
    gui.mainloop()



