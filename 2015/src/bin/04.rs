use std::fs;
use std::time::Instant;

use md5;

const INPUT_FILE: &str = "input/04.txt";

fn part1(input: &str) -> i32 {
    let mut i = 0;
    loop {
        let hash = md5::compute(input.to_owned() + &i.to_string())
            .to_ascii_lowercase()
            .into_iter()
            .map(|b| format!("{:02x}", b))
            .collect::<String>();

        if hash.starts_with("00000") {
            return i;
        }
        i += 1;
    }
}

fn part2(input: &str) -> i32 {
    let mut i = 0;
    loop {
        let hash = md5::compute(input.to_owned() + &i.to_string())
            .to_ascii_lowercase()
            .into_iter()
            .map(|b| format!("{:02x}", b))
            .collect::<String>();

        if hash.starts_with("000000") {
            return i;
        }
        i += 1;
    }
}

fn main() {
    // part 1 tests
    assert_eq!(part1("abcdef"), 609043);
    assert_eq!(part1("pqrstuv"), 1048970);

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
