from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "shots"

STATES = [
    ("mobility-cn", "https://osr.clarelab.moe/mobility?home=CN"),
    ("mobility-city", "https://osr.clarelab.moe/mobility?home=CN&layer=city"),
    ("mobility-institution", "https://osr.clarelab.moe/mobility?home=CN&layer=institution&table=institutions"),
]


def settle(page, ms=6000):
    page.wait_for_timeout(ms)
    for _ in range(24):
        if "Loading" not in page.content():
            break
        page.wait_for_timeout(2500)
    page.wait_for_timeout(2000)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        page = context.new_page()

        for name, url in STATES:
            page.goto(url, wait_until="load", timeout=60000)
            settle(page)
            page.screenshot(path=str(OUT / f"{name}-desktop.png"))
            print(name, "done")

        page.goto("https://osr.clarelab.moe/ranking", wait_until="load", timeout=60000)
        settle(page)
        rows = page.locator("table tbody tr")
        print("ranking rows:", rows.count())
        if rows.count():
            rows.first.click()
            settle(page, 4000)
        page.screenshot(path=str(OUT / "ranking-detail-desktop.png"))
        print("ranking-detail done")

        browser.close()


main()
