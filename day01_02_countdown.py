# 교재 countdown 예제
# 파이썬은 스네이크 표기법, ctlr /를 하면 부분 주석 처리

countdown_list = [5, 4, 3, 2, 1, "hey!"]
#for countdown in 5, 4, 3, 2, 1, "hey!"
for countdown in countdown_list:
    print(countdown)
print(countdown_list[3]) # index는 0번부터 시작
print(countdown_list[-3]) # 역방향으로는 -1부터 시작
print(countdown_list[-1])
print('프로그램 종료')