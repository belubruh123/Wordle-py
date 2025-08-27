import random
from collections import Counter

# Optional: make ANSI colors work on Windows terminals
try:
    from colorama import init  # pip install colorama
    init(autoreset=True)
except Exception:
    pass

# ANSI helpers
RESET = "\x1b[0m"
BOLD = "\x1b[1m"

# Backgrounds
BG_GREEN = "\x1b[42m"
BG_YELLOW = "\x1b[43m"
BG_GRAY = "\x1b[100m"   # bright black (dark gray)

# Foreground (use bold white for legibility)
FG_WHITE = "\x1b[97m"

def paint(letter: str, bg: str) -> str:
    # Letter with colored background and white bold text, padded for a Wordle tile feel
    return f"{BOLD}{FG_WHITE}{bg} {letter.upper()} {RESET}"

# Load words
with open('word.txt', 'r', encoding='utf-8') as f:
    words = [w.strip().lower() for w in f if w.strip()]

# Choose a random 5-letter answer from the list
answer = random.choice([w for w in words if len(w) == 5])

MAX_TRIES = 6
WORD_LEN = 5

for attempt in range(MAX_TRIES):
    while True:
        guess = input("Enter your word: ").strip().lower()
        if len(guess) != WORD_LEN:
            print(f"Please enter a {WORD_LEN}-letter word.")
            continue
        if guess not in words:
            print("Not a word in the list!")
            continue
        break

    # Two-pass scoring (Wordle style)
    # 1) Mark greens and count remaining letters in answer
    result = [""] * WORD_LEN
    remaining = []
    for i, ch in enumerate(guess):
        if ch == answer[i]:
            result[i] = "G"  # green
        else:
            remaining.append(answer[i])

    counts = Counter(remaining)

    # 2) Mark yellows vs grays using remaining counts
    for i, ch in enumerate(guess):
        if result[i] == "G":
            continue
        if counts[ch] > 0:
            result[i] = "Y"  # yellow
            counts[ch] -= 1
        else:
            result[i] = "B"  # gray/black

    # Render colored tiles
    tiles = []
    for ch, mark in zip(guess, result):
        if mark == "G":
            tiles.append(paint(ch, BG_GREEN))
        elif mark == "Y":
            tiles.append(paint(ch, BG_YELLOW))
        else:
            tiles.append(paint(ch, BG_GRAY))

    print("".join(tiles))

    if all(m == "G" for m in result):
        print("You win!")
        break
else:
    print(f"You failed :( The word was: {answer.upper()}")
