import math
import Danish as Aztec

def e_(face, edge) : # e'
    edges = face.edges
    i = edges.index(edge)
    return edges[(i + 2) % 4]

# Am_boundary = [face for face in list(grid.faces.values()) if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == n - 1   ]
#

def weight_computation(grid) :
    n = grid.n
    for k in range(n - 1, 0, -1) :
        Am = grid.get_Am(k)
        for face in Am :
            (i, j) = face.bottom_left
            if (i + j - k) % 2 == 0 :
                e1 = face.edges[0]      # Edges are in anticlockwise order so two consecutive edges are adjacent
                e2 = face.edges[1]

                alpha = e_(face, e1).w
                gamma = e1.w
                beta = e2.w
                delta = e_(face, e2).w

                face.DP.append(e_(face, e1).w*e1.w + e2.w*e_(face, e2).w)

                e1.w = alpha/grid.faces[(i - 1, j)].DP[-1]
                e_(face, e1).w = gamma/grid.faces[(i + 1, j)].DP[-1]
                e2.w = delta/grid.faces[(i, j + 1)].DP[-1]
                e_(face, e2).w = beta/grid.faces[(i, j - 1)].DP[-1]

import Danish2
grid = Aztec.Diamond(10)
weight_computation(grid)
grid.faces[(0,0)].edges[0].w # Returns the weight of first edge in clockwise order of face with bottm left corner at (0,0)
