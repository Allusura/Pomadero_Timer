from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_Label.config(text="Timer", bg=PINK, fg=GREEN, font=(FONT_NAME, 50))
    check_mark.config(text="✔", bg=PINK, fg=GREEN, font=(FONT_NAME, 10, "bold"))
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_Label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_Label.config(text="Break", fg=YELLOW)
        count_down(short_break_sec)
    else:
        timer_Label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Minutes + Seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        # Dynamic Typing + Formatting
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for n in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Window specifications. Title = Pomodoro | Spacing (Padding) = 100pixels, 50pixels
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

# Canvas specifications. 200x224, Pink, 0 highlightthickness (to fix border issue)
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
# Initializing "tomato_img" as the tomato.png
tomato_img = PhotoImage(file="tomato.png")
# Size of the image in the window
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
# Location of the image
canvas.grid(column=1, row=1)

# Timer label
timer_Label = Label(text="Timer", bg=PINK, fg=GREEN, font=(FONT_NAME, 50))
timer_Label.grid(column=1, row=0)
timer_Label.config(pady=20, padx=20)

# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
start_button.config(pady=0, padx=0)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
reset_button.config(pady=0, padx=0)

# Tick mark Label
check_mark = Label(bg=PINK, fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_mark.grid(column=1, row=3)

# Keeps the window open until closed
window.mainloop() 
