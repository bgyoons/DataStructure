# Section 10
# 파이썬 외부 파일 처리의 이해
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MINE - text/csv
import csv
# ex 01
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # next(reader) Header 스킵(열 이름 생략)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# ex 02
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 선택, 문자를 기준으로 split
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) 
    print()

    for c in reader:
        print(c)

# ex 03 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-------------')

# ex 04
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w') as f:  # newline='' : 새로운 라인 생김
    wt = csv.writer(f)
    
    for v in w:
        wt.writerow(v)

# ex 05
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # dir 확인\
    wt.writerows(w) # 리스트를 한번에 씀


# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd) 포함

import pandas as pd

# sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자
xlsx = pd.read_excel('./resource/sample.xlsx') 

# 상위 데이터 확인
print(xlsx.head()) # 첫 번째부터 다섯 번째까지

# 데이터 확인
print(xlsx.tail()) # 끝부분부터 다섯가지

# 데이터 구조
print(xlsx.shape) # 행, 열


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)