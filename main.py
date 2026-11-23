import os

# One Emoji, One Smile: a single warm emoji, nothing else.
EMOJI = "\U0001F979"  # face holding back tears

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
