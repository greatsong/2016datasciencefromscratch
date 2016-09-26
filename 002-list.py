i_list = [1,2,3]
h_list = ["string", 0.1, True]
l_of_lists = [i_list, h_list,   []]

list_length  = len(i_list)
print(list_length)
list_sum  = sum(i_list)
print(list_sum)

x = range(10)
print(x) # range(0,10)으로 출력되는게 정상임!

zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
# x[0] = -1
# range로 만든 오브젝트에는 assign이 안됨!

print(zero, one, nine, eight, x[0])

a = x[:3]
b = x[3:]

print(a, b)

y = [1,2,3]
y.extend(x)

print(y)

y.append(0)
print(y)

_,b = [1,2]