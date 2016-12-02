keypad = [
          ['1'],
     ['2', '3', '4'],
['5', '6', '7', '8', '9'],
     ['A', 'B', 'C'],
          ['D']
]
jumps = [
[-1, -1,  0, -1, -1],
[-1,  0,  1,  2, -1],
[ 0,  1,  2,  3,  4],
[-1,  0,  1,  2, -1],
[-1, -1,  0, -1, -1]
]
x = 0
xglob = 0
y = 2
data = [line for line in open("input.txt", "r")]
for btn in data:
    for i in btn:
        if i == 'U':
            # Up
            if y > 0 and jumps[y - 1][xglob] >= 0:
                x = jumps[y - 1][xglob]
                y -= 1
        elif i == 'D':
            # Down
            if y < 4 and jumps[y + 1][xglob] >= 0:
                x = jumps[y + 1][xglob]
                y += 1
        elif i == 'R':
            # Right
            if x < len(keypad[y]) - 1:
                x += 1
                xglob += 1
        elif i == 'L':
            # Left
            if x > 0:
                x -= 1
                xglob -= 1
    print(keypad[y][x])
