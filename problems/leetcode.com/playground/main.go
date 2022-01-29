package main

import "fmt"

// given ACABACACD
func generateLpsArray(s string) []int {
	n := len(s)                     // 10
	lpsArray := make([]int, len(s)) // [0 0 0 0 0 0 0 0 0 0]

	prefixEndIndex := 0
	// check each unique prefix from the beginning of the string
	for i := 1; i < n; i++ {
		// when i = 1, 0 > 0 && C != A, so false
		// when i = 2, 0 > 0 && A == A, so false.
		// when i = 3, 1 > 0 && B != C, so true. prefixEndIndex = 0
		for prefixEndIndex > 0 && s[i] != s[prefixEndIndex] {
			prefixEndIndex = lpsArray[prefixEndIndex-1]
		}

		// when i = 1, C != A, so false
		// when i = 2, prefixEndIndex = 0 and A == A, so true.
		// prefixEndIndex now becomes 1
		// lpsArray[2] = 1
		// when i = 3, prefixEndIndex = 0 and B != A, so false.
		if s[i] == s[prefixEndIndex] {
			prefixEndIndex++
			lpsArray[i] = prefixEndIndex
		}
	}

	return lpsArray
	// return matchingIndices
}

func main() {
	cases := []string{
		"abceabciiabc",
	}
	for _, c := range cases {
		fmt.Println(generateLpsArray(c))
	}
}
