---
plate: "plate13"
type: "plate"
number: 13
dose: "0.05 / 0.5 / 5"
unreliable: true
plate_factor: 1.0
n_wells: 96
dmso_wells: "B11, B12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 13

`plate13` · dose 0.05 / 0.5 / 5 µM · 96 wells analysed · plate factor 1.00 · ⚠ **unreliable** (its replicate wells do not reproduce)

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: B11, B12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 86,980. Source: `tables/plates.parquet`, `tables/wells.parquet`.

## Layout

*Drug in each well (names cut to 10 characters; the table below has them in full). The per-gene plates notes use the same 8 × 12 layout.*

| |1|2|3|4|5|6|7|8|9|10|11|12|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|A|Abemacicli|c-Kit-IN-1|Ralimetini|PF-0626093|Sonidegib|Hydroxyfas|Pralsetini|olaparib|DTP3|Methylpred|Chlorhexid|Berbamine|
|B|Terfenadin|Pentamidin|Sulfisoxaz|Captopril|Malotilate|Nimesulide|Nimesulide|Nimesulide|Adagrasib|Adagrasib|**DMSO**|**DMSO**|
|C|Berbamine|Daidzin|Fumaric ac|Pravastati|Almonertin|Irinotecan|Belumosudi|Flumatinib|Cytarabine|Afatinib|Topotecan|Naproxen|
|D|Berbamine|Daidzin|Fumaric ac|Pravastati|Almonertin|Irinotecan|Belumosudi|Flumatinib|Cytarabine|Afatinib|Topotecan|Naproxen|
|E|Berbamine|Daidzin|Fumaric ac|Pravastati|Almonertin|Irinotecan|Belumosudi|Flumatinib|Cytarabine|Afatinib|Topotecan|Naproxen|
|F|Daptomycin|Glasdegib|Regorafeni|Fostamatin|Ivabradine|Plicamycin|Ornidazole|Larotrecti|Edoxaban (|Rimonabant|Carbidopa|Ribociclib|
|G|Daptomycin|Glasdegib|Regorafeni|Fostamatin|Ivabradine|Plicamycin|Ornidazole|Larotrecti|Edoxaban (|Rimonabant|Carbidopa|Ribociclib|
|H|Daptomycin|Glasdegib|Regorafeni|Fostamatin|Ivabradine|Plicamycin|Ornidazole|Larotrecti|Edoxaban (|Rimonabant|Carbidopa|Ribociclib|

## Wells

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 96 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[Abemaciclib (drug)]] | 0.05 µM | 96,537 | +0.13 | ⚠ unreliable plate |
| A2 | [[c-Kit-IN-1 (drug)]] | 0.05 µM | 89,568 | +0.03 | ⚠ unreliable plate |
| A3 | [[Ralimetinib dimesylate (drug)]] | 0.05 µM | 96,426 | +0.13 | ⚠ unreliable plate |
| A4 | [[PF-06260933 (drug)]] | 0.05 µM | 120,263 | +0.45 | ⚠ unreliable plate |
| A5 | [[Sonidegib (drug)]] | 0.05 µM | 112,898 | +0.36 | ⚠ unreliable plate |
| A6 | [[Hydroxyfasudil (drug)]] | 0.05 µM | 130,572 | +0.57 | ⚠ unreliable plate |
| A7 | [[Pralsetinib (drug)]] | 0.05 µM | 99,573 | +0.18 | ⚠ unreliable plate, not used in its drug-dose |
| A8 | [[olaparib (drug)]] | 0.05 µM | 86,517 | -0.02 | ⚠ unreliable plate |
| A9 | [[DTP3 (drug)]] | 0.05 µM | 116,454 | +0.41 | ⚠ unreliable plate |
| A10 | [[Methylprednisolone succinate (drug)]] | 0.05 µM | 100,267 | +0.19 | ⚠ unreliable plate |
| A11 | [[Chlorhexidine (diacetate) (drug)]] | 0.5 µM | 82,789 | -0.09 | ⚠ unreliable plate, not used in its drug-dose |
| A12 | [[Berbamine (drug)]] | 0.5 µM | 100,166 | +0.19 | ⚠ unreliable plate, not used in its drug-dose |
| B1 | [[Terfenadine (drug)]] | 0.5 µM | 29,620 | -1.57 | ⚠ unreliable plate, not used in its drug-dose · low cells |
| B2 | [[Pentamidine (isethionate) (drug)]] | 0.5 µM | 34,448 | -1.35 | ⚠ unreliable plate, not used in its drug-dose · low cells |
| B3 | [[Sulfisoxazole (drug)]] | 0.5 µM | 44,050 | -1.00 | ⚠ unreliable plate, not used in its drug-dose |
| B4 | [[Captopril (drug)]] | 0.05 µM | 58,750 | -0.58 | ⚠ unreliable plate, not used in its drug-dose |
| B5 | [[Malotilate (drug)]] | 0.05 µM | 61,944 | -0.51 | ⚠ unreliable plate, not used in its drug-dose |
| B6 | [[Nimesulide (drug)]] | 5 µM | 38,765 | -1.18 | ⚠ unreliable plate · low cells |
| B7 | [[Nimesulide (drug)]] | 0.5 µM | 68,385 | -0.36 | ⚠ unreliable plate |
| B8 | [[Nimesulide (drug)]] | 0.05 µM | 67,806 | -0.38 | ⚠ unreliable plate |
| B9 | [[Adagrasib (drug)]] | 0.05 µM | 80,582 | -0.13 | ⚠ unreliable plate, not used in its drug-dose |
| B10 | [[Adagrasib (drug)]] | 0.05 µM | 74,141 | -0.25 | ⚠ unreliable plate, not used in its drug-dose |
| B11 | DMSO | — | 66,756 | -0.40 | ⚠ unreliable plate · DMSO |
| B12 | DMSO | — | 44,884 | -0.97 | ⚠ unreliable plate · DMSO |
| C1 | [[Berbamine (dihydrochloride) (drug)]] | 5 µM | 23,224 | -1.92 | ⚠ unreliable plate, not used in its drug-dose · low cells |
| C2 | [[Daidzin (drug)]] | 5 µM | 24,389 | -1.85 | ⚠ unreliable plate, not used in its drug-dose · low cells |
| C3 | [[Fumaric acid (drug)]] | 5 µM | 71,953 | -0.29 | ⚠ unreliable plate, not used in its drug-dose |
| C4 | [[Pravastatin (sodium) (drug)]] | 5 µM | 46,798 | -0.91 | ⚠ unreliable plate, not used in its drug-dose |
| C5 | [[Almonertinib (mesylate) (drug)]] | 5 µM | 28,750 | -1.61 | ⚠ unreliable plate, not used in its drug-dose · low cells |
| C6 | [[Irinotecan (hydrochloride) (drug)]] | 5 µM | 40,140 | -1.13 | ⚠ unreliable plate, not used in its drug-dose · low cells |
| C7 | [[Belumosudil (drug)]] | 5 µM | 48,913 | -0.85 | ⚠ unreliable plate, not used in its drug-dose |
| C8 | [[Flumatinib (mesylate) (drug)]] | 5 µM | 74,286 | -0.24 | ⚠ unreliable plate, not used in its drug-dose |
| C9 | [[Cytarabine (drug)]] | 5 µM | 99,382 | +0.18 | ⚠ unreliable plate, not used in its drug-dose |
| C10 | [[Afatinib (drug)]] | 5 µM | 82,217 | -0.10 | ⚠ unreliable plate, not used in its drug-dose |
| C11 | [[Topotecan (hydrochloride) (drug)]] | 5 µM | 90,293 | +0.04 | ⚠ unreliable plate, not used in its drug-dose |
| C12 | [[Naproxen (drug)]] | 5 µM | 65,906 | -0.42 | ⚠ unreliable plate, not used in its drug-dose |
| D1 | [[Berbamine (dihydrochloride) (drug)]] | 0.5 µM | 84,725 | -0.05 | ⚠ unreliable plate, not used in its drug-dose |
| D2 | [[Daidzin (drug)]] | 0.5 µM | 77,496 | -0.18 | ⚠ unreliable plate, not used in its drug-dose |
| D3 | [[Fumaric acid (drug)]] | 0.5 µM | 95,341 | +0.12 | ⚠ unreliable plate, not used in its drug-dose |
| D4 | [[Pravastatin (sodium) (drug)]] | 0.5 µM | 99,303 | +0.18 | ⚠ unreliable plate, not used in its drug-dose |
| D5 | [[Almonertinib (mesylate) (drug)]] | 0.5 µM | 108,342 | +0.30 | ⚠ unreliable plate, not used in its drug-dose |
| D6 | [[Irinotecan (hydrochloride) (drug)]] | 0.5 µM | 109,899 | +0.32 | ⚠ unreliable plate, not used in its drug-dose |
| D7 | [[Belumosudil (drug)]] | 0.5 µM | 119,837 | +0.45 | ⚠ unreliable plate, not used in its drug-dose |
| D8 | [[Flumatinib (mesylate) (drug)]] | 0.5 µM | 114,768 | +0.38 | ⚠ unreliable plate, not used in its drug-dose |
| D9 | [[Cytarabine (drug)]] | 0.5 µM | 96,183 | +0.13 | ⚠ unreliable plate, not used in its drug-dose |
| D10 | [[Afatinib (drug)]] | 0.5 µM | 80,858 | -0.12 | ⚠ unreliable plate, not used in its drug-dose |
| D11 | [[Topotecan (hydrochloride) (drug)]] | 0.5 µM | 113,982 | +0.37 | ⚠ unreliable plate, not used in its drug-dose |
| D12 | [[Naproxen (drug)]] | 0.5 µM | 117,178 | +0.41 | ⚠ unreliable plate, not used in its drug-dose |
| E1 | [[Berbamine (dihydrochloride) (drug)]] | 0.05 µM | 108,937 | +0.31 | ⚠ unreliable plate, not used in its drug-dose |
| E2 | [[Daidzin (drug)]] | 0.05 µM | 79,496 | -0.15 | ⚠ unreliable plate, not used in its drug-dose |
| E3 | [[Fumaric acid (drug)]] | 0.05 µM | 98,475 | +0.16 | ⚠ unreliable plate, not used in its drug-dose |
| E4 | [[Pravastatin (sodium) (drug)]] | 0.05 µM | 83,827 | -0.07 | ⚠ unreliable plate, not used in its drug-dose |
| E5 | [[Almonertinib (mesylate) (drug)]] | 0.05 µM | 88,447 | +0.01 | ⚠ unreliable plate, not used in its drug-dose |
| E6 | [[Irinotecan (hydrochloride) (drug)]] | 0.05 µM | 74,946 | -0.23 | ⚠ unreliable plate, not used in its drug-dose |
| E7 | [[Belumosudil (drug)]] | 0.05 µM | 108,244 | +0.30 | ⚠ unreliable plate, not used in its drug-dose |
| E8 | [[Flumatinib (mesylate) (drug)]] | 0.05 µM | 93,863 | +0.09 | ⚠ unreliable plate, not used in its drug-dose |
| E9 | [[Cytarabine (drug)]] | 0.05 µM | 110,696 | +0.33 | ⚠ unreliable plate, not used in its drug-dose |
| E10 | [[Afatinib (drug)]] | 0.05 µM | 84,775 | -0.05 | ⚠ unreliable plate, not used in its drug-dose |
| E11 | [[Topotecan (hydrochloride) (drug)]] | 0.05 µM | 109,369 | +0.31 | ⚠ unreliable plate, not used in its drug-dose |
| E12 | [[Naproxen (drug)]] | 0.05 µM | 92,251 | +0.07 | ⚠ unreliable plate, not used in its drug-dose |
| F1 | [[Daptomycin (drug)]] | 5 µM | 85,532 | -0.04 | ⚠ unreliable plate |
| F2 | [[Glasdegib (drug)]] | 5 µM | 85,842 | -0.03 | ⚠ unreliable plate |
| F3 | [[Regorafenib (drug)]] | 5 µM | 98,345 | +0.16 | ⚠ unreliable plate, not used in its drug-dose |
| F4 | [[Fostamatinib (disodium hexahydrate) (drug)]] | 5 µM | 78,489 | -0.16 | ⚠ unreliable plate |
| F5 | [[Ivabradine (hydrochloride) (drug)]] | 5 µM | 87,444 | -0.01 | ⚠ unreliable plate |
| F6 | [[Plicamycin (drug)]] | 5 µM | 62,214 | -0.50 | ⚠ unreliable plate |
| F7 | [[Ornidazole (drug)]] | 5 µM | 104,050 | +0.24 | ⚠ unreliable plate |
| F8 | [[Larotrectinib sulfate (drug)]] | 5 µM | 100,190 | +0.19 | ⚠ unreliable plate |
| F9 | [[Edoxaban (tosylate monohydrate) (drug)]] | 5 µM | 108,107 | +0.30 | ⚠ unreliable plate |
| F10 | [[Rimonabant (Hydrochloride) (drug)]] | 5 µM | 100,339 | +0.19 | ⚠ unreliable plate |
| F11 | [[Carbidopa (monohydrate) (drug)]] | 5 µM | 104,087 | +0.24 | ⚠ unreliable plate |
| F12 | [[Ribociclib (drug)]] | 5 µM | 96,124 | +0.13 | ⚠ unreliable plate |
| G1 | [[Daptomycin (drug)]] | 0.5 µM | 53,591 | -0.71 | ⚠ unreliable plate |
| G2 | [[Glasdegib (drug)]] | 0.5 µM | 101,501 | +0.21 | ⚠ unreliable plate |
| G3 | [[Regorafenib (drug)]] | 0.5 µM | 58,016 | -0.60 | ⚠ unreliable plate, not used in its drug-dose |
| G4 | [[Fostamatinib (disodium hexahydrate) (drug)]] | 0.5 µM | 72,525 | -0.28 | ⚠ unreliable plate |
| G5 | [[Ivabradine (hydrochloride) (drug)]] | 0.5 µM | 50,482 | -0.80 | ⚠ unreliable plate |
| G6 | [[Plicamycin (drug)]] | 0.5 µM | 90,857 | +0.05 | ⚠ unreliable plate |
| G7 | [[Ornidazole (drug)]] | 0.5 µM | 73,496 | -0.26 | ⚠ unreliable plate |
| G8 | [[Larotrectinib sulfate (drug)]] | 0.5 µM | 63,183 | -0.48 | ⚠ unreliable plate |
| G9 | [[Edoxaban (tosylate monohydrate) (drug)]] | 0.5 µM | 56,644 | -0.63 | ⚠ unreliable plate |
| G10 | [[Rimonabant (Hydrochloride) (drug)]] | 0.5 µM | 53,403 | -0.72 | ⚠ unreliable plate |
| G11 | [[Carbidopa (monohydrate) (drug)]] | 0.5 µM | 75,411 | -0.22 | ⚠ unreliable plate |
| G12 | [[Ribociclib (drug)]] | 0.5 µM | 82,674 | -0.09 | ⚠ unreliable plate |
| H1 | [[Daptomycin (drug)]] | 0.05 µM | 80,118 | -0.13 | ⚠ unreliable plate |
| H2 | [[Glasdegib (drug)]] | 0.05 µM | 92,624 | +0.07 | ⚠ unreliable plate |
| H3 | [[Regorafenib (drug)]] | 0.05 µM | 109,985 | +0.32 | ⚠ unreliable plate, not used in its drug-dose |
| H4 | [[Fostamatinib (disodium hexahydrate) (drug)]] | 0.05 µM | 102,161 | +0.22 | ⚠ unreliable plate |
| H5 | [[Ivabradine (hydrochloride) (drug)]] | 0.05 µM | 75,625 | -0.22 | ⚠ unreliable plate |
| H6 | [[Plicamycin (drug)]] | 0.05 µM | 107,341 | +0.29 | ⚠ unreliable plate |
| H7 | [[Ornidazole (drug)]] | 0.05 µM | 116,414 | +0.40 | ⚠ unreliable plate |
| H8 | [[Larotrectinib sulfate (drug)]] | 0.05 µM | 76,374 | -0.20 | ⚠ unreliable plate |
| H9 | [[Edoxaban (tosylate monohydrate) (drug)]] | 0.05 µM | 126,206 | +0.52 | ⚠ unreliable plate |
| H10 | [[Rimonabant (Hydrochloride) (drug)]] | 0.05 µM | 94,517 | +0.10 | ⚠ unreliable plate |
| H11 | [[Carbidopa (monohydrate) (drug)]] | 0.05 µM | 137,889 | +0.65 | ⚠ unreliable plate, position not correctable |
| H12 | [[Ribociclib (drug)]] | 0.05 µM | 95,050 | +0.11 | ⚠ unreliable plate, position not correctable |
