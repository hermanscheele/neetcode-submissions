class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]
        if color == start_color: return image

        r = len(image)
        c = len(image[0])

        def dfs(image, visited, i, j, start_color):
            if (i, j) in visited: return

            if i < 0 or i >= r or j < 0 or j >= c or image[i][j] != start_color:
                return

            visited.add((i, j))
            image[i][j] = color

            neighs = [(i+1, j), (i, j+1), (i-1 , j), (i, j-1)]
            for n in neighs:
                dfs(image, visited, n[0], n[1], start_color)
    
            return 
        

        visited = set()
        dfs(image, visited, sr, sc, start_color)

        return image
            
        




        
