# Usage python3 countdownTimer.py
from tkinter import *
from tkinter import ttk
from tkinter import font
import sys
import os

import time
import datetime

global endTime


# Add the required environment variable if it is not set to connect to the display
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


# Function to update and show the time on the screen
def show_time():
    # Get the time remaining until the event
    remainder = endTime - datetime.datetime.now()
    # remove the microseconds part
    remainder = remainder - datetime.timedelta(microseconds=remainder.microseconds)
    # Show the time left
    txt.set(remainder)
    # Trigger the countdown after 1000ms
    master.after(1000, show_time)

# Add a button to allow quiting as it is fullscreen
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Good Bye'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)

#create main window
master = Tk()
master.title("Countdown")
master.geometry("640x200")
master.configure(background='black')
master.attributes("-fullscreen", True)

# Set the labels and buttons on the screen
master.after(1000, show_time)
quitButton(master)


# Set an end date
endTime = datetime.datetime(2020, 5, 2, 0, 0, 0)

# set up multiple font sizes
fntMedium = font.Font(family='Helvetica', size=48, weight='bold')
fntSmall = font.Font(family='Helvetica', size=24, weight='bold')

headingLabel = Label(master, text="Countdown to .....", font=fntSmall, foreground="green", background="black", anchor=CENTER)

# Create a variable string to place the countdown label in
txt = StringVar()
countDownLabel = Label(master, textvariable=txt, font=fntMedium, foreground="green", background="black", anchor=CENTER)

# Lay out labels in the centre of the screen stacked on top of one another
headingLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
countDownLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

# Run forever!
master.mainloop()
