# -*- coding: utf-8 -*-

# 예제 1-1 딕셔너리 -> 시리즈 변환

import pandas as pd #판다스 불러오기
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
sr = pd.Series(dict_data)

print(sr)

# 예제 1-2 시리즈 인덱스
list_data = ['2023-06-08', 3.14, 'HOJIN', 100, True]
sr_1 = pd.Series(list_data)
print(sr_1)  #시리즈 - 정수형 위치 인덱스가 자동으로 설정된다.

idx = sr_1.index     # .index -> 인덱스 배열을 불러옴.
val = sr_1.values    # .values -> 데이터 값의 배열을 불러옴.
print(idx) 
print(val)

# 예제 1-3 시리즈 원소 선택
tup_data = ('호진', '1994-05-24', '여', True)
sr_2 = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr_2)

print(sr_2[0])
print(sr_2['이름'])
print(sr_2[[1,2]])
print(sr_2[['생년월일', '성별']])
print(sr_2[1:2])  #범위 지정(정수형일 경우) - 끝 포함 X
print(sr_2['생년월일':'학생여부']) #범위 지정(인덱스 이름 사용) - 끝 포함

# 예제 1-4 딕셔너리 -> 데이터프레임 변환
