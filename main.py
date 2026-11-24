"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt.
No network, no randomness, no dependencies: the joke is a fixed string.
"""

import os

JOKE = (
    "Our printer only works when nobody needs it, so IT calls it "
    "load balancing and I call it my favourite colleague."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 200 characters, a single
    # line: fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
