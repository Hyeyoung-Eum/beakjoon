//arr.map(callbackFunction, [thisArg])
//arr.map(callbackFunction(currentValue, index, array), thisArg)

//arr.map(함수)

const numbers = [1, 3, 5];
const listItems = numbers.map(function(number){
    console.log(number);
    return number + 1;
});

console.log(listItems);