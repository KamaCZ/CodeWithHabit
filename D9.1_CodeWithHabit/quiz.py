# Quiz 
# Assignment:
# Create a quiz, where there will be 3 questions with the choices a,b,c
# use OOP (object oriented programming)
# in the end the quiz taker gets review with the number of correct and failed answers

from Question import Question

question_prompts = [
    "Which year was Fru Haugans Hotel founded?\n(a) 1794 \n(b) 1974 \n(c) 1995\n",
    "In which city is Fru Haugans Hotel located?\n(a) Sandnessjøen \n(b) Mosjøen \n(c) Brønneysund\n",
    "Where does Fru Haugans Hotel lie in relation to the polar circle? \n(a) south \n(b) north \n(c) on the line\n" 
]

# print(question_prompts[0])
# print(question_prompts[1])
# print(question_prompts[2])


questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"a"),
]


def runquiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print("You answered " + str(score) + " right out of " + str(len(question_prompts)) + "!")   

runquiz(questions)




