use std::collections::HashSet;
use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/03.txt";

fn part1(input: &str) -> i32 {
    let mut x = 0;
    let mut y = 0;
    let mut seen: HashSet<(i32, i32)> = HashSet::from([(x, y)]);
    for c in input.chars() {
        if c == '^' {
            y -= 1;
        } else if c == '>' {
            x += 1;
        } else if c == 'v' {
            y += 1;
        } else if c == '<' {
            x -= 1;
        }
        seen.insert((x, y));
    }
    return seen.len() as i32;
}

fn part2(input: &str) -> i32 {
    let mut sx = 0;
    let mut sy = 0;
    let mut rx = 0;
    let mut ry = 0;
    let mut seen: HashSet<(i32, i32)> = HashSet::from([(sx, sy)]);
    for (i, c) in input.chars().enumerate() {
        let x: &mut i32;
        let y: &mut i32;
        if i % 2 == 0 {
            x = &mut sx;
            y = &mut sy;
        } else {
            x = &mut rx;
            y = &mut ry;
        }

        if c == '^' {
            *y -= 1;
        } else if c == '>' {
            *x += 1;
        } else if c == 'v' {
            *y += 1;
        } else if c == '<' {
            *x -= 1;
        }
        seen.insert((*x, *y));
    }
    return seen.len() as i32;
}

fn main() {
    // part 1 tests
    assert_eq!(part1(">"), 2);
    assert_eq!(part1("^>v<"), 4);
    assert_eq!(part1("^v^v^v^v^v"), 2);

    // part 2 tests
    assert_eq!(part2("^v"), 3);
    assert_eq!(part2("^>v<"), 3);
    assert_eq!(part2("^v^v^v^v^v"), 11);

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
