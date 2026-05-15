class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        # get ones
        ones_idx = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ones_idx.append((i,j))

        if len(ones_idx) == 1:
            return 4


        def dfs(grid, visited, i, j):
            if (i,j) in visited: 
                return 0

            visited.add((i,j))

            perimiter = 0
            neighs = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for ni, nj in neighs:
                
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 0:
                    perimiter += 1
                    continue
                
                new_perimiter = dfs(grid, visited, ni, nj)
                perimiter += new_perimiter


            return perimiter


        s_i = ones_idx[0][0]
        s_j = ones_idx[0][1]
        visited = set()

        perimiter = dfs(grid, visited, s_i, s_j)

        return perimiter




