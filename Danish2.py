import math
import Danish as Aztec

n = 10

def isActive(face, m) :    # Observe that active face with bottom left corner at (0,0) is supposed to be lightgrey when m odd, even otherwise
        i, j = face.bottom_left
        if m % 2 == 0 :
            return ((i + j) % 2 != 0)
        else :
            return ((i + j) % 2 == 0)

def e_(face, edge) : # e'
    edges = face.edges
    i = edges.index(edge)
    return edges[(i + 2) % 4]

grid = Aztec.Diamond(n)

# Am_boundary = [face for face in list(grid.faces.values()) if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == n - 1   ]
#

for k in range(n, 0, -1) :
    #Am = grid.get_Am(k)
    for face in list(grid.faces.values()) :
        (i, j) = face.bottom_left
        if (i + j - k) % 2 == 0 :
            e1 = face.edges[0]      # Edges are in anticlockwise order so two consecutive edges are adjacent
            e2 = face.edges[1]

            alpha = e_(face, e1).w
            gamma = e1.w
            beta = e2.w
            delta = e_(face, e2).w

            DP = alpha*gamma + beta*delta

            e1.w = alpha/DP
            e_(face, e1).w = gamma/DP
            e2.w = delta/DP
            e_(face, e2).w = beta/DP

print(grid.faces[(0,0)].edges[0].w)
#grid.plot_board()

#
# outer_faces = [face for face in grid.faces if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == 2 and isActive(face, 2)   ]
# print(outer_faces)

# for m in range(n - 1, 0, -1) :
#     Am_faces = grid.get_Am(m)
