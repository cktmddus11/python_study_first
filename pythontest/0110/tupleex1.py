'''
Created on 2020. 1. 10.

@author: GDJ_19
튜플 예제
    변경불가 리스트 
'''

tp1 =(10, 20, 30)
print(tp1)
#tp1.append(10) 값 추가 X
print(tp1[0], tp1[1], tp1[2])
#tp1[0] = 100 # 값 변경 X
# 튜플을 리스트로 변환
list = list(tp1)
list.append(40)
# 리스트를 다시 튜플로 변환
tp1 = tuple(list)
print(tp1)
print("tp1 의 크기", len(tp1), "list의 크기", len(list))
print("tp1[1:3]=", tp1[1:3], tp1[1:3], "list[1:3]=", list[1:3])
print("tp1[:3]=", tp1[:3], "list[:3]=", list[:3])
print("tp1[2:]=", tp1[2:], "list[2:]=", list[2:])
print("tp1[::2]=", tp1[::2], "list[::2]=", list[::2]) # 2칸씩 띄어서 


