import diamond as Aztec
import tiling


## defn with onur

n = 2**8  # even please
grid = Aztec.Diamond(n)
# for i in range(int(-n**(1/2)),int(n**(1/2))) :
#     grid.E[frozenset({(-int(n**(1/2)), i),   (-int(n**(1/2))-1,i)})].w[-1] = 0
#     grid.E[frozenset({(int(n**(1/2)) - 1,i), (int(n**(1/2)),i)})].w[-1] = 0

# for i in range(int(-n**(1/2)),int(n**(1/2))) :
#     grid.E[frozenset({(i,-int(n**(1/2))),     (i, -int(n**(1/2))-1)})].w[-1] = 0
#     grid.E[frozenset({(i, int(n**(1/2)) - 1), (i,int(n**(1/2)))})].w[-1] = 0

tiling.weight_computation(grid)
M, _ = tiling.generate_matching(grid, energy=False)

grid.plot_board(matching= M, domino = True)
