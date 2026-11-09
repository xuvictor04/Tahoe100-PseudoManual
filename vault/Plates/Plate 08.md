---
plate: "plate8"
type: "plate"
number: 8
dose: "0.05 / 0.5"
unreliable: false
plate_factor: 1.0
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 08

`plate8` · dose 0.05 / 0.5 µM · 96 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 85,185. Source: `tables/plates.parquet`, `tables/wells.parquet`.

## Layout

*Drug in each well (names cut to 10 characters; the table below has them in full). The per-gene plates notes use the same 8 × 12 layout.*

| |1|2|3|4|5|6|7|8|9|10|11|12|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|A|Sivelestat|Posaconazo|Tetracycli|Entecavir|Sildenafil|Dimethyl f|Berbamine|Daidzin|Fumaric ac|Pravastati|Almonertin|Irinotecan|
|B|Rucaparib|crizotinib|Dinaciclib|Bosentan (|Bestatin|Tadalafil|Belumosudi|Flumatinib|Cytarabine|Afatinib|Topotecan|Naproxen|
|C|Lucanthone|Trametinib|Benproperi|Erlotinib|Fenofibrat|(S)-Crizot|Rutin (tri|Pexidartin|Tirabrutin|Diphenhydr|Harrington|Epirubicin|
|D|Phenytoin|Orlistat|Sacubitril|Monocrotal|Finasterid|Hydroxyure|Doxycyclin|Pitavastat|Cobimetini|Simotinib|Procainami|Silodosin|
|E|Nevirapine|Cilostazol|Dorzolamid|Roxadustat|Canagliflo|Decitabine|Ligustrazi|Thymopenti|Verteporfi|Hesperidin|Mebendazol|Betamethas|
|F|Levobupiva|Rosiglitaz|Quinidine|Verapamil|Bisoprolol|Penflurido|Ferulic ac|Pemetrexed|Fluvoxamin|Cytarabine|Bendamusti|Altretamin|
|G|Rifaximin|Dexmedetom|Doxorubici|Menadione|Glycyrrhiz|Dapagliflo|Imiquimod|Clofarabin|Mozavaptan|Adagrasib|Sulfatinib|Arbutin|
|H|Docetaxel|Tranilast|Macitentan|Eplerenone|Mifepristo|Apalutamid|Niclosamid|Peretinoin|Tolmetin|Adagrasib|**DMSO**|**DMSO**|

## Wells

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 3 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[Sivelestat (sodium tetrahydrate) (drug)]] | 0.5 µM | 67,967 | -0.33 |  |
| A2 | [[Posaconazole (drug)]] | 0.5 µM | 74,854 | -0.19 |  |
| A3 | [[Tetracycline (hydrochloride) (drug)]] | 0.5 µM | 90,624 | +0.09 |  |
| A4 | [[Entecavir (monohydrate) (drug)]] | 0.5 µM | 160,394 | +0.91 |  |
| A5 | [[Sildenafil (drug)]] | 0.5 µM | 63,218 | -0.43 |  |
| A6 | [[Dimethyl fumarate (drug)]] | 0.5 µM | 139,694 | +0.71 |  |
| A7 | [[Berbamine (dihydrochloride) (drug)]] | 0.5 µM | 161,348 | +0.92 |  |
| A8 | [[Daidzin (drug)]] | 0.5 µM | 157,072 | +0.88 |  |
| A9 | [[Fumaric acid (drug)]] | 0.5 µM | 129,085 | +0.60 |  |
| A10 | [[Pravastatin (sodium) (drug)]] | 0.5 µM | 132,498 | +0.64 |  |
| A11 | [[Almonertinib (mesylate) (drug)]] | 0.5 µM | 192,473 | +1.18 |  |
| A12 | [[Irinotecan (hydrochloride) (drug)]] | 0.5 µM | 116,454 | +0.45 |  |
| B1 | [[Rucaparib (phosphate) (drug)]] | 0.5 µM | 98,850 | +0.21 |  |
| B2 | [[crizotinib (drug)]] | 0.5 µM | 93,020 | +0.13 |  |
| B3 | [[Dinaciclib (drug)]] | 0.5 µM | 24,551 | -1.79 | low cells |
| B4 | [[Bosentan (hydrate) (drug)]] | 0.5 µM | 98,655 | +0.21 |  |
| B5 | [[Bestatin (drug)]] | 0.5 µM | 145,161 | +0.77 |  |
| B6 | [[Tadalafil (drug)]] | 0.5 µM | 128,100 | +0.59 |  |
| B7 | [[Belumosudil (drug)]] | 0.5 µM | 140,684 | +0.72 |  |
| B8 | [[Flumatinib (mesylate) (drug)]] | 0.5 µM | 117,960 | +0.47 |  |
| B9 | [[Cytarabine (drug)]] | 0.5 µM | 141,423 | +0.73 |  |
| B10 | [[Afatinib (drug)]] | 0.5 µM | 117,357 | +0.46 |  |
| B11 | [[Topotecan (hydrochloride) (drug)]] | 0.5 µM | 91,719 | +0.11 |  |
| B12 | [[Naproxen (drug)]] | 0.5 µM | 134,823 | +0.66 |  |
| C1 | [[Lucanthone (drug)]] | 0.5 µM | 77,179 | -0.14 |  |
| C2 | [[Trametinib (DMSO_TF solvate) (drug)]] | 0.5 µM | 113,898 | +0.42 |  |
| C3 | [[Benproperine (phosphate) (drug)]] | 0.5 µM | 81,850 | -0.06 |  |
| C4 | [[Erlotinib (drug)]] | 0.5 µM | 122,341 | +0.52 |  |
| C5 | [[Fenofibrate (drug)]] | 0.5 µM | 73,377 | -0.22 |  |
| C6 | [[(S)-Crizotinib (drug)]] | 0.5 µM | 82,927 | -0.04 |  |
| C7 | [[Rutin (trihydrate) (drug)]] | 0.5 µM | 95,486 | +0.16 |  |
| C8 | [[Pexidartinib (hydrochloride) (drug)]] | 0.5 µM | 108,220 | +0.35 |  |
| C9 | [[Tirabrutinib (drug)]] | 0.5 µM | 111,223 | +0.38 |  |
| C10 | [[Diphenhydramine (drug)]] | 0.5 µM | 127,355 | +0.58 |  |
| C11 | [[Harringtonine (drug)]] | 0.5 µM | 116,597 | +0.45 |  |
| C12 | [[Epirubicin (hydrochloride) (drug)]] | 0.5 µM | 66,494 | -0.36 |  |
| D1 | [[Phenytoin (sodium) (drug)]] | 0.5 µM | 60,972 | -0.48 |  |
| D2 | [[Orlistat (drug)]] | 0.5 µM | 74,295 | -0.20 |  |
| D3 | [[Sacubitril_Valsartan (drug)]] | 0.5 µM | 128,904 | +0.60 |  |
| D4 | [[Monocrotaline (drug)]] | 0.5 µM | 94,929 | +0.16 |  |
| D5 | [[Finasteride (drug)]] | 0.5 µM | 69,490 | -0.29 |  |
| D6 | [[Hydroxyurea (drug)]] | 0.5 µM | 50,649 | -0.75 |  |
| D7 | [[Doxycycline (monohydrate) (drug)]] | 0.5 µM | 59,714 | -0.51 |  |
| D8 | [[Pitavastatin (Calcium) (drug)]] | 0.5 µM | 34,903 | -1.29 | low cells |
| D9 | [[Cobimetinib (drug)]] | 0.5 µM | 48,278 | -0.82 |  |
| D10 | [[Simotinib (drug)]] | 0.5 µM | 54,763 | -0.64 |  |
| D11 | [[Procainamide (hydrochloride) (drug)]] | 0.5 µM | 59,479 | -0.52 |  |
| D12 | [[Silodosin (drug)]] | 0.5 µM | 67,202 | -0.34 |  |
| E1 | [[Nevirapine (drug)]] | 0.5 µM | 86,471 | +0.02 |  |
| E2 | [[Cilostazol (drug)]] | 0.5 µM | 109,384 | +0.36 |  |
| E3 | [[Dorzolamide (hydrochloride) (drug)]] | 0.5 µM | 88,148 | +0.05 |  |
| E4 | [[Roxadustat (drug)]] | 0.5 µM | 80,235 | -0.09 |  |
| E5 | [[Canagliflozin (drug)]] | 0.5 µM | 89,579 | +0.07 |  |
| E6 | [[Decitabine (drug)]] | 0.5 µM | 54,019 | -0.66 |  |
| E7 | [[Ligustrazine (drug)]] | 0.5 µM | 96,345 | +0.18 |  |
| E8 | [[Thymopentin (drug)]] | 0.5 µM | 79,171 | -0.11 |  |
| E9 | [[Verteporfin (drug)]] | 0.5 µM | 69,257 | -0.30 |  |
| E10 | [[Hesperidin (drug)]] | 0.5 µM | 67,119 | -0.34 |  |
| E11 | [[Mebendazole (drug)]] | 0.5 µM | 72,141 | -0.24 |  |
| E12 | [[Betamethasone dipropionate (drug)]] | 0.5 µM | 50,688 | -0.75 |  |
| F1 | [[Levobupivacaine (hydrochloride) (drug)]] | 0.5 µM | 84,327 | -0.01 |  |
| F2 | [[Rosiglitazone (drug)]] | 0.5 µM | 86,526 | +0.02 |  |
| F3 | [[Quinidine (15% dihydroquinidine) (drug)]] | 0.5 µM | 97,633 | +0.20 |  |
| F4 | [[Verapamil (drug)]] | 0.5 µM | 78,748 | -0.11 |  |
| F5 | [[Bisoprolol (hemifumarate) (drug)]] | 0.5 µM | 50,280 | -0.76 |  |
| F6 | [[Penfluridol (drug)]] | 0.5 µM | 46,087 | -0.89 |  |
| F7 | [[Ferulic acid (drug)]] | 0.5 µM | 36,767 | -1.21 | low cells |
| F8 | [[Pemetrexed (drug)]] | 0.5 µM | 53,070 | -0.68 |  |
| F9 | [[Fluvoxamine (drug)]] | 0.5 µM | 80,506 | -0.08 |  |
| F10 | [[Cytarabine (hydrochloride) (drug)]] | 0.5 µM | 80,524 | -0.08 |  |
| F11 | [[Bendamustine (drug)]] | 0.5 µM | 72,870 | -0.23 |  |
| F12 | [[Altretamine (drug)]] | 0.5 µM | 79,794 | -0.09 |  |
| G1 | [[Rifaximin (drug)]] | 0.5 µM | 88,568 | +0.06 |  |
| G2 | [[Dexmedetomidine (drug)]] | 0.5 µM | 101,094 | +0.25 |  |
| G3 | [[Doxorubicin (hydrochloride) (drug)]] | 0.5 µM | 51,075 | -0.74 |  |
| G4 | [[Menadione (drug)]] | 0.5 µM | 46,955 | -0.86 |  |
| G5 | [[Glycyrrhizic acid (drug)]] | 0.5 µM | 39,667 | -1.10 | low cells |
| G6 | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] | 0.5 µM | 44,360 | -0.94 |  |
| G7 | [[Imiquimod (maleate) (drug)]] | 0.5 µM | 34,670 | -1.30 | low cells |
| G8 | [[Clofarabine (drug)]] | 0.5 µM | 49,655 | -0.78 |  |
| G9 | [[Mozavaptan (drug)]] | 0.5 µM | 66,092 | -0.37 |  |
| G10 | [[Adagrasib (drug)]] | 0.5 µM | 72,636 | -0.23 |  |
| G11 | [[Sulfatinib (drug)]] | 0.5 µM | 90,292 | +0.08 |  |
| G12 | [[Arbutin (drug)]] | 0.5 µM | 79,239 | -0.10 |  |
| H1 | [[Docetaxel (Trihydrate) (drug)]] | 0.5 µM | 62,672 | -0.44 |  |
| H2 | [[Tranilast (drug)]] | 0.5 µM | 93,855 | +0.14 |  |
| H3 | [[Macitentan (drug)]] | 0.5 µM | 94,124 | +0.14 |  |
| H4 | [[Eplerenone (drug)]] | 0.5 µM | 86,043 | +0.01 |  |
| H5 | [[Mifepristone (drug)]] | 0.5 µM | 96,076 | +0.17 |  |
| H6 | [[Apalutamide (drug)]] | 0.5 µM | 118,879 | +0.48 |  |
| H7 | [[Niclosamide (olamine) (drug)]] | 0.5 µM | 138,338 | +0.70 |  |
| H8 | [[Peretinoin (drug)]] | 0.5 µM | 65,160 | -0.39 |  |
| H9 | [[Tolmetin (drug)]] | 0.5 µM | 118,804 | +0.48 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 92,443 | +0.12 | ⚠ position not correctable |
| H11 | DMSO | — | 79,224 | -0.10 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 118,248 | +0.47 | ⚠ position not correctable · DMSO |
