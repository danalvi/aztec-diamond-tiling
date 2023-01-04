import diamond as Aztec
import tiling

grid = Aztec.Diamond(8)

### definition 1

# grid.E[frozenset({(-6,5),(-6,4)})].w[-1] = 0

# grid.E[frozenset({(-6,4),(-6,3)})].w[-1] = 0
# grid.E[frozenset({(-6,3),(-6,2)})].w[-1] = 0
# grid.E[frozenset({(-6,2),(-6,1)})].w[-1] = 0
# grid.E[frozenset({(-6,1),(-6,0)})].w[-1] = 0
# grid.E[frozenset({(-6,0),(-6,-1)})].w[-1] = 0
# grid.E[frozenset({(-6,-1),(-6,-2)})].w[-1] = 0
# grid.E[frozenset({(-6,-2),(-6,-3)})].w[-1] = 0

# grid.E[frozenset({(-6,-3),(-6,-4)})].w[-1] = 0
# grid.E[frozenset({(-6,-4),(-6,-5)})].w[-1] = 0
# #tiling.weight_computation(grid)
# grid.E[frozenset({(-6,-5),(-5,-5)})].w[-1] = 0

# grid.E[frozenset({(-5,-5),(-4,-5)})].w[-1] = 0
# grid.E[frozenset({(-4,-5),(-3,-5)})].w[-1] = 0
# grid.E[frozenset({(-3,-5),(-2,-5)})].w[-1] = 0

# grid.E[frozenset({(-2,-5),(-1,-5)})].w[-1] = 0
# grid.E[frozenset({(-1,-5),( 0,-5)})].w[-1] = 0
# grid.E[frozenset({( 0,-5),( 1,-5)})].w[-1] = 0
# grid.E[frozenset({( 1,-5),( 2,-5)})].w[-1] = 0

# grid.E[frozenset({( 2,-5),( 3,-5)})].w[-1] = 0
# grid.E[frozenset({( 3,-5),( 4,-5)})].w[-1] = 0
# grid.E[frozenset({( 4,-5),( 5,-5)})].w[-1] = 0
# grid.E[frozenset({( 5,-5),( 6,-5)})].w[-1] = 0
# grid.E[frozenset({( 6,-5),( 7,-5)})].w[-1] = 0

# grid.E[frozenset({( 7,-5),(7,-4)})].w[-1] = 0
# grid.E[frozenset({( 7,-4),(7,-3)})].w[-1] = 0
# grid.E[frozenset({( 7,-3),(7,-2)})].w[-1] = 0
# grid.E[frozenset({( 7,-2),(7,-1)})].w[-1] = 0
# grid.E[frozenset({( 7,-1),(7, 0)})].w[-1] = 0
# grid.E[frozenset({( 7, 0),(7, 1)})].w[-1] = 0
# grid.E[frozenset({(7, 1), (6,1)})].w[-1] = 0
# grid.E[frozenset({(6, 1), (5,1)})].w[-1] = 0
# grid.E[frozenset({(5, 1), (4,1)})].w[-1] = 0
# grid.E[frozenset({(4, 1), (4,2)})].w[-1] = 0

# grid.E[frozenset({(4, 2),(3,2)})].w[-1] = 0
# grid.E[frozenset({(3, 2),(3,3)})].w[-1] = 0
# grid.E[frozenset({(3, 3),(2,3)})].w[-1] = 0
# grid.E[frozenset({(1, 3),(2,3)})].w[-1] = 0
# grid.E[frozenset({(1,3),(1,4)})].w[-1] = 0
# grid.E[frozenset({(1,5),(1,4)})].w[-1] = 0
# grid.E[frozenset({(1,5),(0,5)})].w[-1] = 0
# grid.E[frozenset({(-1,5),(0,5)})].w[-1] = 0
# grid.E[frozenset({(-1,5),(-2,5)})].w[-1] = 0
# grid.E[frozenset({(-2,5),(-3,5)})].w[-1] = 0
# grid.E[frozenset({(-3,5),(-4,5)})].w[-1] = 0
# grid.E[frozenset({(-4,5),(-5,5)})].w[-1] = 0
# grid.E[frozenset({(-5,5),(-6,5)})].w[-1] = 0


## definition 2

grid.E[frozenset({(0,0),(0,-1)})].w[-1] = 0
grid.E[frozenset({(0,0),(-1,0)})].w[-1] = 0
grid.E[frozenset({(0,1),(-1,1)})].w[-1] = 0
grid.E[frozenset({(0,2),(-1,2)})].w[-1] = 0
grid.E[frozenset({(0,2),(0,3)})].w[-1] = 0
grid.E[frozenset({(1,2),(1,3)})].w[-1] = 0
grid.E[frozenset({(2,2),(2,3)})].w[-1] = 0
grid.E[frozenset({(2,2),(3,2)})].w[-1] = 0
grid.E[frozenset({(2,1),(3,1)})].w[-1] = 0
grid.E[frozenset({(2,0),(3,0)})].w[-1] = 0
grid.E[frozenset({(2,0),(2,-1)})].w[-1] = 0
grid.E[frozenset({(1,0),(1,-1)})].w[-1] = 0

tiling.weight_computation(grid)