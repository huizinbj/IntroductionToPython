"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Brett Huizinga.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 5)
blue_turtle.speed = 10  # Fast
blue_size = 300

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 3)
red_turtle.speed = 5  # Slower than blue_turtle
red_size = 150

for k in range(13):
    # Will draw both the circle and square 13 times.
    blue_turtle.draw_square(blue_size)

    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)

    blue_turtle.pen_down()
    blue_size = blue_size - 12

    red_turtle.draw_circle(red_size)

    red_turtle.pen_up()
    red_turtle.left(45)
    red_turtle.backward(10)
    red_turtle.right(45)

    red_turtle.pen_down()
    red_size = red_size - 12

window.close_on_mouse_click()
