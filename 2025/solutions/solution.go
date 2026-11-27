package solutions

type PartTest struct {
	Input  string
	Output int
}

type Solution struct {
	Part1      func(input string) int
	Part2      func(input string) int
	Part1Tests []PartTest
	Part2Tests []PartTest
}

var solutions = make(map[string]Solution)

func Register(day string, part1, part2 func(string) int, part1tests, part2tests []PartTest) {
	solutions[day] = Solution{part1, part2, part1tests, part2tests}
}

func GetSolution(day string) (Solution, bool) {
	solution, ok := solutions[day]
	return solution, ok
}
