package solutions

import (
	"testing"
)

func TestDay01Part1(t *testing.T) {
	input := `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`
	d := Day01{}
	expected := 3
	actual := d.Part1(input)
	if expected != actual {
		t.Errorf("expected %d, actual %d", expected, actual)
	}
}

func TestDay01Part2(t *testing.T) {
	input := `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`
	d := Day01{}
	expected := 6
	actual := d.Part2(input)
	if expected != actual {
		t.Errorf("expected %d, actual %d", expected, actual)
	}


	asdf := d.Part2("R1000")
	if asdf != 10 {
		t.Errorf("for 1000, expected 10, actual %d", asdf)
	}
}
