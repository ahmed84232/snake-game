from turtle import Turtle


class Snake:

    def __init__(self):
        self.snakes: list[Turtle] = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        """Creates the initial three-block snake."""
        for i in range(3):
            snake_block = Turtle(shape="square")
            snake_block.color("yellow")
            snake_block.penup()
            snake_block.goto(x=-i * 20, y=0)  # Start positions (0,0), (-20,0), (-40,0)
            self.snakes.append(snake_block)

    def move_forward(self):
        """Moves the snake forward freely while keeping the body intact."""
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].position())
        self.snakes[0].forward(20)

    def move_backward(self):
        """Moves the snake backward freely while keeping the body intact."""
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].position())
        self.snakes[0].backward(20)

    def turn_left(self):
        """Turns the head left without restrictions."""
        self.snakes[0].left(90)

    def turn_right(self):
        """Turns the head right without restrictions."""
        self.snakes[0].right(90)

    def add_block_to_snake(self):
        """Adds a new block at the tail's position."""
        tail_position = self.snakes[-1].position()
        snake_block = Turtle(shape="square")
        snake_block.color("red")
        snake_block.penup()
        snake_block.goto(tail_position)
        self.snakes.append(snake_block)
