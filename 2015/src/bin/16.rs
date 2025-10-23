use std::fs;
use std::time::Instant;

use regex::Regex;
use std::collections::HashMap;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/16.txt";

static SUE_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$").unwrap());

static EXPECTED: LazyLock<HashMap<&str, i32>> = LazyLock::new(|| {
    "children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"
        .lines()
        .map(|line| {
            let split = line.split_whitespace().collect::<Vec<&str>>();
            (
                split[0].strip_suffix(':').unwrap(),
                split[1].parse().unwrap(),
            )
        })
        .collect()
});

fn part1(input: &str) -> i32 {
    'sues: for line in input.trim().lines() {
        let matches = SUE_RE.captures(line).unwrap();
        let num: i32 = matches[1].parse().unwrap();
        let gifts = [2, 4, 6].map(|i| {
            (
                matches[i].to_string(),
                matches[i + 1].parse::<i32>().unwrap(),
            )
        });

        for (gift_name, count) in gifts {
            if let Some(expected_count) = EXPECTED.get(&gift_name.as_str()) {
                if *expected_count != count {
                    continue 'sues;
                }
            }
        }
        return num;
    }
    unreachable!("there should always be an answer")
}

fn part2(input: &str) -> i32 {
    'sues: for line in input.trim().lines() {
        let matches = SUE_RE.captures(line).unwrap();
        let num: i32 = matches[1].parse().unwrap();
        let gifts = [2, 4, 6].map(|i| {
            (
                matches[i].to_string(),
                matches[i + 1].parse::<i32>().unwrap(),
            )
        });

        for (gift_name, count) in gifts {
            if let Some(expected_count) = EXPECTED.get(&gift_name.as_str()) {
                match gift_name.as_str() {
                    "cats" | "trees" => {
                        if *expected_count >= count {
                            continue 'sues;
                        }
                    }
                    "pomeranians" | "goldfish" => {
                        if *expected_count <= count {
                            continue 'sues;
                        }
                    }
                    _ => {
                        if *expected_count != count {
                            continue 'sues;
                        }
                    }
                }
            }
        }
        return num;
    }
    unreachable!("there should always be an answer")
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
