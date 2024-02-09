#0x09-island_perimeter
---
## Island Perimeter
- This Python function, island_perimeter(grid), calculates the perimeter of an island described in a grid. The grid is represented as a list of lists of integers, where:

- 0 represents water.
- 1 represents land.

### The following rules apply to the grid:

* Each cell in the grid is square, with a side length of 1 unit.
* Cells are connected horizontally or vertically, but not diagonally.
* The grid is rectangular, with its width and height not exceeding 100 units.
* The grid is completely surrounded by water.
* There is only one island (or nothing).
* The island doesn’t have any "lakes," meaning there is no water inside that isn’t connected to the water surrounding the island.