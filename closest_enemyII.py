'''
- We need to find the position of 1 and store it (pos)(x,y)
- Find all enemy positions and store it (enemies) [(x,y),(x,y), ...]
- If there aren't any enemies return 0

-find the length of columns and rows (cols, rows)
- find the distance between our positions (1's positions) and all enemies (distances) ->[3,4,5,9,10]
- iterate over enemies pos -> (x,y)
    - calculate the horizontal distance (left - right) (h_min)
      - direct distance -> abs(pos[y] - enemy[y])
      - wrapped distance -> cols - direct distance 
      - find the min between the wrapped and direct distance (h_min)
    - calculate the vertical distance  (v_min)
      - direct distance -> abs(pos[x] - enemy[x])
      - wrapped distance -> rows - direct distance 
      - find the min between the wrapped and direct distance (v_min)
    -total distance between player 1 and current enemy -> (h_min + v_min)
    - store total distance inside distances variable 
- return min value inside distance variable
'''

def closest_enemy_ii(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    pos = None
    enemies = []

    # Find the position of '1' and all enemy positions '2'
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                pos = (x, y)
            elif grid[x][y] == 2:
                enemies.append((x, y))

    # If there are no enemies, return 0
    if not enemies:
        return 0

    distances = []

    for enemy in enemies:
        # Horizontal distance calculation
        direct_h_dist = abs(pos[1] - enemy[1])
        wrapped_h_dist = cols - direct_h_dist
        h_min = min(direct_h_dist, wrapped_h_dist)

        # Vertical distance calculation
        direct_v_dist = abs(pos[0] - enemy[0])
        wrapped_v_dist = rows - direct_v_dist
        v_min = min(direct_v_dist, wrapped_v_dist)

        # Total distance to the current enemy
        total_dist = h_min + v_min
        distances.append(total_dist)

    # Return the minimum distance
    return min(distances)
