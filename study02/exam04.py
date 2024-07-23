'''
int : 정수(integer) -> 소수점이 없는 수(1,2,3,4,5,6,7,8,9,0)
float : 실수 -> 소수점이 있는 수(3.14, 1.2345, 1.23e10)
bool : boolian이라고도 합니다. 참(true) 또는 거짓(Fales) 2개의 값만 가집니다.
         파이썬에서는 True와 Fales의 첫 글자를 대문자로 사용합니다.
str : 문자열(string) -> 흔히 말하는 텍스츠로 ''또는 ""로 감싸야만 합니다.
        ''처럼 내부에 문자가 없어도 문자열이 생성이 된 것으로 간주합니다.
        
'''
name = '박세희' #str 문자열
age = '20' #str 문자열(작은 따옴표로 감싼 숫자도 문자열입니다)
age = 20 #int정수(소수점이 없는 수)
weight = 99.9 #float 실수(소수점이 있는 수)

'''
각자의 자료형은 형태를 변환할 수 있습니다
'''

age2 = '20' #문자열
print(age2)
print(age2 + '20') #문자열 + 문자열 가능
print(int(age2) + 20) #문자열 + 정수 불가능 -> 문자열을 정수로 변환합니다.
#문자열을 정수나 실수로 변환할 때는 숫자의 형식을 따라야합니다.

print('나이'+ age2)
age3 = 20
print('나이'+ str(age3)) #정수를 문자열로 변환합니다.

light_on = True #bool 불 또는 불리언
print(light_on)
print(int(light_on))
print(float(light_on))
light_on = False #bool 불 또는 불리언
print(light_on)
print(int(light_on))
print(float(light_on))
number = 1.01234567890123456789 #소수점 19자리 기록
print(number) #실수는 소수점 16자리까지 사용가능합니다.
int_number = 10_000_000_000 #정수 입력시 언더바는 무시됩니다.
print(int_number)
print("1234567890123456789")





