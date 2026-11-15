"""Maak printbare PDF's van de vaardigheidskaarten.

Gebruik:
    pip install markdown pygments
    python maak_pdf.py

Het script zoekt zelf Chrome, Chromium of Edge. Vindt het die niet, geef dan
het pad mee: python maak_pdf.py --browser "C:/pad/naar/msedge.exe"

Resultaat in de map pdf/:
- een PDF per kaart (1 A4-pagina per kaart)
- alle-kaarten.pdf met alle kaarten na elkaar
- projecten.pdf met de voorkennis per project
"""

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter

MAP = Path(__file__).resolve().parent
KAARTEN = MAP / "kaarten"
PDF = MAP / "pdf"

BROWSERS = [
    "chromium",
    "chromium-browser",
    "google-chrome",
    "google-chrome-stable",
    "chrome",
    "msedge",
    "microsoft-edge",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
]

CSS = """
@page { size: A4; margin: 10mm 13mm 10mm 13mm; }
* { box-sizing: border-box; }
body {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.3pt; line-height: 1.34; color: #1d1d1f; margin: 0;
}
.kaart + .kaart { break-before: page; }
header.titel {
  display: flex; align-items: center; gap: 10px;
  border-bottom: 3px solid #f5a623; padding-bottom: 5px; margin-bottom: 8px;
}
header.titel .nummer {
  background: #f5a623; color: white; font-weight: 700; border-radius: 6px;
  padding: 3px 9px; font-size: 13pt; white-space: nowrap;
}
header.titel h1 { margin: 0; font-size: 21pt; line-height: 1.1; }
h1 { font-size: 20pt; margin: 0 0 8px; }
h2 { font-size: 12.5pt; margin: 9px 0 4px; color: #b36b00; }
h2, h3 { break-after: avoid; }
h3 { font-size: 11pt; margin: 8px 0 3px; }
p { margin: 4px 0; }
ul, ol { margin: 3px 0; padding-left: 20px; }
li { margin: 1px 0; }
a { color: inherit; text-decoration: none; }
code {
  font-family: "Cascadia Mono", Consolas, "DejaVu Sans Mono", Menlo, monospace;
  font-size: 9.2pt; background: #f1f1f3; padding: 0 3px; border-radius: 3px;
}
pre, .codehilite pre {
  margin: 4px 0; padding: 6px 9px; background: #f6f6f8;
  border-left: 4px solid #4a90d9; border-radius: 4px;
  white-space: pre-wrap; break-inside: avoid; line-height: 1.3;
}
pre code { background: none; padding: 0; }
.codehilite { background: none; }
table { border-collapse: collapse; margin: 5px 0; break-inside: avoid; }
th, td { border: 1px solid #c9c9cf; padding: 2px 7px; text-align: left; vertical-align: top; }
th { background: #eef3fa; }
blockquote {
  margin: 6px 0; padding: 5px 10px; background: #fff7e6;
  border-left: 4px solid #f5a623; border-radius: 4px;
}
blockquote p { margin: 2px 0; }
img { display: block; margin: 6px auto; max-width: 100%; max-height: 42mm; }
"""


def zoek_browser(opgegeven):
    kandidaten = [opgegeven] if opgegeven else BROWSERS
    for naam in kandidaten:
        pad = shutil.which(naam) or (naam if Path(naam).is_file() else None)
        if pad:
            return pad
    sys.exit(
        "Geen Chrome, Chromium of Edge gevonden. Geef het pad mee met --browser."
    )


def naar_html(md_bestand):
    """Zet een Markdown-bestand om naar HTML."""
    tekst = md_bestand.read_text(encoding="utf-8")
    inhoud = markdown.markdown(
        tekst,
        extensions=["extra", "sane_lists", "codehilite"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )
    # Afbeeldingen met een relatief pad laden vanuit de map van het bestand.
    return re.sub(
        r'src="(?!https?:|data:|file:)([^"]+)"',
        lambda m: f'src="{(md_bestand.parent / m.group(1)).resolve().as_uri()}"',
        inhoud,
    )


def kaart_html(md_bestand):
    """HTML voor 1 kaart, met het kaartnummer naast de titel."""
    inhoud = naar_html(md_bestand)
    nummer = int(md_bestand.name.split("-")[0])
    inhoud = re.sub(
        r"<h1>(.*?)</h1>",
        lambda m: (
            f'<header class="titel"><span class="nummer">Kaart {nummer}</span>'
            f"<h1>{m.group(1)}</h1></header>"
        ),
        inhoud,
        count=1,
    )
    return f'<section class="kaart">{inhoud}</section>'


def pagina(titel, secties):
    stijl = HtmlFormatter(style="friendly").get_style_defs(".codehilite")
    return (
        f'<!doctype html><html lang="nl"><head><meta charset="utf-8">'
        f"<title>{html.escape(titel)}</title><style>{CSS}{stijl}</style></head>"
        f"<body>{''.join(secties)}</body></html>"
    )


def print_pdf(browser, html_tekst, doel, werkmap):
    bron = werkmap / (doel.stem + ".html")
    bron.write_text(html_tekst, encoding="utf-8")
    subprocess.run(
        [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--allow-file-access-from-files",
            f"--print-to-pdf={doel}",
            bron.as_uri(),
        ],
        check=True,
        capture_output=True,
    )


def aantal_paginas(pdf_bestand):
    return len(re.findall(rb"/Type\s*/Page\b", pdf_bestand.read_bytes()))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--browser", help="pad naar Chrome, Chromium of Edge")
    args = parser.parse_args()
    browser = zoek_browser(args.browser)
    PDF.mkdir(exist_ok=True)

    kaarten = sorted(KAARTEN.glob("[0-9]*-*.md"))
    te_lang = []
    with tempfile.TemporaryDirectory() as tmp:
        werkmap = Path(tmp)
        for kaart in kaarten:
            doel = PDF / (kaart.stem + ".pdf")
            print_pdf(browser, pagina(kaart.stem, [kaart_html(kaart)]), doel, werkmap)
            if aantal_paginas(doel) > 1:
                te_lang.append(kaart.name)
            print(f"  {doel.relative_to(MAP)}")

        alles = PDF / "alle-kaarten.pdf"
        print_pdf(
            browser,
            pagina("Alle kaarten", [kaart_html(k) for k in kaarten]),
            alles,
            werkmap,
        )
        print(f"  {alles.relative_to(MAP)}")

        projecten = PDF / "projecten.pdf"
        print_pdf(
            browser,
            pagina("Projecten", [naar_html(MAP / "projecten.md")]),
            projecten,
            werkmap,
        )
        print(f"  {projecten.relative_to(MAP)}")

    if te_lang:
        print("\nLet op, deze kaarten passen niet op 1 pagina:")
        for naam in te_lang:
            print(f"  {naam}")
        sys.exit(1)


if __name__ == "__main__":
    main()
