function solution(arr) {
  //중복값제거
  const uniqueArr = [...new Set(arr)];
  //내림차순정렬
  uniqueArr.sort((a, b) => b - a);
  return uniqueArr;
}
