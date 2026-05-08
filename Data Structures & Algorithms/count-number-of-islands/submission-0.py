class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        # get all indicies with 1's
        ones_idxs = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    ones_idxs.append((i,j))
        

        def dfs(grid, visited, i, j):
            if (i,j) in visited: return 0 # visited
            if i < 0 or i >= rows or j < 0 or j >= cols: return 0 # out of bounds
            if grid[i][j] != "1": return 0 # not land

            visited.add((i,j))

            neighs = [(i+1, j), (i-1, j), (i,j+1), (i,j-1)]
            for n in neighs:
                ni = n[0]
                nj = n[1]
                dfs(grid, visited, ni, nj)

            return 1



        visited = set()
        num_islands = 0
        for idx in ones_idxs:
            i = idx[0]
            j = idx[1]

            num_islands += dfs(grid, visited, i, j)


        return num_islands
