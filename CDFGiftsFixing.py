for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=min(a)
    y=min(b)
    res=0
    for i in range(n):
        diff_a=a[i]-x
        diff_b=b[i]-y
        res=res+max(diff_a,diff_b)
    print(res)

'''
We have considered subtracted the min element from "i"th element.
Further we have considered the max of the values of two lists.
We add the max elements in res variable:

ex:
1 2 3 4 5
5 4 3 2 1

Output:
res = 16

min of list1,2 = 1,1

subtracted lists:
1) [0,1,2,3,4]
2) [4,3,2,1,0]

max common list of 1,2:
[4,3,2,3,4]

answer = sum of above list
'''
