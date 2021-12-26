package main

import (
	"regexp"
	"strconv"
)

var numRegex = regexp.MustCompile(`[0-9]+`)

func areNumbersAscending(s string) bool {
	// max time complexity: len(s)
	numbers := numRegex.FindAllString(s, -1)
	var previouslyParsedPositiveNum int64 = -1
	// max time complexity: len(s)
	for _, num := range numbers {
		// 8 bits will be enough to contain a positive number up to 100
		parsedPositiveNum, err := strconv.ParseInt(num, 10, 8)
		if err != nil {
			panic(err)
		}
		if previouslyParsedPositiveNum != -1 && parsedPositiveNum <= previouslyParsedPositiveNum {
			return false
		}
		previouslyParsedPositiveNum = parsedPositiveNum
	}
	return previouslyParsedPositiveNum != -1
}

func main() {
	println(areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
	println(areNumbersAscending("hello world 5 x 5"))
	println(areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))
}
