from turtle import Turtle, Screen, textinput
from random import choice
from enum import Enum


class Color(Enum):
    GREEN = "green"
    RED = "red"
    BLUE = "blue"
    BLACK = "black"
    BROWN = "brown"


class TurtleRacer(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color_name = color.name
        self.shape("turtle")
        self.color(color.value)
        self.penup()
        self.setpos(-230, -170 + position * 80)


def move_turtle(turtle):
    turtle.speed("slowest")
    speeds = [5, 10, 15, 20, 25]
    turtle.forward(choice(speeds))


def get_user_bet():
    bet = textinput(title="Who will win", prompt="Set a bet on who will win (red/green/blue/black/brown): ").lower()
    while bet not in {color.value for color in Color}:
        print("Invalid bet. Please choose a valid color.")
        bet = textinput(title="Who will win", prompt="Set a bet on who will win (red/green/blue/black/brown): ").lower()
    return bet


def race_turtles(turtles):
    for _ in range(27):
        for turtle in turtles:
            move_turtle(turtle)


def determine_winner(turtles):
    distances = [(turtle.color_name, turtle.xcor()) for turtle in turtles]
    distances.sort(key=lambda x: x[1], reverse=True)
    max_distance = distances[0][1]
    winners = [distance for distance in distances if distance[1] == max_distance]
    return winners


def display_results(winners, user_bet):
    print(f"Winner: {winners}")
    if any(winner[0] == user_bet for winner in winners):
        print("Congratulations! You won.")
    else:
        print("Sorry, you lost.")
        for distance in winners:
            if distance[0] == user_bet:
                print(f"You bet on {user_bet} and it finished at {distance[1]:.2f}.")


def main():
    user_bet = get_user_bet()
    turtles = [TurtleRacer(color, position) for position, color in enumerate(Color)]
    race_turtles(turtles)
    winners = determine_winner(turtles)
    display_results(winners, user_bet)
    screen.exitonclick()


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("Turtle Race")
    main()

## startong version :

# from turtle import Turtle, Screen, textinput
# import random
#
# screen = Screen()
# screen.setup(width=500, height=400)
# screen.title("Turtle Race")
#
#
# def gas(x):
#     x.speed("slowest")
#     y = [5, 10, 15, 20, 25]
#     x.forward(random.choice(y))
#
#
# def shape_color(x, y):
#     x.shape("turtle")
#     x.color(str(y))
#     x.penup()
#     return y
#
#
# def set_positions(x, y):
#     x.setpos(-230, -170 + y * 80)
#
#
# ku = Turtle()
# shape_color(ku, "green")
# ku.setpos(-230, -170)
# ku1 = Turtle()
# shape_color(ku1, "red")
# set_positions(ku1, 1)
# ku2 = Turtle()
# shape_color(ku2, "blue")
# set_positions(ku2, 2)
# ku3 = Turtle()
# shape_color(ku3, "black")
# set_positions(ku3, 3)
# ku4 = Turtle()
# shape_color(ku4, "brown")
# set_positions(ku4, 4)
# bet = textinput(title="who will win", prompt="set a bet who will win(red/green/blue/black/brown): ")
#
# race_list = [ku, ku1, ku2, ku3, ku4]
# for _ in range(27):
#     for x in race_list:
#         gas(x)
#
# finish_list = [ku, ku1, ku2, ku3, ku4]
# final_distances = []
# for x in finish_list:
#     final_distances.append((x.color()[0], x.xcor()))
#
# final_distances.sort(key=lambda x: x[1], reverse=True)
# max_distance = final_distances[0][1]
# winners = [final_distances[0]]
# for x in final_distances:
#     if x[1] == winners[0][1] and x[0] != winners[0][0]:
#         winners.append(x)
#
#
# def winner_is():
#     print(f"Winner: {winners}")
#     for x in winners:
#         if x[0] == bet:
#             print("You won")
#
#         else:
#             print("you lost")
#             for y in final_distances:
#                 if y[0] == bet:
#                     print(y)
#
#
# winner_is()
# screen.exitonclick()
