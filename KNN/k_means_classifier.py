import math
import sys
from collections import defaultdict

#returns Euclidean distance between datapoints
def Euclidean(p1,p2):
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

#running epochs
def train(data_points,seeds):
    clusters=defaultdict(list)
    for i in data_points:
        min_seed=[]
        min_dist=sys.maxsize
        for j in range(0,len(seeds)):
            if(min_dist>Euclidean(i,seeds[j])):
                min_dist=Euclidean(i,seeds[j])
                min_seed_index=j
        clusters[min_seed_index].append(i)
    print ("\nClusters ::\n")
    for val in clusters.values():
        print (val)

    for key,val in clusters.items():
        x=0
        y=0
        for j in val:
            x+=j[0]
            y+=j[1]
        seeds[key][0]=x/len(val)
        seeds[key][1]=y/len(val)
    return seeds



#getting No of Data Points
n=int(input())
data_points=[]
for i in range(1,n+1):
    #getting i th data point
    point=input()
    p=point.split(" ");
    p=list(map(int,p))
    data_points.append(p);

seeds=[]
#getting No of Seed points
n=int(input())
for i in range(1,n+1):
    #getting i th seed point
    seed=input()
    s=seed.split(" ");
    s=list(map(int,s))
    seeds.append(s);

#getting No of epochs
epochs=int(input())
for i in range(0,epochs):
    print (i+1," epoch\n")
    seeds=train(data_points,seeds)
    print ("\nNew Centroids\n")
    print (seeds)
    print ("=========================================\n")
