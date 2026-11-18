# news-image-20261117 entry — notes

## Design
Newspaper front page "THE WORLD TODAY", 1024x1024, drawn entirely by
`main.py` with Pillow (stdlib + PIL only, no network, no clock, no
randomness). Masthead + date line, one lead story with a flat illustration
panel (Strait of Hormuz: sea, Qeshm island, explosion burst), four
secondary stories in two 2-column rows, and a bottom "ALSO" ticker.

## Headlines used (verified 2026-11-18 via news search)
- **Lead — U.S. strikes Iran's Qeshm Island after drone attack on Bahrain
  base.** Corroborated by Daily Baku ("US confirms strike on Qeshm
  Island") and Foreign Exchanges (Iranian drone strike on a U.S. facility
  in Bahrain, third in five days).
- **Crimea Bridge partly collapses in Ukrainian strike.** BBC digest
  mirror (arjenholterman.nl): "Putin's Crimean Bridge partly collapses
  as Zelensky hails 'unprecedented' attack"; Foreign Exchanges confirms
  a portion of the bridge destroyed.
- **146,000 march in France as unions strike.** Daily Baku, 21:57
  17 Nov: "146,000 protest across France as unions strike over living
  costs"; 28,000 in Paris.
- **U.S. loses measles elimination status.** BBC digest: "US loses
  measles elimination status after 26 years amid record case numbers",
  5,400+ cases.
- **Japan scrambles jets after Russian incursion.** Asas Press digest
  and BBC digest: two suspected Russian aircraft violated Japanese
  airspace on Tuesday.
- **Ticker:** Russian military plane crash in Kemerovo kills 19 (BBC
  digest); Mongolia's president resigns (Foreign Exchanges); UK /
  Australia / Canada / Italy urge Israel to open Gaza crossings (Asas
  Press digest).
- Dropped from the earlier brief for lack of corroboration in this
  search: Ebola case count in DR Congo (not used).

## Verification (2026-11-18, this session)
- `python3 main.py` run twice: both outputs byte-identical.
  sha256 `b9ce5411c8051874cff3189657817ddc42ee7b1b45f83ab40b1c7eaac2aab731`
- Output: 1024x1024 px, 122,226 bytes (limit 1,048,576).
- Visual inspection of the PNG: masthead fits, no text overflow or
  overlap, ticker fully inside the canvas (last non-white row 958/1024).
- One fix during build: first render overflowed the bottom (ticker
  clipped) and the masthead was too wide; reduced type sizes and the
  illustration height, re-verified after each change.

## Files
- `main.py` — the entry program (draws /output/entry.png)
- `LICENSE` — MIT, with SPDX-License-Identifier line
- `NOTES.md` — this file
