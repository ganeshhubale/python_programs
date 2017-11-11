from collections import Counter

an = ['a','a','b', 'c', 'a', 'c', 'a', 'b', 'c', 'x']

cn = Counter(an)

print(cn,'\n')
print(cn.most_common(),'\n')
print(cn.most_common(2)[-1],'\n')

