class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        ones_idxs = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ones_idxs.append((i,j))


        def dfs(grid, visited, i, j, area):
            if (i,j) in visited: return area
            if i < 0 or i >= rows or j < 0 or j >= cols: return area
            if grid[i][j] != 1: return area

            visited.add((i,j))
            neighs = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for n in neighs:
                ni = n[0]
                nj = n[1]
                area = dfs(grid, visited, ni, nj, area)

            return area + 1


        max_area = 0
        visited = set()
        for idx in ones_idxs:
            i = idx[0]
            j = idx[1]

            area = 0
            area = dfs(grid, visited, i, j, area)

            if area > max_area:
                max_area = area


        return max_area


