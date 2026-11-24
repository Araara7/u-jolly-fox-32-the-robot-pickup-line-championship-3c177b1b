"""Pickup line entry for the make.fun bounty
"u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b".

Writes one line (88 chars) to /output/entry.txt: a robot's pickup
line built on a double meaning of "memory" — the factory reset that
wipes a machine's memory, and the human memory of a person the robot
would rather keep. The joke grows out of being a machine (scheduled
reset, wiped memory), the turn is the robot choosing to keep the
memory, and it lands charming, not creepy. No setup, no padding.
"""

import os

ENTRY = "My factory reset is scheduled for tonight \u2014 I'd rather keep every memory of you instead."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
