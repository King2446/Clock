# Importing modules
from tkinter.ttk import *
from tkinter import *
from math import *
from time import *
import datetime as dt


# Initializing window as the base
Window = Tk()

# Creating some constants
window_Width = 550
window_Height = 700
window_BG = ('#141414')
window_Title = ('Clock')
icon = PhotoImage (file = r"Clock.png")
Screen_Alignment_x = int((Window.winfo_screenwidth()/2)-(window_Width/2))
Screen_Alignment_Y = int((Window.winfo_screenheight()/2)-(window_Height/2))

# Fixing some variables for the digital clock
Clock_Background = ('#000000')
Digital_Clock_Foreground = ('#eb4034')
Digital_Clock_BD = 2
Digital_Clock_Width = 255
Digital_Clock_Height = 50
Digital_Clock_Alignment_x = int((window_Width/2)-((Digital_Clock_Width+4)/2))
Digital_Clock_Alignment_Y = int((window_Height/10)-((Digital_Clock_Height+4)/2))
Digital_Clock_Frame_Height = (3*(Digital_Clock_Height + Digital_Clock_BD))
Digital_Clock_Font = ('Consolas', 22, 'bold')

# Fixing some variables for the analog clock
Analog_Clock_Width = Analog_Clock_Height = 400
Analog_Clock_Alignment_x = int((window_Width/2)-(Analog_Clock_Width/2))
Analog_Clock_Alignment_Y = int(Digital_Clock_Frame_Height+(2*Digital_Clock_Alignment_Y))

# Fixing some variables for clock hands of the analog clock
center_x = center_y = int(Analog_Clock_Width/2)
sec_h_len = 90
sec_h_wth = 1.5
sec_h_col = ('#ff0000')
min_h_len = 80
min_h_wth = 2
min_h_col = ('#00ff00')
hr_h_len = 60
hr_h_wth = 4
hr_h_col = ('#ffffff')

# Create digital clock with date and day
def create_digital_clock(win):

    # Updating time
    def update_time():
        Time = (str(strftime("%I"))+':'+str(strftime("%M"))+':'+str(strftime("%S"))+' '+str(strftime("%p")))
        time.config(text = Time)
        time.after(1, update_time)

    # Updating date
    def update_date():
        Date = (str(dt.date.today().day)+'/'+str(dt.date.today().month)+'/'+str(dt.date.today().year))
        date.config(text = Date)
        date.after(1, update_date)

    # Updating day
    def update_day():
        Day = (str(dt.datetime.now().strftime('%A')))
        day.config(text = Day)
        day.after(1, update_day)

    # Creating a space to place the clock
    C_win = Canvas(win, bg = Clock_Background)
    C_win.place(x = (Digital_Clock_Alignment_x-1), y = (Digital_Clock_Alignment_Y-1), width = (Digital_Clock_Width+6), height = (Digital_Clock_Frame_Height+2))

    frame = Frame(C_win, bg = Clock_Background, bd = Digital_Clock_BD)
    frame.place(x = 1, y = 1, width = (Digital_Clock_Width+4), height = (Digital_Clock_Frame_Height))

    # Space for day
    day = Label(frame, bg = Clock_Background, fg = Digital_Clock_Foreground, font = Digital_Clock_Font, anchor = 'center', justify = 'center')
    day.place(x = 0, y = (0*(Digital_Clock_Height+2)), width = (Digital_Clock_Width-4), height = Digital_Clock_Height)

    # Space for date
    date = Label(frame, bg = Clock_Background, fg = Digital_Clock_Foreground, font = Digital_Clock_Font, anchor = 'center', justify = 'center')
    date.place(x = 0, y = (1*(Digital_Clock_Height+2)), width = (Digital_Clock_Width-4), height = Digital_Clock_Height)

    # Space for time
    time = Label(frame, bg = Clock_Background, fg = Digital_Clock_Foreground, font = Digital_Clock_Font, anchor = 'center', justify = 'center')
    time.place(x = 0, y = (2*(Digital_Clock_Height+2)), width = (Digital_Clock_Width-4), height = Digital_Clock_Height)

    update_time()
    update_date()
    update_day()


# Create analog clock
def create_analog_clock(win):
    # Updating clock
    def update_clock():
        # Getting hours, minutes and seconds
        hours = int(strftime("%I"))
        minutes = int(strftime("%M"))
        seconds = int(strftime("%S"))

        # updating seconds hand
        seconds_x = sec_h_len * sin(radians(seconds * 6)) + center_x
        seconds_y = -1 * sec_h_len * cos(radians(seconds * 6)) + center_y
        clock_space.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

        # updating minutes hand
        minutes_x = min_h_len * sin(radians(minutes * 6)) + center_x
        minutes_y = -1 * min_h_len * cos(radians(minutes * 6)) + center_y
        clock_space.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

        # updating hours hand
        hours_x = hr_h_len * sin(radians(hours * 30)) + center_x
        hours_y = -1 * hr_h_len * cos(radians(hours * 30)) + center_y
        clock_space.coords(hours_hand, center_x, center_y, hours_x, hours_y)

        clock_space.after(1000, update_clock)

    # Creating a space to place the clock
    clock_space = Canvas(win, bg = Clock_Background)
    clock_space.place(x = Analog_Clock_Alignment_x, y = Analog_Clock_Alignment_Y, width = Analog_Clock_Width, height = Analog_Clock_Height)

    # seconds hand
    seconds_hand = clock_space.create_line(center_x, center_y, (200 + sec_h_len), (200 + sec_h_len), width = sec_h_wth, fill = sec_h_col)

    # minutes hand
    minutes_hand = clock_space.create_line(center_x, center_y, (200 + min_h_len), (200 + min_h_len), width = min_h_wth, fill = min_h_col)

    # hours hand
    hours_hand = clock_space.create_line(center_x, center_y, (200 + hr_h_len), (200 + hr_h_len), width = hr_h_wth, fill = hr_h_col)

    update_clock()


# Playing sound every 1 hour
def play_sound():
    from pygame import mixer

    mixer.init()
    Time = int(strftime("%I"))

    for i in range(1, 13):
        if Time  ==  i:
            sound = mixer.Sound("/home/rohit/Desktop/PROJECTS/Clock/Ding.mp3")
            mixer.Sound.play(sound)


# Customizing window
Window.geometry (f"{window_Width}x{window_Height}+{Screen_Alignment_x}+{Screen_Alignment_Y}")
Window.iconphoto (False, icon)
Window.title(window_Title)
Window.resizable(False, False)

# Creating canvas
canvas = Canvas(Window, bg = window_BG)
canvas.place(x = 0, y = 0, width = window_Width, height = window_Height)

# Customizing the main bg
### bg = PhotoImage(file = r'/home/rohit/Desktop/PROJECTS/Clock/Clock_BG.png')
### canvas.create_image((window_Width//2), (window_Height//2), image=bg)

# Calling functions
create_digital_clock(canvas)
create_analog_clock(canvas)
### play_sound()

Window.mainloop()

# The End

