use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/10.txt";

fn convert(input: &str) -> String {
    let mut res = String::new();
    let mut prev_num: Option<u32> = None;
    let mut prev_count = 0;
    for c in input.chars() {
        let num: u32 = c.to_digit(10).unwrap();
        if let Some(prev) = prev_num {
            if num == prev {
                prev_count += 1;
            } else {
                res.push_str(&prev_count.to_string());
                res.push_str(&prev.to_string());
                prev_num = Some(num);
                prev_count = 1;
            }
        } else {
            prev_num = Some(num);
            prev_count = 1;
        }
    }

    if let Some(prev) = prev_num {
        res.push_str(&prev_count.to_string());
        res.push_str(&prev.to_string());
    }
    res
}

fn part1(input: &str) -> i32 {
    let mut ans = input.trim().to_string();
    for _ in 0..40 {
        ans = convert(&ans);
    }
    ans.len().try_into().unwrap()
}

fn part2(input: &str) -> i32 {
    let mut ans = input.trim().to_string();
    for _ in 0..50 {
        ans = convert(&ans);
    }
    ans.len().try_into().unwrap()
}

fn main() {
    // convert tests
    assert_eq!(convert("1"), "11");
    assert_eq!(convert("11"), "21");
    assert_eq!(convert("21"), "1211");
    assert_eq!(convert("1211"), "111221");
    assert_eq!(convert("111221"), "312211");

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
