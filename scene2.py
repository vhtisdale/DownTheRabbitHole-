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
    
    
    #red central
    glPushMatrix()
    glTranslatef(1, -3, 5)
    glRotatef(90, 1, 0, 0)
    mushroom00.draw(0.545, 0.000, 0.545)
    glPopMatrix()


    #small guys right to left
    glPushMatrix()
    glTranslatef(5, -3, 10)
    glRotatef(90, 1, 0, 0)
    mushroom01.draw(0.545, 0.000, 0.645)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-3, -3, 9)
    glRotatef(90, 1, 0, 0)
    mushroom01.draw(0.545, 0.000, 0.645)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-4, -3, 13)
    glRotatef(90, 1, 0, 0)
    mushroom01.draw(0.545, 0.000, 0.645)
    glPopMatrix()
    
    #large backs
    glPushMatrix()
    glTranslatef(-35, 10, -90)
    glRotatef(90, 1, 0, 0)
    mushroom07.draw(0.294, 0.000, 0.510)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-120, 65, -150)
    glRotatef(90, 1, 0, 0)
    mushroom05.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-15, 65, -170)
    glRotatef(90, 1, 0, 0)
    mushroom05.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    
    
    glPushMatrix()
    glTranslatef(10,0,0)
    glRotatef(90, 0, 1, 0)
    grass00.draw(0.641, 0.969, 0.886)
    glPopMatrix()
    
    '''
    glPushMatrix()
    glTranslatef(-50, 0, -80)
    glRotatef(90, 1, 0, 0)
    mushroom06.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    
    
    glPushMatrix()
    glTranslatef(2, 0, 6)
    glRotatef(90, 1, 0, 0)
    mushroom02.draw(0.545, 0.000, 0.545)
    glPopMatrix()
    
    
    #large middle (in back of trio)
    glPushMatrix()
    glTranslatef(5, 14, -40)
    glRotatef(90, 1, 0, 0)
    mushroom03.draw(0.541, 0.169, 0.886)
    glPopMatrix()
    
    
    #large front right
    glPushMatrix()
    glTranslatef(17, 9, -6)
    glRotatef(90, 1, 0, 0)
    mushroom04.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    
    #skinny back
    glPushMatrix()
    glTranslatef(-10, 13, -70)
    glRotatef(90, 1, 0, 0)
    mushroom05.draw(0.402, 0.200, 0.702)
    glPopMatrix()
    
    #large backs from left to right
    glPushMatrix()
    glTranslatef(-25, 33, -80)
    glRotatef(90, 1, 0, 0)
    mushroom07.draw(0.294, 0.000, 0.510)
    glPopMatrix()
    
    
    glPushMatrix()
    glTranslatef(30, 33, -80)
    glRotatef(90, 1, 0, 0)
    mushroom07.draw(0.294, 0.000, 0.410)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(50, 33, -80)
    glRotatef(90, 1, 0, 0)
    mushroom07.draw(0.194, 0.000, 0.310)
    glPopMatrix()

    #large front left
    glPushMatrix()
    glTranslatef(-13, 5, 3)
    glRotatef(90, 1, 0, 0)
    mushroom06.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    
    #little front left
    glPushMatrix()
    glTranslatef(-3, -2, 14)
    glRotatef(90, 1, 0, 0)
    mushroom08.draw(0.641, 0.169, 0.886)
    glPopMatrix()
    '''


def setup():
    # One-time GL setup
    glClearColor(0.678, 0.800, 0.184, 1)
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


#large central
mushroom00 = shapelib.Mushroom4(.2, 4, 4, .5)


mushroom01 = shapelib.Mushroom5(.25, 1, 1.5, .2)
mushroom02 = shapelib.Mushroom3(.25, 2, 2.5, .2)

#large mushroom in background
mushroom03 = shapelib.Mushroom3(4, 20, 20, 4)

mushroom04 = shapelib.Mushroom3(3, 15, 15, 2)

mushroom05 = shapelib.Mushroom3(20, 50, 110, 10)


mushroom07 = shapelib.Mushroom3(5, 25, 40, 5)

#massive mushroom in back left
mushroom06 = shapelib.Mushroom3(3, 20, 35, 3)

mushroom08 = shapelib.Mushroom5(.25, 1.5, 2.5, .35)

grass00 = shapelib.Triangle(1,3)

rx = ry = rz = 0
pyglet.app.run()
# glEnd()
