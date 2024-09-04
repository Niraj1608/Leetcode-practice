class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x, y) for x, y in obstacles)
        result = 0
        x = y = d = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for command in commands:
            if command == -2:
                d = (d - 1) % 4
            elif command == -1:
                d = (d + 1) % 4
            else:
                dx, dy = directions[d]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x += dx
                    y += dy
                    result = max(result, x ** 2 + y ** 2)
        return result