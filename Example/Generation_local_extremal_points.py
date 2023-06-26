import numpy as np
import itertools as iter
#scenario indicates the number of outcomes for each input setting
#for example Scenario[0] means Alice has the outcome number 2,2,2 for each inputs
Scenario=[[2,2,2],[2,2,2]]
number_A_inputs=len(Scenario[0])
number_B_inputs=len(Scenario[1])
max_A_outcome=max(Scenario[0])
max_B_outcome=max(Scenario[1])
#Take an example of one local extremal points
#notation
# a,b: the maximum from Alice or Bob's outcomes
# x,y: the input number of Alice or Bob
#the local extremal points examples are (a,b,x,y)
example=np.zeros([max_A_outcome,max_B_outcome,number_A_inputs,number_B_inputs])
All_list=[];
###example[0,0,0,0]=1
###example[0,0,0,1]=1
###example=ple[0,0,1,0]=1
###example[0,0,1,1]=1
for x in range(number_A_inputs):
  for y in range(number_B_inputs):
    example[0,0,x,y]=1
####################################################################
print("the number of local extremal points",np.prod(Scenario[0])*np.prod(Scenario[1]))

A_index_list=[]
B_index_list=[]
#generate the indexes for python itertools
for i in Scenario[0]:
  A_index_list.append(np.arange(i))
for j in Scenario[1]:
  B_index_list.append(np.arange(j))

Extremal_points_list=[]
#A_indexes means the index for the certain outcome of the input
#for example (0,1,1) means the Alice first outcomes are 0,1,1 respecively
for A_indexes in iter.product(*A_index_list):
  for B_indexes in iter.product(*B_index_list):
    one_extremal_point=np.zeros((max_A_outcome,max_B_outcome,number_A_inputs,number_B_inputs))
    for x in range(len(A_indexes)):
      for y in range(len(B_indexes)):
        one_extremal_point[A_indexes[x],B_indexes[y],x,y]=1
    Extremal_points_list.append(one_extremal_point)

#print the first extremal points
print(Extremal_points_list[0])









