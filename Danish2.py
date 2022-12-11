import math
import Danish as Aztec

n = 2

def isActive(face, m) :    # Observe that active face with bottom left corner at (0,0) is supposed to be lightgrey when m odd, even otherwise
        i, j = face.bottom_left
        if m % 2 == 0 :
            return ((i + j) % 2 != 0)
        else :
            return ((i + j) % 2 == 0)

def e_(edge) : # e'
    face = edge.parent
    edges = face.edges
    i = edges.index(edge)
    return edges[(i + 2) % 4]

grid = Aztec.Diamond(n)

Am_boundary = [face for face in list(grid.faces.values()) if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == n - 1   ]

for face in Am_boundary :
    face.DP.append(2)
    for e in face.edges :
        e.w.append(1)

for k in range(n, 0, -1) :
    Am = grid.get_Am(k - 1)
    for face in Am :
        (i, j) = face.bottom_left
        if (i + j - k) % 2 == 0 :
            e1 = face.edges[0]      # Edges are in anticlockwise order so two consecutive edges are adjacent
            e2 = face.edges[1]

            alpha = e_(e1).w[-1]
            gamma = e1.w[-1]
            beta = e2.w[-1]
            delta = e_(e2).w[-1]

            face.DP.append(e1.w[-1]*e_(e1).w[-1] + e2.w[-1]*e_(e2).w[-1])
            e1.w.append(alpha/face.DP[-1])
            e_(e1).w.append(gamma/face.DP[-1])
            e2.w.append(delta/face.DP[-1])
            e_(e2).w.append(beta/face.DP[-1])

outer_faces = [face for face in grid.get_Am(1) if isActive(face, 1)   ]
#outer_faces = [face for face in grid.faces if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == 4 - 1   ]
for of in outer_faces :
    for e in of.edges :
        print(e.w)

grid.plot_board()

#
# outer_faces = [face for face in grid.faces if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == 2 and isActive(face, 2)   ]
# print(outer_faces)

# for m in range(n - 1, 0, -1) :
#     Am_faces = grid.get_Am(m)
