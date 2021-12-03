Work for [Advent of Code](https://adventofcode.com)

## DAY THREE - PART ONE

### Difficulty: EASY | Approximate: O(n)

This could be done multiple ways, of course bruteforcing always has been **an option** yet my first thoughts upon reading the problem statement led to a more thorough approach and one that ultimately went with. Basic premise was to count both `most_common` and `least_common` of invidual bits from a series which would then create another series of bits (one for each side of the spectrum) and then finally converted to decimal and multipled togther. Falls in line within "_Find the occurences of a char_" set of problems.

My solution focused on having to go through the number of bits only **once** in order to save on time. Since the end result of both `gamma_rate` and `epsilon_rate` were dependant on `most_common` and `least_common` bits respectively. The simple solution was to add up the totals of each column and then compare it with the `len(line) // 2`.

Alternative Solutions:

- Matrix Math
- Bruteforcing
- Probably some "Numpy Magic"

## DAY THREE - PART TWO

### Difficulty: EASY | Approximate: O(n log n)

The second part was a troublesome to transition to: starting off by attempting to retain most of the code, especially the `counter` meant that a lot of time was wasted where is was not needed. After figuring the mistake of trying to use the criteria of Part 1, I switched to sets as a "faux fuzzy search algorithm" due to each report needing to be filtered based on `most_common` and `least_common` bits until an invidual report remained.

Notes:

- Could half the time by splitting `most_common` and `least_common` at the start and passing the smaller sets
