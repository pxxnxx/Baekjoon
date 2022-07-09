function combination(arr, selectNum) {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
    arr.forEach((v, idx, arr) => {
        const fixed = v;
        const restArr = arr.slice(idx + 1);
        const combinationArr = combination(restArr, selectNum - 1);
        const combineFix = combinationArr.map((v) => [fixed, ...v]);
        result.push(...combineFix);
    });
    return result;
}

let fs = require("fs");
let filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

while (true) {
    let put = input.shift().split(" ").map(Number);
    if (put[0] === 0) break;
    let lotto = []
    for (let i=1; i<put.length; i++) lotto.push(put[i])
    let answer = combination(lotto, 6);
    for (const x of answer) {
        for (const y of x)
            process.stdout.write(String(y) + " ")
        console.log()
    }
    console.log()
}