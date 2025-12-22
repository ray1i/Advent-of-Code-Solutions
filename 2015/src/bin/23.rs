use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/23.txt";

enum Register {
    A,
    B,
}

enum Instruction {
    Hlf(Register),
    Tpl(Register),
    Inc(Register),
    Jmp(i32),
    Jie(Register, i32),
    Jio(Register, i32),
}

fn parse_input(input: &str) -> Vec<Instruction> {
    input
        .lines()
        .map(|line| {
            let split: Vec<&str> = line.split(' ').collect();
            assert!(split.len() > 1);
            match split[0] {
                "hlf" => match split[1] {
                    "a" => Instruction::Hlf(Register::A),
                    "b" => Instruction::Hlf(Register::B),
                    _ => panic!("bad hlf"),
                },
                "tpl" => match split[1] {
                    "a" => Instruction::Tpl(Register::A),
                    "b" => Instruction::Tpl(Register::B),
                    _ => panic!("bad tpl"),
                },
                "inc" => match split[1] {
                    "a" => Instruction::Inc(Register::A),
                    "b" => Instruction::Inc(Register::B),
                    _ => panic!("bad inc"),
                },
                "jmp" => {
                    let offset: i32 = split[1].parse().unwrap();
                    Instruction::Jmp(offset)
                }
                "jie" => {
                    let offset: i32 = split[2].parse().unwrap();
                    let register = split[1].trim_end_matches(',');
                    match register {
                        "a" => Instruction::Jie(Register::A, offset),
                        "b" => Instruction::Jie(Register::B, offset),
                        _ => panic!("bad jie"),
                    }
                }
                "jio" => {
                    let offset: i32 = split[2].parse().unwrap();
                    let register = split[1].trim_end_matches(',');
                    match register {
                        "a" => Instruction::Jio(Register::A, offset),
                        "b" => Instruction::Jio(Register::B, offset),
                        _ => panic!("bad jio"),
                    }
                }
                _ => panic!("bad"),
            }
        })
        .collect()
}

fn get_b(instructions: &[Instruction], a_init: u32, b_init: u32) -> u32 {
    let mut ip: usize = 1;
    let mut a: u32 = a_init;
    let mut b: u32 = b_init;

    while 0 < ip && ip <= instructions.len() {
        match &instructions[ip - 1] {
            Instruction::Hlf(reg) => {
                match reg {
                    Register::A => a /= 2,
                    Register::B => b /= 2,
                }
                ip += 1;
            }
            Instruction::Tpl(reg) => {
                match reg {
                    Register::A => a *= 3,
                    Register::B => b *= 3,
                }
                ip += 1;
            }
            Instruction::Inc(reg) => {
                match reg {
                    Register::A => a += 1,
                    Register::B => b += 1,
                }
                ip += 1;
            }
            Instruction::Jmp(offset) => {
                ip = ip.saturating_add_signed((*offset).try_into().unwrap());
            }
            Instruction::Jie(reg, offset) => match reg {
                Register::A => {
                    if a.is_multiple_of(2) {
                        ip = ip.saturating_add_signed((*offset).try_into().unwrap());
                    } else {
                        ip += 1;
                    }
                }
                Register::B => {
                    if b.is_multiple_of(2) {
                        ip = ip.saturating_add_signed((*offset).try_into().unwrap());
                    } else {
                        ip += 1;
                    }
                }
            },
            Instruction::Jio(reg, offset) => match reg {
                Register::A => {
                    if a == 1 {
                        ip = ip.saturating_add_signed((*offset).try_into().unwrap());
                    } else {
                        ip += 1;
                    }
                }
                Register::B => {
                    if b == 1 {
                        ip = ip.saturating_add_signed((*offset).try_into().unwrap());
                    } else {
                        ip += 1;
                    }
                }
            },
        }
    }

    b
}

fn part1(input: &str) -> u32 {
    get_b(&parse_input(input), 0, 0)
}

fn part2(input: &str) -> u32 {
    get_b(&parse_input(input), 1, 0)
}

fn main() {
    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
