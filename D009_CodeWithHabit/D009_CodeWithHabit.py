
from Question import Question

question_prompts = [
    "\nWhat is the capital of the Czech Republic?\n(a) Bratislava\n(b) Prague\n(c) Warsaw\n",
    "\nWhat is the capital of Indonesia?\n(a) Jakarta\n(b) Denpasar\n(c) Manilla\n",
    "\nWhat is the capital of Norway?\n(a) Stockholm\n(b) Helsinki\n(c) Oslo\n",
]


questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You answered " + str(score) + "/" + str(len(questions)) + " right.")

run_quiz(questions)  
