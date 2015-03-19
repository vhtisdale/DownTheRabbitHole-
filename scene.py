# Victoria Tisdale
# 2/24/15

from math import pi, sin, cos

from pyglet.gl import *
import pyglet

from shapelib import vec
import shapelib

try:
    # Try and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    # Override the default on_resize handler to create a 3D projection
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., width / float(height), .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def update(dt):
    global rx, ry, rz
    rx += dt * 1
    ry += dt * 80
    rz += dt * 30
    rx %= 360
    ry %= 360
    rz %= 360
pyglet.clock.schedule(update)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    #zoom out
    glTranslatef(0, 0, -20)
    
    #rotate around the z-axis
    glRotatef(0, 0, 0, 1)
    #rotate around the y-axis
    glRotatef(0, 0, 1, 0)
    #rotate around the x-axis
    glRotatef(0, 1, 0, 0)
    
    
    glPushMatrix()
    glTranslatef(5, 0, 7)
    glRotatef(90, 1, 0, 0)
    mushroom00.draw(1.000, 0.498, 0.314)
    glPopMatrix()


    glPushMatrix()
    glTranslatef(4, 0, 7)
    glRotatef(90, 1, 0, 0)
    mushroom01.draw(0.000, 1.000, 0)
    glPopMatrix()
    '''
    
    
    glPushMatrix()
    glTranslatef(6, 6, 3)
    glRotatef(90, 1, 0, 0)
    mushroom00.draw(0.000, 1.000, 0.498)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(6, -12, -4)
    glRotatef(90, 1, 0, 0)
    mushroom02.draw(0.000, 1.000, 0.498)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(12, 0, -9)
    glRotatef(90, 1, 0, 0)
    mushroom03.draw(0.000, 1.000, 0.498)
    glPopMatrix()
    
    
    glPushMatrix()
    glTranslatef(-14, -33, -10)
    glRotatef(90, 1, 0, 0)
    mushroom05.draw(1.000, 0.498, 0.314)
    glPopMatrix()
    
    
    glPushMatrix()
    glTranslatef(-4, -35, -20)
    glRotatef(90, 1, 0, 0)
    mushroom04.draw(1.000, 0.498, 0.314)
    glPopMatrix()


    glPushMatrix()
    glTranslatef(0, 0, 10)
    glRotatef(90, 1, 0, 0)
    mushroom00.draw(1.000, 0.498, 0.314)
    glPopMatrix()
    '''


def setup():
    # One-time GL setup
    glClearColor(0.000, 0.502, 0.000, 1)
    glColor3f(1, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    # Uncomment this line for a wireframe view
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Simple light setup.  On Windows GL_LIGHT0 is enabled by default,
    # but this is not the case on Linux or Mac, so remember to always 
    # include it.
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glLightfv(GL_LIGHT0, GL_POSITION, vec(.5, .5, 1, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, vec(.5, .5, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(.5, .5, .5, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))

    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.0, 0.5, 0.3, 1))
    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.5, 0.5, 0.5, 1))
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
    # glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)



setup()
# tube = shapelib.ConicalCylinder(64, 2, 1.5, 1)
mushroom00 = shapelib.Mushroom4(.25, 2, 2.5, .25)
mushroom01 = shapelib.Mushroom5(.25, 2, 1.5, .35)
mushroom02 = shapelib.Mushroom3(2, 9, 9, 1.5)
mushroom03 = shapelib.Mushroom3(3, 15, 15, 2)
mushroom04 = shapelib.Mushroom3(3, 15, 30, 1)
mushroom05 = shapelib.Mushroom4(2, 15, 20, 3)
rx = ry = rz = 0
pyglet.app.run()
# glEnd()
