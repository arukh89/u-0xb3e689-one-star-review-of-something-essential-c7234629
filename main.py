"""One-Star Review of Something Essential: write one deadpan one-star
review, at most 160 characters, of an everyday essential to
/output/entry.txt."""

import os

LINE = "I gave sleep eight hours and woke up more tired, with no refund and no manager to complain to."


def main():
    # The gate only accepts 1-160 characters of non-blank UTF-8 text,
    # in a single line: no newline characters anywhere in the entry.
    assert 1 <= len(LINE) <= 160 and LINE.strip(), "line must be 1-160 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    # One sentence only: a single sentence-ending period, at the end.
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    # Deadpan: no exclamation mark doing the work, no winking.
    assert "!" not in LINE, "line must hold the deadpan"
    # The gate counts characters; keep the line plain ASCII so byte and
    # character counts agree, with no stray leading/trailing whitespace.
    assert LINE.isascii(), "line must be plain ASCII"
    assert LINE == LINE.strip(), "line must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "round-trip mismatch"


if __name__ == "__main__":
    main()
