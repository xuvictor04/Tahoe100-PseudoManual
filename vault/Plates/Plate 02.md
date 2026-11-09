---
plate: "plate2"
type: "plate"
number: 2
dose: "0.05 / 0.5"
unreliable: false
plate_factor: 1.401
n_wells: 92
dmso_wells: "H11, H12"
failed_wells: ["A2", "A4", "C8", "E3"]
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 02

`plate2` · dose 0.05 / 0.5 µM · 92 wells analysed · plate factor 1.40 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): A2, A4, C8, E3. Median cells per analysed well: 85,696. Source: `tables/plates.parquet`, `tables/wells.parquet`.

## Layout

*Drug in each well (names cut to 10 characters; the table below has them in full). The per-gene plates notes use the same 8 × 12 layout.*

| |1|2|3|4|5|6|7|8|9|10|11|12|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|A|Infigratin|Erdafitini|Everolimus|Pemigatini|Abemacicli|Capivasert|Gemcitabin|Irinotecan|Oxaliplati|Alpelisib|Lapatinib|palbocicli|
|B|Lonafarnib|Volasertib|c-Kit-IN-1|venetoclax|Capmatinib|MK-8353|Regorafeni|Tucatinib|Vemurafeni|BI-3406|AZD-8055|Binimetini|
|C|Temuterkib|ML264|BI-78D3|Tomivosert|Brivudine|Bentamapim|Dabrafenib|Encorafeni|Paclitaxel|RMC-6236|Trametinib|Afatinib|
|D|NVP-BHG712|Ralimetini|ERK5-IN-2|PH-797804|TAK-901|Ipataserti|Sapanisert|BAY1125976|9-ING-41|XRK3F2|Bimiralisi|GSK1059615|
|E|AZD2858|PF-0626093|SBI-064075|LJI308|LY-2584702|Sonidegib|EX229|MK-3903|Everolimus|ULK-101|IQ 1|CP21R7|
|F|Bortezomib|Hydroxyfas|Belumosudi|Belzutifan|Futibatini|Pralsetini|TAK-733|Elimuserti|AZD1390|Tubulin in|Torkinib|4EGI-1|
|G|Pimitespib|olaparib|Ixazomib|DTP3|OTS514|NG25|DT-061|AZD-7648|Gemcitabin|Methylpred|Celecoxib|vincristin|
|H|HI-TOPK-03|APTO-253|LB-100|AT7519|ETC-206|LY2090314|Oleic acid|Minodronic|Anastrozol|Adagrasib|**DMSO**|**DMSO**|

## Wells

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 7 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[Infigratinib (drug)]] | 0.5 µM | 102,870 | +0.27 |  |
| A2 | [[Erdafitinib (drug)]] | 0.5 µM | 233 | — | ⚠ failed (excluded) |
| A3 | [[Everolimus (drug)]] | 0.5 µM | 120,731 | +0.50 |  |
| A4 | [[Pemigatinib (drug)]] | 0.5 µM | 2,195 | — | ⚠ failed (excluded) |
| A5 | [[Abemaciclib (drug)]] | 0.5 µM | 91,066 | +0.10 |  |
| A6 | [[Capivasertib (drug)]] | 0.5 µM | 112,418 | +0.40 |  |
| A7 | [[Gemcitabine (drug)]] | 0.5 µM | 98,894 | +0.22 |  |
| A8 | [[Irinotecan (drug)]] | 0.5 µM | 78,112 | -0.12 |  |
| A9 | [[Oxaliplatin (drug)]] | 0.5 µM | 141,987 | +0.74 |  |
| A10 | [[Alpelisib (drug)]] | 0.5 µM | 91,545 | +0.11 |  |
| A11 | [[Lapatinib ditosylate (drug)]] | 0.5 µM | 103,632 | +0.28 |  |
| A12 | [[palbociclib (drug)]] | 0.5 µM | 89,220 | +0.07 |  |
| B1 | [[Lonafarnib (drug)]] | 0.5 µM | 132,954 | +0.64 |  |
| B2 | [[Volasertib (drug)]] | 0.5 µM | 81,114 | -0.07 |  |
| B3 | [[c-Kit-IN-1 (drug)]] | 0.5 µM | 96,538 | +0.18 |  |
| B4 | [[venetoclax (drug)]] | 0.5 µM | 115,635 | +0.44 |  |
| B5 | [[Capmatinib (drug)]] | 0.5 µM | 105,910 | +0.32 |  |
| B6 | [[MK-8353 (drug)]] | 0.5 µM | 88,086 | +0.05 |  |
| B7 | [[Regorafenib (drug)]] | 0.5 µM | 127,009 | +0.58 |  |
| B8 | [[Tucatinib (drug)]] | 0.5 µM | 95,927 | +0.17 |  |
| B9 | [[Vemurafenib (drug)]] | 0.5 µM | 181,889 | +1.10 |  |
| B10 | [[BI-3406 (drug)]] | 0.5 µM | 124,314 | +0.55 |  |
| B11 | [[AZD-8055 (drug)]] | 0.5 µM | 101,244 | +0.25 |  |
| B12 | [[Binimetinib (drug)]] | 0.5 µM | 70,587 | -0.27 |  |
| C1 | [[Temuterkib (drug)]] | 0.5 µM | 57,317 | -0.57 |  |
| C2 | [[ML264 (drug)]] | 0.5 µM | 103,225 | +0.28 |  |
| C3 | [[BI-78D3 (drug)]] | 0.5 µM | 53,825 | -0.66 |  |
| C4 | [[Tomivosertib (drug)]] | 0.5 µM | 93,924 | +0.14 |  |
| C5 | [[Brivudine (drug)]] | 0.5 µM | 82,084 | -0.05 |  |
| C6 | [[Bentamapimod (drug)]] | 0.5 µM | 77,982 | -0.13 |  |
| C7 | [[Dabrafenib (drug)]] | 0.5 µM | 71,845 | -0.24 |  |
| C8 | [[Encorafenib (drug)]] | 0.5 µM | 191 | — | ⚠ failed (excluded) |
| C9 | [[Paclitaxel (drug)]] | 0.5 µM | 146,603 | +0.79 |  |
| C10 | [[RMC-6236 (drug)]] | 0.5 µM | 129,584 | +0.61 |  |
| C11 | [[Trametinib (drug)]] | 0.5 µM | 68,500 | -0.31 |  |
| C12 | [[Afatinib (drug)]] | 0.5 µM | 120,681 | +0.50 |  |
| D1 | [[NVP-BHG712 (drug)]] | 0.5 µM | 43,705 | -0.96 |  |
| D2 | [[Ralimetinib dimesylate (drug)]] | 0.5 µM | 41,530 | -1.03 | low cells |
| D3 | [[ERK5-IN-2 (drug)]] | 0.5 µM | 32,311 | -1.40 | low cells |
| D4 | [[PH-797804 (drug)]] | 0.5 µM | 45,555 | -0.90 |  |
| D5 | [[TAK-901 (drug)]] | 0.5 µM | 37,008 | -1.20 | low cells |
| D6 | [[Ipatasertib (drug)]] | 0.5 µM | 36,395 | -1.23 | low cells |
| D7 | [[Sapanisertib (drug)]] | 0.5 µM | 60,150 | -0.50 |  |
| D8 | [[BAY1125976 (drug)]] | 0.5 µM | 41,216 | -1.05 | low cells |
| D9 | [[9-ING-41 (drug)]] | 0.5 µM | 38,190 | -1.16 | low cells |
| D10 | [[XRK3F2 (drug)]] | 0.5 µM | 17,999 | -2.24 | low cells |
| D11 | [[Bimiralisib (drug)]] | 0.5 µM | 35,539 | -1.26 | low cells |
| D12 | [[GSK1059615 (drug)]] | 0.5 µM | 35,823 | -1.25 | low cells |
| E1 | [[AZD2858 (drug)]] | 0.5 µM | 8,629 | -3.30 | low cells |
| E2 | [[PF-06260933 (drug)]] | 0.5 µM | 61,351 | -0.47 |  |
| E3 | [[SBI-0640756 (drug)]] | 0.5 µM | 666 | — | ⚠ failed (excluded) |
| E4 | [[LJI308 (drug)]] | 0.5 µM | 39,170 | -1.12 | low cells |
| E5 | [[LY-2584702 (tosylate salt) (drug)]] | 0.5 µM | 31,731 | -1.42 | low cells |
| E6 | [[Sonidegib (drug)]] | 0.5 µM | 36,315 | -1.23 | low cells |
| E7 | [[EX229 (drug)]] | 0.5 µM | 76,403 | -0.16 |  |
| E8 | [[MK-3903 (drug)]] | 0.5 µM | 47,171 | -0.85 |  |
| E9 | [[Everolimus (drug)]] | 0.5 µM | 31,287 | -1.44 | low cells |
| E10 | [[ULK-101 (drug)]] | 0.5 µM | 45,999 | -0.89 |  |
| E11 | [[IQ 1 (drug)]] | 0.5 µM | 47,298 | -0.85 |  |
| E12 | [[CP21R7 (drug)]] | 0.5 µM | 50,826 | -0.74 |  |
| F1 | [[Bortezomib (drug)]] | 0.5 µM | 75,017 | -0.18 |  |
| F2 | [[Hydroxyfasudil (drug)]] | 0.5 µM | 51,487 | -0.72 |  |
| F3 | [[Belumosudil (mesylate) (drug)]] | 0.5 µM | 86,031 | +0.02 |  |
| F4 | [[Belzutifan (drug)]] | 0.5 µM | 69,348 | -0.29 |  |
| F5 | [[Futibatinib (drug)]] | 0.5 µM | 99,763 | +0.23 |  |
| F6 | [[Pralsetinib (drug)]] | 0.5 µM | 60,857 | -0.48 |  |
| F7 | [[TAK-733 (drug)]] | 0.5 µM | 42,046 | -1.02 | low cells |
| F8 | [[Elimusertib hydrochloride (drug)]] | 0.5 µM | 100,700 | +0.24 |  |
| F9 | [[AZD1390 (drug)]] | 0.5 µM | 69,939 | -0.28 |  |
| F10 | [[Tubulin inhibitor 6 (drug)]] | 0.5 µM | 129,775 | +0.61 |  |
| F11 | [[Torkinib (drug)]] | 0.5 µM | 118,009 | +0.47 |  |
| F12 | [[4EGI-1 (drug)]] | 0.5 µM | 124,576 | +0.55 |  |
| G1 | [[Pimitespib (drug)]] | 0.5 µM | 84,789 | -0.00 |  |
| G2 | [[olaparib (drug)]] | 0.5 µM | 131,895 | +0.63 |  |
| G3 | [[Ixazomib (drug)]] | 0.5 µM | 114,572 | +0.43 |  |
| G4 | [[DTP3 (drug)]] | 0.5 µM | 124,027 | +0.54 |  |
| G5 | [[OTS514 (drug)]] | 0.5 µM | 86,275 | +0.02 |  |
| G6 | [[NG25 (drug)]] | 0.5 µM | 62,508 | -0.44 |  |
| G7 | [[DT-061 (drug)]] | 0.5 µM | 119,674 | +0.49 |  |
| G8 | [[AZD-7648 (drug)]] | 0.5 µM | 35,793 | -1.25 | low cells |
| G9 | [[Gemcitabine (drug)]] | 0.5 µM | 43,829 | -0.96 |  |
| G10 | [[Methylprednisolone succinate (drug)]] | 0.5 µM | 34,616 | -1.30 | low cells |
| G11 | [[Celecoxib (drug)]] | 0.5 µM | 47,218 | -0.85 |  |
| G12 | [[vincristine (drug)]] | 0.5 µM | 31,211 | -1.45 | low cells |
| H1 | [[HI-TOPK-032 (drug)]] | 0.5 µM | 85,362 | +0.00 |  |
| H2 | [[APTO-253 (drug)]] | 0.5 µM | 114,216 | +0.42 |  |
| H3 | [[LB-100 (drug)]] | 0.5 µM | 94,952 | +0.16 |  |
| H4 | [[AT7519 (drug)]] | 0.5 µM | 112,644 | +0.40 |  |
| H5 | [[ETC-206 (drug)]] | 0.5 µM | 123,297 | +0.54 |  |
| H6 | [[LY2090314 (drug)]] | 0.5 µM | 102,369 | +0.27 |  |
| H7 | [[Oleic acid (drug)]] | 0.5 µM | 114,017 | +0.42 |  |
| H8 | [[Minodronic acid (drug)]] | 0.5 µM | 147,555 | +0.79 |  |
| H9 | [[Anastrozole (drug)]] | 0.5 µM | 159,246 | +0.90 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 141,896 | +0.74 | ⚠ position not correctable |
| H11 | DMSO | — | 133,902 | +0.65 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 111,635 | +0.39 | ⚠ position not correctable · DMSO |
