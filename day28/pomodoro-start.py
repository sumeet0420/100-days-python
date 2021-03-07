from tkinter import *

YELLOW = "#f7f5dd"
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=YELLOW, highlightthickness=0)
timer_label = Label(text="Timer", font=("Courier", 24, "bold"))
timer_label.grid(column=1, row=0)
canvas = Canvas(width=400, height=400, bg=YELLOW)
tomato_img = PhotoImage(file="pomodoro.png")
canvas.create_image(200, 200, image=tomato_img)

count_down_is = False
## Countdown
def count_down(count):
    if count >= 0 and count_down_is:
        window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")


def start_time():
    global count_down_is
    if count_down_is:
        count_down(120)
        count_down_is = False

def reset_time():
    canvas.itemconfig(timer_text, text=f"00:00")

## Creating object to change the timer text
timer_text = canvas.create_text(200, 200, text="00:00", fill="black", font=("Courier", 35, "bold"), )
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=("Courier", 14), command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Courier", 14), command=reset_time)
reset_button.grid(column=2, row=2)

window.mainloop()
