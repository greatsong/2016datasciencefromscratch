n = int(input())

def hanoi(n,a,b,c):
    if n == 1 :
    # 1개 남았으면 목적지에 내림
        print(a, 'to', c)
    else :
    # 2개 이상 남았을 경우
        hanoi(n-1,a,c,b)
        # n-1개의 탑을 중간 지역으로 잠시 옮긴 후
        print(a,'to',c)
        # 위의 원반이 다 이동한 상태(자신만 남음)이기 때문에 목적지에 내림
        hanoi(n-1,b,a,c)
        # 중간 지역에 있던 n-1개의 탑을 다시 목적지로 옮김

hanoi(n,1,2,3)