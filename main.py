from tkinter import *

LEFT_FRAME_BG = "#F6FFDE"
seconds = 5
countdown_started = False
COLORS = ['#F0F0F0', '#DCDCDC', '#808080', '#303030', '#000000']


def on_key_press(event):
    global seconds
    if countdown_started:
        seconds = 5
    else:
        start_over()


def countdown():
    global seconds
    if seconds > 0:
        counter_label.config(text=f"{seconds} seconds left")
        seconds -= 1
        text.config(foreground=COLORS[seconds])
        if countdown_started:
            tk.after(1000, countdown)
    else:
        counter_label.config(text=f"Message Destroyed")
        text.delete('1.0', END)


def start_over():
    global seconds
    seconds = 5
    counter_label.config(text=f"{seconds} seconds left")
    text.delete('1.0', END)
    text.focus()
    countdown()


# new window
tk = Tk()

# set window title
tk.title("The Dangerous Writing Prompt")

# open in full screen
tk.wm_state('zoomed')

# add padding to window edge
tk.config(padx=50, pady=50)

# add background
tk.config(background="#AAC8A7")

# Calculate the frame width and height based on the window size
window_width = tk.winfo_screenwidth()
window_height = tk.winfo_screenheight()
main_frame_width = int(window_width * 0.8)
main_frame_height = window_height

# create main frame
frame = Frame(tk)
frame.config(width=main_frame_width, height=main_frame_height)
frame.pack()

# Create the left frame
left_frame = Frame(frame, width=0.3 * main_frame_width, height=main_frame_height, bg=LEFT_FRAME_BG)
left_frame.pack(side="left")

# create welcome label
wlc_label = Label(left_frame, text="Welcome to the DWP App", font=("Arial", 20), background=LEFT_FRAME_BG)
wlc_label.pack(padx=30, pady=15)

# create time label
time_label = Label(left_frame, text="Remaining Time", font=("Arial", 20), background=LEFT_FRAME_BG)
time_label.pack(padx=30, pady=15)

# create time label
counter_label = Label(left_frame, text="", font=("Arial", 20), background=LEFT_FRAME_BG)
counter_label.pack(padx=30, pady=15)

# reset button
reset_button = Button(left_frame, text="Start Over", width=13, command=start_over, font=('Arial', 12))
reset_button.pack(padx=30, pady=15)

# Create the right frame
right_frame = Frame(frame, width=0.7 * main_frame_width, height=main_frame_height, bg="#E3F2C1")
right_frame.pack(side="right")

# create textare
text = Text(right_frame, wrap='word', font=('Arial', 15), pady=20, padx=20, background="white")
text.pack(fill='both', expand=False)

text.focus()
text.bind("<Key>", on_key_press)

# Start the countdown
countdown_started = True
countdown()

# keep window open
tk.mainloop()
