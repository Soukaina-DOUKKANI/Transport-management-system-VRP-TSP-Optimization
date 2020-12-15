import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy.random as rnd
import pandas as pd 

nodes_distances={
 (1, 1): 0,
 (1, 2): 252,
 (1, 3): 244,
 (1, 4): 323,
 (1, 5): 574,
 (1, 6): 530,
 (1, 7): 1396,
 (1, 8): 851,
 (1, 9): 498,
 (1, 10):432,
 (2, 1): 252,
 (2, 2): 0,
 (2, 3): 468,
 (2, 4): 547,
 (2, 5): 798,
 (2, 6): 754,
 (2, 7): 1168,
 (2, 8): 1075,
 (2, 9): 663,
 (2, 10): 204,
 (3, 1): 244,
 (3, 2): 468,
 (3, 3): 0,
 (3, 4): 87.1,
 (3, 5): 338,
 (3, 6): 294,
 (3, 7): 1616,
 (3, 8): 615,
 (3, 9): 535,
 (3, 10):648,
 (4, 1): 323,
 (4, 2): 547,
 (4, 3): 87.1,
 (4, 4): 0,
 (4, 5): 251,
 (4, 6): 207,
 (4, 7): 1696,
 (4, 8): 528,
 (4, 9): 471,
 (4, 10):728,
 (5, 1): 574,
 (5, 2): 798,
 (5, 3): 338,
 (5, 4): 251,
 (5, 5): 0,
 (5, 6): 399,
 (5, 7): 1943,
 (5, 8): 719,
 (5, 9): 662,
 (5, 10): 979,
 (6, 1): 530,
 (6, 2): 754,
 (6, 3): 294,
 (6, 4): 207,
 (6, 5): 399,
 (6, 6): 0,
 (6, 7): 1904,
 (6, 8): 331,
 (6, 9): 350,
 (6, 10): 936,
 (7, 1): 1396,
 (7, 2): 1168,
 (7, 3): 1616,
 (7, 4): 1696,
 (7, 5): 1943,
 (7, 6): 1904,
 (7, 7): 0,
 (7, 8): 2223,
 (7, 9): 1839,
 (7, 10): 969,
 (8, 1): 851,
 (8, 2): 1075,
 (8, 3): 615,
 (8, 4): 528,
 (8, 5): 719,
 (8, 6): 331,
 (8, 7): 2223,
 (8, 8): 0,
 (8, 9): 553,
 (8, 10): 1257,
 (9, 1): 498,
 (9, 2): 663,
 (9, 3): 535,
 (9, 4): 471,
 (9, 5): 662,
 (9, 6): 350,
 (9, 7): 1839,
 (9, 8): 553,
 (9, 9): 0,
 (9, 10): 871,
 (10, 1): 432,
 (10, 2): 204,
 (10, 3): 648,
 (10, 4): 728,
 (10, 5): 979,
 (10, 6): 936,
 (10, 7): 969,
 (10, 8): 1257,
 (10, 9): 871,
 (10, 10): 0}

 #taking 1 the depot:
#compute : savings (=les economies) for each (i,j):
savings=dict()  #dictioanry to store savings (les economies) for each two nodes
for (i,j) in nodes_distances:
    if i==j: continue
    if j==1 or i==1: continue  
    if (i,j) in savings or (j,i) in savings: continue
    saving=nodes_distances[(i,1)]+nodes_distances[(j,1)]-nodes_distances[(i,j)]
    savings[(i,j)]=saving
    

#rank the savings:
savings_sorted={key:value for key,value in sorted(savings.items(), key=lambda item: item[1], reverse=True)}

#verify if a node is adjacent to the depot 1 
def adjacent_to_depot(l,i):
    if l[1]==i or l[-2]==i:
        return True 
    return False

#insert a node next to the depot
def insert_into_list(l,i,j):
    if l[1]==i:
        l.insert(1,j)
    elif l[-2]==i:
        l.insert(-1,j)

#l : list of nodes ordered 
l=[1,1]
first_node=list(savings_sorted.keys())[0]
for k in first_node:
    l.insert(1,k)  #insert the 1st element
#insert the rest
while len(l)<11:
    for (i,j) in savings_sorted:
        if i in l and j in l: continue
        for k,q in (i,j),(j,i):
            if adjacent_to_depot(l,k):
                insert_into_list(l,k,q)
                break

#list the arcs:
l_arcs=[(l[i],l[i+1]) for i in range(len(l)-1)]

def arcs():
    return (l_arcs)
    
nbr_nodes=10 
#nodes coordinates (randomly generated)
nodes_x=rnd.rand(nbr_nodes+1)
nodes_y=rnd.rand(nbr_nodes+1)


#plot nodes:

for i in l:
    plt.annotate(f'{i}',(nodes_x[i],nodes_y[i]))
plt.plot(nodes_x[1], nodes_y[1], c='r', marker='s')
plt.scatter(nodes_x[2:], nodes_y[2:], c='b',marker='s')
#plot the arcs:
for i, j in l_arcs:
    plt.plot([nodes_x[i], nodes_x[j]], [nodes_y[i], nodes_y[j]], c='g', zorder=0)
    output_dir = "C://Users/soukaina/Desktop/TMS/static"
    plt.savefig('{}/graph2.png'.format(output_dir))


def Cities(filepath):
	L=[]
	csv=pd.read_excel(filepath)
	for i in range (len(csv['villes'])):
         L.append(tuple((i+1,csv['villes'][i])))
	return L
