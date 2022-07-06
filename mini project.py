questions=[
    'Who is the developer of python language?',
    'When did India get Independence?',
    'What is the currency in India?',
    'Which State does Bangalore belong to?',
    "Which is the latest iphone?",
    ]

answers =[
    'Guido van',
    '1947',
    'INR',
    'Karnataka',
    'iphone 12'
]


options=[
    ['Dennis Ritchi','Alan Frank','Guido van','Albert'],
    ['1947','1995','2000','1958'],
    ['pounds','dollars','euros','INR'],
    ['karnataka','westbengal','assam','rajasthan'],
    ['iphone SE','iphone 13','iphone 11','iphone 12'],
]

def play_game(username,questions,answers,options):
    print("Hello",username,"to the Quiz game")
    score = 0
    for i in range(len(questions)):
        current_question=questions[i]
        correct_answer=answers[i]
        current_question_options=options[i]
        print("Question:",current_question)
        for index,each_option in enumerate(current_question_options):
            print(index+1,")",each_option, sep='')
        user_answer_index=int(input("enter your choice(1,2,3 or 4):"))
        user_answer=current_question_options[user_answer_index-1]
        if user_answer == correct_answer:
            print("correct Answer")
            score = score + 100
        else:
            print("wrong Answer")
            break

    print("your final score is",score)
    return username, score


def view_scores(names_and_scores):
    for name,score in names_and_scores.items():
        print(name, "has scored",score)


def Quiz(questions,answers,options):
    names_and_scores ={}
    while True:
        print("Welcome to Quiz game!")
        print("1)play Game\n2) view score\n3) exit")
        choice = int(input("please enter your choice:"))
        if choice == 1:
            username= input("please enter your name:")
            username,score=play_game(username, questions, answers, options)
            names_and_scores[username]=score

        elif choice == 2:
            view_scores()
        elif choice == 3:
            break
        else:
            print("your choice is not valid")

Quiz(questions,answers,options)