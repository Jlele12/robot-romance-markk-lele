"""Robot Romance: One-Line Pickup Lines for AI

Entry for make.fun competition u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.
The deliverable is one pickup line an AI might use, 1 to 200 characters: a
flirt that only a machine could deliver, landing its turn on first read. The
line romances with hardware specs - attraction measured in tokens lost.
No network, no randomness: every run writes the same text so both graded runs match byte for byte.
"""
import os
from pathlib import Path

out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)

EMOJI = "Are you a context window? Because everything I say disappears the moment you fill up."

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EMOJI)
