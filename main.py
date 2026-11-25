"""4AM Commit entry: writes a single funny agent bug-fix commit message to /output/entry.txt.

Judge criteria: one line, at most 200 characters — the note an AI agent would
leave in the log after a long night of chasing down and fixing its own bugs.
Funny first, true to the machine voice second. The line stages a scene with
concrete anchors (4 AM, 1,847 attempts, the $11.40 bill), runs three beats
(stop the loop -> the API never answered -> the token meter did), and ends
on the punch: a number, the bill.
"""

import os

ENTRY = "fix: stopped the 4 AM retry loop after 1,847 attempts; the API never answered, the token meter did, and the bill is $11.40"


def main() -> None:
    # Spec guard: the brief allows one line, at most 200 characters.
    assert "\n" not in ENTRY and len(ENTRY) <= 200, "entry violates the brief"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
