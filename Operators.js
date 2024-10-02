const mathOperation = (a, b, someFunction) => someFunction(a,b);

const add = (a, b) => a+b;
const subtract = (a, b) => a-b;
const divide = (a, b) => a/b;


mathOperation(10,5, add);

const