use std::cmp::Ordering;
use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/17.txt";

fn ways(containers: &[i32], total: i32) -> i32 {
    if total == 0 {
        return 1;
    } else if total < 0 || containers.is_empty() {
        return 0;
    }

    ways(&containers[1..], total) + ways(&containers[1..], total - containers.first().unwrap())
}

fn part1(input: &str) -> i32 {
    let containers: Vec<i32> = input
        .trim()
        .lines()
        .map(|num| num.parse().unwrap())
        .collect();
    ways(&containers, 150)
}

fn ways2(containers: &[i32], total: i32, used: i32) -> (i32, i32) {
    if total == 0 {
        return (1, used);
    } else if total < 0 || containers.is_empty() {
        return (0, i32::MAX);
    }

    let not_using_curr = ways2(&containers[1..], total, used);
    let using_curr = ways2(
        &containers[1..],
        total - containers.first().unwrap(),
        used + 1,
    );

    match not_using_curr.1.cmp(&using_curr.1) {
        Ordering::Less => not_using_curr,
        Ordering::Greater => using_curr,
        Ordering::Equal => (not_using_curr.0 + using_curr.0, not_using_curr.1),
    }
}

fn part2(input: &str) -> i32 {
    let containers: Vec<i32> = input
        .trim()
        .lines()
        .map(|num| num.parse().unwrap())
        .collect();
    ways2(&containers, 150, 0).0
}

fn main() {
    // ways test
    assert_eq!(ways(&[20, 15, 10, 5, 5], 25), 4);

    // ways2 test
    assert_eq!(ways2(&[20, 15, 10, 5, 5], 25, 0), (3, 2));

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
