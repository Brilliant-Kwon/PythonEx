str1 = "Life is too short, You need Python"
str1 = str1.lower()
str1 = str1.replace(" ", "")
print(str1)
lst = list(str1)
print(lst)
chars = set(lst)
print(chars)
lst = list(chars)
lst1 = []
for i in lst:
    if 'a' <= i <= 'z':
        lst1.append(i)
print(lst1)
lst1.sort()
print(lst1)
print("알파벳 갯수 : ", len(lst1))
