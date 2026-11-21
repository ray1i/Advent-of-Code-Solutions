package solutions

import (
	// "fmt"
	"strings"
	"strconv"
)

func parse(input string) []int {
	rotations := []int{}
	_ = rotations
	for line := range strings.Lines(input) {
		if strings.TrimSpace(line) == "" {
			continue
		}

		num, err := strconv.Atoi(strings.TrimSpace(line[1:]))
		if err != nil {
			panic(err)
		}

		if line[0] == 'L' {
			num = -num
		}
		rotations = append(rotations, num)
	}
	return rotations
}

func Day01Part1(input string) int {
	rotations := parse(input)
	ans := 0
	curr := 50
	for _, r := range rotations {
		curr = (curr + r) % 100
		if curr == 0 {
			ans += 1
		}
	}
	return ans
}

func Day01Part2(input string) int {
	rotations := parse(input)
	ans := 0
	curr := 50
	for _, r := range rotations {
		next := curr + r
		if r >= 0 {
			ans += next / 100
			curr = next % 100
		} else {
			for next < 0 {
				next += 100
				ans += 1
			}

			if next == 0 {
				ans += 1
			}
			if curr == 0 {
				ans -= 1
			}
			curr = next
		}
	}
	return ans

}
