use std::fs;
use std::time::Instant;

const INPUT_FILE: &str = "input/18.txt";

fn parse(input: &str) -> Vec<Vec<bool>> {
    input
        .trim()
        .lines()
        .map(|line| {
            line.trim()
                .chars()
                .map(|c| match c {
                    '.' => false,
                    '#' => true,
                    _ => panic!("invalid"),
                })
                .collect()
        })
        .collect()
}

fn next(grid: &Vec<Vec<bool>>, keep_corners: bool) -> Vec<Vec<bool>> {
    let mut res = grid.to_owned();

    for y in 0..grid.len() {
        for x in 0..grid[y].len() {
            if keep_corners
                && ((0, 0) == (x, y)
                    || (0, grid.len() - 1) == (x, y)
                    || (grid[y].len() - 1, 0) == (x, y)
                    || (grid[y].len() - 1, grid.len() - 1) == (x, y))
            {
                continue;
            }

            let adj_on: i32 = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
            .iter()
            .map(|&(dx, dy)| {
                if let (Some(nx), Some(ny)) = (x.checked_add_signed(dx), y.checked_add_signed(dy)) {
                    match grid.get(ny).and_then(|row| row.get(nx)) {
                        Some(light) => i32::from(*light),
                        None => 0,
                    }
                } else {
                    0
                }
            })
            .sum();

            if grid[y][x] && !(adj_on == 2 || adj_on == 3) {
                res[y][x] = false;
            } else if !grid[y][x] && adj_on == 3 {
                res[y][x] = true;
            }
        }
    }

    res
}

fn part1(input: &str) -> i32 {
    let init_grid = parse(input);
    let final_grid = (0..100).fold(init_grid, |curr_grid, _| next(&curr_grid, false));
    final_grid
        .into_iter()
        .map(|row| row.into_iter().map(i32::from).sum::<i32>())
        .sum()
}

fn part2(input: &str) -> i32 {
    let mut init_grid = parse(input);
    *init_grid.first_mut().unwrap().first_mut().unwrap() = true;
    *init_grid.first_mut().unwrap().last_mut().unwrap() = true;
    *init_grid.last_mut().unwrap().first_mut().unwrap() = true;
    *init_grid.last_mut().unwrap().last_mut().unwrap() = true;

    let final_grid = (0..100).fold(init_grid, |curr_grid, _| next(&curr_grid, true));
    final_grid
        .into_iter()
        .map(|row| row.into_iter().map(i32::from).sum::<i32>())
        .sum()
}

fn main() {
    // next tests
    for _ in 0..4 {
        let init = parse(
            ".#.#.#
...##.
#....#
..#...
#.#..#
####..",
        );
        let expected = [
            "..##..
..##.#
...##.
......
#.....
#.##..",
            "..###.
......
..###.
......
.#....
.#....",
            "...#..
......
...#..
..##..
......
......",
            "......
......
..##..
..##..
......
......",
        ]
        .map(parse);

        let mut curr = init;
        for expected_grid in expected {
            let next_grid = next(&curr, false);
            assert_eq!(next_grid, expected_grid);
            curr = next_grid;
        }
    }

    for _ in 0..4 {
        let init = parse(
            "##.#.#
...##.
#....#
..#...
#.#..#
####.#",
        );
        let expected = [
            "#.##.#
####.#
...##.
......
#...#.
#.####",
            "#..#.#
#....#
.#.##.
...##.
.#..##
##.###",
            "#...##
####.#
..##.#
......
##....
####.#",
            "#.####
#....#
...#..
.##...
#.....
#.#..#",
            "##.###
.##..#
.##...
.##...
#.#...
##...#",
        ]
        .map(parse);

        let mut curr = init;
        for expected_grid in expected {
            let next_grid = next(&curr, true);
            assert_eq!(next_grid, expected_grid);
            curr = next_grid;
        }
    }

    let input = fs::read_to_string(INPUT_FILE).expect("couldn't read file");

    let start_time = Instant::now();
    let ans = part1(&input);
    println!("part 1: {} (took {:.5?})", ans, start_time.elapsed());

    let start_time = Instant::now();
    let ans = part2(&input);
    println!("part 2: {} (took {:.5?})", ans, start_time.elapsed());
}
