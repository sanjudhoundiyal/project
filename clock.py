from tkinter import *
import time

app_window = Tk()
app_window.title(" made by sanjuDigital Clock")
app_window.geometry("590x150")
app_window.resizable(0, 0)

Text_font = ("boulder", 68, "bold")
background = 'black'
foreground = "red"
border_width = 25

label = Label(app_window, font=Text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

# Function to update the time
def digital_clcok():
    time_live = time.strftime("%I:%M:%S %p")  # Use %p for AM/PM
    label.config(text=time_live)
    label.after(200, digital_clcok)  # Refresh the clock every 200 milliseconds

digital_clcok()
app_window.mainloop()


