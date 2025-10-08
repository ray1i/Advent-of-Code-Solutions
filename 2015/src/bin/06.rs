use std::fs;
use std::time::Instant;

use regex::Regex;
use std::fmt;

const INPUT_FILE: &str = "input/06.txt";

enum Action {
    ON,
    OFF,
    TOGGLE,
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
                Action::ON => "turn on",
                Action::OFF => "turn off",
                Action::TOGGLE => "toggle",
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
    Vec::from_iter(input.lines().map(|line| {
        let nums = re
            .find_iter(line)
            .map(|n| n.as_str().parse::<usize>().expect("thats not a number..."))
            .collect::<Vec<usize>>();

        let action: Action = match &line[..7] {
            "turn on" => Action::ON,
            "turn of" => Action::OFF,
            "toggle " => Action::TOGGLE,
            _ => Action::ON, // whatever
        };

        Instruction {
            action,
            start: (nums[0], nums[1]),
            end: (nums[2], nums[3]),
        }
    }))
}

fn part1(input: &str) -> i32 {
    let instructions = parse_input(input);
    let mut grid = [[false; 1000]; 1000];
    let mut count = 0;
    for inst in instructions.iter() {
        for x in inst.start.0..=inst.end.0 {
            for y in inst.start.1..=inst.end.1 {
                match inst.action {
                    Action::OFF => {
                        if grid[y][x] {
                            count -= 1
                        }
                        grid[y][x] = false
                    }
                    Action::ON => {
                        if !grid[y][x] {
                            count += 1
                        }
                        grid[y][x] = true
                    }
                    Action::TOGGLE => {
                        if grid[y][x] {
                            count -= 1
                        } else {
                            count += 1
                        }
                        grid[y][x] = !grid[y][x]
                    }
                }
            }
        }
    }
    count
}

fn part2(input: &str) -> i32 {
    let instructions = parse_input(input);
    let mut grid = [[0; 1000]; 1000];
    let mut count = 0;

    for inst in instructions.iter() {
        for x in inst.start.0..=inst.end.0 {
            for y in inst.start.1..=inst.end.1 {
                match inst.action {
                    Action::OFF => {
                        if grid[y][x] > 0 {
                            count -= 1;
                            grid[y][x] -= 1;
                        }
                    }
                    Action::ON => {
                        count += 1;
                        grid[y][x] += 1;
                    }
                    Action::TOGGLE => {
                        count += 2;
                        grid[y][x] += 2;
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
