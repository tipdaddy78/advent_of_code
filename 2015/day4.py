import hashlib

key = 'ckczppom'
test1 = 'abcdef609043'
test2 = 'pqrstuv1048970'

i = 1
while True:
    temp = key + str(i)
    k = str(hashlib.md5(temp.encode()).hexdigest())
    if k.startswith('00000'):
        print(key + str(i))
    if k.startswith('000000'):
        print(key + str(i))
        break
    i += 1