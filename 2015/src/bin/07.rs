use std::fs;
use std::time::Instant;

use regex::Regex;
use std::collections::HashMap;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/07.txt";

#[derive(Debug, Clone)]
enum Definition {
    NumValue(u16),
    RefValue(String),
    Not(String),
    And(String, String),
    Or(String, String),
    Lshift(String, i32),
    Rshift(String, i32),
}

static NUM_VALUE_RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^(\d+) -> (\w+)$").unwrap());
static REF_VALUE_RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^(\w+) -> (\w+)$").unwrap());
static NOT_RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^NOT (\w+) -> (\w+)$").unwrap());
static AND_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^(\w+) AND (\w+) -> (\w+)$").unwrap());
static OR_RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"^(\w+) OR (\w+) -> (\w+)$").unwrap());
static LSHIFT_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^(\w+) LSHIFT (\w+) -> (\w+)$").unwrap());
static RSHIFT_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^(\w+) RSHIFT (\w+) -> (\w+)$").unwrap());

impl Definition {
    fn from(line: &str) -> Definition {
        if NUM_VALUE_RE.is_match(line) {
            Definition::NumValue(
                NUM_VALUE_RE
                    .captures(line)
                    .and_then(|caps| caps.get(1))
                    .and_then(|m| m.as_str().parse().ok())
                    .expect("failed to get value"),
            )
        } else if REF_VALUE_RE.is_match(line) {
            Definition::RefValue(
                REF_VALUE_RE
                    .captures(line)
                    .and_then(|caps| caps.get(1))
                    .map(|m| m.as_str().to_string())
                    .expect("failed to get value"),
            )
        } else if NOT_RE.is_match(line) {
            Definition::Not(
                NOT_RE
                    .captures(line)
                    .and_then(|caps| caps.get(1))
                    .map(|m| m.as_str().to_string())
                    .expect("failed to get not"),
            )
        } else if AND_RE.is_match(line) {
            let caps = AND_RE.captures(line).unwrap();
            let a = caps.get(1).unwrap().as_str().to_string();
            let b = caps.get(2).unwrap().as_str().to_string();
            Definition::And(a, b)
        } else if OR_RE.is_match(line) {
            let caps = OR_RE.captures(line).unwrap();
            let a = caps.get(1).unwrap().as_str().to_string();
            let b = caps.get(2).unwrap().as_str().to_string();
            Definition::Or(a, b)
        } else if LSHIFT_RE.is_match(line) {
            let caps = LSHIFT_RE.captures(line).unwrap();
            let a = caps.get(1).unwrap().as_str().to_string();
            let b: i32 = caps.get(2).unwrap().as_str().parse().expect("not number");
            Definition::Lshift(a, b)
        } else if RSHIFT_RE.is_match(line) {
            let caps = RSHIFT_RE.captures(line).unwrap();
            let a = caps.get(1).unwrap().as_str().to_string();
            let b: i32 = caps.get(2).unwrap().as_str().parse().expect("not number");
            Definition::Rshift(a, b)
        } else {
            panic!("invalid input {line}")
        }
    }
}

fn parse_input(input: &str) -> HashMap<String, Definition> {
    input
        .lines()
        .map(|line| {
            let key = line
                .split_whitespace()
                .last()
                .expect("empty string")
                .to_string();
            (key, Definition::from(line))
        })
        .collect()
}

fn get_or_update_value(definitions: &mut HashMap<String, Definition>, key: &String) -> u16 {
    if key.parse::<u16>().is_ok() {
        return key.parse::<u16>().unwrap();
    }

    if let Definition::NumValue(num) = definitions.get(key).unwrap() {
        return *num;
    }

    let definition = definitions.get(key).cloned().unwrap();

    let res = match definition {
        Definition::RefValue(var) => get_or_update_value(definitions, &var),
        Definition::Not(var) => !get_or_update_value(definitions, &var),
        Definition::And(var1, var2) => {
            get_or_update_value(definitions, &var1) & get_or_update_value(definitions, &var2)
        }
        Definition::Or(var1, var2) => {
            get_or_update_value(definitions, &var1) | get_or_update_value(definitions, &var2)
        }
        Definition::Lshift(var, num) => get_or_update_value(definitions, &var) << num,
        Definition::Rshift(var, num) => get_or_update_value(definitions, &var) >> num,
        Definition::NumValue(num) => num, // should never hit this
    };

    definitions.insert(key.to_string(), Definition::NumValue(res));
    res
}

fn part1(input: &str) -> u16 {
    let mut definitions = parse_input(input);
    get_or_update_value(&mut definitions, &String::from("a"))
}

fn part2(input: &str, part1_value: u16) -> u16 {
    let mut definitions = parse_input(input);
    definitions.insert(String::from("b"), Definition::NumValue(part1_value));
    get_or_update_value(&mut definitions, &String::from("a"))
}

fn main() {
    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input, ans);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
