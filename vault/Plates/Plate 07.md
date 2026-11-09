---
plate: "plate7"
type: "plate"
number: 7
dose: "0.05"
unreliable: false
plate_factor: 1.081
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 07

`plate7` · dose 0.05 µM · 96 wells analysed · plate factor 1.08 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 52,146. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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
| A1 | [[Sivelestat (sodium tetrahydrate) (drug)]] | 0.05 µM | 75,084 | +0.52 |  |
| A2 | [[Posaconazole (drug)]] | 0.05 µM | 54,236 | +0.05 |  |
| A3 | [[Tetracycline (hydrochloride) (drug)]] | 0.05 µM | 64,234 | +0.30 |  |
| A4 | [[Entecavir (monohydrate) (drug)]] | 0.05 µM | 48,891 | -0.10 |  |
| A5 | [[Sildenafil (drug)]] | 0.05 µM | 54,627 | +0.06 |  |
| A6 | [[Dimethyl fumarate (drug)]] | 0.05 µM | 49,549 | -0.08 |  |
| A7 | [[Berbamine (dihydrochloride) (drug)]] | 0.05 µM | 52,029 | -0.01 |  |
| A8 | [[Daidzin (drug)]] | 0.05 µM | 56,596 | +0.11 |  |
| A9 | [[Fumaric acid (drug)]] | 0.05 µM | 53,966 | +0.05 |  |
| A10 | [[Pravastatin (sodium) (drug)]] | 0.05 µM | 46,061 | -0.18 |  |
| A11 | [[Almonertinib (mesylate) (drug)]] | 0.05 µM | 44,750 | -0.22 |  |
| A12 | [[Irinotecan (hydrochloride) (drug)]] | 0.05 µM | 39,190 | -0.42 |  |
| B1 | [[Rucaparib (phosphate) (drug)]] | 0.05 µM | 69,160 | +0.40 |  |
| B2 | [[crizotinib (drug)]] | 0.05 µM | 45,903 | -0.19 |  |
| B3 | [[Dinaciclib (drug)]] | 0.05 µM | 11,889 | -2.14 | low cells |
| B4 | [[Bosentan (hydrate) (drug)]] | 0.05 µM | 43,946 | -0.25 |  |
| B5 | [[Bestatin (drug)]] | 0.05 µM | 43,271 | -0.27 |  |
| B6 | [[Tadalafil (drug)]] | 0.05 µM | 45,389 | -0.20 |  |
| B7 | [[Belumosudil (drug)]] | 0.05 µM | 62,999 | +0.27 |  |
| B8 | [[Flumatinib (mesylate) (drug)]] | 0.05 µM | 55,099 | +0.08 |  |
| B9 | [[Cytarabine (drug)]] | 0.05 µM | 68,901 | +0.40 |  |
| B10 | [[Afatinib (drug)]] | 0.05 µM | 52,521 | +0.01 |  |
| B11 | [[Topotecan (hydrochloride) (drug)]] | 0.05 µM | 26,934 | -0.96 |  |
| B12 | [[Naproxen (drug)]] | 0.05 µM | 31,254 | -0.74 |  |
| C1 | [[Lucanthone (drug)]] | 0.05 µM | 121,831 | +1.22 |  |
| C2 | [[Trametinib (DMSO_TF solvate) (drug)]] | 0.05 µM | 97,771 | +0.90 |  |
| C3 | [[Benproperine (phosphate) (drug)]] | 0.05 µM | 66,548 | +0.35 |  |
| C4 | [[Erlotinib (drug)]] | 0.05 µM | 82,538 | +0.66 |  |
| C5 | [[Fenofibrate (drug)]] | 0.05 µM | 92,055 | +0.82 |  |
| C6 | [[(S)-Crizotinib (drug)]] | 0.05 µM | 98,917 | +0.92 |  |
| C7 | [[Rutin (trihydrate) (drug)]] | 0.05 µM | 102,552 | +0.97 |  |
| C8 | [[Pexidartinib (hydrochloride) (drug)]] | 0.05 µM | 67,501 | +0.37 |  |
| C9 | [[Tirabrutinib (drug)]] | 0.05 µM | 80,587 | +0.62 |  |
| C10 | [[Diphenhydramine (drug)]] | 0.05 µM | 75,500 | +0.53 |  |
| C11 | [[Harringtonine (drug)]] | 0.05 µM | 25,754 | -1.02 | low cells |
| C12 | [[Epirubicin (hydrochloride) (drug)]] | 0.05 µM | 21,284 | -1.30 | low cells |
| D1 | [[Phenytoin (sodium) (drug)]] | 0.05 µM | 47,854 | -0.13 |  |
| D2 | [[Orlistat (drug)]] | 0.05 µM | 29,609 | -0.82 |  |
| D3 | [[Sacubitril_Valsartan (drug)]] | 0.05 µM | 55,169 | +0.08 |  |
| D4 | [[Monocrotaline (drug)]] | 0.05 µM | 36,946 | -0.50 |  |
| D5 | [[Finasteride (drug)]] | 0.05 µM | 41,915 | -0.32 |  |
| D6 | [[Hydroxyurea (drug)]] | 0.05 µM | 29,043 | -0.85 |  |
| D7 | [[Doxycycline (monohydrate) (drug)]] | 0.05 µM | 42,682 | -0.29 |  |
| D8 | [[Pitavastatin (Calcium) (drug)]] | 0.05 µM | 38,584 | -0.44 |  |
| D9 | [[Cobimetinib (drug)]] | 0.05 µM | 35,390 | -0.56 |  |
| D10 | [[Simotinib (drug)]] | 0.05 µM | 47,610 | -0.14 |  |
| D11 | [[Procainamide (hydrochloride) (drug)]] | 0.05 µM | 42,247 | -0.31 |  |
| D12 | [[Silodosin (drug)]] | 0.05 µM | 48,688 | -0.10 |  |
| E1 | [[Nevirapine (drug)]] | 0.05 µM | 46,437 | -0.17 |  |
| E2 | [[Cilostazol (drug)]] | 0.05 µM | 53,082 | +0.02 |  |
| E3 | [[Dorzolamide (hydrochloride) (drug)]] | 0.05 µM | 44,030 | -0.25 |  |
| E4 | [[Roxadustat (drug)]] | 0.05 µM | 37,424 | -0.48 |  |
| E5 | [[Canagliflozin (drug)]] | 0.05 µM | 34,609 | -0.60 |  |
| E6 | [[Decitabine (drug)]] | 0.05 µM | 43,262 | -0.27 |  |
| E7 | [[Ligustrazine (drug)]] | 0.05 µM | 57,628 | +0.14 |  |
| E8 | [[Thymopentin (drug)]] | 0.05 µM | 55,924 | +0.10 |  |
| E9 | [[Verteporfin (drug)]] | 0.05 µM | 54,889 | +0.07 |  |
| E10 | [[Hesperidin (drug)]] | 0.05 µM | 71,978 | +0.46 |  |
| E11 | [[Mebendazole (drug)]] | 0.05 µM | 58,415 | +0.16 |  |
| E12 | [[Betamethasone dipropionate (drug)]] | 0.05 µM | 35,650 | -0.55 |  |
| F1 | [[Levobupivacaine (hydrochloride) (drug)]] | 0.05 µM | 69,015 | +0.40 |  |
| F2 | [[Rosiglitazone (drug)]] | 0.05 µM | 71,711 | +0.46 |  |
| F3 | [[Quinidine (15% dihydroquinidine) (drug)]] | 0.05 µM | 75,332 | +0.53 |  |
| F4 | [[Verapamil (drug)]] | 0.05 µM | 71,113 | +0.44 |  |
| F5 | [[Bisoprolol (hemifumarate) (drug)]] | 0.05 µM | 52,312 | +0.00 |  |
| F6 | [[Penfluridol (drug)]] | 0.05 µM | 50,920 | -0.04 |  |
| F7 | [[Ferulic acid (drug)]] | 0.05 µM | 57,165 | +0.13 |  |
| F8 | [[Pemetrexed (drug)]] | 0.05 µM | 59,177 | +0.18 |  |
| F9 | [[Fluvoxamine (drug)]] | 0.05 µM | 68,873 | +0.40 |  |
| F10 | [[Cytarabine (hydrochloride) (drug)]] | 0.05 µM | 73,849 | +0.50 |  |
| F11 | [[Bendamustine (drug)]] | 0.05 µM | 49,881 | -0.07 |  |
| F12 | [[Altretamine (drug)]] | 0.05 µM | 47,564 | -0.14 |  |
| G1 | [[Rifaximin (drug)]] | 0.05 µM | 58,768 | +0.17 |  |
| G2 | [[Dexmedetomidine (drug)]] | 0.05 µM | 58,446 | +0.16 |  |
| G3 | [[Doxorubicin (hydrochloride) (drug)]] | 0.05 µM | 57,843 | +0.15 |  |
| G4 | [[Menadione (drug)]] | 0.05 µM | 34,863 | -0.58 |  |
| G5 | [[Glycyrrhizic acid (drug)]] | 0.05 µM | 33,004 | -0.66 |  |
| G6 | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] | 0.05 µM | 30,899 | -0.76 |  |
| G7 | [[Imiquimod (maleate) (drug)]] | 0.05 µM | 38,214 | -0.45 |  |
| G8 | [[Clofarabine (drug)]] | 0.05 µM | 45,661 | -0.20 |  |
| G9 | [[Mozavaptan (drug)]] | 0.05 µM | 42,713 | -0.29 |  |
| G10 | [[Adagrasib (drug)]] | 0.05 µM | 57,267 | +0.13 |  |
| G11 | [[Sulfatinib (drug)]] | 0.05 µM | 47,179 | -0.15 |  |
| G12 | [[Arbutin (drug)]] | 0.05 µM | 47,430 | -0.14 |  |
| H1 | [[Docetaxel (Trihydrate) (drug)]] | 0.05 µM | 42,025 | -0.32 |  |
| H2 | [[Tranilast (drug)]] | 0.05 µM | 52,264 | -0.00 |  |
| H3 | [[Macitentan (drug)]] | 0.05 µM | 69,020 | +0.40 |  |
| H4 | [[Eplerenone (drug)]] | 0.05 µM | 64,647 | +0.31 |  |
| H5 | [[Mifepristone (drug)]] | 0.05 µM | 45,420 | -0.20 |  |
| H6 | [[Apalutamide (drug)]] | 0.05 µM | 48,784 | -0.10 |  |
| H7 | [[Niclosamide (olamine) (drug)]] | 0.05 µM | 82,954 | +0.67 |  |
| H8 | [[Peretinoin (drug)]] | 0.05 µM | 73,710 | +0.50 |  |
| H9 | [[Tolmetin (drug)]] | 0.05 µM | 78,998 | +0.60 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 64,332 | +0.30 | ⚠ position not correctable |
| H11 | DMSO | — | 37,355 | -0.49 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 50,678 | -0.05 | ⚠ position not correctable · DMSO |
