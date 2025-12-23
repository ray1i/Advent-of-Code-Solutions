use std::fs;
use std::time::Instant;

use std::collections::VecDeque;

const INPUT_FILE: &str = "input/24.txt";

fn get_min_quantum(weights: &[u64], seats: u64) -> u64 {
    let target = weights.iter().sum::<u64>() / seats;

    let mut ways: Vec<Vec<u64>> = Vec::new();
    let mut queue: VecDeque<(u64, usize, Vec<u64>)> = VecDeque::from([(0, 0, Vec::new())]); // sum, idx, seen

    while !queue.is_empty() {
        let (sum, idx, seen) = queue.pop_front().unwrap();

        if sum + weights[idx] == target {
            ways.push([seen.clone(), vec![weights[idx]]].concat());
            continue;
        }

        if idx + 1 >= weights.len() {
            continue;
        }

        // include idx
        if sum + weights[idx] < target {
            queue.push_back((
                sum + weights[idx],
                idx + 1,
                [seen.clone(), vec![weights[idx]]].concat(),
            ));
        }
        // don't include idx
        queue.push_back((sum, idx + 1, seen.clone()));
    }

    let min_length = ways.iter().min_by_key(|&v| v.len()).unwrap().len();
    let possible = ways.iter().filter(|&v| v.len() == min_length);
    possible
        .min_by_key(|&v| v.iter().product::<u64>())
        .unwrap()
        .iter()
        .product()
}

fn part1(input: &str) -> u64 {
    let weights: Vec<u64> = input.lines().map(|line| line.parse().unwrap()).collect();
    get_min_quantum(&weights, 3)
}

fn part2(input: &str) -> u64 {
    let weights: Vec<u64> = input.lines().map(|line| line.parse().unwrap()).collect();
    get_min_quantum(&weights, 4)
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
