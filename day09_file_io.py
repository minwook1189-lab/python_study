# Day 09 - 파일 입출력 (File I/O)
# 데이터분석의 핵심: 파일에서 데이터를 읽고, 결과를 파일로 저장하기

#파일 쓰기
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 파일 입출력 연습입니다.\n")

#파일 읽기
with open("hello.txt", "r", encoding="utf-8") as f:
    내용 = f.read()
    print(내용)

#한 줄씩 읽기
with open("hello.txt", "r", encoding="utf-8") as f:
    for 줄 in f:
        print(줄.strip())

#CSV 파일 다루기
with open("성적.csv", "w", encoding="utf-8-sig") as f:
    f.write("이름,국어,영어,수학\n")
    f.write("철수,85,90,78\n")
    f.write("영희,92,88,95\n")
    f.write("민수,78,82,80\n")

with open("성적.csv", "r", encoding="utf-8-sig") as f:
    for 줄 in f:
        데이터 = 줄.strip().split(",")
        print(데이터)


#각 학생의 평균 계산하기
with open("성적.csv", "r", encoding="utf-8-sig") as f:
    f.readline()
    for 줄 in f:
        데이터 = 줄.strip().split(",")
        이름 = 데이터[0]
        국어 = int(데이터[1])
        영어 = int(데이터[2])
        수학 = int(데이터[3])
        평균 = (국어 + 영어 + 수학)/3
        print(f"{이름}: 평균 {평균:.1f}점")