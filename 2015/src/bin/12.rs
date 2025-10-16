use std::fs;
use std::time::Instant;

use regex::Regex;
use serde_json::{from_str, Value};
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/12.txt";

static NUMBERS_RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"(-?\d+)").unwrap());
fn part1(input: &str) -> i32 {
    NUMBERS_RE
        .find_iter(input)
        .map(|m| m.as_str().parse::<i32>().unwrap())
        .sum()
}

fn parse(obj: &Value) -> i32 {
    match obj {
        Value::Null | Value::Bool(_) | Value::String(_) => 0,
        Value::Number(num) => num.as_i64().unwrap().try_into().unwrap(),
        Value::Array(arr) => arr.iter().map(parse).sum(),
        Value::Object(obj) => {
            let mut res = 0;
            for (_key, val) in obj {
                if let Value::String(string) = val {
                    if string == "red" {
                        return 0;
                    }
                }
                res += parse(val);
            }
            res
        }
    }
}

fn part2(input: &str) -> i32 {
    let obj: Value = from_str(input).unwrap();
    parse(&obj)
}

fn main() {
    // part1 tests
    assert_eq!(part1("[1,2,3]"), 6);
    assert_eq!(part1(r#"{"a":2,"b":4}"#), 6);
    assert_eq!(part1("[[[3]]]"), 3);
    assert_eq!(part1(r#"{"a":{"b":4},"c":-1}"#), 3);
    assert_eq!(part1(r#"{"a":[-1,1]}"#), 0);
    assert_eq!(part1(r#"[-1,{"a":1}]"#), 0);
    assert_eq!(part1("[]"), 0);
    assert_eq!(part1("{}"), 0);

    // part2 tests
    assert_eq!(part2("[1,2,3]"), 6);
    assert_eq!(part2(r#"[1,{"c":"red","b":2},3]"#), 4);
    assert_eq!(part2(r#"{"d":"red","e":[1,2,3,4],"f":5}"#), 0);
    assert_eq!(part2(r#"[1,"red",5]"#), 6);

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
