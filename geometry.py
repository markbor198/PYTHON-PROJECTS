import math

class Point (object):
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        #self.center = Point(x,y,z)
    
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', '+ str(self.z)+ ')'
      

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
    def distance (self, other):
        
        return (float(math.hypot (self.x - other.x, self.y - other.y,\
                            self.z- other.z)))

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and\
                (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))

class Sphere (object):
    #f
  # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x,y,z)
        self.radius = float(radius)
      

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
    def __str__ (self):
        return '(' + str(self.center.x) + ', ' + str(self.center.y) + ', '+ str(self.center.z)+ '), '\
               + 'Radius: ' + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
    def area (self):
        area = 4 * math.pi * (self.radius**2)
        return float(area)
        

  # compute volume of a Sphere
  # returns a floating point number
    def volume (self):
        volume = (4/3) * math.pi * (self.radius**3)
        return float(volume)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
    def is_inside_point (self, p):
        return self.center.distance(p) < self.radius 
        

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, other):
        dist_centers = self.center.distance(other.center)
        return (dist_centers + other.radius) < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
    def is_inside_cube (self, a_cube):
        dist_centers = self.center.distance(a_cube.center)
        return (dist_centers + (a_cube.side * math.sqrt(3))) < self.radius * 2
  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        dist_center = self.center.distance(a_cyl.center)
        return (dist_center + a_cyl.radius * 2) < self.radius * 2

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
    def does_intersect_sphere (self, other):
        dist_centers = self.center.distance(other.center)
        is_inside = (dist_centers + other.radius) < self.radius
        is_outside = dist_centers > (self.radius + other.radius)
        return (not is_inside) and (not is_outside)

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
    def does_intersect_cube (self, a_cube):
        dist_centers = self.center.distance(a_cube.center)
        is_inside = (dist_centers + (a_cube.side * math.sqrt(3))) < self.radius * 2
        is_outside = (dist_centers) > (self.radius * 2 + (a_cube.side * math.sqrt(3)))
        return (not is_inside) and (not is_outside)

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
    def circumscribe_cube (self):
        cube_side = (2 * self.radius )/(math.sqrt(3))
        lrg_cube = Cube(self.center.x,self.center.y,self.center.z,cube_side)
        return lrg_cube

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      
      self.center = Point(x,y,z)
      self.side = float(side)

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      return '(' + str(self.center.x) + ', ' + str(self.center.y) + ', '+ str(self.center.z)+ '), '\
               + 'Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      area = 6 * (self.side**2)
      return float(area)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      volume = self.side**3
      return float(volume)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      return self.center.distance(p) < self.side

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      dist_centers = self.center.distance(a_sphere.center)
      return (dist_centers + 2*a_sphere.radius) < self.side* (math.sqrt(3))
      

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      dist_centers = self.center.distance(other.center)
      return (dist_centers + other.side) < self.side 

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      dist_center = self.center.distance(a_cyl.center)
      return (dist_center + a_cyl.height) < self.side
      

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
      
      dist_centers = self.center.distance(other.center)
      is_inside = (dist_centers + other.side ) < self.side 
      is_outside = (dist_centers ) > self.side + other.side
      return (not is_inside) and (not is_outside)

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
      dist_centers = self.center.distance(other.center)
      return (dist_centers**3)
      

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
      sphere_rad = (self.side/2)
      lrg_sphere = Sphere(self.center.x,self.center.y,self.center.z,sphere_rad)
      return lrg_sphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.center = Point(x,y,z)
      self.radius = float(radius)
      self.height = float(height)

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      
      return '(' + str(self.center.x) + ', ' + str(self.center.y) + ', '+ str(self.center.z)+ '), '\
             + 'Radius: ' + str(self.radius) + ', Height: ' + str(self.height) 

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      area = 2 * math.pi * self.radius * self.height + 2 * math.pi * (self.radius**2)
      return float(area)

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      volume = math.pi * (self.radius ** 2) * self.height
      return float(volume)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return self.center.distance(p) < self.height

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      dist_center = self.center.distance(a_sphere.center)
      return (dist_center + a_sphere.radius) < self.radius 
      
      

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      dist_centers = self.center.distance(a_cube.center)
      return (dist_centers + (a_cube.side * math.sqrt(3))) < self.radius * 2
      

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, other):
      dist_centers = self.center.distance(other.center)
      return (dist_centers + other.radius) < self.radius

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cyl (self, other):
      dist_center = self.center.distance(other.center)
      is_inside = (dist_center + other.height) < self.radius
      is_outside = dist_center > (self.radius + other.height)
      return (not is_inside) and (not is_outside)

def main():
    # read data from standard input
    #geometry_in = open('geometry.in', 'r') 
  # read the coordinates of the first Point p
    coord_p = [float(x) for x in input().split(' ')]    #,coord_py,coord_pz
    
    #coord_p.split(' ')
    origin = float(0)
    orig_point = Point(origin,origin,origin)
  # create a Point object 
    p_point = Point(coord_p[0],coord_p[1],coord_p[2])
    #print(first_point.distance(orig_point))
    
    dist_p = p_point.distance(orig_point)
    
  # read the coordinates of the second Point q
    coord_q = [float(x) for x in input().split(' ')] 
  # create a Point object 
    q_point = Point(coord_q[0],coord_q[1],coord_q[2])
    #print(sec_point.distance(orig_point))
    dist_q= q_point.distance(orig_point)
  # read the coordinates of the center and radius of sphereA
    
  # read the coordinates of the center and radius of sphereA
    coord_sphere_a = [float(x) for x in input().split(' ')] 
  # create a Sphere object
    a_sphere = Sphere(coord_sphere_a[0],coord_sphere_a[1],coord_sphere_a[2],coord_sphere_a[3])
  # read the coordinates of the center and radius of sphereB
    coord_sphere_b = [float(x) for x in input().split(' ')] 
  # create a Sphere object
    b_sphere =  Sphere(coord_sphere_b[0],coord_sphere_b[1],coord_sphere_b[2],coord_sphere_b[3])
  # read the coordinates of the center and side of cubeA
    coord_cube_a = [float(x) for x in input().split(' ')] 
  # create a Cube object 
    a_cube = Cube(coord_cube_a[0],coord_cube_a[1],coord_cube_a[2],coord_cube_a[3])
  # read the coordinates of the center and side of cubeB
    coord_cube_b = [float(x) for x in input().split(' ')] 
  # create a Cube object 
    b_cube = Cube(coord_cube_b[0],coord_cube_b[1],coord_cube_b[2],coord_cube_b[3])
  # read the coordinates of the center, radius and height of cylA
    coord_cyl_a = [float(x) for x in input().split(' ')] 
  # create a Cylinder object 
    a_cyl = Cylinder(coord_cyl_a[0],coord_cyl_a[1],coord_cyl_a[2],coord_cyl_a[3],coord_cyl_a[4])
  # read the coordinates of the center, radius and height of cylB
    coord_cyl_b = [float(x) for x in input().split(' ')] 
  # create a Cylinder object
    b_cyl = Cylinder(coord_cyl_b[0],coord_cyl_b[1],coord_cyl_b[2],coord_cyl_b[3],coord_cyl_b[4])

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
    if dist_p > dist_q :
        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
    elif dist_p <= dist_q :
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

    print('')
  # print if Point p is inside sphereA
    if a_sphere.is_inside_point(p_point) == True:
        print('Point p is inside sphereA')
    elif a_sphere.is_inside_point(p_point) == False:
        print('Point p is not inside sphereA')
        
  # print if sphereB is inside sphereA
    if a_sphere.is_inside_sphere(b_sphere) == True:
        print('sphereB is inside sphereA')
    elif a_sphere.is_inside_sphere(b_sphere) == False:
        print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
    if a_sphere.is_inside_cube(a_cube) == True:
        print('cubeA is inside sphereA')
    elif a_sphere.is_inside_cube(a_cube) == False:
        print('cubeA is not inside sphereA')
  # print if cylA is inside sphereA
    if a_sphere.is_inside_cyl(a_cyl) == True:
        print('cylA is inside sphereA')
    elif a_sphere.is_inside_cyl(a_cyl) == False:
        print('cylA is not inside sphereA')
  # print if sphereA intersects with sphereB
    if b_sphere.does_intersect_sphere(a_sphere) == True:
        print('sphereA does intersect sphereB')
    elif b_sphere.does_intersect_sphere(a_sphere) == False:
        print('sphereA does not intersect sphereB')

  # print if cubeB intersects with sphereB
    if b_sphere.does_intersect_cube(b_cube) == True :
        print('cubeB does intersect sphereB')
    elif b_sphere.does_intersect_cube(b_cube) == False :
        print('cubeB does not intersect sphereB')
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA

    if a_sphere.circumscribe_cube().volume() > a_cyl.volume():
        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')

    elif a_sphere.circumscribe_cube().volume() < a_cyl.volume():
        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
    print('')
  # print if Point p is inside cubeA
    if a_cube.is_inside_point(p_point) == True:
        print('Point p is inside cubeA')
    elif a_cube.is_inside_point(p_point) == False:
        print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
    if a_cube.is_inside_sphere(a_sphere) == True:
        print('sphereA is inside cubeA')
    elif a_cube.is_inside_sphere(a_sphere) == False:
        print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
    if a_cube.is_inside_cube(b_cube) == True:
        print('cubeB is inside cubeA')
    elif a_cube.is_inside_cube(b_cube) == False:
        print('cubeB is not inside cubeA')
  # print if cylA is inside cubeA
    if a_cube.is_inside_cyl(a_cyl) == True:
        print('cylA is inside cubeA')
    elif a_cube.is_inside_cyl(a_cyl) == False:
        print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
    if b_cube.does_intersect_cube(a_cube) == True :
        print('cubeA does intersect cubeB')
    elif b_cube.does_intersect_cube(a_cube) == False :
        print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    if b_cube.intersection_volume(a_cube) > a_sphere.volume():
        print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
    elif b_cube.intersection_volume(a_cube) < a_sphere.volume():
        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
    if a_cube.inscribe_sphere().area() > a_cyl.area():
        print('Surface area of the largest Sphere that is inscribed by cubeA is greater than the Surface area of cylA')

    elif a_cube.inscribe_sphere().area() < a_cyl.area():
        print('Surface area of the largest Sphere that is inscribed by cubeA is not greater than the Surface area of cylA')
    print('')
  # print if Point p is inside cylA
    if a_cyl.is_inside_point(p_point) == True:
        print('Point p is inside cylA')
    elif a_cyl.is_inside_point(p_point) == False:
        print('Point p is not inside cylA')
  # print if sphereA is inside cylA
    if a_cyl.is_inside_sphere(a_sphere) == True:
        print('sphereA is inside cylA')
    elif a_cyl.is_inside_sphere(a_sphere) == False:
        print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
    if a_cyl.is_inside_cube(a_cube) == True:
        print('cubeA is inside cylA')
    elif a_cyl.is_inside_cube(a_cube) == False:
        print('cubeA is not inside cylA')
  # print if cylB is inside cylA
    if a_cyl.is_inside_cyl(b_cyl) == True:
        print('cylB is inside cylA')
    elif a_cyl.is_inside_cyl(b_cyl) == False:
        print('cylB is not inside cylA')
  # print if cylB intersects with cylA
    if a_cyl.does_intersect_cyl(b_cyl) == True :
        print('cylB does intersect cylA')
    elif a_cyl.does_intersect_cyl(b_cyl) == False :
        print('cylB does not intersect cylA')
if __name__ == "__main__":
  main()
