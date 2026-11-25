# 06. 集合

# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を、それぞれ,XとYとして求め、XとY の和集合、積集合、差集合を求めよ。さらに、’se’というbi-gramがXおよびYに含まれるかどうかを調べよ。

def n_gram(target, n):
  result=[]

  for i in range(len(target)-n+1):
    result.append(target[i:i+n])

  return result

X = set(n_gram("paraparaparadise",2))
Y = set(n_gram("paragraph",2))

# 和集合
set_or = X | Y
print("和集合：", set_or)

# 積集合
set_and = X & Y
print("積集合：", set_and)

# 差集合
set_sub = X - Y
print("差集合(X - Y)：", set_sub)
set_sub = Y - X
print("差集合(Y - X)：", set_sub)

if 'se'in X:
  print("'se'はXに含まれる")
else:
    print("'se'はXに含まれない")

if 'se'in Y:
  print("'se'はYに含まれる")
else:
    print("'se'はYに含まれない")