# 09. Typoglycemia

# スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ。ただし、長さが４以下の単語は並び替えないこととする。適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え、その実行結果を確認せよ。

import random

def typoglycemia(text):
  words = text.split()
  result = ""

  for word in words:
    if len(word) <= 4:
      result += word
      result += " "
    else:
      middle = list(word[1:len(word)-1])
      random.shuffle(middle)
      result += word[0] + "".join(middle) + word[len(word)-1]
      result += " "

  return result.strip()

print(typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))