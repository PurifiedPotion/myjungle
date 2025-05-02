def gcd(a, b):
    while b:  # b가 0이 될 때까지 반복
        a, b = b, a % b  # a를 b로, b를 a % b로 갱신
    return a  # b가 0이 되면 a가 최대공약수

print(gcd(48, 18))  # 출력: 6