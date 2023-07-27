//object에 method를 function으로도 받을 수 있다.
//함수명: function (인자){}


let greetings = {
  sayHello: function (name) {
    console.log(`Hello ${name}!`);
  },
  sayHi: function () {
    console.log('Hi!');
  },
  sayBye: function() {
    console.log('Bye!');
  }
};

//따로 매번 console.log를 찍지 않아줘도 된다는!
//console안에 log()함수 메소드를 사용하고 있던 것!
greetings.sayHello('Codeit');
greetings.sayBye();

//또 다른 출력하는 방법
greetings['sayHello']('Codeit');