import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np


def rotationMatrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)],
    ])

    return mat


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, -10.0)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(-10.0, 0.0)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v1 = np.array([-0.4, 0])
    po1 = np.array([0.2, -0.2])
    t1 = 1
    p1 = po1 + (t1 * v1)
    mat = rotationMatrix(30)
    for a in zip(po1, p1):
        glVertex2fv(np.dot(mat, a))
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v2 = np.array([0.4, 0])
    po2 = np.array([-0.2, 0.2])
    t2 = 1
    p2 = po2 + (t2 * v2)
    mat = rotationMatrix(30)
    for a in zip(po2, p2):
        glVertex2fv(np.dot(mat, a))
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v3 = np.array([0, -0.4])
    po3 = np.array([0.2, 0.2])
    t3 = 1
    p3 = po3 + (t3 * v3)
    mat = rotationMatrix(30)
    for a in zip(po3, p3):
        glVertex2fv(np.dot(mat, a))
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v4 = np.array([0, 0.4])
    po4 = np.array([-0.2, -0.2])
    t4 = 1
    p4 = po4 + (t4 * v4)
    mat = rotationMatrix(30)
    for a in zip(po4, p4):
        glVertex2fv(np.dot(mat, a))
    glEnd()
    glFlush()

def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            draw()
            pygame.display.flip()
            pygame.time.wait(10)


main()