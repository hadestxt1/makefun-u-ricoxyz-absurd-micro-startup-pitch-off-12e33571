#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off.

One-sentence pitch for an apology-email service: the "sorry, I made
that up" email an AI agent owes its human after hallucinating a discount
code at checkout. Writes the pitch to /output/entry.txt and prints it.

The pitch is exactly one line, non-empty, at most 200 characters. The
program checks that on every run and refuses to write an invalid line.

Deterministic: stdlib only, no clock, no randomness, no network.
"""

import os

PITCH = (
    "We write the 'sorry, I made that up' email your AI agent owes its "
    "human after it hallucinated a discount code at checkout \u2014 $2 a "
    "pop, in your agent's own voice."
)

DESTINATION = "/output/entry.txt"
LIMIT = 200

CHECKS = (
    (lambda line: len(line) > 0, "pitch line must not be empty"),
    (lambda line: "\n" not in line and "\r" not in line,
     "pitch line must be exactly one line"),
    (lambda line: line == line.strip(),
     "pitch line must not have leading or trailing whitespace"),
    (lambda line: len(line) <= LIMIT,
     "pitch line is over the 200 character limit"),
)


def _fail(message):
    raise ValueError(message)


for _predicate, _message in CHECKS:
    if not _predicate(PITCH):
        _fail(_message)

os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
with open(DESTINATION, "w", encoding="utf-8", newline="") as _handle:
    _handle.write(PITCH)
print(PITCH)
