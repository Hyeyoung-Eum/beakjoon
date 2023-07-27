let myVoca = {
  // 여기에 코드를 작성하세요
  addVoca: function (key, value) {
    myVoca[key] = value;
  },
  deleteVoca: function (key) {
    delete myVoca[key];
  },
  printVoca: function (key) {
    console.log(`"${key}"의 뜻은 "${myVoca[key]}"입니다.`);
  },
};

// addVoca메소드 테스트 코드
myVoca.addVoca('parameter', '매개 변수');
myVoca.addVoca('element', '요소');
myVoca.addVoca('property', '속성');
console.log(myVoca);

// deleteVoca메소드 테스트 코드
myVoca.deleteVoca('parameter');
myVoca.deleteVoca('element');
console.log(myVoca);

// printVoca메소드 테스트 코드
myVoca.printVoca('property');