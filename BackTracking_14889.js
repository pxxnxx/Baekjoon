function count(que){
    let sum = 0;
    for (let i=0; i<que.length; i++) {
        for (let j=i+1; j<que.length; j++) {
            sum += stat[que[i]][que[j]] + stat[que[j]][que[i]]
        }
    }
    return sum
}

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

let n = parseInt(input.shift());

let member = [];
for (let i=0; i<n; i++)
    member.push(i)
let stat = [];
for (let i=0; i<n; i++)
    stat.push(input.shift().split(" ").map(Number));

const comb = combination(member,n/2);

let answer = Number.MAX_SAFE_INTEGER;
for (let i=0; i<comb.length/2; i++) {
    let teamA = comb[i];
    let teamB = comb[comb.length-i-1];
    answer = Math.min(answer, Math.abs(count(teamA)-count(teamB)));
}
console.log(answer)

