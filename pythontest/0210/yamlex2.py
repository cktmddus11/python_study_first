'''
Created on 2020. 2. 10.

@author: GDJ_19
yaml 문서에서 alias, 주석 설정하기
'''
import yaml
yaml_str = """
# 정의
color_def : 
        - &color1 "#FF0000"
        - &color2 "#00FF00"
        - &color3 "#0000FF"
# 별칭 정하기
color : 
    title : *color1
    body : *color2
    link : *color3
    div : *color1
"""
data = yaml.load(yaml_str, Loader=yaml.FullLoader)
print("title=", data["color"]["title"])
print("body=", data["color"]["body"])
print("link=", data["color"]["link"])
print("div=", data["color"]["div"])

