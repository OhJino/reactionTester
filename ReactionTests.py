from tkinter import *
import time
import random

master = Tk()

#timer variable that will stop when mouse is clicked
stop_timer = 0

#timer variable that will stop when screen changes green
timer = 0

#variable that is calculates the difference between timer and stop_timer vars
reaction_time = 0

#random time variable set to change the screen at a random time
ran_time = 0

#Function to calcuolate reaction time once mouse has been clicked
def react(event):
    #set stop_timer to a global var
    global stop_timer
    #stop timer when mouse was clicked
    stop_timer = time.time()
    #reaction_time set to global
    global reaction_time
    #calculate difference. This is the time from when the screen changed colors and when the mouse was clicked
    reaction_time = (stop_timer - timer)
    #multiply by 1000 to convert from sec to ms
    reaction_time *= 1000
    #Change the contents of results label to the reaction time
    #Round to the nearest hundredth
    results.configure(text=round(reaction_time, 2) , font=("Arial Bold", 20), bg="green")
    results.pack()

#Resets the timer back to 0 and sets another random time for the screen to turn green again
def reset(event):
    global reaction_time
    #Reset the reaction_time variable back to 0
    reaction_time = 0
    #Change screen back to red
    master.configure(bg="red")
    #Set another random time for the screen to turn green
    ran_time = random.randint(1000,5000)
    #Reaction time reset to 0 so the results will be set back to 0
    results.configure(text=reaction_time , font=("Arial Bold", 20), bg="red")
    results.pack()
    #Change the screen again after a random time
    master.after(ran_time, changeScreen)



def changeScreen():
    #Change screen to green
    master.configure(bg = "green")
    #Set timer variable to global
    global timer
    #Start timer once the screen turns green
    timer = time.time()
    #Configure the label w/ green bckground
    #Starts off at 0 because the mouse was not clicked yet
    results.configure(text=0, font=("Arial Bold", 20), bg="green")


ran_time = random.randint(1000, 5000)

#name of program set to Reaction Tester
master.title("Reaction Tester")

#Bind Left-Click to react() function - will detect time from when the screen changed red and when mouse was clicked
master.bind("<Button-1>", react)

#Bind the 'R' key to set screen to red and to reset the timer
master.bind("r", reset)

#Set program resolution
master.geometry("500x400")

#Screen starts off red
master.configure(bg = "red")

#Reaction timer starts when screen turns green
master.after(ran_time, changeScreen)

#Displays reaction time between when screen turned green and when mouse was clicked
results = Label(master, text =str(reaction_time), font=("Arial Bold", 20), bg ="red")
results.pack()


master.mainloop()