def hittable_targets(room):
    # Your implementation here!
    # pass

    # Time O m * n
    # Space O1

    # find the position of 'A', row, col

    # start_row = 0
    # end_row = len(room) - 1
    
    # start_col = 0
    # end_col = len(room[0]) - 1
    
    # target = 0
    # UP
    # col = col
    # for i in range(row - 1, -1, -1)
    # if that lement is "T"
        # incremte by target by 1
    # elif "W"
        # break this loop

    # DOWN
    # col = col
    # for i in range(row + 1,end_row +1, 1)

    # LEFT 
    # row = row
    # for i in range(col - 1, start_col - 1, -1)

    # RIGHT
    # row = row
    # for i in range(col + 1, end_col + 1, 1)

    # return target

    A_row = 0
    A_col = 0
    for row in range(len(room)):
        for col in range(len(room[0])):
            if room[row][col] == "A":
                A_row = row
                A_col = col

    # print(A_row, A_col)


    start_row = 0
    end_row = len(room) - 1
    
    start_col = 0
    end_col = len(room[0]) - 1


    target = 0
    # UP
    # A_col = col
    for row in range(A_row - 1, -1, -1):
        if room[row][A_col] == "T":
            target += 1
            break
        if room[row][A_col] == "W":
            break
    
    # print(target)

    # DOWN
    for row in range(A_row + 1, end_row +1, 1):
        if room[row][A_col] == "T":
            target += 1
            break
        if room[row][A_col] == "W":
            break

    # print(target) 

    # LEFT
    for col in range(A_col - 1, start_col - 1, -1):
        if room[A_row][col] == "T":
            target += 1
            break
        if room[A_row][col] == "W":
            break
    # print(target) 


    # RIGHT
    # (col + 1, end_col + 1, 1)
    for col in range(A_col + 1, end_col + 1, 1):
        if room[A_row][col] == "T":
            target += 1
            break
        if room[A_row][col] == "W":
            break
    # print(target) 

    return target

room1 = [
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]

# print(hittable_targets(room1))
assert hittable_targets(room1) == 2

room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]
assert hittable_targets(room2) == 4
# print(hittable_targets(room1))

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
