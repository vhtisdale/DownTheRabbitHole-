# author: Victoria Tisdale
# created: 2/25/15

# generic python libs
from math import pi, sin, cos

# open gl libs
from pyglet.gl import *
import pyglet

# Define a simple function to create ctypes arrays of floats:
def vec(*args):
    return (GLfloat * len(args))(*args)

class Quadrant(object):
  def __init__(self, slices, radius):
    vertices = [0,0,0]
    normals = [0,0,1]

    theta = 0
    theta_step = (.5*pi)/(slices-1)

    for i in range(slices):
      cos_theta = cos(theta)
      sin_theta = sin(theta)

      vertices.extend([cos_theta*radius, sin_theta*radius, 0])
      normals.extend([0, 0, 1])
      
      theta += theta_step

    vertices = (GLfloat * len(vertices))(*vertices)
    normals = (GLfloat * len(normals))(*normals)

    indices = []
    p = slices
    for i in range(slices+1):
      indices.extend([0, i, p])
      p = i
    indices = (GLuint * len(indices))(*indices)
    
    # Compile a display list
    self.list = glGenLists(1)
    glNewList(self.list, GL_COMPILE)

    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glNormalPointer(GL_FLOAT, 0, normals)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
    glPopClientAttrib()

    glEndList()

  def draw(self, r, g, b):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(r, g, b, 1))
    glCallList(self.list)

class Fan(object):
  def __init__(self, slices, radius):
    vertices = [0,0,0]
    normals = [0, 0, 1]

    theta = 0
    theta_step = (2*pi)/(slices-1)

    for i in range(slices):
      cos_theta = cos(theta)
      sin_theta = sin(theta)

      vertices.extend([cos_theta*radius, sin_theta*radius, 0])
      normals.extend([0, 0, 1])
      
      theta += theta_step

    vertices = (GLfloat * len(vertices))(*vertices)
    normals = (GLfloat * len(normals))(*normals)

    indices = []
    p = slices
    for i in range(slices+1):
      indices.extend([0, i, p])
      p = i
    indices = (GLuint * len(indices))(*indices)
    
    # Compile a display list
    self.list = glGenLists(1)
    glNewList(self.list, GL_COMPILE)

    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glNormalPointer(GL_FLOAT, 0, normals)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
    glPopClientAttrib()

    glEndList()

  def draw(self, r, g, b):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(r, g, b, 1))
    glCallList(self.list)

class Tube(object):
  '''
  initialized cylinder object
  takes a dim
  '''
  def __init__(self, slices, height, radius):
    # create the vertex and normal arrays
    vertices = []
    normals = []
    
    theta = 0
    theta_step = (2*pi)/(slices-1)

    for i in range(slices):
      cos_theta = cos(theta)
      sin_theta = sin(theta)

      vertices.extend([cos_theta*radius, sin_theta*radius, 0])
      vertices.extend([cos_theta*radius, sin_theta*radius, height])
      normals.extend([cos_theta, sin_theta, 0])
      normals.extend([cos_theta, sin_theta, 0])
      
      theta += theta_step

    # Create ctypes arrays of the lists
    vertices = (GLfloat * len(vertices))(*vertices)
    normals = (GLfloat * len(normals))(*normals)

    # Create a list of triangle indices.
    indices = []
    p = slices-1
    for i in range(slices):
      indices.extend([i*2, (i*2)+1, (p*2)+1])
      indices.extend([p*2, i*2, (p*2)+1])
      p = i
    indices = (GLuint * len(indices))(*indices)

    # Compile a display list
    self.list = glGenLists(1)
    glNewList(self.list, GL_COMPILE)

    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glNormalPointer(GL_FLOAT, 0, normals)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
    glPopClientAttrib()

    glEndList()

  def draw(self, r, g, b):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(r, g, b, 1))
    glCallList(self.list)

class ConicalTube(object):
  '''
  initialized cylinder object
  takes a dim
  '''
  def __init__(self, slices, height, upper_radius, lower_radius):
    # create the vertex and normal arrays
    vertices = []
    normals = []
    
    theta = 0
    theta_step = (2*pi)/(slices-1)

    for i in range(slices):
      cos_theta = cos(theta)
      sin_theta = sin(theta)

      vertices.extend([cos_theta*lower_radius, sin_theta*lower_radius, 0])
      vertices.extend([cos_theta*upper_radius, sin_theta*upper_radius, height])
      normals.extend([cos_theta, sin_theta, 0])
      normals.extend([cos_theta, sin_theta, 0])
      
      theta += theta_step

    # Create ctypes arrays of the lists
    vertices = (GLfloat * len(vertices))(*vertices)
    normals = (GLfloat * len(normals))(*normals)

    # Create a list of triangle indices.
    indices = []
    p = slices-1
    for i in range(slices):
      indices.extend([i*2, (i*2)+1, (p*2)+1])
      indices.extend([p*2, i*2, (p*2)+1])
      p = i
    indices = (GLuint * len(indices))(*indices)

    # Compile a display list
    self.list = glGenLists(1)
    glNewList(self.list, GL_COMPILE)

    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glNormalPointer(GL_FLOAT, 0, normals)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
    glPopClientAttrib()

    glEndList()

  def draw(self, r, g, b):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(r, g, b, 1))
    glCallList(self.list)

class HemiSphere(object):
  def __init__(self, slices, radius):
    self.radius = radius

    # create the vertex and normal arrays
    vertices = []
    normals = []
    
    theta = 0
    theta_step = (2*pi)/(slices-1)

    for i in range(slices):
      cos_theta = cos(theta)
      sin_theta = sin(theta)

      vertices.extend([cos_theta*lower_radius, sin_theta*lower_radius, 0])
      vertices.extend([cos_theta*upper_radius, sin_theta*upper_radius, height])
      normals.extend([cos_theta, sin_theta, 0])
      normals.extend([cos_theta, sin_theta, 0])
      
      theta += theta_step

    # Create ctypes arrays of the lists
    vertices = (GLfloat * len(vertices))(*vertices)
    normals = (GLfloat * len(normals))(*normals)

    # Create a list of triangle indices.
    indices = []
    p = slices-1
    for i in range(slices):
      indices.extend([i*2, (i*2)+1, (p*2)+1])
      indices.extend([p*2, i*2, (p*2)+1])
      p = i
    indices = (GLuint * len(indices))(*indices)

    # Compile a display list
    self.list = glGenLists(1)
    glNewList(self.list, GL_COMPILE)

    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glNormalPointer(GL_FLOAT, 0, normals)
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
    glPopClientAttrib()

    glEndList()


class Cylinder(object):
  def __init__(self, slices, height, radius):
    self.radius = radius
    self.height = height
    self.fan = Fan(slices, self.radius)
    self.tube = Tube(slices, self.height, self.radius)

  def draw(self, r, g, b):
    self.fan.draw(r, g, b)
    self.tube.draw(r, g, b)
    glTranslatef(0,0,self.height)
    glRotatef(180, 1, 0, 0)
    self.fan.draw(r, g, b)

class ConicalCylinder(object):
  def __init__(self, slices, height, upper_radius, lower_radius):
    self.upper_radius = upper_radius
    self.lower_radius = lower_radius
    self.height = height
    self.upper_fan = Fan(slices, self.upper_radius)
    self.lower_fan = Fan(slices, self.lower_radius)
    self.tube = ConicalTube(slices, self.height, self.upper_radius, self.lower_radius)

  def draw(self, r, g, b):
    self.lower_fan.draw(r, g, b)
    self.tube.draw(r, g, b)
    glTranslatef(0,0,self.height)
    glRotatef(180, 1, 0, 0)
    self.upper_fan.draw(r, g, b)

class Mushroom(object):
  def __init__(self, top_height, top_radius, bottom_height, bottom_radius):
    self.top_height = top_height
    self.top_radius = top_radius
    self.bottom_height = bottom_height
    self.bottom_radius = bottom_radius
    self.top = Cylinder(64, self.top_height, self.top_radius)
    self.bottom = ConicalCylinder(64, self.bottom_height, self.bottom_radius*1.5, self.bottom_radius )

  def draw(self, r, g, b):
    self.bottom.draw(r, g, b)
    glTranslatef(0, 0, self.bottom_height )
    self.top.draw(r, g, b)



class Mushroom2(object):
  def __init__(self, top_height, top_radius, bottom_height, bottom_radius):
    self.top_height = top_height
    self.top_radius = top_radius
    self.bottom_height = bottom_height
    self.bottom_radius = bottom_radius
    self.top = ConicalCylinder(64, self.top_height*2, self.top_radius , self.top_radius* .5)
    self.top2 = Cylinder(64, self.top_height * .5, self.top_radius)
    self.bottom = ConicalCylinder(64, self.bottom_height, self.bottom_radius*1.5, self.bottom_radius )
  
  def draw(self, r, g, b):
    self.bottom.draw(r, g, b)
    glTranslatef(0, 0, self.bottom_height )
    self.top2.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*2)
    self.top.draw(r, g, b)

class Mushroom3(object):
  def __init__(self, top_height, top_radius, bottom_height, bottom_radius):
    self.top_height = top_height
    self.top_radius = top_radius
    self.bottom_height = bottom_height
    self.bottom_radius = bottom_radius
    #top nob
    self.top4 = ConicalCylinder(64, self.top_height*1.5, self.top_radius* .5 , self.top_radius*.25)
    #bottom nob
    self.top3 = ConicalCylinder(64, self.top_height*1.5, self.top_radius* .35 , self.bottom_radius)
    #middle
    self.top = ConicalCylinder(64, self.top_height*2, self.top_radius , self.top_radius* .5)
    #bottom
    self.top2 = Cylinder(64, self.top_height * .5, self.top_radius)
    self.bottom = ConicalCylinder(64, self.bottom_height, self.bottom_radius*1.5, self.bottom_radius )
        
  def draw(self, r, g, b):
    self.bottom.draw(r, g, b)
    glTranslatef(0, 0, self.bottom_height )
    self.top2.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*2)
    self.top.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*1.5)
    self.top3.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*3.5)
    self.top4.draw(r, g, b)

class Mushroom4(object):
  def __init__(self, top_height, top_radius, bottom_height, bottom_radius):
    self.top_height = top_height
    self.top_radius = top_radius
    self.bottom_height = bottom_height
    self.bottom_radius = bottom_radius
    #top nob
    self.top4 = ConicalCylinder(64, self.top_height*1.5, self.top_radius* .5 , self.top_radius*.25)
    #bottom nob
    self.top3 = ConicalCylinder(64, self.top_height*1.5, self.top_radius* .35 , self.bottom_radius)
    #middle
    self.top = ConicalCylinder(64, self.top_height*2.5, self.top_radius , self.top_radius* .5)
    #bottom
    self.top2 = Cylinder(64, self.top_height * .5, self.top_radius)
    self.bottom = ConicalCylinder(64, self.bottom_height, self.bottom_radius*1.5, self.bottom_radius )
        
  def draw(self, r, g, b):
    self.bottom.draw(r, g, b)
    glTranslatef(0, 0, self.bottom_height )
    self.top2.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*2.5)
    self.top.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*2)
    self.top3.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*4.5)
    self.top4.draw(r, g, b)

class Mushroom5(object):
  def __init__(self, top_height, top_radius, bottom_height, bottom_radius):
    self.top_height = top_height
    self.top_radius = top_radius
    self.bottom_height = bottom_height
    self.bottom_radius = bottom_radius
    #top nob
    self.top4 = ConicalCylinder(64, self.top_height*1.5, self.top_radius* .75 , self.top_radius*.25)
    #bottom nob
    self.top3 = ConicalCylinder(64, self.top_height*1.5, self.top_radius* .35 , self.bottom_radius)
    #middle
    self.top = ConicalCylinder(64, self.top_height*2.5, self.top_radius , self.top_radius* .75)
    #bottom
    self.top2 = Cylinder(64, self.top_height * .5, self.top_radius)
    self.bottom = ConicalCylinder(64, self.bottom_height, self.bottom_radius*1.5, self.bottom_radius )
        
  def draw(self, r, g, b):
    self.bottom.draw(r, g, b)
    glTranslatef(0, 0, self.bottom_height )
    self.top2.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*2.5)
    self.top.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*2)
    self.top3.draw(r, g, b)
    glTranslatef(0, 0, -self.top_height*4.5)
    self.top4.draw(r, g, b)

class Mushroom6(object):
  def __init__(self, top_height, top_radius, bottom_height, bottom_radius):
    self.top_height = top_height
    self.top_radius = top_radius
    self.bottom_height = bottom_height
    self.bottom_radius = bottom_radius
    self.top = ConicalCylinder(64, self.top_height*2, self.top_radius , self.top_radius* 1.5)
    self.bottom = ConicalCylinder(64, self.bottom_height, self.bottom_radius*1.5, self.bottom_radius )
        
  def draw(self, r, g, b):
    self.bottom.draw(r, g, b)
    glTranslatef(0, 0, self.bottom_height )
    self.top.draw(r, g, b)



