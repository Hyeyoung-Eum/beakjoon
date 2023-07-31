let today = new Date(2023, 06, 32,0,0,0);
let ourLove = new Date(2019, 5, 12);

console.log(today);
console.log(ourLove);
function loveDayCalc(startDate) {
  let name = '00'
  let timeDiff = today.getTime() - startDate.getTime();
  let dayDiff = timeDiff/ 1000 / 60 / 60 / 24;

  console.log(`${name}님을(를) 사랑한 지 ${dayDiff+1}일째 되는 날 입니다.`)
}

loveDayCalc(ourLove)