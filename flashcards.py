import json

JSON_FILE = "Questions_And_Answers.json"


class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.side_up = "Q"


def generate_new_question(flashcard_list, the_canvas, index_of_card):
    flashcard_list.append(flashcard_list[index_of_card])


def get_flashcards():
    the_file = open(JSON_FILE, "r")
    questions_as_json = json.load(the_file)

    flashcard_list = list()
    for question in questions_as_json:
        flashcard_list.append(FlashCard(question["question"], question["subject"]))
    return flashcard_list
