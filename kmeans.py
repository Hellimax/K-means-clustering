import numpy as np #importing the essential modules
import matplotlib.pyplot as plt

data = 10+(50-10)*np.random.random((2,1000)) #creating a random data sets

data = np.round(data)

c1x,c1y = data[0,0],data[1,0] #taking random points 
c2x,c2y = data[0,1],data[1,1]
c3x,c3y = data[0,2],data[1,2]
c4x,c4y = data[0,3],data[1,3]

plt.ion() #creating a figure to plot the graph
plt.figure(1)
for j in range(20):
    c11x=[]
    c11y=[]
    c22x=[]
    c22y=[]
    c33x=[]
    c33y=[]
    c44x=[]
    c44y=[]
    plt.cla()
    
    for i in range(1000):
        d=[]
        d1=np.sqrt((data[0,i]-c1x)**2+(data[1,i]-c1y)**2)
        d2=np.sqrt((data[0,i]-c2x)**2+(data[1,i]-c2y)**2)
        d3=np.sqrt((data[0,i]-c3x)**2+(data[1,i]-c3y)**2)
        d4=np.sqrt((data[0,i]-c4x)**2+(data[1,i]-c4y)**2)
        d.append(d1)
        d.append(d2)
        d.append(d3)
        d.append(d4)
        minm = min(d)
        
        if d1==minm:
            c11x.append(data[0,i])
            c11y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],"r*")
        elif d2==minm:
            c22x.append(data[0,i])
            c22y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],"g*")
        elif d3==minm:
            c33x.append(data[0,i])
            c33y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],"c*")
        elif d4==minm:
            c44x.append(data[0,i])
            c44y.append(data[1,i])
            plt.plot(data[0,i],data[1,i],"m*")
    plt.plot(c1x,c1y,"ks") #plotting the points to visualise the working of the algorithm
    plt.plot(c2x,c2y,"ks")
    plt.plot(c3x,c3y,"ks")
    plt.plot(c4x,c4y,"ks")
    c1x = sum(c11x)/len(c11x)
    c1y = sum(c11y)/len(c11y)
    c2x = sum(c22x)/len(c22x)
    c2y = sum(c22y)/len(c22y)
    c3x = sum(c33x)/len(c33x)
    c3y = sum(c33y)/len(c33y)
    c4x = sum(c44x)/len(c44x)
    c4y = sum(c44y)/len(c44y)
    plt.title("iter"+str(j+1))
    plt.pause(0.1)
