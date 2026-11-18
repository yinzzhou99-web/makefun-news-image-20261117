#!/usr/bin/env python3
"""THE WORLD TODAY -- front page for Tuesday, 17 November 2026.

Draws a newspaper front page summarising the day's world news and writes
it to /output/entry.png. Deterministic: no network, no clock, no randomness.
Only Pillow (PIL) and the standard library are used.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "/output/entry.png"

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

INK = (15, 15, 15)
RED = (178, 34, 34)
GREY = (90, 90, 90)
PAPER = (255, 255, 255)
SKY = (176, 208, 232)
SEA = (46, 98, 150)
SAND = (214, 186, 130)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, fill=INK, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.12)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def vrule(draw, x, y0, y1, width=1, fill=GREY):
    draw.line([(x, y0), (x, y1)], fill=fill, width=width)


def draw_lead_art(draw, x, y, w, h):
    """Flat illustration: the Strait of Hormuz -- sea, Qeshm island,
    missile arcs and an explosion burst over the island."""
    draw.rectangle([x, y, x + w, y + h], fill=SKY)
    # sun
    draw.ellipse([x + w - 130, y + 22, x + w - 70, y + 82], fill=(250, 214, 90))
    # sea
    draw.rectangle([x, y + int(h * 0.55), x + w, y + h], fill=SEA)
    draw.line([(x, y + int(h * 0.62)), (x + w, y + int(h * 0.62))],
              fill=(255, 255, 255), width=3)
    draw.line([(x, y + int(h * 0.78)), (x + w, y + int(h * 0.78))],
              fill=(255, 255, 255), width=2)
    # island
    ix0, ix1 = x + int(w * 0.30), x + int(w * 0.68)
    iy = y + int(h * 0.55)
    draw.polygon([(ix0, iy), (ix0 + 60, iy - 52), (ix0 + 190, iy - 58),
                  (ix0 + 260, iy - 18), (ix1, iy)], fill=SAND)
    # explosion burst over the island (kept inside the panel)
    cx, cy = x + int(w * 0.50), iy - 40
    for r, col in ((44, (255, 120, 40)), (32, (255, 170, 40)),
                   (18, (255, 220, 90))):
        pts = []
        for k in range(16):
            import math
            ang = k * math.pi / 8
            rr = r if k % 2 == 0 else r * 0.62
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        draw.polygon(pts, fill=col)
    # smoke (inside the panel)
    draw.ellipse([cx - 62, cy - 48, cx - 18, cy - 12], fill=(120, 120, 120))
    draw.ellipse([cx + 8, cy - 52, cx + 56, cy - 14], fill=(150, 150, 150))
    # missile arcs (two dark streaks with white trails)
    draw.line([(x + 60, y + h - 12), (cx - 90, cy - 40)], fill=INK, width=5)
    draw.line([(x + 60, y + h - 12), (cx - 90, cy - 40)],
              fill=(255, 255, 255), width=2)
    draw.line([(x + w - 70, y + h - 8), (cx + 95, cy - 30)], fill=INK, width=5)
    draw.line([(x + w - 70, y + h - 8), (cx + 95, cy - 30)],
              fill=(255, 255, 255), width=2)
    # caption bar
    draw.rectangle([x, y + h - 30, x + w, y + h], fill=(0, 0, 0))
    draw.text((x + 12, y + h - 26),
              "THE STRAIT OF HORMUZ: U.S. STRIKES FOLLOW IRANIAN DRONE ATTACK",
              font=font(SANS_B, 15), fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 20  # margin
    x0, x1 = mx, W - mx

    # ---- masthead ----
    f_mast = font(SERIF, 84)
    d.text((x0, 6), "THE WORLD TODAY", font=f_mast, fill=INK)
    rule(d, x0, 100, x1, 4)
    f_date = font(SANS_B, 26)
    d.text((x0, 110), "TUESDAY, 17 NOVEMBER 2026", font=f_date, fill=RED)
    f_tag = font(SANS, 22)
    tag = "World news in one image"
    d.text((x1 - d.textlength(tag, font=f_tag), 112), tag, font=f_tag,
           fill=GREY)
    rule(d, x0, 152, x1, 2)

    # ---- lead headline ----
    y = 164
    f_lead = font(SERIF, 48)
    lead = ("U.S. STRIKES IRAN'S QESHM ISLAND AFTER "
            "DRONE ATTACK ON BAHRAIN BASE")
    y = draw_lines(d, wrap(d, lead, f_lead, x1 - x0), f_lead, x0, y)
    y += 6
    f_sub = font(SANS, 23)
    sub = ("Washington says the strike answers the third Iranian drone "
           "attack on a U.S. radar site in five days, as tensions "
           "rise across the Gulf.")
    y = draw_lines(d, wrap(d, sub, f_sub, x1 - x0), f_sub, x0, y, fill=GREY)
    y += 10
    draw_lead_art(d, x0, y, x1 - x0, 170)
    y += 170 + 10
    rule(d, x0, y, x1, 2)
    y += 10

    # ---- two-column second row ----
    col_w = (x1 - x0 - 24) // 2
    f_h2 = font(SERIF, 30)
    f_b2 = font(SANS, 19)

    def column(cx, head, body):
        yy = draw_lines(d, wrap(d, head, f_h2, col_w), f_h2, cx, y)
        yy += 4
        yy = draw_lines(d, wrap(d, body, f_b2, col_w), f_b2, cx, yy,
                        fill=GREY)
        return yy

    y2a = column(x0, "CRIMEA BRIDGE PARTLY COLLAPSES IN UKRAINIAN STRIKE",
                 "Kyiv says the missile and drone attack took weeks to "
                 "plan; a road section fell into the Kerch Strait.")
    y2b = column(x0 + col_w + 24,
                 "146,000 MARCH IN FRANCE AS UNIONS STRIKE",
                 "Nationwide protests over living costs bring cities to a "
                 "standstill; 28,000 rally in Paris alone.")
    vrule(d, x0 + col_w + 12, y, max(y2a, y2b))
    y = max(y2a, y2b) + 10
    rule(d, x0, y, x1, 2)
    y += 12

    # ---- two-column third row ----
    y3a = column(x0, "U.S. LOSES MEASLES ELIMINATION STATUS",
                 "After 26 years, more than 5,400 cases are reported "
                 "nationwide.")
    y3b = column(x0 + col_w + 24,
                 "JAPAN SCRAMBLES JETS AFTER RUSSIAN INCURSION",
                 "Tokyo protests after two suspected Russian aircraft "
                 "violate its airspace on Tuesday.")
    vrule(d, x0 + col_w + 12, y, max(y3a, y3b))
    y = max(y3a, y3b) + 10

    # ---- bottom ticker ----
    rule(d, x0, y, x1, 3, RED)
    y += 8
    f_tick = font(SANS_B, 18)
    tick = ("ALSO:  RUSSIAN PLANE CRASH KILLS 19  •  "
            "MONGOLIA PRESIDENT RESIGNS  •  "
            "GAZA CROSSINGS URGED OPEN")
    y = draw_lines(d, wrap(d, tick, f_tick, x1 - x0), f_tick, x0, y,
                   fill=INK)
    y += 8
    rule(d, x0, y, x1, 2)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG")


if __name__ == "__main__":
    main()
