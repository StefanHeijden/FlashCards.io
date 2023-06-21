import json
import random

JSON_FILE = "Questions_And_Answers.json"


class FlashCard:
    def __init__(self, question):
        self.question = question["question"]
        self.answer = question["answer"]
        self.source = question["source"]
        self.subject = question["subject"]
        self.themes = question["themes"]
        self.seen = question["seen"]
        self.side_up = "Q"


def generate_next_random_flashcard(flashcard_list):
    flashcard_list.append(
        pick_random_flash_card(
            get_least_seen_flash_cards(flashcard_list)
        )
    )


def generate_next_random_from_source(flashcard: FlashCard, flashcard_list):
    new_flashcard = pick_random_flash_card(
        get_least_seen_flash_cards(
            get_flash_cards_with_source(flashcard.subject, flashcard_list)
        )
    )
    if new_flashcard is None:
        pick_random_flash_card(
            get_least_seen_flash_cards(
                get_flash_cards_with_source(flashcard.source, flashcard_list)
            )
        )
    if new_flashcard is None:
        generate_next_random_flashcard(flashcard_list)
    else:
        flashcard_list.append(new_flashcard)


def generate_next_random_from_theme(flashcard: FlashCard, flashcard_list):
    themes = flashcard.themes
    random.shuffle(themes)
    new_flashcard = None
    for theme in themes:
        if new_flashcard is not None:
            new_flashcard = pick_random_flash_card(
                get_least_seen_flash_cards(
                    get_flash_cards_with_theme(theme, flashcard_list)
                )
            )
    if flashcard is None:
        generate_next_random_flashcard(flashcard_list)
    else:
        flashcard_list.append(flashcard)


def get_flashcards():
    the_file = open(JSON_FILE, "r")
    questions_as_json = json.load(the_file)

    flashcard_list = list()
    for question in questions_as_json:
        flashcard_list.append(FlashCard(question))
    return flashcard_list


def get_flash_cards_with_subject(subject, flashcards):
    new_flashcards = []
    for flashcard in flashcards:
        if flashcard["subject"] == subject:
            new_flashcards.append(flashcard)
    return new_flashcards


def get_flash_cards_with_source(source, flashcards):
    new_flashcards = []
    for flashcard in flashcards:
        if flashcard.source == source:
            new_flashcards.append(flashcard)
    return new_flashcards


def get_flash_cards_with_theme(theme, flashcards):
    new_flashcards = []
    for flashcard in flashcards:
        for flashcard_theme in flashcards["themes"]:
            if flashcard_theme == theme:
                new_flashcards.append(flashcard)
                break
    return new_flashcards


def get_least_seen_flash_cards(flashcards):
    minimum_seen = 10000
    for flashcard in flashcards:
        if flashcard.seen < minimum_seen:
            minimum_seen = flashcard.seen  # TODO Rewrite!!!

    new_flashcards = []
    for flashcard in flashcards:
        if flashcard.seen <= minimum_seen:
            new_flashcards.append(flashcard)
    return new_flashcards


def pick_random_flash_card(flashcards):
    rnd = random.randint(0, len(flashcards) - 1)
    if len(flashcards) > 0:
        flashcards[rnd].seen = flashcards[rnd].seen + 1
        return flashcards[rnd]
    return None
