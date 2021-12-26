// https://leetcode.com/problems/string-to-integer-atoi/submissions/
package main

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

func myAtoi(s string) int {
	s = strings.TrimSpace(s)
	allDigits := ""
	if strings.HasPrefix(s, "-") {
		allDigits = "-"
		s = s[1:]
	} else if strings.HasPrefix(s, "+") {
		s = s[1:]
	}

	for i := 0; i < len(s); i++ {
		// only neeed 5 bits because it's a single digit
		singleDigit, err := strconv.ParseInt(string(s[i]), 10, 5)
		if err != nil {
			break
		} else if (allDigits == "-" || allDigits == "+" || allDigits == "") && singleDigit == 0 {
			continue
		}

		allDigits += fmt.Sprint(singleDigit)
	}

	parsedDigits, err := strconv.ParseInt(allDigits, 10, 32)

	if errors.Is(strconv.ErrSyntax, err) {
		panic(err)
	}

	return int(parsedDigits)
}

func main() {
	cases := []string{
		"42",
		"          -42",
		"4193 with words",
		"21474836460",
	}
	for _, c := range cases {
		fmt.Println(myAtoi(c))
	}
}
