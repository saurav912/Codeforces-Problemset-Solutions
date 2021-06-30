for i in range(int(input())):
  n,k = list(map(int, input().split()))
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  for i in range(k):
    a.append(max(b))
    a.remove(min(a))
    b.remove(max(b))
  print(sum(a)) 
