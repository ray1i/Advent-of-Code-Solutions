use std::fs;
use std::time::Instant;

use std::collections::HashMap;

const INPUT_FILE: &str = "input/05.txt";

const VOWELS: [char; 5] = ['a', 'e', 'i', 'o', 'u'];

fn part1(input: &str) -> i32 {
    fn is_good_string(string: &str) -> bool {
        // contains at least 3 vowels
        if string
            .chars()
            .fold(0, |acc, c| if VOWELS.contains(&c) { acc + 1 } else { acc })
            < 3
        {
            return false;
        }

        // contains one letter that appears twice in a row
        if string
            .chars()
            .collect::<Vec<char>>()
            .windows(2)
            .all(|pair| pair[0] != pair[1])
        {
            return false;
        }

        // does not contain ab, cd, pq, xy
        const FORBIDDEN: [&str; 4] = ["ab", "cd", "pq", "xy"];
        if FORBIDDEN.iter().any(|bad| string.contains(bad)) {
            return false;
        }

        true
    }

    input.lines().fold(
        0,
        |acc, line| if is_good_string(line) { acc + 1 } else { acc },
    )
}

fn part2(input: &str) -> i32 {
    fn is_good_string(string: &str) -> bool {
        // contains a pair of any two letters that appears at least twice in the string
        let mut pairs: HashMap<String, usize> = HashMap::new();
        let mut seen = false;
        for (i, pair) in string.chars().collect::<Vec<char>>().windows(2).enumerate() {
            let pair = pair.iter().collect::<String>();
            let old_index = pairs.entry(pair).or_insert(i);
            if i > *old_index + 1 {
                seen = true;
                break;
            }
        }
        if !seen {
            return false;
        }

        // contains at least one letter which repeats with exactly one letter between them
        if string
            .chars()
            .collect::<Vec<char>>()
            .windows(3)
            .all(|trio| trio[0] != trio[2])
        {
            return false;
        }

        true
    }

    input.lines().fold(
        0,
        |acc, line| if is_good_string(line) { acc + 1 } else { acc },
    )
}

fn main() {
    // part 1 tests
    assert_eq!(part1("ugknbfddgicrmopn"), 1);
    assert_eq!(part1("aaa"), 1);
    assert_eq!(part1("jchzalrnumimnmhp"), 0);
    assert_eq!(part1("haegwjzuvuyypxyu"), 0);
    assert_eq!(part1("dvszwmarrgswjxmb"), 0);

    // part 2 tests
    assert_eq!(part2("qjhvhtzxzqqjkmpb"), 1);
    assert_eq!(part2("xxyxx"), 1);
    assert_eq!(part2("uurcxstgmygtbstg"), 0);
    assert_eq!(part2("ieodomkazucvgmuy"), 0);
    assert_eq!(part2("xilodxfuxphuiiii"), 1);

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
