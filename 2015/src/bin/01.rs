use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/01.txt";

fn part1(input: &str) -> i32 {
    return i32::try_from(input.chars().filter(|c| *c == '(').count()).unwrap()
        - i32::try_from(input.chars().filter(|c| *c == ')').count()).unwrap();
}

fn part2(input: &str) -> i32 {
    let mut count = 0;
    for (i, c) in input.chars().enumerate() {
        if c == '(' {
            count += 1;
        } else {
            count -= 1;
        }

        if count < 0 {
            return i32::try_from(i + 1).unwrap();
        }
    }
    unreachable!()
}

fn main() {
    // part 1 tests
    assert_eq!(part1("(())"), 0);
    assert_eq!(part1("()()"), 0);
    assert_eq!(part1("((("), 3);
    assert_eq!(part1("(()(()("), 3);
    assert_eq!(part1("))((((("), 3);
    assert_eq!(part1("())"), -1);
    assert_eq!(part1("))("), -1);
    assert_eq!(part1(")))"), -3);
    assert_eq!(part1(")())())"), -3);

    // part 2 tests
    assert_eq!(part2(")"), 1);
    assert_eq!(part2("()())"), 5);

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
