import re

air = 'air.txt'

with open (air, 'r') as f_air:
    a = f_air.read()

reg = re.compile('[^a-zA-z]')

c = []

c = reg.sub('', a)

lfs = []

for i in c:
    lfs.append(i)

lfs.sort()

d = ''

for i in lfs:
    d += i

currCh = d[:1]
curCount = 1
result = ''
r = []

for sbl in d[1:]:
    if sbl != currCh:
        result += (currCh + str(curCount))
        currCh = sbl
        curCount = 1
    else:
        curCount += 1
    match = re.search('\D\d+', result)
    

result += (currCh + str(curCount))

number_match = re.findall('\d+', result)
# print(number_match)
letter_match = re.findall('\D', result)
dict_ = {}
match_number = []

for i in number_match:
    i = int(i)
    match_number.append(i)


for i in range(len(number_match)):
    dict_[letter_match[i]] = match_number[i]

final_dict = dict([max(dict_.items(), key=lambda k_v: k_v[1])])



print(dict_)
print('Самый повторяющийся символ', final_dict)

    

