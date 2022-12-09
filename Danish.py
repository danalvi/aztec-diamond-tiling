
import matplotlib.pyplot as plt
class Diamond :
    def __init__(self, n): # n is the order of the Aztec Diamond
        self.n = n
        self.D = [ [(x,y) for x in range(-n, n + 1) for y in range(-n - 1, n + 1) if x + y == i and abs(x - y) <= n ] for i in range(-n + 1, n + 2)   ] # D^{k}_{n} as defined on [1] p. 11
        self.__D_blk = sum([ self.D[i] for i in range(0, 2*self.n + 1, 2 )], [])
        self.__D_red = sum([ self.D[i] for i in range(1, 2*self.n, 2 )], [])
        self.V = sum(self.D, [])
        self.__grey_faces  = set(sum([ self.D[i] for i in range(0, 2*self.n, 2 )], [] )) # bottom left coordinates of grey faces
        self.__white_faces = set(self.V) - self.__grey_faces                               # bottom left coordinates of white faces
        self.grey_faces = set([self.__face(x, True) for x in self.__grey_faces ])
        self.white_faces = set([self.__face(x, False) for x in self.__white_faces ])
        self.faces = self.grey_faces.union(self.white_faces)

    class __face :                           # This class will remain private ... hidden far from sight
        def __init__(self, bottom_left, isCheck) :
            self.bottom_left = bottom_left # We will identify each face with its bottom left coordinate
            self.isCheck = isCheck         # Weather it is colored light grey or not in the chessboard checkering
        def get_poly(self) :                     # This shall return the face as a polygon in anticlockwise starting from bottom left coordrinate
            x, y = self.bottom_left
            return [x, x + 1, x + 1, x ], [y, y, y + 1, y + 1]
    def plot(self, checker = True) :
        X_red, Y_red = list(zip(*self.__D_red))
        X_blk, Y_blk = list(zip(*self.__D_blk))

        plt.figure(figsize=(7, 7))

        for grey_face in self.grey_faces :
            X, Y = grey_face.get_poly()
            plt.fill(X,Y, color = 'lightgrey')

        plt.scatter(X_blk,Y_blk, color = 'black')
        plt.scatter(X_red,Y_red, color = 'red')
        plt.axis('off')
        plt.show()
    # Add checkboard tomorrow
