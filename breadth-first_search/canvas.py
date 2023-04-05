from tkinter import *
import random
import math
RADIUS = 20
HEIGTH = 600
WIDTH = 600


def circle(canvas: Canvas, x, y, r, text=""):
    id = canvas.create_oval(x-r, y-r, x+r, y+r)
    canvas.create_text(x, y, text=text)
    return id


def plot_graph(graph: dict = {}):
    master = Tk()
    canvas_width = WIDTH
    canvas_height = HEIGTH
    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.pack()
    if graph:
        plotted = ["you"]
        plotted_c = [(300, 300)]
        starting_point = "you"
        while True:
            starting_point = random.choice(plotted)
            parent_x = plotted_c[plotted.index(starting_point)][0]
            parent_y = plotted_c[plotted.index(starting_point)][1]
            circle(w, parent_x, parent_y, RADIUS, text=starting_point)
            children = graph[starting_point]

            for index, child in enumerate(children):
                if child not in plotted:
                    angle = random.random()*math.pi*2
                    child_x = math.cos(angle) * 120 + parent_x
                    child_y = math.sin(angle) * 120 + parent_y
                    plotted_c.append((child_x, child_y))
                    plotted.append(child)
                    circle(w, child_x, child_y, RADIUS, text=child)
                    w.create_line(parent_x, parent_y, child_x, child_y, arrow=LAST)
            if len(plotted) >= 8:
                break    

    w.mainloop()


if __name__ == "__main__":
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    plot_graph(graph)
