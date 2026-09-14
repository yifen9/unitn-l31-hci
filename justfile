default:
    just --list

setup:
    uv sync
    uv run playwright install chromium

shots:
    uv run python scripts/shots.py

report:
    latexmk -xelatex -cd report/main.tex

wireframes:
    uv run python scripts/rasterize.py

sus:
    uv run python analysis/sus.py

tasks:
    uv run python analysis/tasks.py

pages:
    uv run python scripts/pages.py

clean:
    latexmk -C -cd report/main.tex
