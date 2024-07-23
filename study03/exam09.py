l = [1,2,3,4,5]
print(l)

d = {}
print(type(d))
d = {'key1':'value1', 'key2':'value2'}
print(d)

d = {0:10, 1:20, 2:30}
print(d)

print(l[0])
print(l[1])
print(d[0]) #딕셔너리도 인덱싱이 가능하다
print(d[1])
# print(d[0:3]) #딕셔너리는 슬라이싱은 불가능합니다.
d = {'a':'apple', 'b':'banana','c':'carrot'}
# print(d[0]) #딕셔너리는 시퀀스 타입이 아니기 때문에 인덱스가 없습니다.
print(d['a']) #딕셔너리는 키를사용합니다
d['t'] = 'temp' #딕셔너리 추가
print(d)
d.pop('t') #딕셔너리 삭제
print(d)
d['a'] = 'app' #딕셔너리 값 수정
print(d)
d.update(a = 'apple') #update 함수 값에서는 키값에 따옴표로 감싸지 않습니다.
print(d)

