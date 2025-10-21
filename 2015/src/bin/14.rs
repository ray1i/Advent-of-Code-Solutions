use std::fs;
use std::time::Instant;

use itertools::Itertools;
use regex::Regex;
use std::collections::HashMap;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/14.txt";

static NAMES_RE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(
        r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$",
    )
    .unwrap()
});

struct ReindeerDetails {
    speed: i32,
    endurance: i32,
    rest: i32,
}
impl ReindeerDetails {
    fn distance_after(&self, seconds: i32) -> i32 {
        let d = self.endurance + self.rest;
        let whole = seconds / d;
        let remainder = seconds % d;
        whole * self.speed * self.endurance + self.endurance.min(remainder) * self.speed
    }
}

fn parse(input: &str) -> (String, ReindeerDetails) {
    let matches = NAMES_RE.captures(input).unwrap();
    let name = matches[1].to_string();
    let speed: i32 = matches[2].parse().unwrap();
    let endurance: i32 = matches[3].parse().unwrap();
    let rest: i32 = matches[4].parse().unwrap();
    (
        name,
        ReindeerDetails {
            speed,
            endurance,
            rest,
        },
    )
}

fn part1(input: &str) -> i32 {
    input
        .lines()
        .map(|line| parse(line.trim()).1.distance_after(2503))
        .max()
        .unwrap()
}

fn part2(input: &str, seconds: i32) -> i32 {
    let reindeer: HashMap<String, ReindeerDetails> =
        input.lines().map(|line| parse(line.trim())).collect();
    let mut points: HashMap<String, i32> = reindeer.keys().map(|name| (name.clone(), 0)).collect();
    for i in 1..=seconds {
        let winners = reindeer
            .iter()
            .map(|(name, deer)| (name, deer.distance_after(i)))
            .max_set_by_key(|(_name, distance)| *distance);
        winners
            .iter()
            .copied()
            .for_each(|(name, _distance)| *points.get_mut(name).unwrap() += 1);
    }
    *points.values().max().unwrap()
}

fn main() {
    // part1 tests
    assert_eq!(
        parse("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
            .1
            .distance_after(1000),
        1120
    );
    assert_eq!(
        parse("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")
            .1
            .distance_after(1000),
        1056
    );

    // part2 tests
    assert_eq!(
        part2(
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
            1000
        ),
        689
    );

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input, 2503);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
