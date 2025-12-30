use std::fs;
use std::time::Instant;

use regex::Regex;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/25.txt";

static INPUT_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"Enter the code at row (\d+), column (\d+).").unwrap());

const START: u64 = 20151125;
const FACTOR: u64 = 252533;
const DIVISOR: u64 = 33554393;

fn part1(row: usize, col: usize) -> u64 {
    let mut ans: u64 = START;
    let reps = ((row + col - 2) * (row + col - 1) / 2) + col;

    for _ in 1..reps {
        ans = (ans * FACTOR) % DIVISOR;
    }

    ans
}

// fn part2(row: usize, col: usize) -> u64 {
//     0
// }

fn main() {
    assert_eq!(part1(1, 1), START);
    assert_eq!(part1(6, 1), 33071741);
    assert_eq!(part1(1, 6), 33511524);
    assert_eq!(part1(6, 6), 27995004);

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");
    let captures = INPUT_RE.captures(&input).unwrap();
    let (row, col): (usize, usize) = (
        captures.get(1).unwrap().as_str().parse().unwrap(),
        captures.get(2).unwrap().as_str().parse().unwrap(),
    );

    let start_time = Instant::now();
    let ans = part1(row, col);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    // let start_time = Instant::now();
    // let ans = part2(row, col);
    // println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
