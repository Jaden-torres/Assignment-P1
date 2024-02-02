'''
Assignment P1 for GUI
Jaden Torres
Professor: Bruce Montgomery

Class Name: French Numbers

'''


from tkinter import *
from tkinter import ttk
root= Tk() #tkinter call
root.resizable(0,0) #disabeling max option.

def close(): #variable for closing the tkinter window.
    root.destroy() 


ttk.Label(root, text="Do you know the French words for the numbers 1 through 5?").grid() #question
ttk.Label(root, text="Please click the buttons below to see.").grid() #instructions
app = Frame(root) #Tkinter window
app.grid()
def one():  # variable for answer 1 on button 6
    print("un")
    bttn6 = Button(app, text = "un", bg = "green", width = 10)
    bttn6.grid(row = 2000, column = 600)
def two():  #variable for answer 2 on button 6
    print("deux")
    bttn6 = Button(app, text = "deux", bg = "green", width = 10)
    bttn6.grid(row = 2000, column = 600)
def three():    #variable for answer 3 on button 6
    print("trios")
    bttn6 = Button(app, text = "trios", bg = "green", width = 10)
    bttn6.grid(row = 2000, column = 600)
def four():     #variable for answer 4 on button 6
    print("quatre")
    bttn6 = Button(app, text = "quatre", bg = "green", width = 10)
    bttn6.grid(row = 2000, column = 600)
def five():     #variable for answer 5 on button 6
    print("cinq")
    bttn6 = Button(app, text = "cinq", bg = "green", width = 10)
    bttn6.grid(row = 2000, column = 600)


bttn1 = Button(app, text = "1", width = 5, command= one)    #button 1 create
bttn1.grid(row = 250, column = 50)
bttn2 = Button(app, text = "2", width = 5, command = two)    #button 2 create
bttn2.grid(row = 250, column = 100)
bttn3 = Button(app, text = "3", width = 5, command = three)    #button 3 create
bttn3.grid(row = 250, column = 150)
bttn4 = Button(app, text = "4", width = 5, command = four)    #button 4 create
bttn4.grid(row = 250, column = 200)
bttn5 = Button(app, text = "5", width = 5, command = five)    #button 5 create
bttn5.grid(row = 250, column = 250)
exitt = Button(app, text = "Exit", width = 5, command = close)    #exit button create
exitt.grid(row = 350, column = 500)



root.title("French Numbers") #window title
root.geometry("500x500") #window size
root.mainloop() #tk mainloops

'''
Works Cited:

Color Buttons: https://www.geeksforgeeks.org/change-color-of-button-in-python-tkinter/

Minimize Remove: https://stackoverflow.com/questions/2969870/removing-minimize-maximize-buttons-in-tkinter

Buttons: https://www.tutorialspoint.com/python/tk_button.htm

Exit Button: https://www.tutorialspoint.com/how-to-exit-from-python-using-a-tkinter-button


'''
