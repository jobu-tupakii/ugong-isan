def factor_sum(n):
    factor = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            factor.append(i)
    factor.append(n) #놓친 부분! 약수에는 본인도 포함됨... 수학을 다시 배워야 되나...
    #파이썬으로 실행할때 들여쓴 부분 위치도 꼭 확인하자 값이 아예 달라짐

    return sum(factor)

print(factor_sum(12))