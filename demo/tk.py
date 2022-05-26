from tkinter import *
from tkinter import ttk
import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def graph():
    def init():
        pygame.init()
        display = (600, 500)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glClearColor(1.0, 1.0, 1.0, 1.0)
        gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

    def draw():
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        # generate 100 points within -1 to 1 range
        x = np.linspace(-10, 10, 100)
        k = np.linspace(-10, 10, 100)
        d = np.linspace(0.00001, 10, 100)
        c = np.log(d)
        y = np.power(x, 2)
        m = x
        q = np.power(x, 3)
        l = np.sin(k)
        glBegin(GL_LINE_STRIP)
        # for every pair (a, b) of the numbers in x, y
        for a, b in zip(x, y):
            # give (a, b) to OpenGL to draw
            glVertex2f(a, b)
        glEnd()
        glFlush()
        glBegin(GL_LINE_STRIP)
        # for every pair (a, b) of the numbers in x, y
        for a, b in zip(x, m):
            # give (a, b) to OpenGL to draw
            glVertex2f(a, b)
        glEnd()
        glFlush()
        glBegin(GL_LINE_STRIP)
        # for every pair (a, b) of the numbers in x, y
        for a, b in zip(x, q):
            # give (a, b) to OpenGL to draw
            glVertex2f(a, b)
        glEnd()
        glFlush()
        glBegin(GL_LINE_STRIP)
        # for every pair (a, b) of the numbers in x, y
        for a, b in zip(k, l):
            # give (a, b) to OpenGL to draw
            glVertex2f(a, b)
        glEnd()
        glFlush()
        glBegin(GL_LINE_STRIP)
        glColor3f(1.0, 1.0, 0.0)
        for a, b in zip(d, c):
            # give (a, b) to OpenGL to draw
            glVertex2f(a, b)
        glEnd()
        glFlush()
        glBegin(GL_LINE_STRIP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, -10.0)
        glEnd()
        glFlush()
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 0.0)
        glVertex2f(-10.0, 0.0)
        glEnd()
        glFlush()

    def main():
        init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return pygame.quit()


            draw()
            pygame.display.flip()
            pygame.time.wait(10)

    main()


def tk():
    win = Tk()
    win.geometry("800x500")
    # Add an optional Label widget
    Label(win, text="Welcome Choose a Graph to draw", font='Aerial 17 bold italic').pack(pady=10)
    # Create a Button to display the message
    ttk.Button(win, text="Y=Sin(x)", command=graph).pack(pady=10)
    ttk.Button(win, text="Y=x", command=graph).pack(pady=10)
    ttk.Button(win, text="Y=log(x)", command=graph).pack(pady=10)
    ttk.Button(win, text="Y=X^2", command=graph).pack(pady=10)
    ttk.Button(win, text="Y=x^3", command=graph).pack(pady=10)
    ttk.Button(win, text="Y=tan(x)", command=graph).pack(pady=10)
    win.mainloop()


tk()
