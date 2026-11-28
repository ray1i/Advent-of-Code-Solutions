package day03

import (
	"slices"
	"strconv"
	"strings"

	"solutions"
)

func parse(input string) [][]int {
	res := [][]int{}
	for line := range strings.SplitSeq(input, "\n") {
		line_int := []int{}
		for c := range strings.SplitSeq(line, "") {
			c_int, _ := strconv.Atoi(c)
			line_int = append(line_int, c_int)
		}
		res = append(res, line_int)
	}
	return res
}

func maxWithIndex(nums []int) (int, int) {
	maximum := 0
	maximum_index := 0
	for i, n := range nums {
		if n > maximum {
			maximum = n
			maximum_index = i
		}
	}
	return maximum, maximum_index
}

func part1(input string) int {
	lines := parse(input)
	ans := 0

	for _, nums := range lines {
		var max1, max2 int
		max1, max1_i := maxWithIndex(nums)
		if max1_i >= len(nums)-1 {
			max2 = max1
			max1, _ = maxWithIndex(nums[:max1_i])
		} else {
			max2, _ = maxWithIndex(nums[max1_i+1:])
		}
		res := max1*10 + max2
		ans += res
	}

	return ans
}

func maxN(nums []int, n int) []int {
	if len(nums) <= n {
		return nums
	}
	if len(nums) <= 1 {
		return nums
	}

	m, i := maxWithIndex(nums)
	if n == 1 {
		return []int{m}
	}

	right := maxN(nums[i+1:], n-1)
	left := []int{}
	if len(right)+1 < n {
		left = maxN(nums[:i], n-len(right)-1)
	}
	return slices.Concat(left, []int{m}, right)
}

func part2(input string) int {
	lines := parse(input)
	ans := 0

	for _, nums := range lines {
		maxes := maxN(nums, 12)
		res := 0
		for _, m := range maxes {
			res *= 10
			res += m
		}
		ans += res
	}

	return ans
}

var testInput = `987654321111111
811111111111119
234234234234278
818181911112111`

var part1tests = []solutions.PartTest{
	{
		Input:  testInput,
		Output: 357,
	},
}
var part2tests = []solutions.PartTest{
	{
		Input:  testInput,
		Output: 3121910778619,
	},
}

func init() { solutions.Register("03", part1, part2, part1tests, part2tests) }
