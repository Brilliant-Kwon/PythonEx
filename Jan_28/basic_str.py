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


def transform_methods():
    """대소문자 변환관련 메서드들"""
    print("====변환메서드")

    s = "i like Python"
    print("upper:", s.upper())  # 모두 대문자
    print("upper:", s.lower())  # 모두 소문자
    print("swapcase:", s.swapcase())  # 대 <->소
    print("capitalize:", s.capitalize())  # 첫글자만 대문자로
    print("title:", s.title())  # 단어의 첫글자 전부 대문자


def search_methods():
    """검색 메서드 관련"""

    s = "I Like Python, I Like Java"
    print("count:", s.count("Like"))  # 검색어의 개수 반환
    print("find:", s.find("Like"))  # 정방향 검색
    print("find:", s.find("Like", 3))  # 3번 인덱스 이후의 검색
    print("find:", s.find("JS"))  # 없는 객체의 검색 -1

    # print("index:", s.index("Like"), s.index("Like", 3), s.index("JS"))
    # 없는 인덱스를 찾으면 에러 발생
    if "JS" in s: print("index:", s.index("JS"))

    # 역방향 검색 : r
    print("rfind:", s.rfind("Like"))
    print("rfind:", s.rfind("Like", 0, 17))  # 역방향 검색을 위한 범위 설정

    # 특정 문자열로 시작하거나 끝나는지 검색
    url = "http://naver.com"  # 일반접속
    surl = "https://google.com"  # 보안접속
    ftp = "ftp://ftp.naver.com"  # 파일전송프로토콜

    print("startswith url : ", url.startswith("http://"))
    print("startswith surl : ", surl.startswith("https://"))
    print("endswith url : ", url.endswith("naver.com"))
    print("endswith surl : ", surl.endswith("google.com"))

    # 범위 지정가능
    print("startswith ftp : ", ftp.startswith("ftp", 6, 20))


def modify_replace_methods():
    """수정 및 치환 메서드"""
    s = "           Alice and the Heart Queen              "
    print("strip:[", s.strip(), "]", sep="")  # 공백문자제거
    print("lstrip:[", s.lstrip(), "]", sep="")  # 왼쪽공백제거
    print("rstrip:[", s.rstrip(), "]", sep="")  # 오른쪽공백제거

    s = "=======Alice and the Heart Queen======="
    print("strip = :[", s.strip("="), "]", sep="")  # = 문자를 제거

    s = "I Like Java Language"
    print("replace:", s.replace("Java", "Python"))

    print("origin:", s)  # 원본 문자열에는 영향 x


def align_methods():
    """문자열 정렬 관련 메서드"""
    print("====문자열 정렬")

    s = "Alice and the Heart Queen"

    print("center:[", s.center(60), "]", sep="")
    # 60칸을 확보하고, 비어있는 공간은 공백 처리 하면서 가운데에 문자열 위치
    print("ljust:[", s.ljust(60, "*"), "]", sep="")
    print("rjust:[", s.rjust(60, "-"), "]", sep="")

    print("zfill:[", "123".zfill(5), "]", sep="")  # 빈공간 0으로 채움
    print("zfill:[", "12345678".zfill(5), "]", sep="")  # 자리부족해도 만들어서 출력


def split_join_methods():
    """자르기와 합치기"""

    print("====자르기 합치기")

    s = "Ham and Cheese and Bread and Ketchup"
    ingredients = s.split(" and ")
    print(ingredients, type(ingredients))
    print("join:", ",".join(ingredients))  # 합치기

    # 자르기를 할 때 자를 객체의 수를 지정
    print(s.split(" and ", 2))  # and를 기준으로 2개를 잘라줌
    print(s.rsplit(" and ", 2))  # 뒤부터 잘라줌

    lines = """\
    Java
    Python
    HTML
"""
    print("lines split:", lines.split())  # 문자열만 꺼내서 잘라줌
    print("lines splitlines:", lines.splitlines())  # 개행문자기준으로잘라줌
    print("lines splitlines:", lines.splitlines(True))  # 개행문자 유지


def check_methods():
    """is계열 메서드 : 특정 포맷인지 판단"""
    print("1234".isdigit())  # 숫자 형태인가
    print("python".isalpha())  # 알파벳인가
    print("py3".isalnum())  # 알파벳+숫자 판단
    print("py 3".isalnum())  # ->False(공백 때문)

    print("PYTHON".isupper())  # 대문자 형태인가
    print("python".islower())  # 소문자 형태인가
    print("Python Programming".istitle())  # 타이틀 형태인가


def string_format():
    """문자열 포맷 연습"""

    # C스타일의 포맷 문자열
    print("현재 이자율은 %f입니다." % 1.24)
    print("현재 이자율은 %.2f입니다." % 1.24)

    fmt = "%d개의 %s 중 %d개를 먹었다."
    print(fmt % (10, "사과", 3))  # 튜플로 포매팅

    # named formatting
    fmt = "%(total)d개의 %(fruit)s 중에 %(eat)d 개를 먹었다."
    print(fmt % {"total": 10, "fruit": "사과", "eat": 3})
    print(fmt % {"fruit": "사과", "total": 10, "eat": 3})  # 순서 상관 x

    # format 메서드 이용
    fmt = "{}개의 {} 중에 {}개를 먹었다."  # 플레이스 홀더
    print(fmt.format(10, "사과", 3))
    fmt = "{0}개의 {1} 중에 {2}개를 먹었다."  # 순서 지정
    print(fmt.format(10, "사과", 3))

    fmt = "{total}개의 {fruit}중 {eat}개를 먹었다."
    # 인자 값을 이용한 포매팅
    print(fmt.format(total=10, eat=3, fruit="귤"))
    # 사전을 이용한  named  포매팅  (자바의 해쉬테이블과 비슷함.)
    print(fmt.format_map({"total": 10, "fruit": "사과", "eat": 3}))


# define_str()
# string_oper()
# transform_methods()
# search_methods()
# modify_replace_methods()
# align_methods()
# split_join_methods()
# check_methods()
string_format()
