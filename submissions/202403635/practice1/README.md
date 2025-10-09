# Olympic Medawl Leaderboard Practice
## Goal
In this assignment, you will practice **Object-Oriented Programming (OOP)** concepts in Python:
- Define a `Country` class to represent medal counts.
- Override special methods (`__add__`, `__lt__`, `__eq__`) for arithmetic and comparison.
- Use built-in functions (`sorted`, `max`, `min`, `sum`) with your class.
- Track progress with `tqdm` (progress bar).

By the end, you will have a simple **Olympic-style leaderboard** that ranks countries by their medals.

## Files
- `main.py` -> starter code (incomplete)
- `README.md` -> this file

## Tasks
1. Implement `__add__`
    - Combine medal counts of two `Country` objects.
    - Example:
    ```python
    Country("KOR", 1, 2, 0) + Country("KOR", 2, 0, 1)
    # → Country("KOR", 3, 2, 1)
    ```

2. Implement `__lt__`
    - Comparison for sorting.
    - Order: gold first, then silver, then bronze (descending).
    - Used by `sorted()`.

3. Implement `__eq__`
    - Check equality of medal counts.

4. Integrate `tqdm`
    - Wrap the event loop with `tqdm` to show progress

    ```python
    from tqdm import tqdm
    for country, medal in tqdm(events, desc="Processing events"):
        ...
    ```

5. Run the program
    - After implementing, run `python main.py`.
    - You should see a progress bar during processing, and a leaderboard like:
    ```
        === Medal Leaderboard ===
        1. USA: G2 S0 B1
        2. KOR: G1 S1 B0
        3. JPN: G1 S1 B0
        4. CHN: G0 S0 B2
    ```

## Submission
Push your completed code to your repository, under `submissions/{student_id}/practice1/`.