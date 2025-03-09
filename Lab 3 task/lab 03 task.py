# Water Jug Problem using DFS

def water_jug_dfs(cap_x, cap_y, target):
    stack = [(0, 0)]  # Start with both jugs empty
    visited = set()   # To track 
    while stack:
        x, y = stack.pop()  # Get the last state
        print(x,y)

        if x == target or y == target: 
            print("Solution Found!")
            return

        if (x, y) in visited:
            continue
        visited.add((x, y))
        # rules
        stack.append((cap_x, y))  # Fill X
        stack.append((x, cap_y))  # Fill Y
        stack.append((0, y))  # Empty X
        stack.append((x, 0))  # Empty Y
        # Pour X → Y
        new_x = max(0, x - (cap_y - y))
        new_y = min(cap_y, y + x)
        stack.append((new_x, new_y))
        # Pour Y → X
        new_x = min(cap_x, x + y)
        new_y = max(0, y - (cap_x - x))
        stack.append((new_x, new_y))

water_jug_dfs(7, 5, 1)
