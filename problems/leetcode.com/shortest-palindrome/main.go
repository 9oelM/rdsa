// https://leetcode.com/problems/shortest-palindrome/
package main

import (
	"fmt"
	"strings"
)

func isPalindrome(s string) bool {
	if len(s) <= 1 {
		return true
	}

	middle := len(s) / 2

	for i := 0; i < middle; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func reverseString(s string) string {
	if len(s) <= 1 {
		return s
	}

	byteStr := []byte(s)

	middle := len(byteStr) / 2

	for i := 0; i < middle; i++ {
		tmp := byteStr[i]
		byteStr[i] = byteStr[len(byteStr)-1-i]
		byteStr[len(byteStr)-1-i] = tmp
	}

	return string(byteStr)
}

func shortestPalindrome(s string) string {
	for i := 0; i < len(s); i++ {
		prependedString := reverseString(s[len(s)-i:])
		withPrependedString := strings.Join([]string{prependedString, s}, "")
		if isPalindrome(withPrependedString) {
			return withPrependedString
		}
	}

	return ""
}

func main() {
	cases := []string{
		"aacecaaa",
		"abcd",
		"babad",
		"cbbd",
		"a",
		"",
		"bbbbbbbbbbbbbbbbbbbbbbbbbb",
		"bbbbbbbbbbbbbabbbbbbbbbbbabb",
	}
	for _, c := range cases {
		fmt.Println(shortestPalindrome(c))
	}
}
