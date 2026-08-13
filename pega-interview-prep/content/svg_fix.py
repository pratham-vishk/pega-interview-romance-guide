"""Post-process Mermaid SVG for WeasyPrint — convert foreignObject labels to native SVG text."""

import re
import html as html_lib
from xml.etree import ElementTree as ET

SVG_NS = "http://www.w3.org/2000/svg"
XHTML_NS = "http://www.w3.org/1999/xhtml"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


def _extract_text(foreign: ET.Element) -> str:
    texts = []
    for elem in foreign.iter():
        if elem.tag.endswith("p") and elem.text:
            texts.append(elem.text.strip())
        elif elem.tag.endswith("span") and elem.text:
            texts.append(elem.text.strip())
    return " ".join(t for t in texts if t)


def fix_svg_for_pdf(svg_path: str) -> str:
    """Return SVG string with foreignObject labels replaced by SVG text elements."""
    content = open(svg_path, encoding="utf-8").read()
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return content

    # Find parent groups and replace foreignObject with text
    for fo in list(root.iter(f"{{{SVG_NS}}}foreignObject")):
        parent = None
        for p in root.iter():
            if fo in list(p):
                parent = p
                break
        if parent is None:
            continue

        text = _extract_text(fo)
        if not text:
            parent.remove(fo)
            continue

        # Get position from transform on sibling g.label or parent g
        x, y = 0.0, 0.0
        g_parent = parent
        transform = g_parent.get("transform", "")
        m = re.search(r"translate\(([^,]+),\s*([^)]+)\)", transform)
        if m:
            x = float(m.group(1))
            y = float(m.group(2))

        # Adjust for foreignObject position
        fo_x = float(fo.get("x", 0) or 0)
        fo_y = float(fo.get("y", 0) or 0)
        fo_w = float(fo.get("width", 100) or 100)
        fo_h = float(fo.get("height", 24) or 24)

        text_el = ET.Element(f"{{{SVG_NS}}}text")
        text_el.set("x", str(x + fo_x + fo_w / 2))
        text_el.set("y", str(y + fo_y + fo_h / 2 + 5))
        text_el.set("text-anchor", "middle")
        text_el.set("font-family", "DejaVu Sans, Arial, sans-serif")
        text_el.set("font-size", "13")
        text_el.set("fill", "#333333")
        text_el.text = html_lib.unescape(text)

        idx = list(parent).index(fo)
        parent.remove(fo)
        parent.insert(idx, text_el)

    return ET.tostring(root, encoding="unicode")
