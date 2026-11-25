
# 00. パタトクカシーー

# 2つの文字列「パトカー」と「タクシー」の文字を先頭から交互に連結し、文字列「パタトクカシーー」を得よ。


str1 = "パトカー"
str2 = "タクシー"
mix_str = ""

for i in range(len(str1)):
  mix_str += str1[i] + str2[i]

print(mix_str)

str1 = "パトカー"
str2 = "タクシー"
mix_str = ""

for a, b in zip(str1, str2):
  mix_str += a + b

print(mix_str)