import diamond as Aztec
import tiling


## defn with onur

n = 2**4  # even please
grid = Aztec.Diamond(n)
for i in range(int(-n**(2/4)),int(n**(2/4))) :
    grid.E[frozenset({(-int(n**(2/4)), i),   (-int(n**(2/4))-1,i)})].w[-1] = 0
    grid.E[frozenset({(int(n**(2/4)) - 1,i), (int(n**(2/4)),i)})].w[-1] = 0

for i in range(int(-n**(2/4)),int(n**(2/4))) :
    grid.E[frozenset({(i,-int(n**(2/4))),     (i, -int(n**(2/4))-1)})].w[-1] = 0
    grid.E[frozenset({(i, int(n**(2/4)) - 1), (i,int(n**(2/4)))})].w[-1] = 0

tiling.weight_computation(grid)
M, _ = tiling.generate_matching(grid, energy=False)

grid.plot_board(matching= M, domino = True)
