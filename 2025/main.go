package main

import (
	"fmt"
	"time"
	"os"

	"solutions"
)

func timer(name string) func() {
	start := time.Now()
	return func() {
	      fmt.Printf("[%s]: %s\n", name, time.Since(start))
	}
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

	defer timer("day01")()
	solution := solutions.Day01Part1(input)
	fmt.Println(solution)
	
	defer timer("day01part2")()
	solution = solutions.Day01Part2(input)
	fmt.Println(solution)
}
