from turtle import *

speed(100)
setup(height=1000,width=1400)
bgcolor("#00b5e2")
penup()
goto(-8000,150)
pendown()
color("red")
begin_fill()
forward(1400)
right(90)
forward(290)
right(90)
forward(1400)
right(90)
forward(290)
end_fill()
left(180)
forward(290)
color("#509e2f")
begin_fill()
forward(260)
left(90)
forward(1400)
left(90)
forward(260)
end_fill()
penup()
goto(0,0)
pendown()
color("white")
begin_fill()
circle(135)
end_fill()
color("red")
right(90)
forward(15)
left(90)
begin_fill()
circle(120)
end_fill()
color("white")
penup()
goto(60,60)
pendown()
left(15)
begin_fill()
round=0

while round<8:
    left(135)
    forward(140)
    round += 1
end_fill()
hideturtle()
done()