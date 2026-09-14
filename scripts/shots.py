from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "shots"

PAGES = [
    ("mobility", "https://osr.clarelab.moe/mobility"),
    ("ranking", "https://osr.clarelab.moe/ranking"),
    ("info-method", "https://osr.clarelab.moe/info?method=mobility"),
    ("info", "https://osr.clarelab.moe/info"),
]


def shoot(context, suffix):
    page = context.new_page()
    for name, url in PAGES:
        page.goto(url, wait_until="load", timeout=60000)
        page.wait_for_timeout(6000)
        for _ in range(24):
            if "Loading" not in page.content():
                break
            page.wait_for_timeout(2500)
        page.wait_for_timeout(2000)
        page.screenshot(path=str(OUT / f"{name}-{suffix}.png"))
    page.close()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        desktop = browser.new_context(
            viewport={"width": 1440, "height": 900}, device_scale_factor=2
        )
        shoot(desktop, "desktop")
        desktop.close()
        mobile = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=3,
            is_mobile=True,
            has_touch=True,
        )
        shoot(mobile, "mobile")
        mobile.close()
        browser.close()


main()
