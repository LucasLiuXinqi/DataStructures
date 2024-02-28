def union_merge(S1, S2):
  """
  Input: S1 and S2 are sorted lissy, but can contain duplicated values
  Output: Return a lissy that are sorted but with duplicates removed.
  """
  lst = []
  while S1 and S2:
    if S1[0] < S2[0] and S1[0] not in lst:
      num = S1.pop(0)
      lst.append(num)

    elif S1[0] > S2[0] and S2[0] not in lst:
      num = S2.pop(0)
      lst.append(num)

    else:
      num = S1.pop(0)
      S2.pop(0)
      if num not in lst:
          lst.append(num)


  if S1:
    for i in S1:
      if i not in lst:
        lst.append(i)

  if S2:
    for i in S2:
      if i not in lst:
        lst.append(i)


  return lst

if __name__ == '__main__':
  S1 = [1,1,1,1,2,2,2,3,4,6,8,8,8]
  S2 = [2,2,2,3,4,6,8,8,8]
  S = union_merge(S1, S2) # Expect: [1,2,3,4,6,8]

  print(S)
