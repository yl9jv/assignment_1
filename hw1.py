# Name: Yicheng Liang
# Computing ID: yl9jv

import math

k = raw_input("Please enter the value for k: ")
while (not k.isdigit()):
    k = raw_input("Please enter a number for k: ")
k = int(k)
    
m = raw_input("Please enter the value for M: ")
while (not m.isdigit()):
    m = raw_input("Please enter a number for M: ")
m = int(m)

items = []

filename = raw_input("Please enter the file name: ")
f = open(filename, 'r')
while (m > 0):
    line = f.readline()
    if line == "":
        break
    else:
        m -= 1
        temp = line.split()
        items.append((temp[0], float(temp[1]), float(temp[2])))

new_item = raw_input("Please enter the values for x and y: ")
temp = new_item.split()
x = float(temp[0])
y = float(temp[1])

while (x != 1.0 and y != 1.0):
    neighbors = []

    for item in items:
        distance = math.sqrt(math.pow((x - item[1]), 2) + math.pow((y - item[2]), 2))
        neighbors.append((item[0], item[1], item[2], distance))
    
    neighbors = sorted(neighbors, key=lambda a:a[3])
    counter = 0
    cat1 = ""
    cat2 = ""
    num_cat1 = 0
    num_cat2 = 0
    cat1_distance = 0
    cat2_distance = 0
    print "(1) nearest neighbors: "
    k_NN = []
    while counter != k:
        print neighbors[counter]
        if cat1 == "":
            cat1 = neighbors[counter][0]
            num_cat1 += 1
            cat1_distance += neighbors[counter][3]
        elif (cat1 != neighbors[counter][0] and cat2 == ""):
            cat2 = neighbors[counter][0]
            num_cat2 += 1
            cat2_distance += neighbors[counter][3]
        elif cat1 == neighbors[counter][0]:
            num_cat1 += 1
            cat1_distance += neighbors[counter][3]
        elif cat2 == neighbors[counter][0]:
            num_cat2 += 1
            cat2_distance += neighbors[counter][3]
        counter += 1
        k_NN.append(neighbors[counter])
    print ''
    
    if num_cat1 < num_cat2:
        print "(2)point classified as: " + cat2
    else:
        print "(2)point classified as: " + cat1
    print ''
    
    print "(3) average distance from " + cat1 + " is: " + str(cat1_distance / num_cat1)
    print " average distance from " + cat2 + " is: " + str(cat2_distance / num_cat2)
    print ""
    print ""
    
    new_item = raw_input("Please enter the values for x and y: ")
    temp = new_item.split()
    x = float(temp[0])
    y = float(temp[1])
