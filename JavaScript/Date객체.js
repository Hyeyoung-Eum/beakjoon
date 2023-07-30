//내장 객체(Standard bulit-in objects)
//:가장 대표적인 예가 Date 객체

//Date 객체
let myDate = new Date();

///()안에 숫자를 넣으면,
///1970년 1월 1일 00:00:00 UTC + (숫자)밀리초만큼 더해져서 나온다.
//1000밀리초 = 1초

//new Date('문자열'); 방식
let myDate1 = new Date('2023-04-30');
let myDate2 = new Date('2023-07-30T23:52:58');
let myDate3 = new Date(2000, 04, 30, 23, 11, 23, 500);
//년, 월까지만 필수 입력. 나머지 생략시 0으로 뜸. 
//month는 0부터 시작함.( 0월 = 1월)
console.log(myDate);
console.log(myDate1);
console.log(myDate2);
console.log(myDate3);


console.log(myDate.getTime());
//myDate객체가, 1970년 1월 1일 00:00:00 UTC부터 몇 밀리 초 지났는지?
let timeDiff = myDate.getTime() - today.getTime();
//해당 시간이 지금으로부터 얼마만큼의 차이를 가지고 있는지 계산 가능.

//let myDate = new Date(2017, 4, 18, 19, 11, 16);
//getFullYear() 2017
//getMonth() 4(5월))
//getDate() 18 일자
//getDay() 4 요일(0이 일요일)
//getHours() 19
//getMinutes() 11
//getSeconds() 16
//getMilliseconds() 0