use std::fs;
use std::time::Instant;

use itertools::Itertools;
use regex::Regex;
use std::cmp::max;
use std::collections::HashMap;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/13.txt";

static NAMES_RE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).$")
        .unwrap()
});
fn parse(input: &str) -> HashMap<String, HashMap<String, i32>> {
    let mut adj: HashMap<String, HashMap<String, i32>> = HashMap::new();
    input.lines().for_each(|line| {
        let matches = NAMES_RE.captures(line).unwrap();
        let name1 = matches[1].to_string();
        let name2 = matches[4].to_string();
        let num: i32 = matches[3].parse().unwrap();

        adj.entry(name1.clone()).or_insert(HashMap::new());
        adj.entry(name2.clone()).or_insert(HashMap::new());

        match &matches[2] {
            "gain" => {
                adj.get_mut(&name1).unwrap().insert(name2.clone(), num);
            }
            "lose" => {
                adj.get_mut(&name1).unwrap().insert(name2.clone(), -num);
            }
            _ => panic!("fuck"),
        }
    });
    adj
}

fn part1(input: &str) -> i32 {
    let adj = parse(input);
    let mut ans = 0;
    for path in adj.keys().permutations(adj.keys().len()) {
        ans = max(
            ans,
            path.windows(2)
                .map(|window| -> [&String; 2] { window.try_into().unwrap() })
                .fold(0, |acc, [name1, name2]| {
                    acc + adj[name1][name2] + adj[name2][name1]
                })
                + adj[*path.first().unwrap()][*path.last().unwrap()]
                + adj[*path.last().unwrap()][*path.first().unwrap()],
        );
    }

    ans
}

fn part2(input: &str) -> i32 {
    let adj = parse(input);
    let mut ans = 0;
    for path in adj
        .keys()
        .chain([&String::from("me")])
        .permutations(adj.keys().len() + 1)
    {
        ans = max(
            ans,
            path.iter()
                .cloned()
                .chain([&path[0].clone()]) // stupid
                .collect::<Vec<_>>()
                .windows(2)
                .map(|window| -> [&String; 2] { window.try_into().unwrap() })
                .fold(0, |acc, [name1, name2]| {
                    acc + adj.get(name1).and_then(|x| x.get(name2)).unwrap_or(&0)
                        + adj.get(name2).and_then(|x| x.get(name1)).unwrap_or(&0)
                }),
        );
    }

    ans
}

fn main() {
    const TEST_STRING: &str = "Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.";

    // part1 tests
    assert_eq!(part1(TEST_STRING), 330);

    // part2 tests

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
