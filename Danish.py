
import matplotlib.pyplot as plt
class Diamond :
    def __init__(self, n): # n is the order of the Aztec Diamond
        self.n = n
        self.D = [ [(x,y) for x in range(-n, n + 1) for y in range(-n - 1, n + 1) if x + y == i and abs(x - y) <= n ] for i in range(-n + 1, n + 2)   ] # D^{k}_{n} as defined on [1] p. 11

    class Face :
            # To be done tomorrow
    def plot(self) :
        D_blk = sum([ self.D[i] for i in range(0, 2*self.n + 1, 2 )], [])
        D_red = sum([ self.D[i] for i in range(1, 2*self.n, 2 )], [])

        X_red, Y_red = list(zip(*D_red))
        X_blk, Y_blk = list(zip(*D_blk))

        plt.figure(figsize=(7, 7))
        plt.scatter(X_blk,Y_blk, color = 'black')
        plt.scatter(X_red,Y_red, color = 'red')
        plt.axis('off')
        plt.show()


grid = Diamond(4)
grid.plot()
