from tkinter import *
from theme import THEME
from canvas import init_window, create_canvas
from flashcards import get_flashcards
from canvas_methods import next_card, flip, prev_card
import random


def start_game(flashcard_list, the_canvas):
    random.shuffle(flashcard_list)

    the_canvas.create_text(270, 170, width=530, font="Times 20 italic bold", text=flashcard_list[0].question)
    the_canvas.configure(bg="white")
    the_canvas.place(x=225, y=60)

    flip_button = Button(text="Flip Card", font=("fixedsys", 30),
                         command=lambda: flip(flashcard_list, the_canvas), bg=THEME["button"], fg="white")
    flip_button.pack(side=BOTTOM, pady=40)
    next_button = Button(text="Next", font=("fixedsys", 30),
                         command=lambda: next_card(flashcard_list, the_canvas), bg=THEME["button"], fg="white")
    next_button.place(x=640, y=491)
    prev_button = Button(text="Prev", font=("fixedsys", 30),
                         command=lambda: prev_card(flashcard_list, the_canvas), bg=THEME["button"], fg="white")
    prev_button.place(x=250, y=491)


window = init_window()
the_canvas = create_canvas(window)
flashcards = get_flashcards()

start_game(flashcards, Canvas(window, width=550, height=370, highlightthickness=0))
window.mainloop()
