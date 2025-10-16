use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/11.txt";

fn is_valid(password: &str) -> bool {
    // cannot contain i, o, l
    if password.contains(['i', 'o', 'l']) {
        return false;
    }

    // contains increasing straight
    if password
        .as_bytes()
        .windows(3)
        .all(|substring| !(substring[0] == substring[1] - 1 && substring[1] == substring[2] - 1))
    {
        return false;
    }

    // password contains 2 different, non-overlapping pairs
    if password
        .as_bytes()
        .windows(2)
        .map(|substring| substring[0] == substring[1])
        .fold((0, false), |(count, prev): (i32, bool), curr| {
            if curr && !prev {
                (count + 1, curr)
            } else {
                (count, curr)
            }
        })
        .0
        < 2
    {
        return false;
    }

    true
}

fn next_password(password: &str) -> String {
    let mut new = password.as_bytes().iter().fold(0, |acc: u64, curr| {
        (acc * 26) + (u64::from(*curr) - 'a' as u64)
    }) + 1;
    let mut ans = String::new();
    while ans.len() < 8 {
        ans.push(u8::try_from((new % 26) + 'a' as u64).unwrap() as char);
        new /= 26;
    }
    ans.chars().rev().collect()
}

fn part1(input: &str) -> String {
    let mut ans = next_password(input.trim());
    while !is_valid(&ans) {
        ans = next_password(&ans);
    }
    ans
}

fn part2(input: &str) -> String {
    part1(input)
}

fn main() {
    // is_valid tests
    assert!(!is_valid("hijklmmn"));
    assert!(!is_valid("abbceffg"));
    assert!(!is_valid("hijklmmn"));
    assert!(!is_valid("abcdefgh"));
    assert!(is_valid("abcdffaa"));
    assert!(!is_valid("ghijklmn"));
    assert!(is_valid("ghjaabcc"));

    // part1 tests
    assert_eq!(part1("abcdefgh"), "abcdffaa");
    assert_eq!(part1("ghijklmn"), "ghjaabcc");

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&ans);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
