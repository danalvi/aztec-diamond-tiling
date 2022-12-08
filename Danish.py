import math
import matplotlib.pyplot as plt

n=5

V = [ (x,y) for x in range(-n, n + 1) for y in range(-n, n + 1) if abs( x - (1/2)) + abs(y - 1/2)  <= 5  ]
V_ = [(x,y) for x in range(-n,n + 1) for y in range(-n,n+1) if x + y == 6 and abs(x-y) <= 5 ]
#print(V)
X = [i for (i,j) in V]
Y = [j for (i,j) in V]

X_ = [i for (i,j) in V_]
Y_ = [j for (i,j) in V_]

plt.figure(figsize=(7, 7))
#plt.plot([1,1], [2,3])
#plt.fill([1,1,2,2],[1,2,2,1], facecolor='lightgrey')
plt.scatter(X,Y, color = 'red')
plt.scatter(X_,Y_, color = 'black')
#plt.axis('off')
plt.show()
print(V)

class Diamond :
    def __init__(self, order):
        self.order = order
     V = [ (x,y) for x in range(-n, n + 1) for y in range(-n, n + 1) if abs( x - (1/2)) + abs(y - 1/2)  <= 5  ]
