single_line = '한 줄의 문자형'
single_line2 = "쌍따옴표도 사용가능합니다."
# single_line = "시작 기호와 끝 기호는 일치해야만 합니다' 컨트롤 슬러쉬(/) 주석표시됨
multiple_line = '''대한민국
만세'''
multiple_line2 = """대한민국 
만세"""

print(single_line, single_line2,multiple_line,multiple_line2 )
print(single_line + single_line2)
print("SBS\n아카데미") 
print(type(single_line))
print(type(1))
print(type(1,0))
print(true) #bool자료형
print("true") #str자료형
print("\n")

s = 'hello' #문자열은 리스트와 동일하게 취급합니다. 그래서 인덱스 번호를 가집니다.
#프로그래밍에서 숫자의 시작은 0부터입니다
#h->0 e->
#h e l l o 문자열
#0 1 2 3 4 문자열의 인덱스 번호
#-5-4-3-2-1 역순(좌에서 우방향) 인덱스 번호
print(s)
print(s[1])
print(s[-4])

s2 = s[1]
print(s)
print(s2)

s3 = s[0] + s[1] + s[2]
print(s3)
s4 = s[0:3]
#hello
#01234
#시작 인덱스는 그대로 사용: 끝 인덱스의 앞문자까지 출력:STEP은 간격 (37페이지 정도 내용) :간격(기본값은 1)
print(s4)
s5 = s[0:4:2]
print(s5)
s6 = s[0:5:2]
print(s6)
s7 = s[1:5:1]
print(s7)
s7 = s[1:5]
print(s7)
s7 = s[1:] #끝번호를 생략하면 문자열의 끝까지 출력합니다.
print(s7)
s8 = s[0:2:]
print(s8)
s8 = s[:2] #시작번호를 생략하면 첫 문자부터 시작합니다.
print(s8)

