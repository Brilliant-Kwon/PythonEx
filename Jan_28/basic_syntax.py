# 파이썬 기본 문법
def arith_oper():  # 산술 연산자 관련 연습
    print("==== 사칙 연산")
    # +,-,*,/
    print(7 / 3)  # 정수/정수 실수
    print(7 // 3)  # 정수/정수의 몫
    print(7 % 3)  # 정수/정수의 나머지

    # 몫과 나머지 함께 전달
    print(divmod(7, 3))
    print("몫 :", divmod(7, 3)[0])
    print("나머지 :", divmod(7, 3)[1])

    # 제곱
    print(7 ** 3)
    print(pow(7, 3))  # 함수 이용 구하기


def complex_ex():
    print("==== 복소수")
    print(3 + 4J)
    print(complex(7, 3))

    print("실수부 : ", 3 + 4j.real)  # 실수부
    print("허수부 : ", 3 + 4j.imag)  # 허수부
    print("켤레복소수 : ", 3 + 4j.conjugate())  # 켤레복소수


def rel_oper():
    print("==== 비교연산자")

    print("1 > 3 ?", 1 > 3)  # boolean의 첫글자 대문자로 출력 된다.
    s1 = "Python";
    s2 = "Python";
    print("문자열 == : ", s1 == s2)

    # 복합 관계식
    a = 5
    print("a > 0 이고 a < 10 ? ", 0 < a and a < 10)  # 줄일 수 있다.
    print("a > 0 이고 a < 10 ? ", 0 < a < 10)  # 복합 관계식


# arith_oper()
# complex_ex()
rel_oper()
