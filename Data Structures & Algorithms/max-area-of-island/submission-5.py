class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def get_ones():
            ones_idx = []
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1: ones_idx.append((i,j))
            return ones_idx
        

        def dfs(grid, visited, i, j):
            if (i, j) in visited: return 1
            visited.add((i,j))

            count = 1
            neighs = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for ni, nj in neighs:
                
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols: continue
                if grid[ni][nj] != 1: continue
                if (ni,nj) in visited: continue

                count += dfs(grid, visited, ni, nj) 

            return count


        ones_idx = get_ones()
        visited = set()
        max_area = 0

        for i, j in ones_idx:

            area = dfs(grid, visited, i, j)
            max_area = max(max_area, area)


        return max_area




