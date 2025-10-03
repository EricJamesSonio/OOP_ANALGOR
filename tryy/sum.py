def summing(lst):
    answer = []
    total = 0
    for i in lst:
        total += i
        answer.append(total)
    return answer

lst =[1,2,3,4]
x = summing (lst)
print(x)