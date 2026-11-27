package day02

import (
	"strconv"
	"strings"

	"solutions"
)

type idRange struct {
	start int
	end   int
}

func parse(input string) []idRange {
	res := []idRange{}
	for _, line := range strings.Split(input, ",") {
		start_s, end_s, _ := strings.Cut(strings.TrimSpace(line), "-")
		start, _ := strconv.Atoi(start_s)
		end, _ := strconv.Atoi(end_s)
		res = append(res, idRange{start, end})
	}

	return res
}

func part1(input string) int {
	isInvalid := func(id int) bool {
		id_str := strconv.Itoa(id)
		return id_str[0:len(id_str)/2] == id_str[len(id_str)/2:]
		//
		// temp := id
		// left := id
		// right := 0
		//
		// exp := 1
		// for temp > 0 {
		// 	right += left % 10 * exp
		// 	left /= 10
		// 	temp /= 100
		// 	exp *= 10
		// }
		// right += exp
		// left += exp
		// // fmt.Printf("%d, %d, %d\n", exp, left, right)
		//
		// return left == right
	}

	ranges := parse(input)

	invalid := make(map[int]struct{})

	for _, r := range ranges {
		start, end := r.start, r.end
		for id := start; id <= end; id++ {
			if isInvalid(id) {
				invalid[id] = struct{}{}
			}
		}
	}

	ans := 0
	for id, _ := range invalid {
		ans += id
	}

	return ans
}

func part2(input string) int {
	isInvalid := func(id int) bool {
		id_str := strconv.Itoa(id)
		for parts := 2; parts <= len(id_str); parts++ {
			if len(id_str)%parts != 0 {
				continue
			}
			part_size := len(id_str) / parts
			good := true
			for part := 0; part < parts-1; part++ {
				first := id_str[part*part_size : (part+1)*part_size]
				second := id_str[(part+1)*part_size : (part+2)*part_size]
				if first != second {
					good = false
					break
				}
			}
			if good {
				return true
			}

		}
		return false
	}

	ranges := parse(input)

	invalid := make(map[int]struct{})

	for _, r := range ranges {
		start, end := r.start, r.end
		for id := start; id <= end; id++ {
			if isInvalid(id) {
				invalid[id] = struct{}{}
			}
		}
	}

	ans := 0
	for id, _ := range invalid {
		ans += id
	}

	return ans
}

var part1tests = []solutions.PartTest{
	{
		Input:  `11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124`,
		Output: 1227775554,
	},
}
var part2tests = []solutions.PartTest{
	{
		Input:  `11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124`,
		Output: 4174379265,
	},
}

func init() { solutions.Register("02", part1, part2, part1tests, part2tests) }
