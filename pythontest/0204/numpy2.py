'''
Created on 2020. 2. 4.

@author: GDJ_19
numpy2.py : numpy 예제. 기능 실습
'''
import numpy as np

x= np.arange(10) # 0 부터 9까지 숫자로 이루어진 배열
print(x) # [0, 1, 2, 3, 4, 5,6 7, 8, 9]
print(x[:5]) # [0, 1, 2, 3,4]
print(x[4:7]) # [4, 5, 6]
print(x[::2]) #[0, 2, 4, 6, 8]
print(x[1::2]) # [1, 3, 5, 7, 9]
print(x[1:8:3]) #[1, 4, 7]
print(x[::-1]) # [9, 8, 7, 6,5 4, 3, 2,1, 0]
# 0부터 9까지 난수를 4행 5열 배열에 저장
x = np.random.randint(10, size = (4, 5))
print(x)
# 2개의 행과 3개의 열
print(x[:2, :3])
# 모든행과 한개 씩 걸러서 열 조회
print(x[:, ::2])
# 행을 역으로 열도 역으로 조회
print(x[::-1, ::-1])