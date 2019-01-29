def define_dict():
    """사전 정의 예제"""

    dct = dict()  # 빈사전
    print(dct, type(dct))

    # Literal 이용 생성
    dct = {"baseball": 9, "basketball": 5}

    # 접근할 때는 키 값 이용 접근
    dct['volleyball'] = 6
    print(dct)

    # 연결 +, 반복 * 안됨, 인덱스 접근 x
    # 길이와 in, not in
    # in, not in,->키값에 포함되어 있는지
    print(dct, "length:", len(dct))
    print("baseball in dct key?", "baseball" in dct)

    # 키워드 인자를 이용한 사전 생성
    d1 = dict(key1="value1", key2="value2")
    print(d1)

    # 튜플의 리스트를 이용한 사전 생성
    d2 = dict([("key", 1), ("key2", 2), ("key3", 3)])
    print(d2, type(d2))

    # 키 목록과 값 목록이 별도로 있을 때
    keys = ('Kim', 'Lee', 'Park')
    values = (90, 85, 95)

    z = zip(keys, values)
    print(z, type(z))

    d3 = dict(zip(keys, values))
    print(d3, type(d3))

    # 사전의 키 : 변경 불가 객체
    d3[True] = "true"
    d3[10] = 10
    d3["string"] = "Python"
    d3[(1, 2, 3)] = "Tuple"

    # d3[(1, 2, 3)] = "List" #변경 가능 객체는 키로 사용 불가


def dict_methods():
    """사전의 메서드"""

    dct = {"soccer": 11, "baseball": 9, "volleyball": 6}

    # keys()
    keys = dct.keys()
    print(keys, type(keys))
    list_keys = list(keys)
    print(list_keys, type(list_keys))

    # values()
    values = dct.values()
    print(values, type(values))
    list_values = list(values)
    print(list_values, type(list_values))

    # values()를 이용한 값 검색
    print(9 in dct.values())

    # items() : 키 - 값 쌍의 목록을 반환
    items = dct.items()
    print(items, type(items))
    list_item = list(items)
    print(list_item, type(list_item))

    # 튜플이니까 인덱스 접근 0
    print("KEY:", list_item[0][0], "Value:", list_item[0][1])


def using_dict():
    phones = {
        "둘리": "000-00000000",
        "도우너": "111111111111",
        "희동이": "111111112123123"
    }
    print(phones)

    pcopy = phones.copy()
    # 키-값 추가
    pcopy['고길동'] = "333-33333333333"
    print(pcopy)
    # 키를 이용한 값에 접근 : 키 접근 vs get 접근 비교
    # print(pcopy['마이콜'])  #키에러 : 키가 없음
    print(pcopy.get('마이콜'))  # 키가 없으면 : None
    print(pcopy.get('마이콜', "unknown"))  # 키가 없을 때 기본값 설정

    # 삭제 del
    del pcopy['고길동']
    print(pcopy)

    # 삭제시 값을 가져온 후 삭제
    name = pcopy.pop('둘리')
    print(name)

    # 키-값 튜플을 가져온 후 삭제
    item = pcopy.popitem()
    print(item)
    print("name:", item[0], "phone:", item[1])
    item = pcopy.popitem()
    print(item)


def loop():
    """사전의 순회"""

    phones = {
        "둘리": "000-00000000",
        "도우너": "111111111111",
        "희동이": "111111112123123"
    }
    # 기본 순회
    for key in phones:
        print("key:", key, ", value:", phones.get(key))

    # 사전에서 key 목록을 받아온 후 해당 키값으로 접근
    for key in phones.keys():
        print("key:", key, "value:", phones.get(key))

    # 사전에서 key-value 튜플의 목록을 받아서 루프
    for key, value in phones.items():  # 튜플로 받아오니까 언패킹
        print("key:", key, "value:", value)


# 튜플이니까


# define_dict()
# dict_methods()
# using_dict()
loop()
