class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        grid = image

        s_color = grid[sr][sc]
        grid[sr][sc] = color

        visited = set()
        def dfs(grid, visited, i, j):    
            if (i,j) in visited: return
            visited.add((i,j))

            grid[i][j] = color

            neighs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for neigh in neighs:
                ni = neigh[0]
                nj = neigh[1]

                if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] != s_color: continue
                dfs(grid, visited, ni, nj)
                
            return


        dfs(grid, visited, sr, sc)

        return grid


        
