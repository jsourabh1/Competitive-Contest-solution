or _ in range(int(input())):
 
  m = int(input())
 
  arr_1 = list(map(int, input().split()))
 
  res = []
  vis = [0] * (m+1)
 
  for i in range(m-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    vis[a] += 1
    vis[b] += 1
    if vis[a] > 1:
      res += [arr_1[a]]
    if vis[b] > 1:
      res += [arr_1[b]]
 
  res = sorted(res)[::-1]
  s = sum(arr_1)
  result = [str(s)]
  for x in res:
    s += x
    result += [str(s)]
 
  print(" ".join(result))