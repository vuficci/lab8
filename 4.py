import random

def generate_doors(num_doors, num_prizes):
    if num_prizes > num_doors:
        raise ValueError("Количество призов не может быть больше количества дверей")
    
    # Генерируем список дверей
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for index in prize_indices:
        doors[index] = "приз"
    return doors

def simulate_game(num_doors, num_prizes):
    # Генерируем двери
    doors = generate_doors(num_doors, num_prizes)
    
    # Игроки делают свой выбор
    player1_choice = random.randint(0, num_doors - 1)
    player2_choice = random.randint(0, num_doors - 1)
    
    # Открываем одну из дверей, за которой нет приза
    available_doors = [i for i in range(num_doors) if i != player1_choice and doors[i] != "приз"]
    if available_doors:
        revealed_door = random.choice(available_doors)
    else:
        return False, False  # Возвращаем флаг, если не осталось доступных дверей для открытия
    
    # Игрок 1 меняет свой выбор
    player1_new_choice = [i for i in range(num_doors) if i != player1_choice and i != revealed_door][0]
    
    # Определяем победителя
    player1_win = doors[player1_new_choice] == "приз"
    player2_win = doors[player2_choice] == "приз"
    
    return player1_win, player2_win

def calculate_win_probabilities(num_doors, num_prizes, num_simulations):
    player1_wins_change = 0
    player2_wins_no_change = 0
    
    for _ in range(num_simulations):
        player1_win, player2_win = simulate_game(num_doors, num_prizes)
        if player1_win:
            player1_wins_change += 1
        if player2_win:
            player2_wins_no_change += 1
    
    probability_change = player1_wins_change / num_simulations
    probability_no_change = player2_wins_no_change / num_simulations
    
    return probability_change, probability_no_change

try:
    num_doors = int(input("Введите количество дверей: "))
    num_prizes = int(input("Введите количество призов: "))
    num_simulations = 10000

    probability_change, probability_no_change = calculate_win_probabilities(num_doors, num_prizes, num_simulations)

    print("Вероятность выигрыша для игрока, меняющего свой выбор:", probability_change)
    print("Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе:", probability_no_change)

except ValueError as e:
    print("Ошибка:", e)