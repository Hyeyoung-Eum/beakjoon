def number_coroutine():
    while True: #코루틴 값이 들어오는 만큼 계속 재실행하기 위해 무한루프 사용
        x = (yield) #코루틴 바깥에서 값을 받아옴.()필수
        print(x)

co = number_coroutine() #코루틴 객체 생성
next(co) #코루틴 안의 yield까지 코드 최초 실행.(yield 공간 파둠)

co.send(1)
co.send(2)
co.send(3)