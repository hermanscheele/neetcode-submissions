class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]
        if color == start_color: return image


        def dfs(image, visited, i, j, start_color):
            if (i, j) in visited: return

            r = len(image)
            c = len(image[0])
            
            if i < 0 or i >= r or j < 0 or j >= c:
                return
            
            if image[i][j] != start_color:
                return
                

            visited.add((i, j))
            start_color = image[i][j]
            image[i][j] = color

            top = (i+1, j)
            right = (i, j+1)
            down = (i-1 , j)
            left = (i, j-1)
            

            dfs(image, visited, top[0], top[1], start_color)
            dfs(image, visited, right[0], right[1], start_color)
            dfs(image, visited, down[0], down[1], start_color)
            dfs(image, visited, left[0], left[1], start_color)

            return 
        
        

        visited = set()
        dfs(image, visited, sr, sc, start_color)


        return image
            
        




        
