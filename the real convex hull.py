import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
    return (q.x*r.y-q.y*r.x)-(p.x*r.y-p.x*q.y)+(p.y*r.x-p.y*q.x) #(q.x-p.x)*(r.y-p.y)-(q.y-p.y)*(r.x-p.x)
# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):
    print(sorted_points)
    upper_hull = []
    lower_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    
    for p in range(2,len(sorted_points)):
        upper_hull.append(sorted_points[p])
        
        while len(upper_hull)>=3 and det(upper_hull[-3],upper_hull[-2],upper_hull[-1]) >= 0:
            upper_hull.pop(-2)
    print('yo',sorted_points[-1])       
    lower_hull.append(sorted_points[-1]) #[len(sorted_points)-1])
    lower_hull.append(sorted_points[-2])# [len(sorted_points)-2])
    print('should be 2',lower_hull)
    
    for p in range(len(sorted_points)-2,-1,-1):
        lower_hull.append(sorted_points[p])
        #print(lower_hull)
        while len(lower_hull)>=3 and det(lower_hull[-3],lower_hull[-2],lower_hull[-1]) >= 0:
            lower_hull.pop(-2)
    '''if upper_hull[-1].__eq__(lower_hull[0]) == True:
        print('is equal test') 
        lower_hull.pop(0) '''
    #if lower_hull[-1] 
    print(len(upper_hull))
    print(len(lower_hull))
    lower_hull.pop(0)
    lower_hull.pop(-1)
    '''if lower_hull[-1] != sorted_points[1] and det(upper_hull[0],upper_hull[1],lower_hull[-1])<=0 :
        print('test')
        lower_hull.append(sorted_points[1])
        return upper_hull + lower_hull
    elif lower_hull[-1] != sorted_points[1] and det(upper_hull[0],upper_hull[1],lower_hull[-1])>=0:#.__eq__(   sorted_points[1]) is True:   
        print('test2')
        #lower_hull.pop(-1)
        return upper_hull + lower_hull'''

    #print(lower_hull)  #[0:].__str__())
    #print(upper_hull)    #[0:].__str__())
    #convex =  upper_hull.extend(lower_hull[0:])
    #print(convex)
    return  upper_hull + lower_hull

def main(coords):
    points = []
  # read data from standard input
    print(len(coords))
    hull_in = coords
    #print(hull_in)
  # read line by line, create Point objects and store in a list
    #n = hull_in[0]
    for x in hull_in:#range(0,len(hull_in)-1):
        #line = x #.split('\t')
        #print(line)
        #x_coord = int(line[0])
        #y_coord = int(line[1])
        p_n = Point(x[0],x[1])
        
        
        points.append(p_n)
  # sort the list according to x-coordinates
    points = sorted(points)
    #print(points)
    for x in (points):
        #sorted(x.__str__())
        print(x.__str__())
  # get the convex hull      
    get_convex = convex_hull(points)
    
  # run your test cases
    result = []
    #return  [x for x in get_convex]
    '''for x in get_convex:
        result.append(x)'''
    #for x in get_convex:
    return get_convex
    #print(get_convex)
  # print your results to standard output
    #get_area = area_poly(get_convex)
    #print()
    
    #print('Area of Convex Hull =', get_area)
    #return convex hull
