import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

initial_point = (0, 0, 0)
vertices_of_cube = (
    np.add(initial_point, 1 * (0.5, -0.5, -0.5)),
    np.add(initial_point, 1 * (0.5, 0.5, -0.5)),
    np.add(initial_point, 1 * (-0.5, 0.5, -0.5)),
    np.add(initial_point, 1 * (-0.5, -0.5, -0.5)),
    np.add(initial_point, 1 * (0.5, -0.5, 0.5)),
    np.add(initial_point, 1 * (0.5, 0.5, 0.5)),
    np.add(initial_point, 1 * (-0.5, -0.5, 0.5)),
    np.add(initial_point, 1 * (-0.5, 0.5, 0.5)),
)

edges_of_cube = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def draw_cube():
    glBegin(GL_LINES)
    glColor3f(1, 1, 0.0)
    for edge in edges_of_cube:
        for vertex in edge:
            glVertex3fv(vertices_of_cube[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -6)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
