import csv
import statistics
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data" / "tasks.csv"


def main():
    rows = list(csv.DictReader(DATA.open(encoding="utf-8")))
    if not rows:
        print("no task logs in", DATA)
        return
    by_task = defaultdict(list)
    for r in rows:
        by_task[r["task"]].append(r)
    print("| Task | Success | Assisted | Median time (s) | Errors |")
    print("| --- | --- | --- | --- | --- |")
    for task in sorted(by_task):
        rs = by_task[task]
        n = len(rs)
        ok = sum(int(r["success"]) for r in rs)
        assisted = sum(int(r["assisted"]) for r in rs)
        med = statistics.median(int(r["time_s"]) for r in rs)
        errs = sum(int(r["errors"]) for r in rs)
        print(f"| {task} | {ok}/{n} | {assisted} | {med:.0f} | {errs} |")


main()
