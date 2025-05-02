import random
import json
import time

def save_statistics(statistics, filename='statistics.json'):
    with open(filename, 'a') as file:
        json.dump(statistics, file)
        file.write('\n')  # Перенос строки для разделения записей

def play_game():
    number_to_guess = random.randint(1, 100)  # Загадываем число от 1 до 100
    attempts = 0
    start_time = time.time()

    while True:
        attempts += 1
        guess = int(input("Угадай число от 1 до 100: "))

        if guess < number_to_guess:
            print("Загаданное число больше.")
        elif guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            end_time = time.time()
            time_taken = end_time - start_time
            result = "Победа"
            print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток.")
            print(f"Время игры: {time_taken:.2f} секунд.")

            statistics = {
                "attempts": attempts,
                "time_taken": time_taken,
                "result": result
            }

            save_statistics(statistics)
            break

if __name__ == '__main__':
    play_game()
