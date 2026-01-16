# 점수를 입력받되, 잘못된 입력이면 다시 물어보기

while True:
    입력값 = input("점수를 입력하세요(0~100): ")
    
    # 1단계: 숫자인지 확인
    if not 입력값.isdigit():
        print("숫자만 입력하세요.")
        continue  # 다시 while 처음으로 돌아감
    
    # 2단계: 숫자로 변환
    점수 = int(입력값)
    
    # 3단계: 범위 확인 (0~100)
    if 점수 < 0 or 점수 > 100:
        print("0~100 사이로 입력하세요.")
        continue  # 다시 while 처음으로 돌아감
    
    # 4단계: 여기까지 왔으면 올바른 점수 -> 반복 종료
    break  # while 루프 빠져나감

# 5단계: 학점 출력 (day03_score.py와 동일)
if 점수 >= 90:
    print("A 학점입니다.")
elif 점수 >= 80:
    print("B 학점입니다.")
elif 점수 >= 70:
    print("C 학점입니다.")
elif 점수 >= 60:
    print("D 학점입니다.")
else:
    print("F 학점입니다.")

