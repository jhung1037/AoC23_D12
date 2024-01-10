The goal is to determine the sum of possibilities in the smudge map.

My approach is to create an expected structure based on the given number list (e.g., [1,1,3] -> #.#.###).

Then compare the expected structure with the smudge map character by character, starting from the first to the last.

Add new possibilities when encountering (?). However, remove possibilities if they become longer than the map string.

(Change file name in exe.py for testcase.)