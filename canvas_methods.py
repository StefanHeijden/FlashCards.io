from stats import STATS
from flashcards import generate_next_random_flashcard, generate_next_random_from_source, generate_next_random_from_theme


def flip(flashcard_list, the_canvas):
    the_canvas.delete("all")
    current_on_screen = flashcard_list[STATS["index"]]
    if current_on_screen.side_up == "Q":
        the_canvas.create_text(270, 170, width=530, font="Times 20 italic bold", text=current_on_screen.answer)
        current_on_screen.side_up = "A"
    else:
        the_canvas.create_text(270, 170, width=530, font="Times 20 italic bold", text=current_on_screen.question)
        current_on_screen.side_up = "Q"


def put_card_on_the_screen(flashcard_list, the_canvas):
    the_canvas.delete("all")
    next_card_on_screen = flashcard_list[STATS["index"]]
    the_canvas.create_text(270, 170, width=530, font="Times 20 italic bold", text=next_card_on_screen.question)
    next_card_on_screen.side_up = "Q"


def next_card(flashcard_list, the_canvas):
    STATS["index"] = STATS["index"] + 1
    if STATS["index"] >= len(flashcard_list):
        generate_next_random_flashcard(flashcard_list)
    put_card_on_the_screen(flashcard_list, the_canvas)


def next_card_from_subject(flashcard_list, the_canvas):
    STATS["index"] = STATS["index"] + 1
    if STATS["index"] >= len(flashcard_list):
        generate_next_random_from_source(flashcard_list[STATS["index"] - 1], flashcard_list)
    put_card_on_the_screen(flashcard_list, the_canvas)


def next_card_from_theme(flashcard_list, the_canvas):
    STATS["index"] = STATS["index"] + 1
    if STATS["index"] >= len(flashcard_list):
        generate_next_random_from_theme(flashcard_list[STATS["index"] - 1], flashcard_list)
    put_card_on_the_screen(flashcard_list, the_canvas)


def prev_card(flashcard_list, the_canvas):
    if STATS["index"] >= 0:
        STATS["index"] = STATS["index"] - 1
        put_card_on_the_screen(flashcard_list, the_canvas)
