data = [map(int, line.split()) for line in open("input.txt")]
possible = 0
# Go through 3 rows at a time so that the three rows are i, i+1 and i+2
# 3 rows gives 3 triangles (in column form)
for i in range(0, len(data), 3):
    # Go through each colum
    for j in range(3):
        # Check if the sum of any combination of two sides is less than then third
        if data[i][j] + data[i+1][j] <= data[i+2][j] or data[i][j] + data[i+2][j] <= data[i+1][j] or data[i+1][j] + data[i+2][j] <= data[i][j]:
            continue
        possible += 1
print(possible)
