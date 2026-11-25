package solutions

import (
	"strings"
	"strconv"
)


type Day02 struct {}

type idRange struct {
	start int
	end int
}

func (d Day02) parse(input string) []idRange {
	res := []idRange{}
	for _, line := range strings.Split(input, ",") {
		start_s, end_s, _ := strings.Cut(strings.TrimSpace(line), "-")
		start, _ := strconv.Atoi(start_s)
		end, _ := strconv.Atoi(end_s)
		res = append(res, idRange{start, end})
	}

	return res
}

func (d Day02) Part1(input string) int {
	isInvalid := func(id int) bool {
		id_str := strconv.Itoa(id)
		return id_str[0:len(id_str) / 2] == id_str[len(id_str) / 2:]
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

	ranges := d.parse(input)

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

func (d Day02) Part2(input string) int {
	isInvalid := func(id int) bool {
		id_str := strconv.Itoa(id)
		for parts := 2; parts <= len(id_str); parts++ {
			if len(id_str) % parts != 0 { continue }
			part_size := len(id_str) / parts
			good := true
			for part := 0; part < parts - 1; part++ {
				first := id_str[part * part_size : (part + 1) * part_size]
				second := id_str[(part + 1) * part_size : (part + 2) * part_size]
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

	ranges := d.parse(input)

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
