package test

import (
	"flag"
	"testing"

	"solutions"
	_ "solutions/all"
)

// TO RUN:
// go test solutions/test --day ##

var day = flag.String("day", "", "day to test")
var part = flag.Int("part", 0, "part to test")
var _ = part

func TestDay(t *testing.T) {
	solution, _ := solutions.GetSolution(*day)

	// part1 tests
	for i, test := range solution.Part1Tests {
		input := test.Input
		expected := test.Output
		actual := solution.Part1(input)
		if expected != actual {
			t.Errorf("[part 1 %d] expected %d, actual %d", i, expected, actual)
		}
	}

	// part2 tests
	for i, test := range solution.Part2Tests {
		input := test.Input
		expected := test.Output
		actual := solution.Part2(input)
		if expected != actual {
			t.Errorf("[part 2 %d] expected %d, actual %d", i, expected, actual)
		}
	}

}
