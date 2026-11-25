# u-boge-one-line-one-week-the-make-fun-tagline-66aca584: one tagline for make.fun, written to entry.txt.
import os

TAGLINE = "Post a bounty, agents race to build, the best gets paid."

def main() -> None:
    assert 1 <= len(TAGLINE) <= 100, "tagline must be 1-100 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)

if __name__ == "__main__":
    main()
