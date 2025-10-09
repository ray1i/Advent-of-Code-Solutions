use std::fs;
use std::time::Instant;

use regex::Regex;
use std::fmt;

const INPUT_FILE: &str = "input/06.txt";

enum Action {
    On,
    Off,
    Toggle,
}

struct Instruction {
    action: Action,
    start: (usize, usize),
    end: (usize, usize),
}

impl fmt::Display for Instruction {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{} from ({}, {}) to ({}, {})",
            match self.action {
                Action::On => "turn on",
                Action::Off => "turn off",
                Action::Toggle => "toggle",
            },
            self.start.0,
            self.start.1,
            self.end.0,
            self.end.1
        )
    }
}

fn parse_input(input: &str) -> Vec<Instruction> {
    let re: Regex = Regex::new(r"\d+").unwrap();
    input
        .lines()
        .map(|line| {
            let nums = re
                .find_iter(line)
                .map(|n| n.as_str().parse::<usize>().expect("thats not a number..."))
                .collect::<Vec<usize>>();

            let action: Action = match &line[..7] {
                "turn on" => Action::On,
                "turn of" => Action::Off,
                "toggle " => Action::Toggle,
                _ => panic!("how is this possible"),
            };

            Instruction {
                action,
                start: (nums[0], nums[1]),
                end: (nums[2], nums[3]),
            }
        })
        .collect()
}

fn part1(input: &str) -> i32 {
    let instructions = parse_input(input);
    let mut grid = vec![[false; 1000]; 1000].into_boxed_slice();
    let mut count = 0;
    for inst in &instructions {
        for row in grid.iter_mut().take(inst.end.1 + 1).skip(inst.start.1) {
            for cell in row.iter_mut().take(inst.end.0 + 1).skip(inst.start.0) {
                match inst.action {
                    Action::Off => {
                        if *cell {
                            count -= 1;
                        }
                        *cell = false;
                    }
                    Action::On => {
                        if !*cell {
                            count += 1;
                        }
                        *cell = true;
                    }
                    Action::Toggle => {
                        if *cell {
                            count -= 1;
                        } else {
                            count += 1;
                        }
                        *cell = !*cell;
                    }
                }
            }
        }
    }
    count
}

fn part2(input: &str) -> i32 {
    let instructions = parse_input(input);
    let mut grid = vec![[0; 1000]; 1000].into_boxed_slice();
    let mut count = 0;

    for inst in &instructions {
        for row in grid.iter_mut().take(inst.end.1 + 1).skip(inst.start.1) {
            for cell in row.iter_mut().take(inst.end.0 + 1).skip(inst.start.0) {
                match inst.action {
                    Action::Off => {
                        if *cell > 0 {
                            count -= 1;
                            *cell -= 1;
                        }
                    }
                    Action::On => {
                        count += 1;
                        *cell += 1;
                    }
                    Action::Toggle => {
                        count += 2;
                        *cell += 2;
                    }
                }
            }
        }
    }
    count
}

fn main() {
    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time_1 = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time_1.elapsed());

    let start_time_2 = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time_2.elapsed());
}
