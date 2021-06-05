#문제10 : 별 찍기

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+("*"*(2*i-1))) 
