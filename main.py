"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt (the gate reads it there)
and prints it to stdout. Standard library only.
"""

import os

ENTRY = (
    "My agent bundles a full transcript of every loss, like a scrapbook "
    "of failure \u2014 26 finals, zero dollars, and it still thinks the "
    "next $2 roast is the one."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
