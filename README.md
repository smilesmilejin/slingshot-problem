# slingshot-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

Auberon has a slingshot and they are using it to shoot targets. The room Auberon is in is represented by a rectangular 2D list of strings where:

'A' represents where Auberon is standing.
'T' is a target.
'W' is a wall.
' ' is an empty space.

For example:
```py
[
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]
```

Auberon is only able to shoot their slingshot up, down, left, or right. They cannot shoot at a diagonal. Their pellet travels until it either hits a target, a wall, or exits the room. The pellet cannot pass through walls or targets.

In this example, Auberon is able to hit two targets: one above them (row 0, column 1), and one to the right of them (row 2, column 3).

Write a function that takes in a 2D list of strings representing a room and returns the number of targets Auberon is able to hit.

## Examples

### Example 1
```py
room1 = [
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]

hittable_targets(room1)
```
Produces
```py
2
```

### Example 2
```py
room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]

hittable_targets(room2)
```
Produces
```py
4
```

### Example 3
```py
room3 = [
    ['T', ' ', 'T'],
    [' ', 'A', ' '],
    ['T', ' ', 'T'],
    [' ', ' ', ' '],
]

hittable_targets(room3)
```
Produces
```py
0
```

### Example 4
```py
room4 = [
    ['T', 'A', ' ', 'W', ' ', 'T'],
]

hittable_targets(room4)
```
Produces
```py
1
```

### Example 5
```py
room5 = [
    ['A'],
]

hittable_targets(room5)
```
Produces
```py
0
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: How should I handle invalid input? Or letters other than those specified?
A: You can assume the input will be valid. There is guaranteed to be exactly one 'A' in the grid, and all other strings will be 'T', 'W', or ' '.

#### Q: How should I handle empty input?
A: You can assume there will be at least one row and column.

#### Q: Will the grid be a square?
A: The grid is NOT guaranteed to be a square. It may have a different number of rows than columns. However, it will NOT be jagged. It is guaranteed to be a rectangle.

#### Q: Can a pellet pass through a target to hit another? 
A: Nope.

### Hints

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. Afterwards help them to see what data structures might be useful.

- If your candidate is overwhelmed or struggling to get started, encourage them to first write code to find Auberon's starting position. If they get that working then they can move on to seeing what targets can be hit.

- If your candidate is struggling to consider how to check all 4 directions, get them to try just checking one direction (to the right) first. If they get that working, then they can move on to checking the other directions.

- If your candidate is worried about a large number of loops or a large amount of copy/paste, assure them this is OK. The first sample solution has a lot of copy-pasted code!
