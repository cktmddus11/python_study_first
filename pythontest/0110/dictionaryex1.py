'''
Created on 2020. 1. 10.

@author: GDJ_19
'''

singer = {}
singer['이름']  = '트와이스'
singer['구성원수'] = 9
singer['데뷔곡'] = '우아하게'
singer['소속사'] = 'JYP'
for i in singer.keys():
    print("%s => %s" %(i, singer[i]))
    
    
singer["소속사"]  = "SM"    
print(singer)
print(type(singer))  #    <class 'dict'>
print(type(singer.keys())) #<class 'dict_keys'>
print(singer['데뷔곡'])
    