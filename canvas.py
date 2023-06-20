from tkinter import *
from theme import THEME


def create_background(the_canvas, color1=THEME["back_ground_primary"], color2=THEME["back_ground_secondary"]):
    the_canvas.create_rectangle(0, 0, 1000, 600, fill=color1, outline="")
    the_canvas.create_rectangle(10, 10, 990, 590, fill=color2, outline="")
    the_canvas.create_rectangle(20, 20, 980, 580, fill=color1, outline="")
    the_canvas.create_rectangle(30, 30, 970, 570, fill=color2, outline="")
    return the_canvas


def create_pillars(the_canvas):
    # Left pillars
    the_canvas.create_rectangle(40, 40, 80, 560, fill=THEME["pillars"], outline="")
    the_canvas.create_rectangle(100, 40, 140, 560, fill=THEME["pillars"], outline="")
    the_canvas.create_rectangle(160, 40, 200, 560, fill=THEME["pillars"], outline="")
    # Right pillars
    the_canvas.create_rectangle(920, 40, 960, 560, fill=THEME["pillars"], outline="")
    the_canvas.create_rectangle(860, 40, 900, 560, fill=THEME["pillars"], outline="")
    the_canvas.create_rectangle(800, 40, 840, 560, fill=THEME["pillars"], outline="")
    return the_canvas


def create_canvas(window):
    the_canvas = Canvas(window, width=1000, height=600, highlightthickness=0)
    the_canvas.place(x=0, y=0)

    the_canvas = create_background(the_canvas)
    the_canvas = create_pillars(the_canvas)
    start_label = Label(text="FLASHCARDS", font=("fixedsys", 155), bg=THEME["back_ground_secondary"], fg="white", pady=90)
    start_label.place(x=245, y=100)
    return the_canvas


def init_window():
    window = Tk()
    window.configure(bg=THEME["back_ground_secondary"])
    window.resizable(False, False)
    window.geometry("1001x601")
    window.title("Flashcard-App")
    return window
