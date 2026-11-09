---
plate: "plate1"
type: "plate"
number: 1
dose: "0.05"
unreliable: false
plate_factor: 1.059
n_wells: 86
dmso_wells: "H11, H12"
failed_wells: ["A5", "B3", "D2", "E2", "E6", "F2", "F4", "G2", "G4", "G10"]
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 01

`plate1` · dose 0.05 µM · 86 wells analysed · plate factor 1.06 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): A5, B3, D2, E2, E6, F2, F4, G2, G4, G10. Median cells per analysed well: 61,277. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 13 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[Infigratinib (drug)]] | 0.05 µM | 66,929 | +0.13 |  |
| A2 | [[Erdafitinib (drug)]] | 0.05 µM | 64,978 | +0.09 |  |
| A3 | [[Everolimus (drug)]] | 0.05 µM | 47,152 | -0.38 |  |
| A4 | [[Pemigatinib (drug)]] | 0.05 µM | 49,649 | -0.30 |  |
| A5 | [[Abemaciclib (drug)]] | 0.05 µM | 55 | — | ⚠ failed (excluded) |
| A6 | [[Capivasertib (drug)]] | 0.05 µM | 63,756 | +0.06 |  |
| A7 | [[Gemcitabine (drug)]] | 0.05 µM | 74,969 | +0.29 |  |
| A8 | [[Irinotecan (drug)]] | 0.05 µM | 75,915 | +0.31 |  |
| A9 | [[Oxaliplatin (drug)]] | 0.05 µM | 70,054 | +0.20 |  |
| A10 | [[Alpelisib (drug)]] | 0.05 µM | 47,995 | -0.35 |  |
| A11 | [[Lapatinib ditosylate (drug)]] | 0.05 µM | 57,594 | -0.09 |  |
| A12 | [[palbociclib (drug)]] | 0.05 µM | 42,483 | -0.53 |  |
| B1 | [[Lonafarnib (drug)]] | 0.05 µM | 85,625 | +0.49 |  |
| B2 | [[Volasertib (drug)]] | 0.05 µM | 64,360 | +0.07 |  |
| B3 | [[c-Kit-IN-1 (drug)]] | 0.05 µM | 85 | — | ⚠ failed (excluded) |
| B4 | [[venetoclax (drug)]] | 0.05 µM | 70,781 | +0.21 |  |
| B5 | [[Capmatinib (drug)]] | 0.05 µM | 55,817 | -0.13 |  |
| B6 | [[MK-8353 (drug)]] | 0.05 µM | 65,033 | +0.09 |  |
| B7 | [[Regorafenib (drug)]] | 0.05 µM | 47,212 | -0.37 |  |
| B8 | [[Tucatinib (drug)]] | 0.05 µM | 70,036 | +0.20 |  |
| B9 | [[Vemurafenib (drug)]] | 0.05 µM | 69,997 | +0.19 |  |
| B10 | [[BI-3406 (drug)]] | 0.05 µM | 67,704 | +0.15 |  |
| B11 | [[AZD-8055 (drug)]] | 0.05 µM | 81,726 | +0.42 |  |
| B12 | [[Binimetinib (drug)]] | 0.05 µM | 53,142 | -0.20 |  |
| C1 | [[Temuterkib (drug)]] | 0.05 µM | 59,975 | -0.03 |  |
| C2 | [[ML264 (drug)]] | 0.05 µM | 52,843 | -0.21 |  |
| C3 | [[BI-78D3 (drug)]] | 0.05 µM | 48,857 | -0.32 |  |
| C4 | [[Tomivosertib (drug)]] | 0.05 µM | 62,772 | +0.04 |  |
| C5 | [[Brivudine (drug)]] | 0.05 µM | 63,912 | +0.06 |  |
| C6 | [[Bentamapimod (drug)]] | 0.05 µM | 46,266 | -0.40 |  |
| C7 | [[Dabrafenib (drug)]] | 0.05 µM | 65,497 | +0.10 |  |
| C8 | [[Encorafenib (drug)]] | 0.05 µM | 79,671 | +0.38 |  |
| C9 | [[Paclitaxel (drug)]] | 0.05 µM | 72,511 | +0.25 |  |
| C10 | [[RMC-6236 (drug)]] | 0.05 µM | 53,766 | -0.19 |  |
| C11 | [[Trametinib (drug)]] | 0.05 µM | 44,975 | -0.44 |  |
| C12 | [[Afatinib (drug)]] | 0.05 µM | 41,165 | -0.57 |  |
| D1 | [[NVP-BHG712 (drug)]] | 0.05 µM | 76,925 | +0.33 |  |
| D2 | [[Ralimetinib dimesylate (drug)]] | 0.05 µM | 61 | — | ⚠ failed (excluded) |
| D3 | [[ERK5-IN-2 (drug)]] | 0.05 µM | 61,596 | +0.01 |  |
| D4 | [[PH-797804 (drug)]] | 0.05 µM | 71,298 | +0.22 |  |
| D5 | [[TAK-901 (drug)]] | 0.05 µM | 43,241 | -0.50 |  |
| D6 | [[Ipatasertib (drug)]] | 0.05 µM | 50,235 | -0.28 |  |
| D7 | [[Sapanisertib (drug)]] | 0.05 µM | 82,052 | +0.42 |  |
| D8 | [[BAY1125976 (drug)]] | 0.05 µM | 73,627 | +0.27 |  |
| D9 | [[9-ING-41 (drug)]] | 0.05 µM | 78,325 | +0.36 |  |
| D10 | [[XRK3F2 (drug)]] | 0.05 µM | 61,344 | +0.00 |  |
| D11 | [[Bimiralisib (drug)]] | 0.05 µM | 69,479 | +0.18 |  |
| D12 | [[GSK1059615 (drug)]] | 0.05 µM | 67,421 | +0.14 |  |
| E1 | [[AZD2858 (drug)]] | 0.05 µM | 70,226 | +0.20 |  |
| E2 | [[PF-06260933 (drug)]] | 0.05 µM | 114 | — | ⚠ failed (excluded) |
| E3 | [[SBI-0640756 (drug)]] | 0.05 µM | 71,371 | +0.22 |  |
| E4 | [[LJI308 (drug)]] | 0.05 µM | 56,886 | -0.10 |  |
| E5 | [[LY-2584702 (tosylate salt) (drug)]] | 0.05 µM | 44,655 | -0.45 |  |
| E6 | [[Sonidegib (drug)]] | 0.05 µM | 714 | — | ⚠ failed (excluded) |
| E7 | [[EX229 (drug)]] | 0.05 µM | 48,034 | -0.35 |  |
| E8 | [[MK-3903 (drug)]] | 0.05 µM | 52,239 | -0.23 |  |
| E9 | [[Everolimus (drug)]] | 0.05 µM | 52,860 | -0.21 |  |
| E10 | [[ULK-101 (drug)]] | 0.05 µM | 53,794 | -0.18 |  |
| E11 | [[IQ 1 (drug)]] | 0.05 µM | 71,840 | +0.23 |  |
| E12 | [[CP21R7 (drug)]] | 0.05 µM | 60,539 | -0.01 |  |
| F1 | [[Bortezomib (drug)]] | 0.05 µM | 39,945 | -0.61 |  |
| F2 | [[Hydroxyfasudil (drug)]] | 0.05 µM | 979 | — | ⚠ failed (excluded) |
| F3 | [[Belumosudil (mesylate) (drug)]] | 0.05 µM | 63,111 | +0.05 |  |
| F4 | [[Belzutifan (drug)]] | 0.05 µM | 1,524 | — | ⚠ failed (excluded) |
| F5 | [[Futibatinib (drug)]] | 0.05 µM | 62,019 | +0.02 |  |
| F6 | [[Pralsetinib (drug)]] | 0.05 µM | 59,221 | -0.05 |  |
| F7 | [[TAK-733 (drug)]] | 0.05 µM | 71,195 | +0.22 |  |
| F8 | [[Elimusertib hydrochloride (drug)]] | 0.05 µM | 48,844 | -0.32 |  |
| F9 | [[AZD1390 (drug)]] | 0.05 µM | 66,351 | +0.12 |  |
| F10 | [[Tubulin inhibitor 6 (drug)]] | 0.05 µM | 57,390 | -0.09 |  |
| F11 | [[Torkinib (drug)]] | 0.05 µM | 54,419 | -0.17 |  |
| F12 | [[4EGI-1 (drug)]] | 0.05 µM | 54,831 | -0.16 |  |
| G1 | [[Pimitespib (drug)]] | 0.05 µM | 51,749 | -0.24 |  |
| G2 | [[olaparib (drug)]] | 0.05 µM | 123 | — | ⚠ failed (excluded) |
| G3 | [[Ixazomib (drug)]] | 0.05 µM | 35,792 | -0.77 |  |
| G4 | [[DTP3 (drug)]] | 0.05 µM | 81 | — | ⚠ failed (excluded) |
| G5 | [[OTS514 (drug)]] | 0.05 µM | 53,856 | -0.18 |  |
| G6 | [[NG25 (drug)]] | 0.05 µM | 49,501 | -0.30 |  |
| G7 | [[DT-061 (drug)]] | 0.05 µM | 44,214 | -0.47 |  |
| G8 | [[AZD-7648 (drug)]] | 0.05 µM | 73,035 | +0.26 |  |
| G9 | [[Gemcitabine (drug)]] | 0.05 µM | 90,855 | +0.57 |  |
| G10 | [[Methylprednisolone succinate (drug)]] | 0.05 µM | 51 | — | ⚠ failed (excluded) |
| G11 | [[Celecoxib (drug)]] | 0.05 µM | 42,614 | -0.52 |  |
| G12 | [[vincristine (drug)]] | 0.05 µM | 54,177 | -0.17 |  |
| H1 | [[HI-TOPK-032 (drug)]] | 0.05 µM | 26,129 | -1.23 | low cells |
| H2 | [[APTO-253 (drug)]] | 0.05 µM | 61,210 | +0.00 |  |
| H3 | [[LB-100 (drug)]] | 0.05 µM | 87,764 | +0.52 |  |
| H4 | [[AT7519 (drug)]] | 0.05 µM | 77,064 | +0.33 |  |
| H5 | [[ETC-206 (drug)]] | 0.05 µM | 60,092 | -0.03 |  |
| H6 | [[LY2090314 (drug)]] | 0.05 µM | 61,094 | -0.00 |  |
| H7 | [[Oleic acid (drug)]] | 0.05 µM | 60,889 | -0.01 |  |
| H8 | [[Minodronic acid (drug)]] | 0.05 µM | 68,205 | +0.16 |  |
| H9 | [[Anastrozole (drug)]] | 0.05 µM | 87,855 | +0.52 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 58,321 | -0.07 | ⚠ position not correctable |
| H11 | DMSO | — | 83,959 | +0.46 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 87,338 | +0.51 | ⚠ position not correctable · DMSO |
