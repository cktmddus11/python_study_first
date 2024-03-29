'''
Created on 2020. 1. 20.

@author: GDJ_19
정규식 예제, 정규식 모듈 사용 X
'''
data = '''
    park 800905-1234567
    kim 700905-1234567
    choi 850101-a123456
'''
result = []
for line in data.split("\n"):
    # line : park 800905-1234567
    word_result = []
    for word in line.split(" "):
# word : park
# word :  800905-1234567 배열로
# word_result : [park, 800905-*******]
# isdigit() :  숫자인 경우 True
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-"+"*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))