data = [line for line in open("input.txt", "r")]
button = 5
for btn in data:
    for i in btn:
        if i == 'U':
            # Up
            if button - 3 > 0:
                button -= 3
        elif i == 'D':
            # Down
            if button + 3 < 10:
                button += 3
        elif i == 'R':
            # Right
            if button % 3 != 0:
                button += 1
        elif i == 'L':
            # Left
            if (button - 1) % 3 != 0:
                button -= 1
    print(button)
