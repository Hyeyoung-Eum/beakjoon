#첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다.
# (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다.

# 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

# now=input().split()
# now_hour=int(now[0])
# now_min=int(now[1])

#위의 세 줄은 아래 한 줄로 변경 가능
now_hour, now_min = map(int, input().split())

run_time=int(input())

total_min=now_hour*60+now_min+run_time

final_hour=total_min//60
if (final_hour>=24) :
    final_hour = final_hour-24

final_min=total_min%60

print(final_hour, final_min)
