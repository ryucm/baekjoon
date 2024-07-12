num = int(input())

i = 0
result = []
while len(result) <= 10000:
  if '666' in str(i):
    result.append(int(i))
  i += 1
print(result[num-1])