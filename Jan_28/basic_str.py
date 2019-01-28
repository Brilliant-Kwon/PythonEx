# 문자열 연습
def define_str():
    """
    이 함수는 문자열 정의에 대한 연습입니다.
    """
    # 한 줄 문자열의 정의
    s1 = "Hello Python"  # 직접 리터럴
    s2 = str("Hello Python")
    s3 = str(3.14159)

    print(s1, s2, s3)
    print(type(s1), type(s2), type(s3))

    print(s1, "is str instance ? ", isinstance(s1, str))

    # 여러 줄 문자열
    s4 = """Life is too short, you need Python.
여러 줄 문자열
여러 줄 문자열은 함수 docstring으로도 활용
여러 줄 문자열은 여러 줄 주석으로도 활용
"""

    print(s4)


def string_oper():
    """
    문자열 연산 연습
    """
    print("====문자열 연산 연습 함수")
    str_1 = "Life is too short, You need Python!"

    # 시퀀스 형의 길이
    print("str length:", len(str_1))
    # 인덱스를 이용한 접근
    print(str_1[0], str_1[1], str_1[2], str_1[3])  # 정방향 인덱스
    print(str_1[-7], str_1[-6], str_1[-5])  # 역방향 인덱스

    # 문자열은 immutable(변경 불가) 자료형
    # str[0] = "1"      # 오류

    # 슬라이싱
    print(str_1[12:17])
    print(str_1[-7:-1])
    print(str_1[:17])  # 처음부터 슬라이싱
    print(str_1[-7:])  # 끝까지 슬라이싱
    print(str_1[:])  # 모두 슬라이싱

    # 연결 (+)    #산술 연산자의 의미는 X
    print("Python" + " " + "Programming")
    print("Python" + str(3))

    # 반복 (*)
    print("Python" * 3)

    # 포함여부 : in, not in
    print("P" in str_1)
    print("P" not in str_1)


# define_str()
string_oper()
