use std::fs;
use std::time::Instant;

use itertools::Itertools;
use std::collections::BinaryHeap;

const INPUT_FILE: &str = "input/22.txt";

enum Move {
    MagicMissile,
    Drain,
    Shield,
    Poison,
    Recharge,
}
impl Move {
    fn cost(&self) -> u32 {
        match self {
            Move::MagicMissile => 53,
            Move::Drain => 73,
            Move::Shield => 113,
            Move::Poison => 173,
            Move::Recharge => 229,
        }
    }
}

#[derive(Clone, Ord, PartialOrd, Eq, PartialEq, Debug)]
struct State {
    my_health: u32,
    mana: u32,

    boss_health: u32,
    boss_damage: u32,

    shield_timer: u32,
    poison_timer: u32,
    recharge_timer: u32,
}

impl State {
    fn is_move_possible(&self, the_move: &Move) -> bool {
        if self.mana < the_move.cost() {
            return false;
        }

        match the_move {
            Move::MagicMissile | Move::Drain => true,
            Move::Shield => self.shield_timer == 0,
            Move::Poison => self.poison_timer == 0,
            Move::Recharge => self.recharge_timer == 0,
        }
    }

    fn take_boss_turn(&mut self) {
        self.my_health = self
            .my_health
            .saturating_sub(1.max(self.boss_damage - (if self.shield_timer > 0 { 7 } else { 0 })));
    }

    fn take_effects(&mut self) {
        // on my turn
        if self.poison_timer > 0 {
            self.boss_health = self.boss_health.saturating_sub(3);
            self.poison_timer = self.poison_timer.saturating_sub(1);
        }

        self.shield_timer = self.shield_timer.saturating_sub(1);

        if self.recharge_timer > 0 {
            self.mana += 101;
            self.recharge_timer = self.recharge_timer.saturating_sub(1);
        }
    }

    fn take_move(&mut self, the_move: &Move) {
        match the_move {
            Move::MagicMissile => {
                self.boss_health = self.boss_health.saturating_sub(4);
            }
            Move::Drain => {
                self.boss_health = self.boss_health.saturating_sub(2);
                self.my_health += 2;
            }
            Move::Shield => {
                self.shield_timer = 6;
            }
            Move::Poison => {
                self.poison_timer = 6;
            }
            Move::Recharge => {
                self.recharge_timer = 5;
            }
        }
        self.mana = self.mana.saturating_sub(the_move.cost());
    }
}

// Health, Damage
fn parse_input(input: &str) -> (u32, u32) {
    let lines: Vec<&str> = input.trim().lines().collect();
    assert!(lines.len() == 2);
    lines
        .iter()
        .map(|&line| line.split_whitespace().last().unwrap().parse().unwrap())
        .collect_tuple()
        .unwrap()
}

fn part1(input: &str) -> i32 {
    let (boss_health, boss_damage) = parse_input(input);
    let start_state = State {
        my_health: 50,
        mana: 500,
        boss_health,
        boss_damage,

        shield_timer: 0,
        poison_timer: 0,
        recharge_timer: 0,
    };

    let mut queue: BinaryHeap<(i32, State)> = BinaryHeap::new();
    queue.push((0, start_state));

    while !queue.is_empty() {
        let (curr_cost, curr_state) = queue.pop().unwrap();

        for the_move in [
            Move::MagicMissile,
            Move::Drain,
            Move::Shield,
            Move::Poison,
            Move::Recharge,
        ] {
            let mut new_state = curr_state.clone();
            let spent: i32 = curr_cost - i32::try_from(the_move.cost()).unwrap();

            new_state.take_effects();
            if new_state.boss_health == 0 {
                return -curr_cost;
            }

            if !new_state.is_move_possible(&the_move) {
                continue;
            }

            new_state.take_move(&the_move);
            new_state.take_effects();
            if new_state.boss_health == 0 {
                return -spent;
            }

            new_state.take_boss_turn();
            if new_state.my_health == 0 {
                continue;
            }

            queue.push((spent, new_state));
        }
    }

    unreachable!("we should have a result.")
}

fn part2(input: &str) -> i32 {
    let (boss_health, boss_damage) = parse_input(input);
    let start_state = State {
        my_health: 50 - 1,
        mana: 500,
        boss_health,
        boss_damage,

        shield_timer: 0,
        poison_timer: 0,
        recharge_timer: 0,
    };

    let mut queue: BinaryHeap<(i32, State)> = BinaryHeap::new();
    queue.push((0, start_state));

    while !queue.is_empty() {
        let (curr_cost, curr_state) = queue.pop().unwrap();

        for the_move in [
            Move::MagicMissile,
            Move::Drain,
            Move::Shield,
            Move::Poison,
            Move::Recharge,
        ] {
            let mut new_state = curr_state.clone();
            let spent: i32 = curr_cost - i32::try_from(the_move.cost()).unwrap();

            new_state.take_effects();
            if new_state.boss_health == 0 {
                return -curr_cost;
            }

            if !new_state.is_move_possible(&the_move) {
                continue;
            }

            new_state.take_move(&the_move);
            new_state.take_effects();
            if new_state.boss_health == 0 {
                return -spent;
            }

            new_state.take_boss_turn();
            if new_state.my_health == 0 {
                continue;
            }

            // HARD MODE!
            new_state.my_health = new_state.my_health.saturating_sub(1);
            if new_state.my_health == 0 {
                continue;
            }
            //

            queue.push((spent, new_state));
        }
    }

    unreachable!("we should have a result.")
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
