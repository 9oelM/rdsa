/*
	Implement a function in JavaScript which takes two parameters and
	return result based on certain criteria.
	Run tests to understand the requirements.
*/

const validate = actionType => {
    const INVALID_ACTION_TYPE = 'invalid action type',
        ACTION_OUT_OF_RANGE = 'action out of range'

    if(!Number.isInteger(actionType)){
        throw new Error(INVALID_ACTION_TYPE)
        return
    }
    if (actionType === 1 || actionType === 2){
        return
    }
    throw new Error(ACTION_OUT_OF_RANGE)
}

const processString = inputString => {
    // When action is 1 and if input string has a repeating character in same case (upper/lower) then return the string as it is
    if ([...new Set(inputString.split(''))].length === 1){
        return inputString
    }

    // When action is 1 and input string has a repeating character but in different case (upper/lower) then it must destroy each other and remaining string should be returned.
    let dict = {}
    let resultStr = ''
    for (const c of inputString){
        const upperCase = c.toUpperCase()
        if(!dict[upperCase])
            dict[upperCase] = 1
        else
            dict[upperCase] += 1
    }
    for (const c of inputString){
        const upperCase = c.toUpperCase()
        if(dict[upperCase] < 2){
            resultStr = `${resultStr}${c}`
        }
    }
    return resultStr
}

function main(actionType,inputString){
    validate(actionType)
    if(actionType === 1){
        return processString(inputString)
    }
}

main(1, "ABabABabeDefc")
