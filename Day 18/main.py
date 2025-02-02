# import colorgram

# colors = colorgram.extract('image.jpg', 20)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)

tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
tim.speed("fastest")


color_list = [(202, 172, 108), (240, 246, 244), (153, 181, 196), (192, 161, 177), (152, 186, 174), (214, 204, 114), (207, 179, 197), (163, 202, 213), (175, 188, 212), (160, 213, 187), (114, 122, 185), (214, 181, 180), (186, 157, 62), (198, 205, 49)]

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()