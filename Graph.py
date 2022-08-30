#  File: Graph.py

#  Description:A23

#  Student Name:Mark Borjas

#  Student UT EID:mab7886 

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created:11/28/20

#  Date Last Modified:11/29/20
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
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

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
    vertex = self.Vertices[vertexIndex]
    for i in range(len(vertex)):
      if vertex[i] != 0:
        neighbors.append(vertex[i])
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

  

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
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
    del self.Vertices[vertexIndex]
    del self.adjMat[vertexIndex]

    for i in range (len(self.Vertices)):
      del self.adjMat[i][vertexIndex]

def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    #print (city)
    cities.add_vertex (city)

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
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()
  #print (start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  #print (start_index)

  # test depth first search
  print ("\nDepth First Search from " + start_vertex)
  cities.dfs (start_index)
  #print ()

  # test breadth first search
  print("\nBreadth First Search")
  cities.bfs(start_index)
  # test deletion of an edge
  del_edges = sys.stdin.readline().strip().split()
  print("\nDeletion of an edge")
  cities.delete_edge(del_edges[0],del_edges[1])
  

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print ()
  #print ()

  # test deletion of a vertex
  print("\nDeletion of a vertex")
  del_vertex = sys.stdin.readline().strip()
  cities.delete_vertex(del_vertex)
  num_vertices -= 1

  
  #print Vertices
  print("\nList of Vertices")
  for i in cities.Vertices:
    print(i)
  #print()

  #print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()
if __name__ == "__main__":
  main()

