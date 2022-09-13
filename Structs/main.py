nodes = int(input("How many nodes are there? "))
elements = int(input("How many elements are there? "))
print("")
xcord = []
ycord = []

for i in range(nodes):
  x = float(input(f"Enter the x cordinate of node {i+1}: "))
  y = float(input(f"Enter the y cordinate of node {i+1}: "))
  print("")
  xcord.append(x)
  ycord.append(y)
# print(xcord)
# print(ycord)

start_node_of_ele = []
end_node_of_ele = []
length_of_ele = []

for i in range(elements):
  start = int(input(f"Enter the start node of element {i+1}: "))
  end = int(input(f"Enter the end node of element {i+1}: "))
  print("")
  start_node_of_ele.append(start)
  end_node_of_ele.append(end)
  x1 = xcord[start-1]
  y1 = ycord[start-1]
  x2 = xcord[end-1]
  y2 = ycord[end-1]
  length = float(((x2-x1)**2 + (y2-y1)**2)**0.5)
  length_of_ele.append(length)
# print(start_node_of_ele)
# print(end_node_of_ele)
# print(length_of_ele)

support_num = int(input("How many nodes have supports? "))
supcondition = ['P = pinned',
                'V = Vertical restrained (Horizontal is free to move)']
support_list = [0 for i in range(nodes)]
# print(f"support_list { support_list}")

for i in range(support_num):
  support_node = int(input("Enter the node number with support: "))
  for condition in supcondition:
    print(condition)
  support_condition = input("Enter the condition of the support: ")
  print("")
  if support_condition == "P":
      support_list[support_node-1] = "P"
  if support_condition == "V":
      support_list[support_node-1] = "V"
# print(f"support_list { support_list}")

x_loaded = [0 for i in range(nodes)]
y_loaded = [0 for i in range(nodes)]
loaded_nodes = int(input("How many of the nodes have a load? "))

for i in range(loaded_nodes):
    node_num = int(input("What is the node number with load? "))
    xload = int(input("What is the force on the x axis? "))
    x_loaded[node_num-1] = xload
    yload = int(input("What is the force on the y axis? "))
    print("")
    y_loaded[node_num-1] = yload
# print(x_loaded)
# print(y_loaded)

x_force = x_loaded
y_force = y_loaded

x_index_p = support_list.index("P")
y_index_p = support_list.index("P")
y_index_v = support_list.index("V")

tempx = 0
tempy = 0

for x in x_loaded:
    tempx += x
x_force[x_index_p] = -tempx

# Moment on node 1
x_cord = [0,5,5,0]
y_cord = [0,0,5,5]
moment_temp = 0

for node, val in enumerate(y_loaded):
    moment_temp += val * x_cord[node]
for node, val in enumerate(x_loaded):
    moment_temp += -(val * y_cord[node]) # problem here maybe

moment_force= float(moment_temp/x_cord[y_index_v])
y_force[y_index_v] = -moment_force

# Y force
for y in y_loaded:
    tempy += y
y_force[y_index_p] = tempy

# print(f"x force {x_force}")
# print(f"y force {y_force}")


print("The external forces of this truss are:")
for i in range(nodes):
    print(f"Node {i}: ({float(x_force[i])}, {float(y_force[i])})")




