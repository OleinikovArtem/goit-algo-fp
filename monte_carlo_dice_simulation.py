# Task 7

import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo_simulation(rolls):
    results = [roll_dice() for _ in range(rolls)]
    probabilities = {i: results.count(i) / rolls for i in range(2, 13)}
    return probabilities


def main():
    rolls = 100000
    probabilities = monte_carlo_simulation(rolls)

    print("Ймовірності сум при киданні двох кубиків:")
    for sum_value, probability in probabilities.items():
        print(f"Сума {sum_value}: {probability:.2%}")

    # Створення графіка
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (метод Монте-Карло)')
    plt.show()


if __name__ == "__main__":
    main()
