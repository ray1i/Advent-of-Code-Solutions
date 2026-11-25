package main

import (
	"fmt"
	"time"
	"os"

	"solutions"
)

func runWithTimer(title string, fn func() int) {
	var start time.Time
	var ans int

	defer func() {
	      fmt.Printf("[%s] %d (took %s)\n", title, ans, time.Since(start))
	}()

	start = time.Now()
	ans = fn()
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("need day number: e.g. go run main 01")
		os.Exit(1)
	}

	day := os.Args[1]
	inputFile := fmt.Sprintf("./input/%s.txt", day)
	input_b, _ := os.ReadFile(inputFile)
	input := string(input_b)

	var solution solutions.Solution

	switch day {
	case "01": solution = solutions.Day01{}
	case "02": solution = solutions.Day02{}
	default:
		fmt.Println("not a valid day.")
		os.Exit(1)
	}

	runWithTimer("part 1", func() int { return solution.Part1(input) })
	runWithTimer("part 2", func() int { return solution.Part2(input) })
}
