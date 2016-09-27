n = int(input())

def hanoi(n,a,b,c,d):
    if n == 1 :
        print(1,a+'->'+d)
    elif n == 2 :
        print(1,a+'->'+b)
        print(2,a+'->'+d)
        print(1,b+'->'+d)
    else :
        hanoi(n-2,a,b,d,c)
        print(n-1, a + '->' + b)
        print(n,a+'->'+d)
        print(n-1, b + '->' + d)
        hanoi(n-2,c,a,b,d)

hanoi(n,'A','B','C','D')