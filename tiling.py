import math
import numpy as np
import diamond as Aztec

def e_(face, edge) : # e'
    edges = face.edges
    i = edges.index(edge)
    return edges[(i + 2) % 4]

# Am_boundary = [face for face in list(grid.faces.values()) if abs(face.bottom_left[0]) + abs(face.bottom_left[1]) == n - 1   ]


def weight_computation(grid) :
    n = grid.n 
    for k in range(n-1, -1, -1) :
        #print(k)
        Ak = grid.get_Am(k + 1)
        for face in Ak:
            (i, j) = face.bottom_left
            if ((i + j + (k + 1) ) % 2 != 0)  :
                #print(str(i) + ' ' + str(j) + ' ' + str(k+1))

                e1 = face.edges[0]      # Edges are in anticlockwise order so two consecutive edges are adjacent
                e2 = face.edges[1]

                alpha = e_(face, e1).w[k]
                gamma = e1.w[k]
                beta = e2.w[k]
                delta = e_(face, e2).w[k]
            
                if alpha == None :
                    print("Error for alpha for face " + str((i,j)) + " at step " + str(k))
                if beta == None :
                    print("Error at beta for face " + str((i,j)) + " at step " + str(k) + str(e2.w) )
                if delta == None :
                    print("Error at delta for face " + str((i,j)) + " at step " + str(k))
                if gamma == None :
                    print("Error at gamma for face " + str((i,j)) + " at step " + str(k))

                # Case 1

                face.DP[k] = alpha*gamma + beta*delta
                if face.DP[k] != 0 :
                    e_(face, e1).w[k-1] = gamma / face.DP[k]
                    e1.w[k-1] = alpha / face.DP[k]
                    e2.w[k-1] = delta / face.DP[k]
                    e_(face, e2).w[k-1] = beta / face.DP[k]
    #             else :
    #                 if (alpha + beta != 0) and delta == 0 and gamma == 0 :                    # Top right
    #                     e1.w[k-1] = alpha
    #                     e_(face, e1).w[k-1] = 1 / (alpha + beta)
    #                     e2.w[k-1] = 1 / (alpha + beta)
    #                     e_(face, e2).w[k-1] = beta
    #                 elif (delta + gamma != 0) and alpha == 0 and beta == 0 :                    # Bottom left
    #                     e1.w[k-1] = 1 / (delta + gamma)
    #                     e_(face, e1).w[k-1] = gamma
    #                     e2.w[k-1] = delta
    #                     e_(face, e2).w[k-1] = 1 / (delta + gamma)
    #                 elif (alpha + delta != 0) and gamma == 0 and beta == 0 :                    # Top left
    #                     e1.w[k-1] = alpha
    #                     e_(face, e1).w[k-1] = 1 / (alpha + delta)
    #                     e2.w[k-1] = delta
    #                     e_(face, e2).w[k-1] = 1 / (alpha + delta)
    #                 elif (gamma + beta != 0) and alpha == 0 and delta == 0 :                     # Bottom Right
    #                     e1.w[k-1] = 1 / (gamma + beta)
    #                     e_(face, e1).w[k-1] = gamma
    #                     e2.w[k-1] = 1 / (gamma + beta)
    #                     e_(face, e2).w[k-1] = beta
    #                 # Case 3
    #                 elif alpha == 0 and beta == 0 and delta == 0 and gamma == 0 :
    #                     e1.w[k-1] = 1 / math.sqrt(2)
    #                     e_(face, e1).w[k-1] = 1 / math.sqrt(2)
    #                     e2.w[k-1] = 1 / math.sqrt(2)
    #                     e_(face, e2).w[k-1] = 1 / math.sqrt(2)    
                
    # # STEP 2 -----------------------------------------------------------------------------------------------------------------------

    # for k in range(n - 1, 1, -1) :
    #     Ak = grid.get_Am(k + 1)
    #     for face in Ak:
    #         (i, j) = face.bottom_left
    #         if ((i + j + (k + 1) ) % 2 != 0)  :
    #             def is_in_Ak(edge, m):
    #                 (u1,v1) , (u2, v2) = sorted(edge.e)
    #                 return abs(u1 - 1/2) + abs(v1 - 1/2) <= m and abs(u2 - 1/2) + abs(v2 - 1/2) <= m
                
    #             def is_at_boundary(edge, m) :
    #                 if m < 1 :
    #                     print("m less than zero")
    #                     return           
    #                 (u1,v1) , (u2, v2) = edge.e
    #                 return ((abs(u1 - 1/2) + abs(v1 - 1/2) == m) and (abs(u2 - 1/2) + abs(v2 - 1/2) == m - 1)) or ((abs(u1 - 1/2) + abs(v1 - 1/2) == m - 1) and (abs(u2 - 1/2) + abs(v2 - 1/2) == m)) or ((abs(u1 - 1/2) + abs(v1 - 1/2) == m) and (abs(u2 - 1/2) + abs(v2 - 1/2) == m))

    #             e1 = face.edges[0]      # Edges are in anticlockwise order so two consecutive edges are adjacent
    #             e2 = face.edges[1]

    #             alpha = e_(face, e1).w[k]
    #             gamma = e1.w[k]
    #             beta = e2.w[k]
    #             delta = e_(face, e2).w[k]

    #             if alpha*gamma + beta*delta == 0 :

    #                 if (alpha == 0 and beta == 0) :
    #                     if (is_at_boundary(e_(face, e1), k + 1) and is_at_boundary(e2, k + 1) ) :
    #                         print("NOT TILEABLE!" + " for face " + str((i,j)) + " at step " + str(k))
    #                         return
    #                     elif (not is_at_boundary(e_(face, e1), k + 1) and not is_at_boundary(e2, k + 1) ) : 
    #                         swap_face = grid.faces[(i+1, j+1)]
    #                         if is_in_Ak(swap_face.edges[0], k) :
    #                             swap_face.edges[0].w[k-1] = 0
    #                         if is_in_Ak(swap_face.edges[3], k) :
    #                             swap_face.edges[3].w[k-1] = 0
                    
    #                 if (delta == 0 and gamma == 0) :
    #                     if (is_at_boundary(e_(face, e2), k + 1) and is_at_boundary(e1, k + 1)) :
    #                         print("NOT TILEABLE!" + " for face " + str((i,j)) + " at step " + str(k))
    #                         return
    #                     elif (not is_at_boundary(e_(face, e2), k + 1) and not is_at_boundary(e1, k + 1)) :
    #                         swap_face = grid.faces[(i-1, j-1)]
    #                         if is_in_Ak(swap_face.edges[1], k) :
    #                             swap_face.edges[1].w[k-1] = 0
    #                         if is_in_Ak(swap_face.edges[2], k) :
    #                             swap_face.edges[2].w[k-1] = 0

    #                 if (alpha == 0 and delta == 0) :
    #                     if (is_at_boundary(e_(face, e1), k + 1) and is_at_boundary(e_(face, e2), k + 1)) :
    #                         print("NOT TILEABLE!" + " for face " + str((i,j)) + " at step " + str(k))
    #                         return
    #                     elif (not is_at_boundary(e_(face, e1), k + 1) and not is_at_boundary(e_(face, e2), k + 1)) :
    #                         swap_face = grid.faces[(i-1, j+1)]
    #                         if is_in_Ak(swap_face.edges[0], k) :
    #                             swap_face.edges[0].w[k-1] = 0
    #                         if is_in_Ak(swap_face.edges[1], k) :
    #                             swap_face.edges[1].w[k-1] = 0 
                    
    #                 if (gamma == 0 and beta == 0) :
    #                     if (is_at_boundary(e1, k + 1) and is_at_boundary(e2, k + 1) ) :
    #                         print("NOT TILEABLE!" + " for face " + str((i,j)) + " at step " + str(k) )
    #                         return
    #                     elif (not is_at_boundary(e1, k + 1) and not is_at_boundary(e2, k + 1) ) :
    #                         swap_face = grid.faces[(i+1, j-1)]
    #                         if is_in_Ak(swap_face.edges[2], k ) :
    #                             swap_face.edges[2].w[k-1] = 0
    #                         if is_in_Ak(swap_face.edges[3], k) :
    #                             swap_face.edges[3].w[k-1] = 0


def generate_matching(grid, energy = False) :
    n = grid.n
    rng = np.random.default_rng()
    M = dict()

    for k in range(0, n) :
        #print(k)
        Am = grid.get_Am(k+1)     #   Get A_k's face
        for face in Am :
             (i, j) = face.bottom_left
             if (i + j + (k + 1) ) % 2 != 0 :

                alpha = face.edges[2]
                gamma = face.edges[0]
                beta  = face.edges[1]
                delta = face.edges[3]

                # Case 1
                if ((frozenset(alpha.e) in M) and (frozenset(gamma.e) in M ) ) : # or ((frozenset(beta.e) in M) or (frozenset(delta.e) in M)) ):
                    del M[frozenset(alpha.e)]
                    del M[frozenset(gamma.e)]
                elif ((frozenset(beta.e) in M) and (frozenset(delta.e) in M )) :
                    del M[frozenset(beta.e)]
                    del M[frozenset(delta.e)]
                 # Case 2
                elif (frozenset(alpha.e) in M) :
                    del M[frozenset(alpha.e)]
                    M[frozenset(gamma.e)] = gamma
                elif (frozenset(gamma.e) in M) :
                    del M[frozenset(gamma.e)]
                    M[frozenset(alpha.e)] = alpha
                elif (frozenset(beta.e) in M) :
                    del M[frozenset(beta.e)]
                    M[frozenset(delta.e)] = delta
                elif (frozenset(delta.e) in M) :
                    del M[frozenset(delta.e)]
                    M[frozenset(beta.e)] = beta
                elif ( (frozenset(alpha.e) not in M) and (frozenset(beta.e) not in M) and (frozenset(delta.e) not in M) and (frozenset(gamma.e) not in M) ) :
                    if (alpha.w[k]*gamma.w[k] + beta.w[k]*delta.w[k]) == 0 :
                        return generate_matching(grid)
                    if rng.random() < alpha.w[k]*gamma.w[k] / (alpha.w[k]*gamma.w[k] + beta.w[k]*delta.w[k]) :
                        M[frozenset(gamma.e)] = gamma
                        M[frozenset(alpha.e)] = alpha
                    else :
                        M[frozenset(delta.e)] = delta
                        M[frozenset(beta.e)] =  beta

        E = dict()
        
        if (energy) :
            for edge in list(M.keys()) :
                (u1, v1), (u2,v2) = sorted(tuple(edge)) 
                if v1 == v2 :                       # horizontal - check then non check (left to right)
                    if (u1 + v1 - grid.n) % 2 == 0 :
                        E[edge] = np.array([ 1, 0])
                    else :                          # horizontal - noncheck then check (left to right)
                        E[edge] = np.array([-1, 0]) 
                if u1 == u2 :
                    if (u1 + v1 - grid.n) % 2 == 0 :
                        E[edge] = np.array([0,  1])
                    else :
                        E[edge] = np.array([0, -1])

    return M, E
