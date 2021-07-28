/*
 this decimal to binary function implemention follows successive division
 approach and assumes that the given number will always be an positive number
 
 @parms {Number} number
 @return {Array} binary representation of a given number
*/
function decimalToBinary(number) {
    let dividend = number;
    let remainders = [];

    while (dividend) {
        remainders.push(dividend % 2);
        dividend = parseInt(Math.floor(dividend / 2));
    }

    return remainders.reverse(remainders);
}

/*
 @parms {Array} binaryArr
 @return {Number} decimal representation of given binary value
*/
function binaryToDecimal(binaryArr) {
    let binary = binaryArr.reverse(binaryArr);

    let sum = 0;
    for (pow = 0; pow <= (binary.length - 1); pow++) {
        if (binary[pow] === 0) continue;

        if (pow === 0) {
            sum += 1;
            continue;
        }

        if (pow === 1) {
            sum += 2;
            continue;
        }

        sum += 2 ** pow;
    }

    return sum;
}

function solution(no) {
    const binary = decimalToBinary(no);

    return binaryToDecimal(binary.reverse(binary));
}

console.log(solution(13));
