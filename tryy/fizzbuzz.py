
def fizzbuzz(n):
    answer = []
    for i in range(1, n):
        if i % 3 and 5 == 0:
            answer.append("Fizzbuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(i)

    return answer

x = fizzbuzz(15)
print(x)