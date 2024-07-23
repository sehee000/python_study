t = (1,2,3,4,5) #대괄호는 리스트 소괄호는 튜플
print(t)
t2 = (1, 3.14, "대한민국",True) 
print(t[0]) #인덱싱 사용 가능합니다.
print(t[::2]) #슬라이싱 사용 가능합니다
t3 = t[0] #t3는 int값을 가진 변수
print(t3)
print(type(t3))
li = [10,20,30,40,50]
li2 = li[0:3]
print(li2)
t3 = t[0:3]
print(t3)

li.append(60)
print(li)

# t3.append(6) #튜플은 추가 수정 삭제 불가합니다.
# print(t3)

li[0] = 100
print(li)

# t[0] = 1000 #튜플은 수정 불가
#print(t)
#ctrl 엔터 누르면 다음줄 내려감 ctrl 쉬프트 케이 한 줄 다 지워짐 

s = {1,2,3,4,5} #중괄호는 셋을 의미합니다.
print(s)

l = [1,1,1,2,2,2]
print(l)
tt = (1,1,1,2,2,2)
print(tt)
s = {1,1,1,2,2,2} #set은 값을 중복할 수 없습니다.
#set은 순서과 뒤바뀔 수 있습니다
print(s)

list_empty = []
print(type(list_empty))
list_construct = list() #생성함수를 이용하여 리스트 생성
print(type(list_construct))
tuple_empty = ()
print(type(tuple_empty))
tuple_construct = tuple() #생성함수
print(type(tuple_construct))
set_consturct = set() #생성함수
print(type(set_consturct))
set_empty = {} #set은 중괄호 초기화를 사용할 수 없습니다. dict의 생성에 사용합니다
print(type(set_empty))

print(s[0]) #43p

s.add(3) #set의 추가는 append나 insert가 아닌 add를 사용합니다.
print(s)

s.add(3) #이미 존재하는 값은 중복이라서 추가되지 않습니다.
print(s)

s.remove(1) #set의 삭제는 pop이 아닌 remove를 사용한다.
print(s)
#s.remove(1) #없는 값을 삭제할 경우 에러가 발생한다.
print(s)
s.discard(2) #set의 삭제는 remove이외에도 discard를 사용할 수 있습니다.
print(s)
s.discard(2) #없는 값을 삭제할 경우 에러 없이 출력합니다.
print(s)





