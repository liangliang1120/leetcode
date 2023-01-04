class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(numRoom):
            if numRoom in visited:
                return
            visited.add(numRoom)
            for nextRoom in rooms[numRoom]:
                dfs(nextRoom)
        n = len(rooms)
        visited = set()
        dfs(0)
        return len(visited) == len(rooms)
