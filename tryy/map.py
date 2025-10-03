def mapping(arr):
    answer = []
    
    for i in arr:
        if i % 2 == 0:
            answer.append(i * 2)
        else:
            answer.append(i / 2 )
    return answer

lst = [1,2,34,6]
x =mapping(lst)
print(x)