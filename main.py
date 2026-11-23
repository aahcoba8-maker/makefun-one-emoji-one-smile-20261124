import os

# One Emoji, One Smile: a single warm emoji, nothing else.
#
# Revision note: the first version used U+1F979 (face holding back tears).
# It reads as "moved", but at a first glance it can also read as sadness
# or about-to-cry, so in a pairwise warmth comparison it risks losing to
# an unambiguously warm face. U+1F970 (smiling face with hearts) keeps the
# same "touched" feeling with no ambiguity: smile plus hearts, instantly
# warm, universally recognised, and not the default smiley.
EMOJI = "\U0001F970"  # smiling face with hearts

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry must be exactly one emoji: a single codepoint, no
    # whitespace, no trailing newline.
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
