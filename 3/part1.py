# Converts every line into an array of 3 integers
data = [map(int, line.split()) for line in open("input.txt")]
possible = 0
for tri in data:
    # Check if the sum of any combination of two sides is less than then third 
    if tri[0] + tri[1] <= tri[2] or tri[0] + tri[2] <= tri[1] or tri[1] + tri[2] <= tri[0]:
        continue
    possible += 1
print(possible)
