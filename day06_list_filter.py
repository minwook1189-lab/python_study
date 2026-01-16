점수들 = [85, 33, 78, 95, 88]
print("원본 점수들:", 점수들)

고득점 = [점수 for 점수 in 점수들 if 점수 >=80]
print("80점 이상:", 고득점)

오름차순 = sorted(점수들)
print("오름차순:", 오름차순)

내림차순 = sorted(점수들, reverse=True)
print("내림차순:", 내림차순)

print("평균:", sum(점수들)/len(점수들))
print("최고점", max(점수들))
print("최저점", min(점수들))