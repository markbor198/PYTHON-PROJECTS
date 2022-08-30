import math
class Point (object):
    
    
    def __init__ (self, x = 0, y = 0):
        self.x = int(x)
        self.y = int(y)
        
        #self.center = Point(x,y,z)
    
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
      

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
    def properties (self, other):
        return Point(abs(self.x - other.x), abs(self.y - other.y))

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
    def distance (self,other):
        return (int(math.hypot (self.x - other.x, self.y - other.y)))

 

class Rectangle (object):
    
  # constructor 
    def __init__ (self, x = 0, y = 0, x2 = 0, y2 = 0):
    
        self.left = Point(x, y)
        self.right = Point(x2,y2)

   
  # compute the area
    def area (self):
        
        rect_coor = self.left.properties(self.right)
        area = rect_coor.x * rect_coor.y
        return area

  # determine if a rectangle intersects a rect
  
def intersect_area (r1, r2):
    
    dist_x = min(r1.right.x,r2.right.x) - max(r1.left.x,r2.left.x)
    dist_y = min(r1.right.y,r2.right.y) - max(r1.left.y,r2.left.y)
    if dist_x >= 0 and dist_y >= 0:
        return dist_x * dist_y

def main():

  # read the data
    office_size = [int(x) for x in input().split(' ')]
    office_bldg = Rectangle(0,0,office_size[0],office_size[1])
    total_space = office_bldg.area()
    cont_area = 0
    num_employ = int(input())
    employ_name = []
    cube_req = []
    obj_cube = []
    alloc_cube = []
    no_cont = []
    cont_cubes = []
    new_area =[]
    i = 0
    while i <= num_employ-1:
        employ_input = [x for x in input().split(' ')]
        employ_name.append(employ_input[0])
        employ_req = Rectangle(employ_input[1],employ_input[2],employ_input[3],employ_input[4])
        cube_req.append((employ_req.left.__str__(),employ_req.right.__str__()))
        obj_cube.append(employ_req)
        i += 1
 
    j = 1
    print(obj_cube)
    alloc_cube.append(obj_cube[0])
    
    if intersect_area(obj_cube[1],alloc_cube[0])   == None:
            print('test0 cases')
            no_cont.append(alloc_cube[0].area())
            
    while j < len(obj_cube):
        '''if intersect_area(obj_cube[1],alloc_cube[0])   == None:
            print('test0 cases')
            #cont_area += intersect_area(obj_cube[j],alloc_cube[j-1])
            no_cont.append(alloc_cube[0].area())# -intersect_area(obj_cube[j],alloc_cube[j-1]))
            #new_area.append(obj_cube[j].area() -intersect_area(obj_cube[j],alloc_cube[j-1]))
            #alloc_cube.append(obj_cube[j])'''
        

        
        if intersect_area(alloc_cube[j-1],obj_cube[j]) != None:
            print('test1 case')
            cont_area += intersect_area(obj_cube[j],alloc_cube[j-1])
            new_area.append(alloc_cube[j-1].area() -intersect_area(obj_cube[j],alloc_cube[j-1]))
            new_area.append(obj_cube[j].area() -intersect_area(obj_cube[j],alloc_cube[j-1]))
            alloc_cube.append(obj_cube[j])
            
            
        elif intersect_area(obj_cube[j],alloc_cube[j-1])==  None :
            print('test2 case')
            no_cont.append(obj_cube[j].area())
            alloc_cube.append(obj_cube[j])
            cont_area += 0

        j+=1
    new_area.extend(no_cont)
    total_space = total_space - sum(new_area) - cont_area
    print('Total',office_bldg.area())
    print('Unallocated',total_space)
    print('Contested',cont_area)
    z = 0
    while z <= num_employ-1:
        print(employ_name[z], new_area[z])
        z += 1
    
         
    
    #print(total_space)

  # print the following results after computation

  # compute the total office space

  # compute the total unallocated space

  # compute the total contested space

  # compute the uncontested space that each employee gets
if __name__ == "__main__":
    main()
