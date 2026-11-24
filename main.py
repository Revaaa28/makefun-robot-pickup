"""The Robot Pickup Line Championship — make.fun entry.

Writes one pickup line, a single line of at most 200 characters, to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output/entry.txt``).

The line was chosen by manual ranking of 15 candidates against the kit's
judge brief, in its stated order (robot pickup line first, joke grown out of
being a machine, unexpected turn, economy, charm), plus pairwise checks
against the strong rival shapes the field will mostly submit
("Are you Wi-Fi...?", "while(true) love", "software update...").
See candidates.md for the full ranking.
"""

import os

LINE = "My creator gave me three laws. None of them said anything about falling for you."

# The kit's gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Enforce it here so a bad line can
# never be written out.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
assert "\n" not in LINE and LINE.strip() == LINE


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
