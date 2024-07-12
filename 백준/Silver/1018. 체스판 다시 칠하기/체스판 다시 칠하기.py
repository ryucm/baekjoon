N,M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(input())

result = []

for i in range(N-7):
    for j in range(M-7):
        least_W = 0
        least_B = 0
        for check1 in range(i,i+8):
            for check2 in range(j,j+8):
                if (check1+check2) % 2 ==0:
                    if matrix[check1][check2] != 'W':
                        least_W += 1
                    if matrix[check1][check2] != 'B':
                        least_B += 1
                else:
                    if matrix[check1][check2] != 'W':
                        least_B += 1
                    if matrix[check1][check2] != 'B':
                        least_W += 1
        result.append(min(least_B,least_W))
        
print(min(result))