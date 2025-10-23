use std::fs;
use std::time::Instant;

use itertools::repeat_n;
use itertools::Itertools;
use regex::Regex;
use std::sync::LazyLock;

const INPUT_FILE: &str = "input/15.txt";

static INGREDIENT_RE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(
        r"^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$",
    )
    .unwrap()
});

#[derive(Debug)]
struct Ingredient {
    capacity: i32,
    durability: i32,
    flavor: i32,
    texture: i32,
    calories: i32,
}

fn parse(input: &str) -> (String, Ingredient) {
    let matches = INGREDIENT_RE.captures(input).unwrap();
    let name = matches[1].to_string();
    let capacity: i32 = matches[2].parse().unwrap();
    let durability: i32 = matches[3].parse().unwrap();
    let flavor: i32 = matches[4].parse().unwrap();
    let texture: i32 = matches[5].parse().unwrap();
    let calories: i32 = matches[6].parse().unwrap();
    (
        name,
        Ingredient {
            capacity,
            durability,
            flavor,
            texture,
            calories,
        },
    )
}

fn total_score(ingredients: &[Ingredient], counts: &[u8]) -> Option<i32> {
    assert_eq!(
        ingredients.len(),
        counts.len(),
        "total_score has invalid argument lengths: ingredients: {}, counts: {}",
        ingredients.len(),
        counts.len()
    );

    if counts
        .iter()
        .fold(0u8, |acc, curr| acc.saturating_add(*curr))
        != 100
    {
        return None;
    }

    let total = ingredients.iter().zip(counts.iter().copied()).fold(
        Ingredient {
            capacity: 0,
            durability: 0,
            flavor: 0,
            texture: 0,
            calories: 0,
        },
        |acc, (ing, count)| Ingredient {
            capacity: acc.capacity + ing.capacity * i32::from(count),
            durability: acc.durability + ing.durability * i32::from(count),
            flavor: acc.flavor + ing.flavor * i32::from(count),
            texture: acc.texture + ing.texture * i32::from(count),
            calories: acc.calories + ing.calories * i32::from(count),
        },
    );

    if total.capacity <= 0 || total.durability <= 0 || total.flavor <= 0 || total.texture <= 0 {
        return Some(0);
    }

    Some(total.capacity * total.durability * total.flavor * total.texture)
}

fn part1(input: &str) -> i32 {
    let ingredients = input
        .trim()
        .lines()
        .map(|line| parse(line).1)
        .collect::<Vec<_>>();

    let mut ans = 0;
    for counts in repeat_n(0..=100, ingredients.len()).multi_cartesian_product() {
        let total = total_score(&ingredients, &counts);
        if let Some(t) = total {
            ans = ans.max(t);
        }
    }

    ans
}

fn total_score2(ingredients: &[Ingredient], counts: &[u8]) -> Option<i32> {
    assert_eq!(
        ingredients.len(),
        counts.len(),
        "total_score has invalid argument lengths: ingredients: {}, counts: {}",
        ingredients.len(),
        counts.len()
    );

    if counts
        .iter()
        .fold(0u8, |acc, curr| acc.saturating_add(*curr))
        != 100
    {
        return None;
    }

    let total = ingredients.iter().zip(counts.iter().copied()).fold(
        Ingredient {
            capacity: 0,
            durability: 0,
            flavor: 0,
            texture: 0,
            calories: 0,
        },
        |acc, (ing, count)| Ingredient {
            capacity: acc.capacity + ing.capacity * i32::from(count),
            durability: acc.durability + ing.durability * i32::from(count),
            flavor: acc.flavor + ing.flavor * i32::from(count),
            texture: acc.texture + ing.texture * i32::from(count),
            calories: acc.calories + ing.calories * i32::from(count),
        },
    );

    if total.capacity <= 0
        || total.durability <= 0
        || total.flavor <= 0
        || total.texture <= 0
        || total.calories != 500
    {
        return Some(0);
    }

    Some(total.capacity * total.durability * total.flavor * total.texture)
}

fn part2(input: &str) -> i32 {
    let ingredients = input
        .trim()
        .lines()
        .map(|line| parse(line).1)
        .collect::<Vec<_>>();

    let mut ans = 0;
    for counts in repeat_n(0..=100, ingredients.len()).multi_cartesian_product() {
        let total = total_score2(&ingredients, &counts);
        if let Some(t) = total {
            ans = ans.max(t);
        }
    }

    ans
}

fn main() {
    // part1 tests
    assert_eq!(
        part1(
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
        ),
        62_842_880
    );
    // part2 tests
    assert_eq!(
        part2(
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
        ),
        57_600_000
    );

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
