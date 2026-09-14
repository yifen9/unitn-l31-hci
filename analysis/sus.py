import csv
import statistics
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data" / "sus.csv"


def score(row):
    odd = sum(int(row[f"q{i}"]) - 1 for i in (1, 3, 5, 7, 9))
    even = sum(5 - int(row[f"q{i}"]) for i in (2, 4, 6, 8, 10))
    return (odd + even) * 2.5


def main():
    rows = list(csv.DictReader(DATA.open(encoding="utf-8")))
    if not rows:
        print("no responses in", DATA)
        return
    scores = [(r["participant"], score(r)) for r in rows]
    print("| Participant | SUS |")
    print("| --- | --- |")
    for p, s in scores:
        print(f"| {p} | {s:.1f} |")
    values = [s for _, s in scores]
    mean = statistics.mean(values)
    sd = statistics.stdev(values) if len(values) > 1 else 0.0
    print(f"| mean | {mean:.1f} |")
    print(f"| sd | {sd:.1f} |")


main()
