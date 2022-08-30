#  File: TopoSort.py

#  Description: A24

#  Student Name: Mark Borjas

#  Student UT EID: mab7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50850 

#  Date Created: 11/29/20

#  Date Last Modified: 12/2/20

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))
  def is_inside(self,label):
    labels = []
    while not self.is_empty():
      labels.append(self.pop())
    labels.reverse()
    for vert in label:
      self.push(vert)
    if label in labels:
      return True
    return False

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  def peek(self):
    return self.queue[0]

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))
  

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return i
    #return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if not (self.has_vertex (label)):
      #return

    # add vertex to the list of vertices
      self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append(0)

    # add a new row for the new vertex
      new_row = []
      for i in range (nVert):
        new_row.append (0)
      self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight


  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight (self, fromVertexLabel, toVertexLabel):
    edge_weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
    if (edge_weight != 0):
      return (edge_weight)
    return -1

  # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors (self, vertexLabel):
    neighbors = []
    vertexIndex = self.get_index(vertexLabel)
    #vertex = self.Vertices[vertexIndex]
    for i in range(len(self.Vertices)):
      if self.adjMat[vertexIndex][i] > 0:
        neighbors.append(self.Vertices[i])
    return neighbors

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1
  # get a copy of the list of Vertex objects
  def get_vertices (self):
    vertices = self.Vertices
    for i in range(len(vertices)):
      print(vertices)

  def trav_adj_unvisted_vertex(self,theStack):
    num_vertices = len(self.Vertices)
    vert = theStack.peek()
    for v in range(num_vertices):
      if self.adjMat[v][i] > 0 and (self.Vertices[i]).was_visited() :
        if theStack.is_inside(v):
          return -2
      if self.adjMat[v][i] > 0 and not self.Vertices[v].was_visited():
        return v
    return -1
      

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    #print (self.Vertices[v])
    theStack.push(v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        #print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    # make queue
    theQueue = Queue()

    #set v as visited and then push it onto the queue
    (self.Vertices[v]).visited = True
    print(self.Vertices[v])
    theQueue.enqueue(v)

    while not theQueue.is_empty():
      un_visited = self.get_adj_unvisited_vertex(theQueue.peek())

      if un_visited == -1:
        un_visited = theQueue.dequeue()
      else:
        self.Vertices[un_visited].visited = True
        print(self.Vertices[un_visited])
        theQueue.enqueue(un_visited)

    num_vert = len(self.Vertices)
    for i in range(num_vert):
      self.Vertices[i].visited = False
    

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    firstIndex = self.get_index(fromVertexLabel)
    lastIndex = self.get_index(toVertexLabel)
    self.adjMat[firstIndex][lastIndex] = 0
    self.adjMat[lastIndex][firstIndex] = 0

  
  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    vertexIndex = self.get_index(vertexLabel)
    num_verts = len(self.Vertices)
    
    for i in range(num_verts):
      
      for j in range(vertexIndex, num_verts -1):
        self.adjMat[i][j] = self.adjMat[i][j+1]
        
      self.adjMat[i].pop()
      
    self.adjMat.pop(vertexIndex)
    
    for vertex in self.Vertices:
      if vertex.label == vertexLabel:
        self.Vertices.remove(vertex)
    
  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
    
    vertices = self.Vertices
    for vert in vertices:
      if self.cycle_helper(None,vert):
        return True
      for i in range(len(vertices)):
        vertices[i].visited = False
    return False

      
  def cycle_helper(self,prev,vertex):
    if vertex.was_visited() == True:
      return True
    vertex.visited = True
    neighbors = self.get_neighbors(vertex.label)

    if prev in neighbors:
      neighbors.remove(prev)
    if len(neighbors) == 0:
      return False
    for neighbor in neighbors:
      return self.cycle_helper(vertex,neighbor)

    
  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    num_verts = len(self.Vertices)
    copy = Graph()
    copy.Vertices = self.Vertices
    copy.adjMat = self.adjMat
    topo_sort = []
    delete = []
    
    while len(copy.Vertices) > 0:
      idx = 0
      
      while idx < len(copy.Vertices):
        visited = False
        vertex = copy.Vertices[idx].label
        
        for i in range(len(copy.Vertices)):
          if copy.adjMat[i][idx] == 1:
            visited = True
            break
          
        if visited:
          idx +=1
          
        else:
          
          topo_sort.append(vertex)
          delete.append(vertex)
          idx+=1
          
      while len(delete) > 0:
        copy.delete_vertex(delete[0])
        delete.pop(0)
        
    return topo_sort
    
    
                 
    
def main():
  # create the Graph object
  theGraph = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    vert = line.strip()
    #print (city)
    theGraph.add_vertex (vert)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)
  #print (num_edges)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    #print (edge)
    edge = edge.split()
    start = theGraph.get_index(edge[0])
    finish = theGraph.get_index(edge[1])
    #weight = theGraph.get_index(edge[2])

    theGraph.add_directed_edge (start, finish)

  
  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
    print ("The Graph has a cycle.")
  else:
    print ("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)

  
  
if __name__ == "__main__":
  
  main()

