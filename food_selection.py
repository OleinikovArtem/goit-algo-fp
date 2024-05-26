# task 6

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    selected_items = []
    for item, values in sorted_items:
        if total_cost + values['cost'] <= budget:
            selected_items.append(item)
            total_cost += values['cost']
    return selected_items


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_list = list(items.items())

    for i in range(1, n + 1):
        name, values = item_list[i - 1]
        for w in range(budget + 1):
            if values['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - values['cost']] + values['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    res = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            res.append(item_list[i - 1][0])
            w -= item_list[i - 1][1]['cost']
    return res


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    # Виклик жадібного алгоритму
    greedy_result = greedy_algorithm(items, budget)
    print("Жадібний алгоритм: ", greedy_result)

    # Виклик алгоритму динамічного програмування
    dp_result = dynamic_programming(items, budget)
    print("Динамічне програмування: ", dp_result)
