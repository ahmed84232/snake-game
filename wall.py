from turtle import Turtle


class Wall:

    def __init__(self):
        self.right_pos = None
        self.left_pos = None
        self.upper_pos = None
        self.down_pos = None

        self.left_wall()
        self.right_wall()
        self.up_wall()
        self.down_wall()

    def left_wall(self):
        left_block = Turtle()
        left_block.shape("square")
        left_block.color("white")
        left_block.penup()
        left_block.shapesize(stretch_len=0.5, stretch_wid=30)
        left_block.setpos(-300, 0)
        self.left_pos = left_block.pos()


    def right_wall(self):
        right_block = Turtle()
        right_block.shape("square")
        right_block.color("white")
        right_block.penup()
        right_block.shapesize(stretch_len=0.5, stretch_wid=30)
        right_block.setpos(300, 0)
        self.right_pos = right_block.pos()


    def up_wall(self):
        upper_block = Turtle()
        upper_block.shape("square")
        upper_block.color("white")
        upper_block.penup()
        upper_block.shapesize(stretch_len=30, stretch_wid=0.5)
        upper_block.setpos(0, 300)
        self.upper_pos = upper_block.pos()


    def down_wall(self):
        down_block = Turtle()
        down_block.shape("square")
        down_block.color("white")
        down_block.penup()
        down_block.shapesize(stretch_len=30, stretch_wid=0.5)
        down_block.setpos(0, -300)
        self.down_pos = down_block.pos()

