import tkinter.messagebox
from tkinter import *
import math

RED_COLOR = "#E00543"
GREEN_COLOR = "#79D70F"
BACKGROUND_COLOR = "#FDF1DB"
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WORK_MIN = 25
timer = None
reps = 0


def start_timer():
    global reps
    reps += 1
    if reps == 8:
        minute = LONG_BREAK_MIN
    elif reps % 2 == 0:
        tkinter.messagebox.showinfo("Stop Working", "Times to Relax!")
        minute = SHORT_BREAK_MIN
    else:
        tkinter.messagebox.showwarning("Start Working", "Times to Focus!")
        minute = WORK_MIN
    second = minute * 60
    countdown(second, minute)
    start_button["state"] = "disable"


def countdown(count, start_count):
    global arc
    global timer
    global oval
    if count >= 0:
        canvas.delete(arc)
        arc = canvas.create_arc(canvas_middle[0] - radius, canvas_middle[1] - radius, canvas_middle[0] + radius,
                                canvas_middle[1] + radius, start=90, extent=-(360 - 360 / (start_count * 60) * count), outline="")
        canvas.itemconfig(arc, fill=RED_COLOR)
        timer = window.after(1000, countdown, count - 1, start_count)
        minute, second = divmod(count, 60)
        time_label["text"] = f"{'0' if minute < 10 else ''}{minute}:{'0' if second < 10 else ''}{second}"
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "🍅"
        check_marks.config(text=marks, font=("Arial", 15, "bold"), bg=BACKGROUND_COLOR, fg="red")


def reset_timer():
    global timer
    global reps
    reps = 0
    canvas.delete(arc)
    canvas.itemconfig(arc, fill=GREEN_COLOR)
    start_button.config(state="active")
    window.after_cancel(timer)
    time_label.config(text="00:00")
    check_marks.config(text="")


window = Tk()
window.title("Pomodoro Timer")
window["background"] = BACKGROUND_COLOR
window.minsize(width=200, height=200)
window.config(padx=25, pady=25)

canvas = Canvas(window, width=320, height=320, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1)
radius = 130
canvas_middle = [int(canvas['width'])/2, int(canvas['height'])/2]
oval = canvas.create_oval(canvas_middle[0] - radius, canvas_middle[1] - radius, canvas_middle[0] + radius, canvas_middle[1] + radius, outline="")
arc = canvas.create_arc(canvas_middle[0] - radius, canvas_middle[1] - radius, canvas_middle[0] + radius, canvas_middle[1] + radius, start=90, extent=0, fill="", outline="")
canvas.itemconfig(oval, fill=GREEN_COLOR)
canvas.itemconfig(arc, fill=RED_COLOR)

time_label = Label(text="00:00", font=("Arial", 30, "bold"), background=BACKGROUND_COLOR, fg=RED_COLOR)
time_label.grid(column=1, row=0)

check_marks = Label()
check_marks.grid(column=1, row=2)

start_button = Button(text="START", command=start_timer, highlightthickness=0, bg=GREEN_COLOR, fg="black")
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", command=reset_timer, highlightthickness=0, bg=RED_COLOR, fg="white")
reset_button.grid(column=2, row=2)

window.mainloop()