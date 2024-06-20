import random

def computer_question():
    questions = [
        "Что происходит?",
        "Почему небо синее?",
        "Как вы думаете, что я думаю?",
        "Какие ваши планы на выходные?",
        "Как вам котики?",
        "Что вы думаете о погоде?",
        "Как прошел ваш день?",
        "Что пообедали?",
        "Как вы относитесь к путешествиям?",
        "Что вас вдохновляет?"
    ]
    return random.choice(questions)

def computer_answer():
    answers = [
        "Мне кажется, я потерял счет времени и пространства!",
        "Чем больше я знаю, тем больше понимаю, что мало знаю.",
        "Вот именно, слишком много вопросов, а ответов так мало!",
        "Я бы ответил, но мой лист бумаги с ответами сломался!",
        "Думаю, моя операционная система заглючила на этом вопросе!",
        "Пожалуй, это один из тех вопросов, на которые надо задавать вечные вопросы!",
        "Кажется, моя квантовая подсистема перегрузилась от этого вопроса!",
        "А вы уверены, что вы хотите знать ответ на этот вопрос?",
        "Вот это поворот! Я бы сам задал такой вопрос!",
        "Я бы ответил, но мне пришло уведомление о важном обновлении!"
    ]
    return random.choice(answers)

def player_question():
    return input("Ваш вопрос: ")

def play():
    computer_score = 0
    player_score = 0
    history = []

    for _ in range(5):
        print("\nХод компьютера:")
        if random.random() <= 0.7:  # 70% вероятность поймать мяч
            print("Компьютер поймал мяч!")
            answer = player_question()
            history.append(("Компьютер", "Вы", answer))
            computer_score += 1
        else:
            print("Компьютер не поймал мяч...")
            question = computer_question()
            print(f"Компьютер задает вопрос: {question}")
            answer = input("Ответ на вопрос компьютера: ")
            history.append(("Компьютер", "Компьютер", question, answer))

        print("\nВаш ход:")
        if random.random() <= 0.7:  # 70% вероятность поймать мяч
            print("Вы поймали мяч!")
            answer = computer_answer()
            print(f"Компьютер отвечает: {answer}")
            history.append(("Вы", "Компьютер", answer))
            player_score += 1
        else:
            print("Вы не поймали мяч...")
            question = player_question()
            answer = input("Ответ на ваш вопрос: ")
            history.append(("Вы", "Вы", question, answer))

    print("\nРезультаты:")
    print(f"Компьютер: {computer_score}")
    print(f"Вы: {player_score}")

    print("\nИстория:")
    for turn in history:
        print("-" * 20)
        for step in turn:
            print(step)

play()