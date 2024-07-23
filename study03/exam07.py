li = [1,2,3,4,5] #리스트는 대괄호로 생성 가능합니다.
print(li)
print(type(li))

li1 = [1, 3.14, '대한민국', True]
print(li1) #39P내용

#40p
print(li[0]) #1
print(li[1]) #2
print(li[2]) #3
print(li[3]) #4
print(li[4]) #5
# print(li[5]) #없음

#리스트의 슬라이싱
print(li[0:3])
print(li[::2]) #시작인덱스 생략은 처음부터 : 끝인덱스 생략은 끝까지: 2개 간격으로
print(li[0:-2])
print(li[-2:0:-1]) #음수를 이용한 슬라이싱도 가능합니다. 

#리스트의 요소 추가
li2 = [10, 20,30,40,50]
li2.append(60)
print(li2)
li2.insert(1,100) #첫번째 입력값은 인덱스 번호, 두번째 입력값은 추가하는 value
print(li2) #insert는 인덱스 번호에 값을 추가하고 그 위치에 있던 값은 뒤로 한칸씩 이동시킵니다.
#append는 가장 뒤에 값을 추가하므로 연산이 빠르지만 insert는 값을 추가하고
#입력된 값 뒤의 모든 값을 한칸씩 이동시키는 연산이 추가되기 때문에 append보다 느립니다. 

#리스트의 요소 삭제
li2.pop() #끝 번호 인덱스 삭제
print(li2)
li2.pop(1) #인덱스 번호를 지정하면 지정번호가 삭제
print(li2)