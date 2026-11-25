# 08. 暗号文

# 与えられた文字列の各文字を、以下の仕様で変換する関数cipherを実装せよ。英小文字ならば (219 - 文字コード) のASCIIコードに対応する文字に置換その他の文字はそのまま出力この関数を用い、英語のメッセージを暗号化・復号化せよ。

def cipher(text):
  result = ""
  for c in text:
     if 'a' <= c <= 'z':
      result += chr(219 - ord(c))
     else:
      result += c
  return result

print(cipher("abC!d"))
print(cipher("zyC!w"))