# shapetest.py
# Victoria Tisdale
# March 18, 2015

from math import pi, sin, cos

from pyglet.gl import *
import pyglet

from shapelib import vec
import shapelib

################################################################################
############################## openGL framework ################################
################################################################################

try:
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., width / float(height), .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def update(dt):
    global rx, ry, rz
    rx += dt * 30
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
    glTranslatef(0, 0, -20)
    glRotatef(rx, 0, 1, 0)
    glPushMatrix()
    glTranslatef(0, 0, -2)
    shape.draw(0,1,1)
    glPopMatrix()
    
def setup():
    # One-time GL setup
    glClearColor(0, 0, 0, 1)
    glColor3f(1, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glLightfv(GL_LIGHT0, GL_POSITION, vec(0, 0, 10, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, vec(.5, .5, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
    # glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
    # glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(.5, .5, .5, 1))
    # glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))


############################# End openGL Framework #############################

################################################################################
############################# Shape Test Functions #############################
################################################################################

# def test_hemisphere():
  
if __name__ == "__main__":
  setup()
  rx = ry = rz = 0
  shape = shapelib.Hemisphere(16, 10)
  pyglet.app.run()

     
  