#문제 34: sort 구현하기

height = list(input().split())
height = [int(i) for i in height] 

if height != sorted(height):
    print("NO")
else :
    print("YES")
