n=int(input())
print(n//2)
print("2 "*(n//2-1),n%2+2)

'''
user_input = int(input())
prime_number = [2,3,5,7]
answer = []
for i in prime_number:
    temp1 = user_input // i
    temp2 = user_input % i
    if temp2 == 0:
        answer.extend([i] * temp1)
        break
    else:
        if (i + temp2) in prime_number:
            answer.extend([i] * (temp1 -1))
            answer.append(i + temp2)
            break
        else:
            pass
print(len(answer))
print(*answer)
'''
