use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/02.txt";

fn part1(input: &str) -> i32 {
    let mut ans = 0;
    for line in input.lines() {
        let [a, b, c]: [i32; 3] = line
            .split("x")
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>()
            .try_into()
            .expect("bad input");
        ans += (2 * a * b)
            + (2 * b * c)
            + (2 * c * a)
            + vec![a * b, b * c, c * a].iter().min().unwrap();
    }
    return ans;
}

fn part2(input: &str) -> i32 {
    let mut ans = 0;
    for line in input.lines() {
        let [a, b, c]: [i32; 3] = line
            .split("x")
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>()
            .try_into()
            .expect("bad input");
        ans += (a * b * c) + 2 * vec![a + b, b + c, c + a].iter().min().unwrap();
    }
    return ans;
}

fn main() {
    // part 1 tests
    assert_eq!(part1("2x3x4"), 58);
    assert_eq!(part1("1x1x10"), 43);

    // part 2 tests
    assert_eq!(part2("2x3x4"), 34);
    assert_eq!(part2("1x1x10"), 14);

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
