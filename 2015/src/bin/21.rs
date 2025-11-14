use std::fs;
use std::time::Instant;

use itertools::Itertools;

const INPUT_FILE: &str = "input/21.txt";

struct Equipment(u32, u32, u32);

const WEAPONS: [Equipment; 5] = [
    Equipment(8, 4, 0),
    Equipment(10, 5, 0),
    Equipment(25, 6, 0),
    Equipment(40, 7, 0),
    Equipment(74, 8, 0),
];

const ARMOUR: [Equipment; 6] = [
    Equipment(13, 0, 1),
    Equipment(31, 0, 2),
    Equipment(53, 0, 3),
    Equipment(75, 0, 4),
    Equipment(102, 0, 5),
    Equipment(0, 0, 0), // no armour
];

const RINGS: [Equipment; 8] = [
    Equipment(20, 0, 1),
    Equipment(25, 1, 0),
    Equipment(40, 0, 2),
    Equipment(50, 2, 0),
    Equipment(80, 0, 3),
    Equipment(100, 3, 0),
    Equipment(0, 0, 0), // no ring
    Equipment(0, 0, 0), // no ring
];

// Health, Damage, Armour
fn parse_input(input: &str) -> (u32, u32, u32) {
    let lines: Vec<&str> = input.trim().lines().collect();
    assert!(lines.len() == 3);
    lines
        .iter()
        .map(|&line| line.split_whitespace().last().unwrap().parse().unwrap())
        .collect_tuple()
        .unwrap()
}

const MY_HEALTH: u32 = 100;

fn i_win(
    boss_health: u32,
    boss_damage: u32,
    boss_armour: u32,
    weapon: &Equipment,
    armour: &Equipment,
    ring1: &Equipment,
    ring2: &Equipment,
) -> bool {
    let my_damage = weapon.1 + armour.1 + ring1.1 + ring2.1;
    let my_armour = weapon.2 + armour.2 + ring1.2 + ring2.2;
    let boss_dps = (boss_damage.saturating_sub(my_armour)).max(1);
    let my_dps = (my_damage.saturating_sub(boss_armour)).max(1);

    boss_health / my_dps <= MY_HEALTH / boss_dps
}

fn part1(input: &str) -> u32 {
    let (boss_health, boss_damage, boss_armour) = parse_input(input);

    let mut ans = u32::MAX;

    for weapon in WEAPONS {
        for armour in ARMOUR {
            for (ring1, ring2) in RINGS.iter().tuple_combinations() {
                let cost = weapon.0 + armour.0 + ring1.0 + ring2.0;

                if i_win(
                    boss_health,
                    boss_damage,
                    boss_armour,
                    &weapon,
                    &armour,
                    ring1,
                    ring2,
                ) {
                    ans = ans.min(cost);
                }
            }
        }
    }

    ans
}

fn part2(input: &str) -> u32 {
    let (boss_health, boss_damage, boss_armour) = parse_input(input);

    let mut ans = 0;

    for weapon in WEAPONS {
        for armour in ARMOUR {
            for (ring1, ring2) in RINGS.iter().tuple_combinations() {
                let cost = weapon.0 + armour.0 + ring1.0 + ring2.0;

                if !i_win(
                    boss_health,
                    boss_damage,
                    boss_armour,
                    &weapon,
                    &armour,
                    ring1,
                    ring2,
                ) {
                    ans = ans.max(cost);
                }
            }
        }
    }

    ans
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
