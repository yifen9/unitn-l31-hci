import re
from pathlib import Path

LOG = Path(__file__).resolve().parents[1] / "report" / "main.log"

text = LOG.read_text(encoding="utf-8", errors="ignore")
match = re.search(r"Output written on .*\((\d+) pages?", text)
if not match:
    raise SystemExit("no page count in main.log, compile first")
pages = int(match.group(1))
print(f"total pages: {pages}")
print("limit: 12 content pages, excluding title/toc page and references")
