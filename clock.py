from tkinter import *
import time

root = Tk()
time1 = ''
clock = Label(root, font=('Helvetica', 100), bg='#000', fg='green')
clock.pack(fill=BOTH, expand=1)


def update():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%I:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, update)


update()
root.mainloop()
