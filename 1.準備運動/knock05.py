# 05. n-gram

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ。この関数を用い、”I am an NLPer”という文から文字tri-gram、単語bi-gramを得よ。

def n_gram(target, n):
  result = []

  for i in range(len(target) - n+1):
    result.append(target[i:i+n])

  return result

print("tri-gram:", n_gram("I am an NLPer",3))
print("bi-gram:", n_gram("I am an NLPer".split(),2))