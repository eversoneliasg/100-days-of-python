# Day 18

## Understanding Turtle Graphics and how to use the documentation

Turtle documentation: https://docs.python.org/3/library/turtle.html <br>
Turtle uses tkinter, that is a module responsible for GUI.

## Challenge 1

Drawing a square with our turtle.

## Importing modules

Basic import: `import turtle`<br><br>
With the basic import we would have to create our turtle by typing the module name: `tim = turtle.Turtle()`<br><br>
It is very convenient to import like this: `from turtle import Turtle` > [keyword] + [module name] + [keyword] + [thing in module] <br><br>
As above, we could create our turtle as follows: `tim = Turtle()`<br><br>
We can also import everything from the module by using `from turtle import *` > [keyword] + [module name] + [keyword] + [*]<br><br>
However it can make your code very confusing. From which module does the function come? It is not very common.<br><br>
**Tip**: if you only use the module once or twice, use basic import. 3 or more times, use the more convenient import. <br><br>
**Aliasing modules**: we can give alias to modules: `import turtle as t` > [keyword] + [module name] + [keyword] + [alias name] <br>
Like above, we just need to type: `tim = t.Turtle()`<br><br>
**Installing modules**: some modules have to be installed before use. This way, we can pick only the modules that we need. <br>
PyCharm highlights the module we need to install. It warns us if we need to install it.

## Challenge 2

We are going to draw a dashed line.

## Challenge 3

Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.<br><br>
Each form will have a random color. Each side will have 100 lenght. Each drawing will be inside of each other.<br>

## Challenge 4

Now, we will code a random walk for our turtle. Our turtle will be faster and will draw thicker colored line.<br><br>
The random walk has many applications, as you can see here: https://en.wikipedia.org/wiki/Random_walk <br>

## Python tuples and random RGB colours

Tuples are very similar to lists. While a list would be `my_list = [1, 3, 8]`, a tuple would be `my_tuple = (1, 3, 8)`. <br><br>
The elements inside a tuple can be accessed by their indexes: `my_tuple[0]`.<br><br>
The difference is that I can't change the values inside a tuple. This way, `my_tuple[0] = 12` won't compile.<br><br>
Tuples will give you security about things you don't want to be changed. You can convert a tuple into a list with `list(my_tuple)`.<br><br>
RBG calculator: https://www.w3schools.com/colors/colors_rgb.asp <br><br>
In turtle we can change the color by passing a tuple as RGB (see challenge 4).

## Challenge 5

Our turtle will draw a spirograph.

## Artwork project

For this project, we will use the colorgram.py library. Link: https://pypi.org/project/colorgram.py/ <br><br>
We will replicate a spot painting from the artist Damien Hirst.<br>
Our painting will have 100 dots (10x10) separated by 50 paces and with random colors taken from an original painting.