#!/usr/bin/env python3
# Draws a fractal that exhibits the property of self-similarity
# Makhtar Diouf
# $Id$
# Ref: http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsSierpinskiTriangle.html
import turtle

def drawTriangle(points, color, turt):
    turt.fillcolor(color)
    turt.up()
    turt.goto(points[0][0], points[0][1])
    turt.down()
    turt.begin_fill()
    turt.goto(points[1][0], points[1][1])
    turt.goto(points[2][0], points[2][1])
    turt.goto(points[0][0], points[0][1])
    turt.end_fill()

def getMid(p1, p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, turt):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 
                'violet', 'orange']

    drawTriangle(points, colormap[degree], turt)

    if degree > 0:
        sierpinski([points[0], 
                        getMid(points[0], points[1]), 
                        getMid(points[0], points[2])], 
                   degree-1, turt)

        sierpinski([points[1], 
                        getMid(points[0], points[1]), 
                        getMid(points[1], points[2])], 
                   degree-1, turt)

        sierpinski([points[2],
                        getMid(points[2], points[1]), 
                        getMid(points[0], points[2])], 
                   degree-1, turt)

def main():
   turt = turtle.Turtle()
   turt.set_title("Sierpinski triangle")
   myWin = turtle.Screen()
   points = [[-100, -50], [0, 100], [100, -50]]
   sierpinski(points, 3, turt)
   myWin.exitonclick()

main()
