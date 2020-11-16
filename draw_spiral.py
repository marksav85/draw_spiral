# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:18:31 2020

@author: marks
"""
import turtle

def shape_square(ninja_turtle):
    for i in range(1,5):
        ninja_turtle.forward(100)
        ninja_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    #Create turtle Raph - Draws a square
    raph = turtle.Turtle()
    raph.shape("turtle")
    raph.color("yellow")
    raph.speed()
    for i in range(1,37):
        draw_square(raph)
        raph.right(10)
