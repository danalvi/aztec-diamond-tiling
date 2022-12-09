
import matplotlib.pyplot as plt

class Diamond :
    def __init__(self, n): # n is the order of the Aztec Diamond
        self.n = n
        self.D = [ [(x,y) for x in range(-n, n + 1) for y in range(-n - 1, n + 1) if x + y == i and abs(x - y) <= n ] for i in range(-n + 1, n + 2)   ] # D^{k}_{n} as defined on [1] p. 11
        self.__D_blk = sum([ self.D[i] for i in range(0, 2*self.n + 1, 2 )], [])
        self.__D_red = sum([ self.D[i] for i in range(1, 2*self.n, 2 )], [])
        self.V = sum(self.D, [])
        self.__m = 5
        # Faces

        self.__grey_faces  = set(sum([ self.D[i] for i in range(0, 2*self.n, 2 )], [] ))                   # bottom left coordinates of grey faces, decided to keep it private as it's a messy/internal representation
        self.__white_faces = set(sum([ self.D[i][1 : self.n ] for i in range(1, 2*self.n - 1, 2 )], [] ))  # bottom left coordinates of white faces; ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
        self.grey_faces = set([self.__face(x, True) for x in self.__grey_faces ])
        self.white_faces = set([self.__face(x, False) for x in self.__white_faces ])
        self.faces = self.grey_faces.union(self.white_faces)

        # Edges

        self.E = set({})

        for face in self.grey_faces :               # adding the edges of the grey faces is sufficient to have all edges. However, these are direcfed
            self.E = self.E.union(face.edges)

    class __face :                                  # This class will remain private ... hidden far from sight
        def __init__(self, bottom_left, isCheck) :
            self.bottom_left = bottom_left                                    # We will identify each face with its bottom left coordinate
            self.isCheck = isCheck
            x, y = self.bottom_left                                       # Weather it is colored light grey or not in the chessboard checkering
            self.corners = [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]
            self.edges = set({ self.edge(((x, y), (x + 1, y))),
                               self.edge(((x + 1, y), (x + 1, y + 1) )),
                               self.edge(((x + 1, y + 1), (x, y + 1) )),
                               self.edge(((x, y + 1), (x,y)))  } )

        def edge(self, e) :
            parent = self
            class edge :
                def __init__(self, e) :
                    self.e = e
                    self.parent = parent
            return edge(e)

        def get_poly(self) :                        # This shall return the face as a polygon in anticlockwise starting from bottom left coordrinate
            x, y = self.bottom_left
            return [x, x + 1, x + 1, x ], [y, y, y + 1, y + 1]

    def plot_board(self, checker = True, edges = False, dotsVisible = True) :                  # This plots the underlying board. When the matching algorithm is implemented we will write the Aztec Diamond with domino plot
        X_red, Y_red = list(zip(*self.__D_red))
        X_blk, Y_blk = list(zip(*self.__D_blk))

        plt.figure(figsize=(7, 7))

        if checker :
            for grey_face in self.grey_faces :
                X, Y = grey_face.get_poly()
                plt.fill(X,Y, color = 'lightgrey')

        if edges :
            for (u1,v1), (u2,v2) in self.E :
                plt.plot([u1,u2], [v1, v2], color = 'lightgrey', linewidth = 0.5)

        # # This is only for debugging purposes (to see the white faces, colored blue for visibility )

        # for face in self.faces :
        #     X, Y = face.get_poly()
        #     plt.fill(X,Y, color = 'lightblue')

        alpha_ = 1
        if not dotsVisible :
            alpha_ = 0

        plt.scatter(X_blk,Y_blk, color = 'black', alpha = alpha_ )
        plt.scatter(X_red,Y_red, color = 'red', alpha = alpha_)
        plt.axis('off')
        plt.show()
