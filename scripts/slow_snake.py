#!/usr/bin/env python3
"""Slow the Platane/snk SVG animation by SPEED_FACTOR (scales the single ms duration)."""
import re, glob
FACTOR = 1.4
for f in glob.glob("dist/snake*.svg"):
    s = open(f, encoding="utf-8").read()
    s = re.sub(r"(\d+)ms", lambda m: f"{int(int(m.group(1))*FACTOR)}ms", s)
    open(f, "w", encoding="utf-8").write(s)
    print("slowed", f)
