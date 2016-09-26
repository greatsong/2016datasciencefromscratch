# p. 19

def double(x):
    return x * 2

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)
# print(x)

y = apply_to_one(lambda x: x + 4)
# print(y)

def my_print(msg = "기본 출력값") :
    print(msg)

my_print("안녕?")
my_print()

def substract(a=0, b=0):
    return a-b

print(substract(10,5))
print(substract(0,5))
print(substract(b=5))

a = '''hello
hello
hello
'''
print(a)

# p.21 예외처리

try :
    print(0/0)
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다")