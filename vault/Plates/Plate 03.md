---
plate: "plate3"
type: "plate"
number: 3
dose: "0.05 / 5"
unreliable: false
plate_factor: 1.913
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 03

`plate3` · dose 0.05 / 5 µM · 96 wells analysed · plate factor 1.91 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 33,710. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 3 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[Infigratinib (drug)]] | 5 µM | 45,929 | +0.45 |  |
| A2 | [[Erdafitinib (drug)]] | 5 µM | 46,121 | +0.46 |  |
| A3 | [[Everolimus (drug)]] | 5 µM | 78,448 | +1.23 |  |
| A4 | [[Pemigatinib (drug)]] | 5 µM | 36,018 | +0.10 |  |
| A5 | [[Abemaciclib (drug)]] | 5 µM | 42,446 | +0.34 |  |
| A6 | [[Capivasertib (drug)]] | 5 µM | 25,487 | -0.39 |  |
| A7 | [[Gemcitabine (drug)]] | 5 µM | 41,653 | +0.31 |  |
| A8 | [[Irinotecan (drug)]] | 5 µM | 72,177 | +1.11 |  |
| A9 | [[Oxaliplatin (drug)]] | 5 µM | 40,759 | +0.28 |  |
| A10 | [[Alpelisib (drug)]] | 5 µM | 29,263 | -0.20 |  |
| A11 | [[Lapatinib ditosylate (drug)]] | 5 µM | 71,031 | +1.08 |  |
| A12 | [[palbociclib (drug)]] | 5 µM | 33,875 | +0.02 |  |
| B1 | [[Lonafarnib (drug)]] | 5 µM | 8,557 | -1.97 | low cells |
| B2 | [[Volasertib (drug)]] | 5 µM | 22,322 | -0.59 |  |
| B3 | [[c-Kit-IN-1 (drug)]] | 5 µM | 28,381 | -0.24 |  |
| B4 | [[venetoclax (drug)]] | 5 µM | 26,952 | -0.31 |  |
| B5 | [[Capmatinib (drug)]] | 5 µM | 24,244 | -0.47 |  |
| B6 | [[MK-8353 (drug)]] | 5 µM | 29,445 | -0.19 |  |
| B7 | [[Regorafenib (drug)]] | 5 µM | 39,058 | +0.22 |  |
| B8 | [[Tucatinib (drug)]] | 5 µM | 75,767 | +1.18 |  |
| B9 | [[Vemurafenib (drug)]] | 5 µM | 67,433 | +1.01 |  |
| B10 | [[BI-3406 (drug)]] | 5 µM | 60,987 | +0.86 |  |
| B11 | [[AZD-8055 (drug)]] | 5 µM | 54,297 | +0.70 |  |
| B12 | [[Binimetinib (drug)]] | 5 µM | 23,373 | -0.52 |  |
| C1 | [[Temuterkib (drug)]] | 5 µM | 54,251 | +0.69 |  |
| C2 | [[ML264 (drug)]] | 5 µM | 57,009 | +0.77 |  |
| C3 | [[BI-78D3 (drug)]] | 5 µM | 69,415 | +1.05 |  |
| C4 | [[Tomivosertib (drug)]] | 5 µM | 48,845 | +0.54 |  |
| C5 | [[Brivudine (drug)]] | 5 µM | 73,898 | +1.14 |  |
| C6 | [[Bentamapimod (drug)]] | 5 µM | 54,466 | +0.70 |  |
| C7 | [[Dabrafenib (drug)]] | 5 µM | 119,849 | +1.84 |  |
| C8 | [[Encorafenib (drug)]] | 5 µM | 111,694 | +1.74 |  |
| C9 | [[Paclitaxel (drug)]] | 5 µM | 111,034 | +1.73 |  |
| C10 | [[RMC-6236 (drug)]] | 5 µM | 91,133 | +1.44 |  |
| C11 | [[Trametinib (drug)]] | 5 µM | 75,297 | +1.17 |  |
| C12 | [[Afatinib (drug)]] | 5 µM | 77,341 | +1.21 |  |
| D1 | [[NVP-BHG712 (drug)]] | 5 µM | 35,563 | +0.09 |  |
| D2 | [[Ralimetinib dimesylate (drug)]] | 5 µM | 47,917 | +0.52 |  |
| D3 | [[ERK5-IN-2 (drug)]] | 5 µM | 91,086 | +1.44 |  |
| D4 | [[PH-797804 (drug)]] | 5 µM | 40,079 | +0.26 |  |
| D5 | [[TAK-901 (drug)]] | 5 µM | 63,643 | +0.93 |  |
| D6 | [[Ipatasertib (drug)]] | 5 µM | 87,667 | +1.39 |  |
| D7 | [[Sapanisertib (drug)]] | 5 µM | 98,021 | +1.55 |  |
| D8 | [[BAY1125976 (drug)]] | 5 µM | 92,892 | +1.47 |  |
| D9 | [[9-ING-41 (drug)]] | 5 µM | 93,710 | +1.48 |  |
| D10 | [[XRK3F2 (drug)]] | 5 µM | 78,435 | +1.23 |  |
| D11 | [[Bimiralisib (drug)]] | 5 µM | 93,662 | +1.48 |  |
| D12 | [[GSK1059615 (drug)]] | 5 µM | 78,627 | +1.23 |  |
| E1 | [[AZD2858 (drug)]] | 5 µM | 15,301 | -1.13 | low cells |
| E2 | [[PF-06260933 (drug)]] | 5 µM | 20,924 | -0.68 |  |
| E3 | [[SBI-0640756 (drug)]] | 5 µM | 20,852 | -0.68 |  |
| E4 | [[LJI308 (drug)]] | 5 µM | 26,953 | -0.31 |  |
| E5 | [[LY-2584702 (tosylate salt) (drug)]] | 5 µM | 10,300 | -1.70 | low cells |
| E6 | [[Sonidegib (drug)]] | 5 µM | 16,887 | -0.99 |  |
| E7 | [[EX229 (drug)]] | 5 µM | 32,915 | -0.03 |  |
| E8 | [[MK-3903 (drug)]] | 5 µM | 28,807 | -0.22 |  |
| E9 | [[Everolimus (drug)]] | 5 µM | 21,708 | -0.63 |  |
| E10 | [[ULK-101 (drug)]] | 5 µM | 22,770 | -0.56 |  |
| E11 | [[IQ 1 (drug)]] | 5 µM | 23,554 | -0.51 |  |
| E12 | [[CP21R7 (drug)]] | 5 µM | 25,418 | -0.40 |  |
| F1 | [[Bortezomib (drug)]] | 5 µM | 12,986 | -1.37 | low cells |
| F2 | [[Hydroxyfasudil (drug)]] | 5 µM | 19,715 | -0.77 |  |
| F3 | [[Belumosudil (mesylate) (drug)]] | 5 µM | 27,999 | -0.26 |  |
| F4 | [[Belzutifan (drug)]] | 5 µM | 22,275 | -0.59 |  |
| F5 | [[Futibatinib (drug)]] | 5 µM | 21,099 | -0.67 |  |
| F6 | [[Pralsetinib (drug)]] | 5 µM | 18,338 | -0.87 |  |
| F7 | [[TAK-733 (drug)]] | 5 µM | 33,545 | +0.00 |  |
| F8 | [[Elimusertib hydrochloride (drug)]] | 5 µM | 16,475 | -1.02 | low cells |
| F9 | [[AZD1390 (drug)]] | 5 µM | 32,881 | -0.03 |  |
| F10 | [[Tubulin inhibitor 6 (drug)]] | 5 µM | 26,707 | -0.33 |  |
| F11 | [[Torkinib (drug)]] | 5 µM | 14,902 | -1.17 | low cells |
| F12 | [[4EGI-1 (drug)]] | 5 µM | 24,665 | -0.44 |  |
| G1 | [[Pimitespib (drug)]] | 5 µM | 18,572 | -0.85 |  |
| G2 | [[olaparib (drug)]] | 5 µM | 26,905 | -0.32 |  |
| G3 | [[Ixazomib (drug)]] | 5 µM | 24,637 | -0.44 |  |
| G4 | [[DTP3 (drug)]] | 5 µM | 27,151 | -0.30 |  |
| G5 | [[OTS514 (drug)]] | 5 µM | 18,579 | -0.85 |  |
| G6 | [[NG25 (drug)]] | 5 µM | 33,481 | -0.00 |  |
| G7 | [[DT-061 (drug)]] | 5 µM | 23,734 | -0.50 |  |
| G8 | [[AZD-7648 (drug)]] | 5 µM | 24,634 | -0.44 |  |
| G9 | [[Gemcitabine (drug)]] | 5 µM | 21,058 | -0.67 |  |
| G10 | [[Methylprednisolone succinate (drug)]] | 5 µM | 28,167 | -0.25 |  |
| G11 | [[Celecoxib (drug)]] | 5 µM | 32,706 | -0.04 |  |
| G12 | [[vincristine (drug)]] | 5 µM | 21,631 | -0.63 |  |
| H1 | [[HI-TOPK-032 (drug)]] | 5 µM | 25,686 | -0.38 |  |
| H2 | [[APTO-253 (drug)]] | 5 µM | 42,089 | +0.33 |  |
| H3 | [[LB-100 (drug)]] | 5 µM | 37,166 | +0.15 |  |
| H4 | [[AT7519 (drug)]] | 5 µM | 47,117 | +0.49 |  |
| H5 | [[ETC-206 (drug)]] | 5 µM | 39,421 | +0.23 |  |
| H6 | [[LY2090314 (drug)]] | 5 µM | 50,863 | +0.60 |  |
| H7 | [[Oleic acid (drug)]] | 5 µM | 29,126 | -0.20 |  |
| H8 | [[Minodronic acid (drug)]] | 5 µM | 38,253 | +0.19 |  |
| H9 | [[Anastrozole (drug)]] | 5 µM | 42,193 | +0.33 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 23,843 | -0.49 | ⚠ position not correctable |
| H11 | DMSO | — | 39,806 | +0.25 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 33,927 | +0.02 | ⚠ position not correctable · DMSO |
