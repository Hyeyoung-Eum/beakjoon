//scoreObject.subject로 하면 왜 안되지? 싶었는데
//당장 subject라는 프로퍼티 명은 없기 때문이다.
//이렇게 동적으로 할당해줄 때는, 대괄호 표기법으로 scoreObject[subject] 로 적용해야한다.

let hyesoonScore = {
  '데이터 모델링의 이해': 10,
  '데이터 모델과 성능': 8,
  'SQL 기본': 22,
  'SQL 활용': 18,
  'SQL 최적화 기본 원리': 20,
};

let minsoonScore = {
  '데이터 모델링의 이해': 14,
  '데이터 모델과 성능': 8,
  'SQL 기본': 12,
  'SQL 활용': 4,
  'SQL 최적화 기본 원리': 16,
};

function passChecker(scoreObject) {

  let totalScore = 0;

  for (let subject in scoreObject) {
    totalScore += scoreObject[subject];
  }

  if (totalScore >= 60) {
    console.log('축하합니다! 합격입니다!');
  } else {
    console.log('아쉽지만 불합격입니다..');       
  }
}

passChecker(hyesoonScore);
passChecker(minsoonScore);