점수입력 = input("점수를 입력하세요: ")
점수 = int(점수입력)
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