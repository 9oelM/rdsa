// https://leetcode.com/problems/longest-palindromic-substring/
package main

import "fmt"

func isPalindrome(s string) bool {
	if len(s) == 1 {
		return true
	}

	for i := 0; i < len(s)/2; i++ {
		counterCharIndex := len(s) - i - 1
		if s[i] != s[counterCharIndex] {
			return false
		}
	}
	return true
}

func longestPalindrome(s string) string {
	for i := len(s); i >= 2; i-- {
		numOfPossiblePalindromeCases := len(s) - i + 1
		for j := 0; j < numOfPossiblePalindromeCases; j++ {
			if isPalindrome(s[j : i+j]) {
				return s[j : i+j]
			}
		}
	}

	if len(s) > 0 {
		return string(s[0])
	}
	return ""
}

func main() {
	cases := []string{
		"babad",
		"cbbd",
		"a",
		"",
		"bbbbbbbbbbbbbbbbbbbbbbbbbb",
		"bbbbbbbbbbbbbabbbbbbbbbbbabb",
	}
	for _, c := range cases {
		fmt.Println(longestPalindrome(c))
	}
}
