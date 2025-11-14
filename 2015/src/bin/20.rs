use std::fs;
use std::time::Instant;

use itertools::Itertools;

const INPUT_FILE: &str = "input/20.txt";

const MAX_SEARCH: usize = 1_000_000;

fn part1(input: &str) -> usize {
    let n = input.trim().parse::<usize>().unwrap() / 10;

    let mut seen = [1; MAX_SEARCH];

    for i in 2..MAX_SEARCH {
        let mut j = i;
        while j < MAX_SEARCH {
            seen[j] += i;
            j += i;
        }
    }

    seen.iter().find_position(|&val| *val >= n).unwrap().0
}

fn part2(input: &str) -> usize {
    let n = input.trim().parse::<usize>().unwrap();

    let mut seen = [0; MAX_SEARCH];

    for i in 1..MAX_SEARCH {
        let mut j = i;
        while j < MAX_SEARCH && j / i <= 50 {
            seen[j] += i * 11;
            j += i;
        }
    }

    seen.iter().find_position(|&val| *val >= n).unwrap().0
}

fn main() {
    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
