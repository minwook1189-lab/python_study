나이_문자 = input("나이를 입력하세요: ")
나이 = int(나이_문자)

if 나이 < 20:
    print("미성년자입니다.")
elif 나이 < 65:
    print("중장년입니다.")
else:
    print("노년입니다.")