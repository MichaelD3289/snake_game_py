from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

blocks = []

for position in starting_positions:
    block = Turtle(shape="square")
    block.color("white")
    block.penup()
    block.goto(position)
    blocks.append(block)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for block_num in range(len(blocks) - 1, 0, -1):
        new_x = blocks[block_num - 1].xcor()
        new_y = blocks[block_num - 1].ycor()
        blocks[block_num].goto(new_x, new_y)

    blocks[0].forward(20)


screen.exitonclick()
# if __name__ == '__main__':
#     main()


