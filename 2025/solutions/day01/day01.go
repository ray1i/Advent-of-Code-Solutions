package day01

import (
	"strconv"
	"strings"

	"solutions"
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

func part1(input string) int {
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

func part2(input string) int {
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

var part1tests = []solutions.PartTest{
	{
		Input: `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`,
		Output: 3,
	},
}
var part2tests = []solutions.PartTest{
	{
		Input: `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`,
		Output: 6,
	},
	{
		Input:  "R1000",
		Output: 10,
	},
}

func init() { solutions.Register("01", part1, part2, part1tests, part2tests) }
