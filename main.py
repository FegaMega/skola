output = [0, 1]
i = 2
x = 0
while i < 101:
    x = int(output[i-2] + output[i-1])
    output.append(x)
    i += 1
print(output)
