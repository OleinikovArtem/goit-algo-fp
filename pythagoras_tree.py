# Task 2
import turtle


def draw_tree(t, branch_length, angle, level):
    if level > 0:
        t.forward(branch_length)
        new_length = branch_length * 0.7
        t.left(angle)
        draw_tree(t, new_length, angle, level - 1)
        t.right(2 * angle)
        draw_tree(t, new_length, angle, level - 1)
        t.left(angle)
        t.backward(branch_length)


def main():
    level = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    t.speed(0)

    draw_tree(t, 100, 30, level)

    screen.exitonclick()


if __name__ == "__main__":
    main()
