use std::fs;
use std::time::Instant;

use regex::Regex;
use regex::Replacer;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/08.txt";

static DECODE_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r#"(\\\\)|(\\")|(\\x((?:\d|[a-f]){2}))"#).unwrap());

struct EscapeReplacer;
impl Replacer for EscapeReplacer {
    fn replace_append(&mut self, caps: &regex::Captures<'_>, dst: &mut String) {
        if let Some(_) = caps.get(1) {
            dst.push_str("\\");
        } else if let Some(_) = caps.get(2) {
            dst.push_str("\"");
        } else if let Some(_hex_match) = caps.get(3) {
            let _hex = caps.get(4).unwrap().as_str();
            dst.push_str("a"); // placeholder for now
        }
    }
}

fn decode_input(input: &str) -> Vec<String> {
    input
        .lines()
        .map(|line| DECODE_RE.replace_all(line, EscapeReplacer).to_string())
        .collect()
}

fn part1(input: &str) -> i32 {
    let code_len = input.lines().map(|line| line.len() as i32).sum::<i32>();

    let decoded = decode_input(input);
    let string_len = decoded
        .iter()
        .map(|line| line.len() as i32 - 2)
        .sum::<i32>();

    // println!("code: {code_len}, string: {string_len}");
    code_len - string_len
}

// -=-=- //

static ENCODE_RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r#"(\\)|(")"#).unwrap());

struct SpecialReplacer;
impl Replacer for SpecialReplacer {
    fn replace_append(&mut self, _caps: &regex::Captures<'_>, dst: &mut String) {
        dst.push_str("##"); // this is good for now i think?
    }
}

fn encode_input(input: &str) -> Vec<String> {
    input
        .lines()
        .map(|line| ENCODE_RE.replace_all(line, SpecialReplacer).to_string())
        .collect()
}

fn part2(input: &str) -> i32 {
    let encoded = encode_input(input);
    let encoded_len = encoded
        .iter()
        .map(|line| line.len() as i32 + 2)
        .sum::<i32>();

    let code_len = input.lines().map(|line| line.len() as i32).sum::<i32>();

    // println!("encoded: {encoded_len}, code: {code_len}");
    encoded_len - code_len
}

fn main() {
    // part 1 tests
    assert_eq!(
        part1(
            "\"\"
\"abc\"
\"aaa\\\"aaa\"
\"\\x27\""
        ),
        12
    );

    // part 2 tests
    assert_eq!(
        part2(
            "\"\"
\"abc\"
\"aaa\\\"aaa\"
\"\\x27\""
        ),
        19
    );

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
