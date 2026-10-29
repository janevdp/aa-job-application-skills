"""Read the design of a source CV (PDF or DOCX) and print a style sheet.

Usage: python3 extract_design.py <source file>

PDF: lists the embedded font names (BaseFont), with the subset prefix removed,
     and the page size of each page. Sizes and colours are not stored in a PDF
     as named styles, so they must be confirmed visually (Read tool on the PDF).
DOCX: reads word/styles.xml and word/document.xml and lists fonts, sizes (pt),
      colours (hex), page size and margins (cm).
"""
import re
import sys
import zipfile
from collections import Counter

EMU_PER_CM = 360000
TWIPS_PER_CM = 567


def pdf_style(path):
    data = open(path, "rb").read()
    fonts = Counter()
    for name in re.findall(rb"/BaseFont\s*/([^\s/<>\[\]]+)", data):
        clean = re.sub(rb"^[A-Z]{6}\+", b"", name).decode("latin-1")
        fonts[clean] += 1
    sizes = Counter()
    boxes = re.findall(rb"/MediaBox\s*\[\s*([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s*\]", data)
    pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
    print("PDF style sheet")
    print(f"- Pages: {pages}")
    for x0, y0, x1, y1 in set(boxes):
        w = (float(x1) - float(x0)) / 72 * 2.54
        h = (float(y1) - float(y0)) / 72 * 2.54
        print(f"- Page box: {w:.1f} x {h:.1f} cm")
    print("- Fonts embedded:")
    for name, count in fonts.most_common():
        print(f"  - {name} ({count} references)")
    print("- Sizes and colours: confirm visually with the Read tool on the PDF.")


def docx_style(path):
    z = zipfile.ZipFile(path)
    doc = z.read("word/document.xml").decode("utf8")
    styles = z.read("word/styles.xml").decode("utf8") if "word/styles.xml" in z.namelist() else ""
    fonts = Counter(re.findall(r'w:ascii="([^"]+)"', doc + styles))
    sizes = Counter(int(s) / 2 for s in re.findall(r'<w:sz w:val="(\d+)"', doc + styles))
    colours = Counter(c.upper() for c in re.findall(r'<w:color w:val="([0-9A-Fa-f]{6})"', doc + styles))
    pg = re.search(r'<w:pgSz w:w="(\d+)" w:h="(\d+)"', doc)
    mar = re.search(r'<w:pgMar w:top="(\d+)" w:right="(\d+)" w:bottom="(\d+)" w:left="(\d+)"', doc)
    print("DOCX style sheet")
    if pg:
        print(f"- Page size: {int(pg.group(1)) / TWIPS_PER_CM:.1f} x {int(pg.group(2)) / TWIPS_PER_CM:.1f} cm")
    if mar:
        t, r, b, l = (int(v) / TWIPS_PER_CM for v in mar.groups())
        print(f"- Margins (top, right, bottom, left): {t:.1f}, {r:.1f}, {b:.1f}, {l:.1f} cm")
    print("- Fonts:")
    for name, count in fonts.most_common():
        print(f"  - {name} ({count})")
    print("- Font sizes (pt):")
    for size, count in sorted(sizes.items()):
        print(f"  - {size} pt ({count})")
    print("- Colours (hex):")
    for col, count in colours.most_common():
        print(f"  - #{col} ({count})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    if path.lower().endswith(".pdf"):
        pdf_style(path)
    elif path.lower().endswith(".docx"):
        docx_style(path)
    else:
        sys.exit("Use a .pdf or .docx file")
