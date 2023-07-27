let current = 1;
let previous = 0;
let n = 50; //fibonacci n번째 수까지 출력하기

for (let i=1; i<=n;i++){
  console.log(current);
  let temp = previous;
  previous = current;
  current = temp + current;
}