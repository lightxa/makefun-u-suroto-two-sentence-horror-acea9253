"""Two-Sentence Horror entry.

Writes one original horror story of exactly two sentences to
/output/entry.txt. Pure standard library, deterministic, no network.

The story is validated before it is written: exactly two sentences,
1 to 400 characters, UTF-8, not only whitespace, so a gate failure
cannot slip through silently.
"""

import os

STORY = (
    "Every night I set my husband's slippers by the door, "
    "a habit I never broke. "
    "This morning one was warm, and the other was gone."
)


def sentence_count(text: str) -> int:
    """Count sentences: a sentence ends on '.', '!' or '?'."""
    return sum(1 for char in text if char in ".!?")


def validate(text: str) -> None:
    """Raise ValueError unless the text passes the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry is {len(text)} characters, must be 1-400")
    if sentence_count(text) != 2:
        raise ValueError(
            f"entry has {sentence_count(text)} sentences, must be exactly 2"
        )
    text.encode("utf-8")


def main() -> None:
    validate(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
