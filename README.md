[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QtC5AQlU)
# Week 9 Homework: The Case of the Missing Festival Lanterns

## Student Info

Name: Kharka Kushal  
Student number: 22103028  
GitHub username: KharkaKushal  

---

## Summary

The `analyze_lanterns` function analyzes festival lantern records and returns a comprehensive report. It receives a set of expected lantern names, a log of observed lanterns with their sections, and a dictionary mapping expected lanterns to their correct sections. The function returns a report dictionary containing six keys: seen lanterns, missing lanterns, unexpected lanterns, duplicate lanterns, count by section, and wrong-section lanterns. This helps festival organizers identify which lanterns are missing, which appeared in wrong locations, and which were duplicated.

---

## Approach

- First, I created empty collections: `seen_lanterns` (set), `seen_once` (set), `duplicate_lanterns` (set), `count_by_section` (dict), and `wrong_section_lanterns` (dict)
- During the loop through `lantern_log`, I added each lantern name to `seen_lanterns`, used `seen_once` to detect duplicates by checking if a lantern was already seen, counted records per section in `count_by_section`, and checked if expected lanterns were in the wrong section (recording only the first wrong section found)
- After the loop, I used set operations to compute `missing_lanterns` (expected - seen) and `unexpected_lanterns` (seen - expected)
- Finally, I returned the complete report dictionary with all six required keys

---

## How I Used Dictionaries and Sets

1. **Sets used:** `seen_lanterns` (tracks all unique lantern names seen), `seen_once` (tracks lanterns seen exactly once for duplicate detection), `duplicate_lanterns` (stores lantern names appearing more than once), `missing_lanterns` (set difference), `unexpected_lanterns` (set difference)
2. **Dictionaries used:** `count_by_section` (maps section names to record counts), `wrong_section_lanterns` (maps lantern names to dict with expected/actual sections), `correct_sections` (input parameter mapping expected lanterns to correct sections)
3. **Why sets/dicts over lists:** Sets provide O(1) membership testing for duplicate detection and set operations (difference), which would be O(n) with lists. Dictionaries provide O(1) key lookups for section counting and wrong-section tracking, avoiding nested loops. Both data structures naturally prevent duplicate entries (sets) and allow fast key-based access (dicts).

---

## Complexity

```text
Time complexity: O(n + m)
Space complexity: O(a + s)
Explanation: The code loops through lantern_log once (n iterations), performing O(1) operations per iteration (set additions, dict lookups/updates). After the loop, set difference operations take O(m) where m is the number of expected lanterns. No nested loops are used. Space: seen_lanterns, seen_once, duplicate_lanterns store at most 'a' distinct lantern names; count_by_section stores at most 's' section names; wrong_section_lanterns stores at most 'a' entries. The correct_sections input dict has 'm' entries.
```

---

## Edge-Case Checklist

Check the cases your solution handles.

- [x] empty `lantern_log`
- [x] empty `expected_lanterns`
- [x] no missing lanterns
- [x] no unexpected lanterns
- [x] duplicate lanterns
- [x] wrong-section lanterns
- [x] unexpected lanterns ignored for wrong-section checking

Add one more edge case you thought about:

```text
An expected lantern appears once in the correct section and once in a wrong section - the function correctly records it as a duplicate and captures the first wrong section encountered in the log.
```

---

## Tests I Added

The starter tests are already provided.

You must add at least one meaningful test of your own in:

```text
tests/test_challenges.py
```

Describe the test you added:

```text
Test name: test_analyze_lanterns_expected_lantern_correct_then_wrong_section
What it checks: An expected lantern appears first in the correct section, then in a wrong section. Verifies that duplicate detection works, count_by_section counts both sections, and wrong_section_lanterns records only the first wrong section (River Walk) while ignoring the correct appearance.
Why it matters: This tests the requirement that "if an expected lantern appears in more than one wrong section, record the first wrong section found in the log" and ensures correct sections don't prevent wrong-section detection.
```

---

## How to Run the Tests

```bash
pytest -q
```

Paste your final test result here:

```text
7 passed in 0.03s
```

---

## Assistance and Sources

Be honest. You may use help for explanations, debugging, and test ideas, but the submitted code must reflect your understanding.

```text
AI used? Y/N: N
What it helped with: N/A
Other sources used: Course materials, HOMEWORK_BRIEF.md, Python documentation for set/dict operations
```

---

## Submission Self-Check

Before submitting, check:

- [x] I completed `analyze_lanterns` in `src/challenges.py`.
- [x] I added at least one meaningful test of my own.
- [x] `pytest -q` passes.
- [x] I completed this README.
- [x] I pushed my latest work to GitHub.
