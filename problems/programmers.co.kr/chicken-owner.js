function solution(preWorkPerPartTimer, outputPerPartTimer, numChickenOrdered) {
    let preWorkDP = []
    const MY_OUTPUT = 2
    let result = [numChickenOrdered / MY_OUTPUT]
    let timeTaken = 0
    let answer = -1
    for(let recruitNum = 1; ; recruitNum++){

        for(let crntWorkingPartTimer = 0; crntWorkingPartTimer < recruitNum; crntWorkingPartTimer++){
            if (crntWorkingPartTimer >= preWorkDP.length && preWorkDP.length !== 0){ // NOT already computed
                //const time = preWorkPerPartTimer / crntWorkingPartTimer
                //preWorkDP.push(timer)
                //timeTaken = preWorkDP
                timeTaken += preWorkDP.reduce((acc,val) => acc+val)
                timeTaken += preWorkPerPartTimer / (crntWorkingPartTimer * outputPerPartTimer + MY_OUTPUT)
                preWorkDP.push(timeTaken)
           }
        }
        // work altogether
        timeTaken += numChickenOrdered / (recruitNum * outputPerPartTimer + MY_OUTPUT)
        result.push(timeTaken)
        //console.log(result)
        if(2 <= result.length && result[0] < result[1]){
            answer = result[0]
            break
        }
        else if(3 <= result.length && result[recruitNum-2] > result[recruitNum-1] && result[recruitNum-1] < result[recruitNum]){
            answer = result[recruitNum-1]
            break
        }
        timeTaken = 0
    }
    return Number(answer.toFixed(6))
}
/*
30.0	1.0	2.0	1.0
30.0	2.0	100.0	39.166667
30.5	3.14159	1999.1999	63.968001
500.0	4.0	2000.0	526.190476
*/
function main() {
    const cases = [[30, 1, 2], [30, 2, 100], [30.5, 3.14159, 1999.1999], [500, 4, 2000]]
    cases.forEach((c, i) => {
        //if(i === 1)
            solution(c[0], c[1], c[2])})
}

main()
