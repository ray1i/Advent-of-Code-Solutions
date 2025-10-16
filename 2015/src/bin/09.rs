use std::fs;
use std::time::Instant;

use fera::unionfind::UnionFind;
use itertools::Itertools;
use std::cmp::max;
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;

const INPUT_FILE: &str = "input/09.txt";

fn part1(input: &str) -> i32 {
    let mut dists: BinaryHeap<(i32, &str, &str)> = BinaryHeap::new();
    let mut locations: HashSet<&str> = HashSet::new();
    for line in input.lines() {
        let split = line.split_whitespace().collect::<Vec<&str>>();
        let location1 = split[0];
        let location2 = split[2];
        dists.push((-split[4].parse::<i32>().unwrap(), location1, location2));
        locations.insert(location1);
        locations.insert(location2);
    }

    let total_locations = i32::try_from(locations.len()).unwrap();
    let mut degrees: HashMap<&str, i32> = locations.iter().map(|location| (*location, 0)).collect();

    let mut union_find: UnionFind<&str> = UnionFind::new();
    locations
        .iter()
        .for_each(|location| union_find.make_set(location));
    let mut curr_locations = 0;
    let mut ans = 0;
    while curr_locations < total_locations - 2 {
        let (dist, location1, location2) = dists.pop().expect("ran out of edges");

        if degrees[&location1] >= 2
            || degrees[&location2] >= 2
            || union_find.in_same_set(location1, location2)
        {
            continue;
        }
        *degrees.get_mut(&location1).unwrap() += 1;
        *degrees.get_mut(&location2).unwrap() += 1;
        ans += -dist;
        union_find.union(location1, location2);

        if degrees[&location1] >= 2 {
            curr_locations += 1;
        }
        if degrees[&location2] >= 2 {
            curr_locations += 1;
        }
    }

    ans
}

fn part2(input: &str) -> i32 {
    let mut dists: HashMap<(&str, &str), i32> = HashMap::new();
    let mut locations: HashSet<&str> = HashSet::new();
    for line in input.lines() {
        let split = line.split_whitespace().collect::<Vec<&str>>();
        let location1 = split[0];
        let location2 = split[2];
        dists.insert((location1, location2), split[4].parse::<i32>().unwrap());
        dists.insert((location2, location1), split[4].parse::<i32>().unwrap());
        locations.insert(location1);
        locations.insert(location2);
    }

    let mut ans = 0;
    for path in locations.iter().copied().permutations(locations.len()) {
        ans = max(
            ans,
            path.windows(2)
                .map(|window| -> [&str; 2] { window.try_into().unwrap() })
                .fold(0, |acc, [location1, location2]| {
                    acc + dists[&(location1, location2)]
                }),
        );
    }
    ans
}

fn main() {
    // part1 tests
    assert_eq!(
        part1(
            "London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"
        ),
        605
    );

    // part2 tests
    assert_eq!(
        part2(
            "London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"
        ),
        982
    );

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
