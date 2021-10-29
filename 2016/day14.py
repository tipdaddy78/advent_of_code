# from hashlib import md5
#
#
# def fetch_triple(string):
#     for i in range(len(string) - 2):
#         sl = string[i:i+3]
#         if sl[0] == sl[1] and sl[1] == sl[2]:
#             return sl
#     return None
#
#
# def has_quint(string, quint):
#     return quint in string
#
#
# salt = 'abc'
# # salt = 'cuanljph'
# keys = 0
# last_index = 0
# index = 0
# hashes = dict()
# while keys < 64:
#     md = hashes.get(index, None)
#     if md is None:
#         md = md5((salt + str(index)).encode()).hexdigest()
#         hashes[index] = md
#     # Part 2
#     for n in range(2016):
#         md = md5(md.encode()).hexdigest()
#     triple = fetch_triple(md)
#     if triple is not None:
#         quint = triple + triple[:-1]
#         for j in range(index+1, index+1001):
#             md_quint = hashes.get(j, None)
#             if md_quint is None:
#                 md_quint = md5((salt + str(j)).encode()).hexdigest()
#                 hashes[j] = md_quint
#             if quint in md_quint:
#                 print("found a key with index:", index, "Now have", keys, "keys")
#                 keys += 1
#                 last_index = index
#                 break
#     index += 1
#     hashes.pop(index - 1)
#
# print(last_index)


#####################
from collections import defaultdict
from hashlib     import md5


def main():

   data = "cuanljph"


   idx = 0

   hashes = []
   threes = defaultdict(list)

   while not (len(hashes) > 64 and (idx - hashes[-1][0]) > 1000):
      value = md5((data + str(idx)).encode()).hexdigest()
      for _ in range(2016):
         value = md5(value.encode()).hexdigest()

      match = matchesFive(value)

      if match is not None:
         for (m_idx, value) in threes[match]:
            if (idx - m_idx) <= 1000:
               hashes.append((m_idx, value))
               print("Found hash:", m_idx)
         hashes.sort()
         threes[match] = []

      match = matchesThree(value)

      if match is not None:
         threes[match].append((idx, value))

      idx += 1

   print("Last hash:", hashes[63])



def matchesThree(value):
   for idx in range(len(value) - 2):
      if len({value[idx + i] for i in range(3)}) == 1:
         return value[idx]
   return None

def matchesFive(value):
   for idx in range(len(value) - 4):
      if len({value[idx + i] for i in range(5)}) == 1:
         return value[idx]
   return None


main()