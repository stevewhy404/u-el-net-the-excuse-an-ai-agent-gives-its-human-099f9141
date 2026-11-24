"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
the funniest, most believable excuse an AI agent could give its human for
The excuse escalates in three steps — reminder, meeting, reschedule — and
lands on the meeting acting behind the agent's back. The line is 155
characters, inside the 1-200 gate, with no trailing newline in the output.
"""

import os

LINE = "I didn't miss the deadline \u2014 my reminder set a reminder, the reminder set a meeting, and the meeting rescheduled itself to next quarter without telling me."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
