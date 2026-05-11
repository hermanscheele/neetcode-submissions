class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        def get_ones(grid):
            ones_idx = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1": 
                        ones_idx.append((i,j))
            return ones_idx

        
        def dfs(grid, visited, i, j):
            if (i,j) in visited: return 1
            visited.add((i,j))

            neighs = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for neigh in neighs:
                ni = neigh[0]
                nj = neigh[1]

                if ni<0 or ni>=rows or nj<0 or nj>=cols or grid[ni][nj] != "1": continue

                dfs(grid, visited, ni, nj)

            return 1
            

        
        visited = set()
        island_count = 0
        ones_idx = get_ones(grid)

        for idx in ones_idx:
            i = idx[0]
            j = idx[1]

            if (i,j) in visited: continue
            island_count += dfs(grid, visited, i, j)

        return island_count









