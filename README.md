Work for [Advent of Code](https://adventofcode.com)

| Day | Difficulty | Part 1   | Part 2   |
| --- | ---------- | -------- | -------- |
| 1   | Easy       | 725 µs   | 1,269 µs |
| 2   | Easy       | 501 µs   | 571 µs   |
| 3   | Easy       | 1,991 µs | 167 µs   |
| 4   | Medium     | 86 µs    | 86 µs    |
| 5   | Medium     | 152 µs   | 125 µs   |

## Day Three

### Part 1 | Approximate: O(n)

This could be done multiple ways, of course bruteforcing always has been **an option** yet my first thoughts upon reading the problem statement led to a more thorough approach and one that ultimately went with. Basic premise was to count both `most_common` and `least_common` of invidual bits from a series which would then create another series of bits (one for each side of the spectrum) and then finally converted to decimal and multipled togther. Falls in line within "_Find the occurences of a char_" set of problems.

My solution focused on having to go through the number of bits only **once** in order to save on time. Since the end result of both `gamma_rate` and `epsilon_rate` were dependant on `most_common` and `least_common` bits respectively. The simple solution was to add up the totals of each column and then compare it with the `len(line) // 2`.

Alternative Solutions:

- Matrix Math
- Bruteforcing
- Probably some "Numpy Magic"

### Part 2 | Approximate: O(n log n)

The second part was a troublesome to transition to: starting off by attempting to retain most of the code, especially the `counter` meant that a lot of time was wasted where is was not needed. After figuring the mistake of trying to use the criteria of Part 1, I switched to sets as a "faux fuzzy search algorithm" due to each report needing to be filtered based on `most_common` and `least_common` bits until an invidual report remained.

Notes:

- Could half the time by splitting `most_common` and `least_common` at the start and passing the smaller sets

## Day Five

### Part 1 and 2 | Approximate: O(n)

Day five was the hardest so far and a subset of "_Find the intersection(s) between N points_" problems. These crux around these problems is managing coordinates, **not** the discovery of intersections, and can take a bit of mixing to get it right. Numpy was the solution for me; trivial to manage the state of the grid along its axis and generating the coordinates of points for the diagonals.

Even though part 1 only asked to focus on the straight axis, obviously the second part was focusing on the diagonals given the difficulty. So I wanted to focus on doing it in one go.
