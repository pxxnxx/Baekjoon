var fs = require("fs");
var filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
var input = fs.readFileSync(filePath).toString().trim().split('\n');

const n = parseInt(input.shift());
const arr = input.shift().split(" ").map(Number);
const opt = input.shift().split(" ").map(Number);
let max = -1000000000;
let min = 10000000;
function backTracking(ret, val, que) {
    if (val == n-1){
        max = Math.max(max, ret);
        min = Math.min(min, ret);
        return
    }
    for (let i=0; i<4; i++) {
        if (que[i] > 0) {
            que[i] -= 1;
            let temp = ret;
            if (i==0) 
                ret += arr[val+1];
            else if (i==1) 
                ret -= arr[val+1];
            else if (i==2) 
                ret *= arr[val+1];
            else { 
                ret /= arr[val+1];
                if (ret > 0) ret = Math.floor(ret);
                else ret = Math.ceil(ret);
            }
            backTracking(ret, val+1, que);
            que[i] += 1;
            ret = temp;
        }

    }
}
backTracking(arr[0], 0, opt);
console.log(max);
console.log(min);