# Day 10 - 에러 처리 (Error Handling)
# 프로그램이 오류로 멈추지 않도록 에러를 잡아서 처리하기

# 1. 기본 try-except
try:
    숫자 = int(input("숫자를 입력하세요: "))
    print(f"입력한 숫자: {숫자}")
except ValueError:
    print("숫자가 아닙니다!")

# 2. 여러 에러 처리
try:
    숫자 = int(input("숫자를 입력하세요: "))
    결과 = 10 / 숫자
    print(f"10 / {숫자} = {결과}")
except ValueError:
    print("숫자가 아닙니다!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")

# 3. finally (에러 여부와 상관없이 항상 실행)
try:
    숫자 = int(input("숫자를 입력하세요: "))
    print(f"입력한 숫자: {숫자}")
except ValueError:
    print("숫자가 아닙니다!")
finally:
    print("프로그램을 종료합니다.")

# 4. 실전 예제 - 성적 입력 안전하게 받기
성적들 = []
for i in range(3):
    while True:
        try:
            점수 = int(input(f"{i+1}번째 점수 입력: "))
            if 점수 < 0 or 점수 > 100:
                print("0~100 사이의 점수를 입력하세요!")
            else:
                성적들.append(점수)
                break
        except ValueError:
            print("숫자만 입력하세요!")

print(f"\n입력된 성적: {성적들}")
print(f"평균: {sum(성적들)/len(성적들):.1f}점")
