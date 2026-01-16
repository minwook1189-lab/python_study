점수들 = []

for i in range(5):
    입력값 = input(f"{i+1}번째 점수를 입력하세요: ")
    점수 = int(입력값)
    점수들.append(점수)

print("입력한 점수들:", 점수들)
print("평균:", sum(점수들) / len(점수들))
print("최고점:", max(점수들))
print("최저점:", min(점수들))