# importing the module
import turtle
import time
import random

# setting up a screen
app = turtle.Screen()
app.setup(width=1000, height=600)
app.bgcolor("green")
app.title("Saw That Snake!")
app.cv._rootwindow.resizable(False, False)
app.tracer(0)
# the path needs to be changed to your path otherwise it wont work
image = "C:/Users/your path here/buzzsaw.gif"
app.addshape(image)
# objects
# saw
saw = turtle.Turtle()
saw.shape(image)
saw.penup()
saw.speed(0)
saw.goto(0, 250)
sawspeed = 20

saw2 = turtle.Turtle()
saw2.shape(image)
saw2.penup()
saw2.speed(0)
saw2.goto(0, 125)
saw2speed = 20

saw3 = turtle.Turtle()
saw3.shape(image)
saw3.penup()
saw3.speed(0)
saw3.goto(0, 0)
saw3speed = 20

saw4 = turtle.Turtle()
saw4.shape(image)
saw4.penup()
saw4.speed(0)
saw4.goto(0, -125)
saw4speed = 20

saw5 = turtle.Turtle()
saw5.shape(image)
saw5.penup()
saw5.speed(0)
saw5.goto(0, -250)
saw5speed = 20

saw.left(20)
saw.heading()
saw2.left(20)
saw3.left(20)
saw4.left(20)
saw5.left(20)

# score
score = 0
highscore = 0
# head
snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.color("gold")
snakehead.shape("circle")
snakehead.penup()
snakehead.goto(0, 25)
snakehead.direction = "stop"
# food(berry)
food = turtle.Turtle()
food.speed(0)
food.color("#4f86f7")
food.shape("circle")
food.penup()
food.goto(0, 100)
food.left(15)
# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.shape("square")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Highscore: 0", align="center", font=("Terminal", 25))
# functions and variables
segments = []
delay = 0.1


def go_up():
    if snakehead.direction != "down":
        snakehead.direction = "up"


def go_down():
    if snakehead.direction != "up":
        snakehead.direction = "down"


def go_left():
    if snakehead.direction != "right":
        snakehead.direction = "left"


def go_right():
    if snakehead.direction != "left":
        snakehead.direction = "right"


def snake_motivation():
    if snakehead.direction == "up":
        y = snakehead.ycor()
        snakehead.sety(y + 20)
    if snakehead.direction == "down":
        y = snakehead.ycor()
        snakehead.sety(y - 20)
    if snakehead.direction == "left":
        x = snakehead.xcor()
        snakehead.setx(x - 20)
    if snakehead.direction == "right":
        x = snakehead.xcor()
        snakehead.setx(x + 20)


# keyboard bindings
app.listen()
app.onkeypress(go_up, "w")
app.onkeypress(go_down, "s")
app.onkeypress(go_left, "a")
app.onkeypress(go_right, "d")


# main game loop
while 1:
    app.update()

    # buzzsaw moving
    x = saw.xcor()
    x += sawspeed
    saw.setx(x)
    # saw check
    if saw.xcor() > 490:
        sawspeed *= -1
    if saw.xcor() < -490:
        sawspeed *= -1

    # buzzsaw moving
    x2 = saw2.xcor()
    x2 += saw2speed
    saw2.setx(x2)
    # saw check
    if saw2.xcor() > 490:
        saw2speed *= -1
    if saw2.xcor() < -490:
        saw2speed *= -1

    # buzzsaw moving
    x3 = saw3.xcor()
    x3 += saw3speed
    saw3.setx(x3)
    # saw check
    if saw3.xcor() > 490:
        saw3speed *= -1
    if saw3.xcor() < -490:
        saw3speed *= -1

    # buzzsaw moving
    x4 = saw4.xcor()
    x4 += saw4speed
    saw4.setx(x4)
    # saw check
    if saw4.xcor() > 490:
        saw4speed *= -1
    if saw4.xcor() < -490:
        saw4speed *= -1

    # buzzsaw moving
    x5 = saw5.xcor()
    x5 += saw5speed
    saw5.setx(x5)
    # saw check
    if saw5.xcor() > 490:
        saw5speed *= -1
    if saw5.xcor() < -490:
        saw5speed *= -1

    if (snakehead.ycor() < 250 + 40) and (snakehead.ycor() > 250 - 40) and (snakehead.xcor() < saw.xcor()+40) and (snakehead.xcor() > saw.xcor()-40):
        time.sleep(1)
        snakehead.goto(0, 50)
        snakehead.direction = "stop"
        # reset the score
        score = 0
        pen.clear()
        pen.write("Score:{}  Highscore:{}".format(score, highscore),
                  align="center", font=("Terminal", 25))
        # segment fixing
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments
        segments.clear()

    if (snakehead.ycor() < 125 + 40) and (snakehead.ycor() > 125 - 40) and (snakehead.xcor() < saw2.xcor()+40) and (snakehead.xcor() > saw2.xcor()-40):
        time.sleep(1)
        snakehead.goto(0, 50)
        snakehead.direction = "stop"
        # reset the score
        score = 0
        pen.clear()
        pen.write("Score:{}  Highscore:{}".format(score, highscore),
                  align="center", font=("Terminal", 25))
        # segment fixing
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments
        segments.clear()

    if (snakehead.ycor() < 0 + 40) and (snakehead.ycor() > 0 - 40) and (snakehead.xcor() < saw3.xcor()+45) and (snakehead.xcor() > saw3.xcor()-45):
        time.sleep(1)
        snakehead.goto(0, 50)
        snakehead.direction = "stop"
        # reset the score
        score = 0
        pen.clear()
        pen.write("Score:{}  Highscore:{}".format(score, highscore),
                  align="center", font=("Terminal", 25))
        # segment fixing
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments
        segments.clear()

    if (snakehead.ycor() < -125 + 40) and (snakehead.ycor() > -125 - 40) and (snakehead.xcor() < saw4.xcor()+40) and (snakehead.xcor() > saw4.xcor()-40):
        time.sleep(1)
        snakehead.goto(0, 50)
        snakehead.direction = "stop"
        # reset the score
        score = 0
        pen.clear()
        pen.write("Score:{}  Highscore:{}".format(score, highscore),
                  align="center", font=("Terminal", 25))
        # segment fixing
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments
        segments.clear()

    if (snakehead.ycor() < -250 + 40) and (snakehead.ycor() > -250 - 40) and (snakehead.xcor() < saw5.xcor()+42) and (snakehead.xcor() > saw5.xcor()-42):
        time.sleep(1)
        snakehead.goto(0, 50)
        snakehead.direction = "stop"
        # reset the score
        score = 0
        pen.clear()
        pen.write("Score:{}  Highscore:{}".format(score, highscore),
                  align="center", font=("Terminal", 25))
        # segment fixing
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments
        segments.clear()

    # border collision checking
    if snakehead.xcor() > 490 or snakehead.xcor() < -490 or snakehead.ycor() > 290 or snakehead.ycor() < -290:
        time.sleep(1)
        snakehead.goto(0, 50)
        snakehead.direction = "stop"
        # reset the score
        score = 0
        pen.clear()
        pen.write("Score:{}  Highscore:{}".format(score, highscore),
                  align="center", font=("Terminal", 25))
        # segment fixing
        for segment in segments:
            segment.goto(1000, 1000)
        # clear the segments
        segments.clear()
        # food collision checking
    if snakehead.distance(food) < 20:
        # move the food to random spots
        x = random.randrange(-290, 290)
        y = random.randrange(-290, 290)
        food.goto(x, y)
        # randomly rotating the food===
        rotation = random.randint(0, 360)
        food.left(rotation)
        # add snake segments============
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        # increase the score
        score += 10
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write("Score:{}  Highscore:{}".format(score, highscore),
                  align="center", font=("Terminal", 25))
        # move end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # move segment 0 to where the head is
    if len(segments) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        segments[0].goto(x, y)
    snake_motivation()
    # checking body collision with head
    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0, 50)
            snakehead.direction = "stop"
            # segment fixing
            for segment in segments:
                segment.goto(1000, 1000)
            # clear the segments
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score:{}  Highscore:{}".format(score, highscore),
                      align="center", font=("Terminal", 25))

    time.sleep(delay)

app.mainloop()
