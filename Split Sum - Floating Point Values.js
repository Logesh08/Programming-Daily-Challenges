// Split Sum - Floating Point Values
// The program must accept N floating point values as the input. The program must divide the given N floating point values into the following two categories.
// 1) The floating point values are greater than X.5, where X is the integer part of a floating point value.
// 2) The floating point values are less than or equal to X.5, where X is the integer part of a floating point value.
// Finally, the program must print the sum of the integer parts of the floating point values in both categories separated by a space as the output.

// Boundary Condition(s):
// 1 <= N <= 100
// 1.00000 <= Each floating point value <= 99999.99999

// Input Format:
// The first line contains N.
// The second line contains N floating point values separated by a space.

// Output Format:
// The first line contains two integers separated by a space representing the two sum values based on the given conditions.

// Example Input/Output 1:
// Input:
// 5
// 100.50001 12.5 10.45 9.501 20.49999

// Output:
// 109 42

// Explanation:
// Here N = 5.
// The floating values under the 1st category are 100.50001 and 9.501.
// The floating values under the 2nd category are 12.5, 10.45 and 20.49999.
// The sum of 100 and 9 is 109.
// The sum of 12, 10 and 20 is 42.
// Hence the output is
// 109 42
 
// Example Input/Output 2:
// Input:
// 6
// 1.5 2.1 3.0 10.6 10.99 5.51

// Output:
// 25 6









var readline = require('readline');
var reader = readline.createInterface({
  input: process.stdin,
  terminal: true
});

var lines = [];

reader.on('line', function (line) {
    lines.push(line);
});

reader.on('close', function () {
    var n = Number(lines[0]);
    var a = 0 ,b = 0;
    lines[1].split(' ').forEach((item,index)=>{
        item = item.split('.')
        var val = Number(item[0]) , decimal =  item[1];
        if (Number(decimal[0])>=5 && Number(decimal.split('').reverse().join(''))>5){
            a += val ;
        }else{
            b += val ;
        }
    });
    console.log(a,b);
});