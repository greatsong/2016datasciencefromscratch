my_tuple = (1,2)
your_tuple = 3,4

try:
    my_tuple[1] = 3
except TypeError :
    print('튜플은 수정할 수 없습니다')

def sum_and_product(x,y):
    return (x+y), (x*y)
sp = sum_and_product(2,3)
s, p = sum_and_product(5,10)
print(sp, s, p)

