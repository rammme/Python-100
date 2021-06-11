#문제20 : 몫과 나머지

n = list(map(int, input().split()))
result = n[0] // n[1]
left = n[0] % n[1]

print(result, left)