class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit=set()
        initial=image[sr][sc]
        self.dfs(sr,sc,color,initial,image,visit)
        return image

    def dfs(self,i,j,val,initial,image,visit):
        if i < 0 or j < 0 or j >= len(image[0]) or i >= len(image):
            return 
        if (i,j) in visit:
            return
        if image[i][j] != initial:
            return
        image[i][j]=val
        visit.add((i,j))

        self.dfs(i+1,j,val,initial,image,visit)
        self.dfs(i-1,j,val,initial,image,visit)
        self.dfs(i,j+1,val,initial,image,visit)
        self.dfs(i,j-1,val,initial,image,visit)