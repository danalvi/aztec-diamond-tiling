import math
import numpy as np
import matplotlib.pyplot as plt

class Diamond :
    def __init__(self, n): # n is the order of the Aztec Diamond
        self.n = n
        self.D = [ [(x,y) for x in range(-n, n + 1) for y in range(-n - 1, n + 1) if x + y == i and abs(x - y) <= n ] for i in range(-n + 1, n + 2)   ] # D^{k}_{n} as defined on [1] p. 11
        V = len(self.D)
        #self.w_m = math.pow(1 / math.pow(2,((self.n+1)*(self.n)/2)),(1/(V/2)))
        self.__D_blk = sum([ self.D[i] for i in range(0, 2*self.n + 1, 2 )], [])
        self.__D_red = sum([ self.D[i] for i in range(1, 2*self.n, 2 )], [])
        self.V = sum(self.D, [])
        self.__m = 5
        # Faces

        self.__grey_faces  = set(sum([ self.D[i] for i in range(0, 2*self.n, 2 )], [] ))                   # bottom left coordinates of grey faces, decided to keep it private as it's a messy/internal representation
        self.__white_faces = set(sum([ self.D[i][1 : self.n ] for i in range(1, 2*self.n - 1, 2 )], [] ))  # bottom left coordinates of white faces; ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
        self.grey_faces = set([self.__face(x, True) for x in self.__grey_faces ])
        self.white_faces = set([self.__face(x, False) for x in self.__white_faces ])

        F = self.grey_faces.union(self.white_faces)

        self.faces = dict()
        for f in F :
            self.faces[f.bottom_left] = f

        # Edges

        self.E = dict()

        for face in list(self.faces.values()) :                    # adding the edges of the grey faces is sufficient to have all edges. However, these are direcfed
            x, y = face.bottom_left
            self.E[frozenset({(x, y), (x + 1, y)})] = self.edge( {(x, y), (x + 1, y)})
            self.E[frozenset({(x + 1, y), (x + 1, y + 1)})] = self.edge( {(x + 1, y), (x + 1, y + 1)})
            self.E[frozenset({(x + 1, y + 1), (x, y + 1)})] = self.edge( {(x + 1, y + 1), (x, y + 1)})
            self.E[frozenset({(x, y + 1), (x, y)})] = self.edge( {(x, y + 1), (x, y)} )

        for face in list(self.faces.values()) :
            x, y = face.bottom_left
            face.edges = [  self.E[frozenset( {(x, y), (x + 1, y)})],
                            self.E[frozenset( {(x + 1, y), (x + 1, y + 1)})],
                            self.E[frozenset( {(x + 1, y + 1), (x, y + 1)})],
                            self.E[frozenset({(x, y + 1), (x, y)})]  ]



        self.V_h =  [(x,y) for x in range(-self.n - 1, self.n + 2) for y in range(-self.n - 1, self.n + 2) if abs(x) + abs(y) <= self.n + 1]
        self.E_h = dict()

    def height_function(self, matching) :
        visited = dict()

        for v in self.V_h :
            visited[v] = False

        queue = []
        queue.append((-self.n - 1, 0))
        visited[(-self.n - 1, 0)] = True

        def nbrs(i, j) :
            n = []
            if (-1)**(self.n + i + j) == 1 :
                return [(i, j + 1), (i, j - 1)]
            else :
                return [(i + 1, j), (i - 1, j)]

        # First BFS to construct the oriented edges

        while queue:
            (i,j) = queue.pop(0)
            N = [(i_,j_) for (i_,j_) in nbrs(i,j) if abs(i_) + abs(j_) <= self.n + 1  ]
            for (i_,j_) in N:
                if visited[(i_,j_)] == False:
                    self.E_h[((i,j),(i_,j_))] = 0
                    queue.append((i_,j_))
                    visited[(i_,j_)] = True
                else :
                    for (i_,j_) in N :
                        if ((i,j), (i_, j_)) not in self.E_h.keys() :
                            self.E_h[((i,j),(i_,j_))] = 0

        self.E_h[((3,0),(4,0))] = 0


            # Second BFS to return height function
        h = dict()       # V_h to Integer

        for v in self.V_h :
            visited[v] = False

        queue = []
        queue.append((-self.n - 1, 0))
        visited[(-self.n - 1, 0)] = True
        h[(- self.n - 1, 0 )] = 0   # normalize

        domino_edges_cross = set({}) # implemented internally as a hash table in python
        for ((u1, v1), (u2,v2)) in list(matching.keys()) :
            ((u1, v1), (u2,v2)) = ((u1 - 1/2, v1 - 1/2), (u2 - 1/2,v2 -1/2))
            if u1 == u2 :
                domino_edges_cross.add(frozenset({(u1 - 1/2, (v1+v2) /2 ), (u2 + 1/2, (v1+v2) /2 )}))
            if v1 == v2 :
                domino_edges_cross.add(frozenset({((u1+u2) /2, v1 - 1/2  ), ( (u1+u2)/2, v2 + 1/2 )}))

        while queue:
            (i,j) = queue.pop(0 )
            N = [(i_,j_) for (i_,j_) in nbrs(i,j) if abs(i_) + abs(j_) <= self.n + 1  ]
            for (i_,j_) in N:
                if visited[(i_,j_)] == False:
                    # check if crosses a domino, action in both cases
                    e = frozenset({(i,j), (i_,j_)})
                    if e in domino_edges_cross :
                        h[(i_,j_)] = h[(i,j)] - 3
                    else :
                        h[(i_,j_)] = h[(i,j)] + 1
                    queue.append((i_,j_))
                    visited[(i_,j_)] = True
            h[(self.n + 1,0)] = 0
        return h

    def get_Am(self, m) :
        return [face for face in list(self.faces.values()) if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) <= m - 1   ]
    
    def get_Am_boundary(self, m) :
        return [face for face in list(self.faces.values()) if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == m - 1   ]

    def __face(self, bottom_left, isCheck) :
        parent = self
        class __face :                                  # This class will remain private ... hidden far from sight
            def __init__(self, bottom_left, isCheck) :
                self.parent = parent
                self.bottom_left = bottom_left                                    # We will identify each face with its bottom left coordinate
                self.isCheck = isCheck
                self.edges = []
                self.DP = [None for _ in range(1, parent.n)] + [1]
            def get_poly(self) :                        # This shall return the face as a polygon in anticlockwise starting from bottom left coordrinate
                x, y = self.bottom_left
                return [x, x + 1, x + 1, x ], [y, y, y + 1, y + 1]
        return __face(bottom_left, isCheck)


    def edge(self, e) :
        parent = self
        class edge :
            def __init__(self, e) :
                self.e = e
                self.vec = None
                self.parent = parent
                self.w = [None for _ in range(1, parent.n)] + [1]
        return edge(e)

    def plot_board(self, checker = False, edges = False, dotsVisible = False, matching = dict(), domino = True, height = False, debug = False) :                  # This plots the underlying board. When the matching algorithm is implemented we will write the Aztec Diamond with domino plot
        X_red, Y_red = list(zip(*self.__D_red))
        X_blk, Y_blk = list(zip(*self.__D_blk))

        plt.figure(figsize=(10, 10))

        if checker :
            for grey_face in self.grey_faces :
                X, Y = grey_face.get_poly()
                plt.fill(X,Y, color = 'lightgrey')

        if edges :
            for edge in list(self.E.values()) :
                (u1,v1), (u2,v2) = edge.e
                plt.plot([u1,u2], [v1, v2], color = 'lightgrey', linewidth = 0.5)

        M = [tuple(edge.e) for edge in matching.values()]
        
        if M != [] and domino == False :
            for e in M :
                (u1, v1), (u2,v2) = e
                plt.plot([u1,u2], [v1, v2], color = 'red', linewidth = 1)
        elif M != [] and domino == True :
            for e in M :
                edgecol = 'black'
                if self.n > 70 :
                    edgecol = 'None'
                (u1, v1), (u2,v2) = sorted(e)       # (u1,v1) will be bottom left
                if v1 == v2 :                       # horizontal - check then non check (left to right)
                    if (u1 + v1 - self.n) % 2 == 0 :
                        X = [ u1 - (1/2), u1 - (1/2), u2 + (1/2), u2 + (1/2) ]
                        Y = [ v1 + (1/2), v1 - (1/2), v2 - (1/2), v2 + (1/2) ]
                        plt.fill(X,Y, color = 'red', edgecolor=edgecol)
                    else :                          # horizontal - noncheck then check (left to right)
                        X = [ u1 - (1/2), u1 - (1/2), u2 + (1/2), u2 + (1/2) ]
                        Y = [ v1 + (1/2), v1 - (1/2), v2 - (1/2), v2 + (1/2) ]
                        plt.fill(X,Y, color = 'blue', edgecolor=edgecol)
                if u1 == u2 :
                    if (u1 + v1 - self.n) % 2 == 0 :
                        X = [u1 - (1/2), u1 + (1/2), u2 + (1/2), u2 - (1/2)]
                        Y = [v1 - (1/2), v1 - (1/2), v2 + (1/2), v2 + (1/2)]
                        plt.fill(X,Y, color = 'green', edgecolor=edgecol)
                    else :
                        X = [u1 - (1/2), u1 + (1/2), u2 + (1/2), u2 - (1/2)]
                        Y = [v1 - (1/2), v1 - (1/2), v2 + (1/2), v2 + (1/2)]
                        plt.fill(X,Y, color = 'yellow', edgecolor=edgecol)
            if height :
                h = self.height_function(matching)
                V_h_shift = [(x + 1/2,y + 1/2) for (x,y) in self.V_h]
                V_h_label = [h[(u,v)] for (u,v) in self.V_h]
                X_height_lbl, Y_height_lbl = list(zip(*V_h_shift))

                for i, lbl in enumerate(V_h_label):
                    plt.annotate(lbl, (X_height_lbl[i], Y_height_lbl[i]))

        # For debugging only. This was to check if the orientation graph was right and therefore the BFS. This was a struggle.
        if debug  :
            E_h_translated = [((u1 +1/2,v1 + 1/2), ( u2 + 1/2, v2 + 1/2)) for ((u1,v1),(u2,v2)) in self.E_h.keys()]
            base_arrows, head_arrows = list(zip(*E_h_translated))
            head_arrows = tuple(np.array(head_arrows) - np.array(base_arrows))
            for i in range(len(base_arrows)) :
                plt.arrow(base_arrows[i][0], base_arrows[i][1], head_arrows[i][0], head_arrows[i][1], head_width=0.05, head_length=0.1, fc='k', ec='k', length_includes_head=True)

        # This is only for debugging purposes (to see the white faces, colored blue for visibility )

        # for face in self.faces :
        #     X, Y = face.get_poly()
        #     plt.fill(X,Y, color = 'lightblue')

        alpha_ = 1
        if not dotsVisible :
            alpha_ = 0

        plt.scatter(X_blk,Y_blk, color = 'black', alpha = alpha_ )
        plt.scatter(X_red,Y_red, color = 'red', alpha = alpha_)
        #plt.axis('off')
        plt.show()
