from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "design" / "wireframes"


def main():
    svgs = sorted(SRC.glob("*.svg"))
    if not svgs:
        print("no svgs in", SRC)
        return
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 1200}, device_scale_factor=2)
        for svg in svgs:
            page.goto(svg.as_uri())
            page.wait_for_timeout(300)
            element = page.locator("svg").first
            element.screenshot(path=str(svg.with_suffix(".png")))
            print(svg.name, "->", svg.with_suffix(".png").name)
        browser.close()


main()
