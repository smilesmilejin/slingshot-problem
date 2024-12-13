def hittable_targets(room):
    # First, find Auberon by iterating over all
    # rows and columns
    for i, row in enumerate(room):
        for j, item in enumerate(row):
            if item == 'A':
                # save starting location in row, column format
                starting_loc = (i, j)

    # Will hold the number of targets hit
    hits = 0

    # Have four loops - one to search in each direction
    # Note that these loops are almost entirely copy/pasted, only
    # the last line of each while loop is different.
    # To see a more elegant, but slightly harder to understand solution,
    # see alternate implementation after the hints

    ### LOOP 1: SEARCH TO THE RIGHT ###
    # Set r and c to Auberon's location
    r, c = starting_loc
    # Step to the right until either
    # - A wall is hit
    # - A target is hit
    # - The edge of the room is exceeded
    while 0 <= r < len(room) and \
          0 <= c < len(room[0]):
        # If a target is hit, increase the hit count by one, and stop
        # looking in that direction
        if room[r][c] == 'T':
            hits += 1
            break
        # If a wall is hit, stop looking in that direction
        if room[r][c] == 'W':
            break
        c += 1 # if neither wall nor target is hit, increase column by 1 (move to the right)


    ### LOOP 2: SEARCH TO THE LEFT ###
    # Set r and c to Auberon's location
    r, c = starting_loc
    # Search by going to the left
    while 0 <= r < len(room) and \
          0 <= c < len(room[0]):
        # If a target is hit, increase the hit count by one, and stop
        # looking in that direction
        if room[r][c] == 'T':
            hits += 1
            break
        # If a wall is hit, stop looking in that direction
        if room[r][c] == 'W':
            break
        c -= 1 # if neither wall nor target is hit, decrease column by 1 (move to the left)

              
    ### LOOP 3: SEARCH DOWN ###       
    # Set r and c to Auberon's location
    r, c = starting_loc
    while 0 <= r < len(room) and \
          0 <= c < len(room[0]):
        # If a target is hit, increase the hit count by one, and stop
        # looking in that direction
        if room[r][c] == 'T':
            hits += 1
            break
        # If a wall is hit, stop looking in that direction
        if room[r][c] == 'W':
            break
        r += 1 # if neither wall nor target is hit, increase row by 1 (move down)


    ### LOOP4: SEARCH UP ###
    # Set r and c to Auberon's location
    r, c = starting_loc
    while 0 <= r < len(room) and \
          0 <= c < len(room[0]):
        # If a target is hit, increase the hit count by one, and stop
        # looking in that direction
        if room[r][c] == 'T':
            hits += 1
            break
        # If a wall is hit, stop looking in that direction
        if room[r][c] == 'W':
            break
        r -= 1 # if neither wall nor target is hit, decrease row by 1 (move up)

    return hits


room1 = [
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]
assert hittable_targets(room1) == 2

room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]
assert hittable_targets(room2) == 4

room3 = [
    ['T', ' ', 'T'],
    [' ', 'A', ' '],
    ['T', ' ', 'T'],
    [' ', ' ', ' '],
]
assert hittable_targets(room3) == 0

room4 = [
    ['T', 'A', ' ', 'W', ' ', 'T'],
]
assert hittable_targets(room4) == 1

room5 = [
    ['A'],
]
assert hittable_targets(room5) == 0

print("All tests passed!")
print("If time remains, discuss time & space complexity")
