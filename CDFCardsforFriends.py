x = int(input())
for i in range(x):
	w,h,n=map(int,input().split())
	res=1
	while(w%2==0):
		w/=2
		res*=2
	while(h%2==0):
		h/=2
		res*=2
	if(res<n):print("NO")
	else:print("YES")
