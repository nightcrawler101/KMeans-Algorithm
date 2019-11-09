# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print ("hello world")
import math
import copy

listOfPoints=[[12.5,13.6],[12,19.9],[12,13],[16.67,12.24],[33.3,22.2],[20,20],[15,12],[16,16],[19.9,20.9],[14,4],[15.5,13.5],[18,19.5]] #points considered
noOfClusters=(int)(input("Enter number of clusters: "))

i,j,difference,absoluteDifference,total,sumTotal,p=0,0,0,0,0,0,0 #total variables required
k=1
centroids=[]
clusterDistance=[]
clusterList=[]
commonCluster=[]
newCentroids=[]

while i < noOfClusters:
    print(listOfPoints)
    index=(int)(input("Enter centroid index from list of points above"))
    centroids.append(listOfPoints[index])
    del(listOfPoints[index])
    i=i+1
    
print("Centroids", centroids)
newCentroids=copy.deepcopy(centroids)#nested list hence deep copy

print("List Of Points: ",listOfPoints)

while True:
    for point in listOfPoints:
        for centroid in centroids:
            while i <len(point) and j<len(centroid):
                absoluteDifference+=(point[i]-centroid[j])**2#finding differenece square
                i=i+1
                j=j+1        
            i,j=0,0
            distance=math.sqrt(absoluteDifference)#calculating square root of difference square to get result
            clusterDistance.append(distance)
            absoluteDifference=0
        clusterList.append(clusterDistance.index(min(clusterDistance)))#taking the minimum of cluster distance (distance of point from all centroids) and storing it in cluster list
        clusterDistance=[]
        
    clusterSet=set(clusterList)#to get unique value of cluster ids present
    print("List:",clusterList)
    print("Set: ",clusterSet)
      
    for i in clusterSet:
       for j in range(len(clusterList)):
           if i==clusterList[j]:
               commonCluster.append(listOfPoints[j])#all points belonging to same cluster ID taken in one list
       print(commonCluster)
        
                             
       for a in range(len(newCentroids)):#newCentroids-list containing complete centroids
               for t in range(len(newCentroids[a])):#taking one list at a time in newCentroids
                   for b in range(len(commonCluster)):#contains list of all points belonging to one cluster
                       for u in range(len(commonCluster[b])):#taking one list at a time in commonCluster
                           if t==u and a==p:#adding respective X,Y,Z.. coorindates and taking one list at a time from newCentroids 
                               k=k+1
                               newCentroids[a][t]+=commonCluster[b][u]
                           u=u+1
                       b=b+1   
                   newCentroids[a][t]/=k#sum is divided by total number of points in the cluster
                   k=1
                   t=t+1
               a=a+1
       p=p+1 #in newCentroids we have all the centroids present, but since we have to traverse each centroid listone after the other this comes in handy  
       k=1
       commonCluster=[]#for a new cluster of points belonging to one centroid
           
    print("New Centroids:",newCentroids)
    if centroids==newCentroids:
        break
    else:
        centroids=copy.deepcopy(newCentroids)#nested list
        clusterList=[]
        p=0
        k=1
    
    
                           
                       
                       
          
     
      
            
                
            
            
        
            
                
        
        
        
        
        
        
        
    


        
        
        
        
            
        
    





    
    
    





