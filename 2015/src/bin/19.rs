use std::fs;
use std::time::Instant;

use regex::Regex;
use std::collections::HashMap;
use std::collections::HashSet;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/19.txt";

static REPLACEMENTS_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^(\w+) => (\w+)$").unwrap());
fn parse(input: &str) -> (HashMap<String, HashSet<String>>, &str) {
    let mut output: HashMap<String, HashSet<String>> = HashMap::new();

    let mut input_iter = input.lines();
    while let Some(line) = input_iter.next() {
        if line.is_empty() {
            return (output, input_iter.next().unwrap());
        }

        let matches = REPLACEMENTS_RE.captures(line).unwrap();
        let from = matches[1].to_string();
        let to = matches[2].to_string();

        let set = output.entry(from).or_default();
        set.insert(to);
    }
    unreachable!("input should end when we reach the target string")
}

fn get_generatable(
    original: &str,
    replacements: &HashMap<String, HashSet<String>>,
) -> HashSet<String> {
    replacements
        .iter()
        .flat_map(|(k, v)| {
            original.match_indices(k).flat_map(move |(i, _)| {
                let (pre, suf_bad) = original.split_at(i);
                let suf = suf_bad.strip_prefix(k).unwrap();
                v.iter()
                    .map(move |replacement| format!("{pre}{replacement}{suf}"))
            })
        })
        .collect()
}

fn part1(input: &str) -> i32 {
    let (replacements, original) = parse(input);
    let generatable = get_generatable(original, &replacements);
    i32::try_from(generatable.len()).unwrap()
}

// This reverses the relationship, replaced -> original
fn parse2(input: &str) -> (HashMap<String, String>, &str) {
    let mut output: HashMap<String, String> = HashMap::new();

    let mut input_iter = input.lines();
    while let Some(line) = input_iter.next() {
        if line.is_empty() {
            return (output, input_iter.next().unwrap());
        }

        let matches = REPLACEMENTS_RE.captures(line).unwrap();
        let from = matches[2].to_string();
        let to = matches[1].to_string();

        assert!(!output.contains_key(&from));
        output.insert(from, to);
    }
    unreachable!("input should end when we reach the target string")
}

fn part2(input: &str) -> u32 {
    let (replacements, target) = parse2(input);
    let mut cur = target.to_string();
    let mut steps = 0;

    while cur != "e" {
        for (from, to) in &replacements {
            if cur.contains(from) {
                cur = cur.replacen(from, to, 1);
                steps += 1;
            }
        }
    }

    steps
}

fn main() {
    // part1 tests
    assert_eq!(
        part1(
            "H => HO
H => OH
O => HH

HOH"
        ),
        4
    );

    assert_eq!(
        part1(
            "H => HO
H => OH
O => HH

HOHOHO"
        ),
        7
    );

    // part2 tests
    //     assert_eq!(
    //         part2(
    //             "e => H
    // e => O
    // H => HO
    // H => OH
    // O => HH
    //
    // HOH"
    //         ),
    //         3
    //     );
    //
    //     assert_eq!(
    //         part2(
    //             "e => H
    // e => O
    // H => HO
    // H => OH
    // O => HH
    //
    // HOHOHO"
    //         ),
    //         6
    //     );

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
