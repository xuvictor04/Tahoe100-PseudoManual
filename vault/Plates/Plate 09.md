---
plate: "plate9"
type: "plate"
number: 9
dose: "0.05 / 5"
unreliable: false
plate_factor: 1.04
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 09

`plate9` · dose 0.05 / 5 µM · 96 wells analysed · plate factor 1.04 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 51,695. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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
| A1 | [[Sivelestat (sodium tetrahydrate) (drug)]] | 5 µM | 118,690 | +1.20 |  |
| A2 | [[Posaconazole (drug)]] | 5 µM | 114,895 | +1.15 |  |
| A3 | [[Tetracycline (hydrochloride) (drug)]] | 5 µM | 105,538 | +1.03 |  |
| A4 | [[Entecavir (monohydrate) (drug)]] | 5 µM | 119,857 | +1.22 |  |
| A5 | [[Sildenafil (drug)]] | 5 µM | 113,560 | +1.14 |  |
| A6 | [[Dimethyl fumarate (drug)]] | 5 µM | 99,349 | +0.94 |  |
| A7 | [[Berbamine (dihydrochloride) (drug)]] | 5 µM | 86,903 | +0.75 |  |
| A8 | [[Daidzin (drug)]] | 5 µM | 98,473 | +0.93 |  |
| A9 | [[Fumaric acid (drug)]] | 5 µM | 100,533 | +0.96 |  |
| A10 | [[Pravastatin (sodium) (drug)]] | 5 µM | 117,225 | +1.18 |  |
| A11 | [[Almonertinib (mesylate) (drug)]] | 5 µM | 129,269 | +1.32 |  |
| A12 | [[Irinotecan (hydrochloride) (drug)]] | 5 µM | 83,802 | +0.70 |  |
| B1 | [[Rucaparib (phosphate) (drug)]] | 5 µM | 125,347 | +1.28 |  |
| B2 | [[crizotinib (drug)]] | 5 µM | 59,849 | +0.21 |  |
| B3 | [[Dinaciclib (drug)]] | 5 µM | 9,252 | -2.48 | low cells |
| B4 | [[Bosentan (hydrate) (drug)]] | 5 µM | 26,653 | -0.95 |  |
| B5 | [[Bestatin (drug)]] | 5 µM | 58,220 | +0.17 |  |
| B6 | [[Tadalafil (drug)]] | 5 µM | 37,569 | -0.46 |  |
| B7 | [[Belumosudil (drug)]] | 5 µM | 46,475 | -0.15 |  |
| B8 | [[Flumatinib (mesylate) (drug)]] | 5 µM | 56,625 | +0.13 |  |
| B9 | [[Cytarabine (drug)]] | 5 µM | 35,130 | -0.55 |  |
| B10 | [[Afatinib (drug)]] | 5 µM | 39,408 | -0.39 |  |
| B11 | [[Topotecan (hydrochloride) (drug)]] | 5 µM | 21,672 | -1.25 | low cells |
| B12 | [[Naproxen (drug)]] | 5 µM | 42,988 | -0.26 |  |
| C1 | [[Lucanthone (drug)]] | 5 µM | 73,364 | +0.51 |  |
| C2 | [[Trametinib (DMSO_TF solvate) (drug)]] | 5 µM | 48,369 | -0.09 |  |
| C3 | [[Benproperine (phosphate) (drug)]] | 5 µM | 48,867 | -0.08 |  |
| C4 | [[Erlotinib (drug)]] | 5 µM | 44,686 | -0.21 |  |
| C5 | [[Fenofibrate (drug)]] | 5 µM | 48,742 | -0.08 |  |
| C6 | [[(S)-Crizotinib (drug)]] | 5 µM | 56,463 | +0.13 |  |
| C7 | [[Rutin (trihydrate) (drug)]] | 5 µM | 49,113 | -0.07 |  |
| C8 | [[Pexidartinib (hydrochloride) (drug)]] | 5 µM | 69,967 | +0.44 |  |
| C9 | [[Tirabrutinib (drug)]] | 5 µM | 88,722 | +0.78 |  |
| C10 | [[Diphenhydramine (drug)]] | 5 µM | 58,886 | +0.19 |  |
| C11 | [[Harringtonine (drug)]] | 5 µM | 97,184 | +0.91 |  |
| C12 | [[Epirubicin (hydrochloride) (drug)]] | 5 µM | 61,072 | +0.24 |  |
| D1 | [[Phenytoin (sodium) (drug)]] | 5 µM | 58,311 | +0.18 |  |
| D2 | [[Orlistat (drug)]] | 5 µM | 70,988 | +0.46 |  |
| D3 | [[Sacubitril_Valsartan (drug)]] | 5 µM | 63,127 | +0.29 |  |
| D4 | [[Monocrotaline (drug)]] | 5 µM | 47,355 | -0.12 |  |
| D5 | [[Finasteride (drug)]] | 5 µM | 49,414 | -0.06 |  |
| D6 | [[Hydroxyurea (drug)]] | 5 µM | 57,998 | +0.17 |  |
| D7 | [[Doxycycline (monohydrate) (drug)]] | 5 µM | 40,328 | -0.36 |  |
| D8 | [[Pitavastatin (Calcium) (drug)]] | 5 µM | 29,065 | -0.83 |  |
| D9 | [[Cobimetinib (drug)]] | 5 µM | 34,160 | -0.60 |  |
| D10 | [[Simotinib (drug)]] | 5 µM | 23,846 | -1.11 | low cells |
| D11 | [[Procainamide (hydrochloride) (drug)]] | 5 µM | 45,596 | -0.18 |  |
| D12 | [[Silodosin (drug)]] | 5 µM | 33,062 | -0.64 |  |
| E1 | [[Nevirapine (drug)]] | 5 µM | 69,593 | +0.43 |  |
| E2 | [[Cilostazol (drug)]] | 5 µM | 66,145 | +0.36 |  |
| E3 | [[Dorzolamide (hydrochloride) (drug)]] | 5 µM | 60,280 | +0.22 |  |
| E4 | [[Roxadustat (drug)]] | 5 µM | 56,809 | +0.14 |  |
| E5 | [[Canagliflozin (drug)]] | 5 µM | 33,673 | -0.62 |  |
| E6 | [[Decitabine (drug)]] | 5 µM | 58,452 | +0.18 |  |
| E7 | [[Ligustrazine (drug)]] | 5 µM | 39,005 | -0.40 |  |
| E8 | [[Thymopentin (drug)]] | 5 µM | 46,070 | -0.16 |  |
| E9 | [[Verteporfin (drug)]] | 5 µM | 34,645 | -0.57 |  |
| E10 | [[Hesperidin (drug)]] | 5 µM | 40,242 | -0.36 |  |
| E11 | [[Mebendazole (drug)]] | 5 µM | 120,632 | +1.22 |  |
| E12 | [[Betamethasone dipropionate (drug)]] | 5 µM | 69,606 | +0.43 |  |
| F1 | [[Levobupivacaine (hydrochloride) (drug)]] | 5 µM | 52,452 | +0.02 |  |
| F2 | [[Rosiglitazone (drug)]] | 5 µM | 38,488 | -0.42 |  |
| F3 | [[Quinidine (15% dihydroquinidine) (drug)]] | 5 µM | 52,309 | +0.02 |  |
| F4 | [[Verapamil (drug)]] | 5 µM | 62,995 | +0.29 |  |
| F5 | [[Bisoprolol (hemifumarate) (drug)]] | 5 µM | 50,907 | -0.02 |  |
| F6 | [[Penfluridol (drug)]] | 5 µM | 32,686 | -0.66 |  |
| F7 | [[Ferulic acid (drug)]] | 5 µM | 43,476 | -0.25 |  |
| F8 | [[Pemetrexed (drug)]] | 5 µM | 27,636 | -0.90 |  |
| F9 | [[Fluvoxamine (drug)]] | 5 µM | 41,284 | -0.32 |  |
| F10 | [[Cytarabine (hydrochloride) (drug)]] | 5 µM | 50,596 | -0.03 |  |
| F11 | [[Bendamustine (drug)]] | 5 µM | 34,758 | -0.57 |  |
| F12 | [[Altretamine (drug)]] | 5 µM | 54,614 | +0.08 |  |
| G1 | [[Rifaximin (drug)]] | 5 µM | 48,115 | -0.10 |  |
| G2 | [[Dexmedetomidine (drug)]] | 5 µM | 56,654 | +0.13 |  |
| G3 | [[Doxorubicin (hydrochloride) (drug)]] | 5 µM | 32,841 | -0.65 |  |
| G4 | [[Menadione (drug)]] | 5 µM | 35,638 | -0.53 |  |
| G5 | [[Glycyrrhizic acid (drug)]] | 5 µM | 56,139 | +0.12 |  |
| G6 | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] | 5 µM | 48,626 | -0.09 |  |
| G7 | [[Imiquimod (maleate) (drug)]] | 5 µM | 29,795 | -0.79 |  |
| G8 | [[Clofarabine (drug)]] | 5 µM | 36,062 | -0.52 |  |
| G9 | [[Mozavaptan (drug)]] | 5 µM | 39,677 | -0.38 |  |
| G10 | [[Adagrasib (drug)]] | 5 µM | 74,207 | +0.52 |  |
| G11 | [[Sulfatinib (drug)]] | 5 µM | 70,023 | +0.44 |  |
| G12 | [[Arbutin (drug)]] | 5 µM | 58,126 | +0.17 |  |
| H1 | [[Docetaxel (Trihydrate) (drug)]] | 5 µM | 52,420 | +0.02 |  |
| H2 | [[Tranilast (drug)]] | 5 µM | 67,639 | +0.39 |  |
| H3 | [[Macitentan (drug)]] | 5 µM | 36,717 | -0.49 |  |
| H4 | [[Eplerenone (drug)]] | 5 µM | 65,707 | +0.35 |  |
| H5 | [[Mifepristone (drug)]] | 5 µM | 54,390 | +0.08 |  |
| H6 | [[Apalutamide (drug)]] | 5 µM | 45,847 | -0.17 |  |
| H7 | [[Niclosamide (olamine) (drug)]] | 5 µM | 22,470 | -1.20 | low cells |
| H8 | [[Peretinoin (drug)]] | 5 µM | 40,523 | -0.35 |  |
| H9 | [[Tolmetin (drug)]] | 5 µM | 50,821 | -0.02 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 46,021 | -0.17 | ⚠ position not correctable |
| H11 | DMSO | — | 66,763 | +0.37 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 51,081 | -0.01 | ⚠ position not correctable · DMSO |
