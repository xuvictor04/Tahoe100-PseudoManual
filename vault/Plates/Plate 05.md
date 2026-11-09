---
plate: "plate5"
type: "plate"
number: 5
dose: "0.05 / 0.5"
unreliable: false
plate_factor: 1.0
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 05

`plate5` · dose 0.05 / 0.5 µM · 96 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 57,868. Source: `tables/plates.parquet`, `tables/wells.parquet`.

## Layout

*Drug in each well (names cut to 10 characters; the table below has them in full). The per-gene plates notes use the same 8 × 12 layout.*

| |1|2|3|4|5|6|7|8|9|10|11|12|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|A|8-Hydroxyq|Chlorhexid|Trifluridi|Berbamine|Retinoic a|Cysteamine|Vinblastin|Pasireotid|Riluzole h|Palmatine|Isocorydin|Raltitrexe|
|B|Furosemide|Clotrimazo|Sodium Sal|Gallic aci|(R)-Verapa|Pyridoxine|Acetohexam|Temsirolim|Megestrol|Diammonium|L-Thyroxin|Ropivacain|
|C|Salicylic|Quinestrol|Tofacitini|Trimetrexa|Gemfibrozi|18β-Glycyr|Tolcapone|Terfenadin|Aliskiren|Fluvoxamin|S-Adenosyl|Idarubicin|
|D|Elagolix s|Resveratro|Rapamycin|Saquinavir|Tofacitini|Thymol|Almonertin|Darinapars|Vilanterol|Lenalidomi|Azithromyc|Ritonavir|
|E|Pentamidin|Adenosine|Sulfisoxaz|Norepineph|Ciclopirox|Lidocaine|Demeclocyc|Mitoxantro|Larotrecti|Busulfan|Cepharanth|Radotinib|
|F|Docetaxel|Triclosan|Tucidinost|Bergenin|Allantoin|Bimatopros|Triamcinol|Olanzapine|Rimonabant|Pentagastr|Lumatepero|Relugolix|
|G|Homoharrin|Hexylresor|Baicalin|Berberine|Medroxypro|Neratinib|Sinomenine|Goserelin|Fusidic ac|Balsalazid|Cloxacilli|Artesunate|
|H|Pyridoxine|Folic acid|Selinexor|Adenine|Gallic aci|Lipoic aci|Amsacrine|Anethole t|Clonidine|Adagrasib|**DMSO**|**DMSO**|

## Wells

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 3 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[8-Hydroxyquinoline (drug)]] | 0.5 µM | 68,297 | +0.24 |  |
| A2 | [[Chlorhexidine (diacetate) (drug)]] | 0.5 µM | 81,466 | +0.49 |  |
| A3 | [[Trifluridine (drug)]] | 0.5 µM | 57,510 | -0.01 |  |
| A4 | [[Berbamine (drug)]] | 0.5 µM | 72,170 | +0.32 |  |
| A5 | [[Retinoic acid (drug)]] | 0.5 µM | 56,102 | -0.04 |  |
| A6 | [[Cysteamine (hydrochloride) (drug)]] | 0.5 µM | 35,212 | -0.72 |  |
| A7 | [[Vinblastine (sulfate) (drug)]] | 0.5 µM | 31,322 | -0.88 |  |
| A8 | [[Pasireotide (acetate) (drug)]] | 0.5 µM | 58,439 | +0.02 |  |
| A9 | [[Riluzole hydrochloride (drug)]] | 0.5 µM | 47,552 | -0.28 |  |
| A10 | [[Palmatine (chloride) (drug)]] | 0.5 µM | 32,808 | -0.82 |  |
| A11 | [[Isocorydine (drug)]] | 0.5 µM | 35,490 | -0.70 |  |
| A12 | [[Raltitrexed (drug)]] | 0.5 µM | 34,861 | -0.73 |  |
| B1 | [[Furosemide (drug)]] | 0.5 µM | 49,243 | -0.23 |  |
| B2 | [[Clotrimazole (drug)]] | 0.5 µM | 42,329 | -0.45 |  |
| B3 | [[Sodium Salicylate (drug)]] | 0.5 µM | 52,389 | -0.14 |  |
| B4 | [[Gallic acid (hydrate) (drug)]] | 0.5 µM | 46,141 | -0.33 |  |
| B5 | [[(R)-Verapamil (hydrochloride) (drug)]] | 0.5 µM | 50,208 | -0.20 |  |
| B6 | [[Pyridoxine (drug)]] | 0.5 µM | 27,431 | -1.08 | low cells |
| B7 | [[Acetohexamide (drug)]] | 0.5 µM | 48,706 | -0.25 |  |
| B8 | [[Temsirolimus (drug)]] | 0.5 µM | 29,402 | -0.98 |  |
| B9 | [[Megestrol (drug)]] | 0.5 µM | 46,603 | -0.31 |  |
| B10 | [[Diammonium Glycyrrhizinate (drug)]] | 0.5 µM | 57,846 | +0.00 |  |
| B11 | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] | 0.5 µM | 37,316 | -0.63 |  |
| B12 | [[Ropivacaine (hydrochloride monohydrate) (drug)]] | 0.5 µM | 30,695 | -0.91 |  |
| C1 | [[Salicylic acid (drug)]] | 0.5 µM | 85,189 | +0.56 |  |
| C2 | [[Quinestrol (drug)]] | 0.5 µM | 93,802 | +0.70 |  |
| C3 | [[Tofacitinib (drug)]] | 0.5 µM | 59,718 | +0.05 |  |
| C4 | [[Trimetrexate (drug)]] | 0.5 µM | 63,404 | +0.13 |  |
| C5 | [[Gemfibrozil (drug)]] | 0.5 µM | 70,447 | +0.28 |  |
| C6 | [[18β-Glycyrrhetinic acid (drug)]] | 0.5 µM | 39,678 | -0.54 |  |
| C7 | [[Tolcapone (drug)]] | 0.5 µM | 90,169 | +0.64 |  |
| C8 | [[Terfenadine (drug)]] | 0.5 µM | 59,658 | +0.05 |  |
| C9 | [[Aliskiren (drug)]] | 0.5 µM | 64,100 | +0.15 |  |
| C10 | [[Fluvoxamine (maleate) (drug)]] | 0.5 µM | 41,258 | -0.49 |  |
| C11 | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] | 0.5 µM | 90,753 | +0.65 |  |
| C12 | [[Idarubicin (hydrochloride) (drug)]] | 0.5 µM | 66,986 | +0.21 |  |
| D1 | [[Elagolix sodium (drug)]] | 0.5 µM | 45,253 | -0.35 |  |
| D2 | [[Resveratrol (drug)]] | 0.5 µM | 55,189 | -0.07 |  |
| D3 | [[Rapamycin (drug)]] | 0.5 µM | 43,519 | -0.41 |  |
| D4 | [[Saquinavir (drug)]] | 0.5 µM | 39,658 | -0.54 |  |
| D5 | [[Tofacitinib (citrate) (drug)]] | 0.5 µM | 45,863 | -0.33 |  |
| D6 | [[Thymol (drug)]] | 0.5 µM | 32,019 | -0.85 |  |
| D7 | [[Almonertinib (hydrochloride) (drug)]] | 0.5 µM | 52,280 | -0.15 |  |
| D8 | [[Darinaparsin (drug)]] | 0.5 µM | 64,926 | +0.17 |  |
| D9 | [[Vilanterol (drug)]] | 0.5 µM | 43,156 | -0.42 |  |
| D10 | [[Lenalidomide (hemihydrate) (drug)]] | 0.5 µM | 40,495 | -0.51 |  |
| D11 | [[Azithromycin (hydrate) (drug)]] | 0.5 µM | 44,141 | -0.39 |  |
| D12 | [[Ritonavir (drug)]] | 0.5 µM | 44,021 | -0.39 |  |
| E1 | [[Pentamidine (isethionate) (drug)]] | 0.5 µM | 84,972 | +0.56 |  |
| E2 | [[Adenosine (drug)]] | 0.5 µM | 89,477 | +0.63 |  |
| E3 | [[Sulfisoxazole (drug)]] | 0.5 µM | 61,039 | +0.08 |  |
| E4 | [[Norepinephrine (hydrochloride) (drug)]] | 0.5 µM | 95,488 | +0.72 |  |
| E5 | [[Ciclopirox (drug)]] | 0.5 µM | 78,751 | +0.45 |  |
| E6 | [[Lidocaine (hydrochloride) (drug)]] | 0.5 µM | 40,342 | -0.52 |  |
| E7 | [[Demeclocycline (drug)]] | 0.5 µM | 75,842 | +0.39 |  |
| E8 | [[Mitoxantrone (dihydrochloride) (drug)]] | 0.5 µM | 50,811 | -0.19 |  |
| E9 | [[Larotrectinib (drug)]] | 0.5 µM | 52,615 | -0.14 |  |
| E10 | [[Busulfan (drug)]] | 0.5 µM | 62,486 | +0.11 |  |
| E11 | [[Cepharanthine (drug)]] | 0.5 µM | 41,345 | -0.48 |  |
| E12 | [[Radotinib (drug)]] | 0.5 µM | 31,957 | -0.86 |  |
| F1 | [[Docetaxel (drug)]] | 0.5 µM | 70,321 | +0.28 |  |
| F2 | [[Triclosan (drug)]] | 0.5 µM | 63,759 | +0.14 |  |
| F3 | [[Tucidinostat (drug)]] | 0.5 µM | 56,089 | -0.04 |  |
| F4 | [[Bergenin (drug)]] | 0.5 µM | 46,787 | -0.31 |  |
| F5 | [[Allantoin (drug)]] | 0.5 µM | 55,444 | -0.06 |  |
| F6 | [[Bimatoprost (drug)]] | 0.5 µM | 42,162 | -0.46 |  |
| F7 | [[Triamcinolone (drug)]] | 0.5 µM | 57,795 | -0.00 |  |
| F8 | [[Olanzapine (drug)]] | 0.5 µM | 75,976 | +0.39 |  |
| F9 | [[Rimonabant (drug)]] | 0.5 µM | 77,934 | +0.43 |  |
| F10 | [[Pentagastrin (drug)]] | 0.5 µM | 43,137 | -0.42 |  |
| F11 | [[Lumateperone (tosylate) (drug)]] | 0.5 µM | 70,769 | +0.29 |  |
| F12 | [[Relugolix (drug)]] | 0.5 µM | 91,897 | +0.67 |  |
| G1 | [[Homoharringtonine (drug)]] | 0.5 µM | 45,276 | -0.35 |  |
| G2 | [[Hexylresorcinol (drug)]] | 0.5 µM | 68,000 | +0.23 |  |
| G3 | [[Baicalin (drug)]] | 0.5 µM | 60,542 | +0.07 |  |
| G4 | [[Berberine (chloride hydrate) (drug)]] | 0.5 µM | 57,889 | +0.00 |  |
| G5 | [[Medroxyprogesterone acetate (drug)]] | 0.5 µM | 39,341 | -0.56 |  |
| G6 | [[Neratinib (maleate) (drug)]] | 0.5 µM | 46,111 | -0.33 |  |
| G7 | [[Sinomenine (drug)]] | 0.5 µM | 83,249 | +0.53 |  |
| G8 | [[Goserelin (acetate) (drug)]] | 0.5 µM | 83,098 | +0.52 |  |
| G9 | [[Fusidic acid (drug)]] | 0.5 µM | 63,883 | +0.14 |  |
| G10 | [[Balsalazide (sodium hydrate) (drug)]] | 0.5 µM | 79,722 | +0.46 |  |
| G11 | [[Cloxacillin (sodium) (drug)]] | 0.5 µM | 84,329 | +0.54 |  |
| G12 | [[Artesunate (drug)]] | 0.5 µM | 102,059 | +0.82 |  |
| H1 | [[Pyridoxine (hydrochloride) (drug)]] | 0.5 µM | 109,707 | +0.92 |  |
| H2 | [[Folic acid (drug)]] | 0.5 µM | 107,494 | +0.89 |  |
| H3 | [[Selinexor (drug)]] | 0.5 µM | 53,549 | -0.11 |  |
| H4 | [[Adenine (drug)]] | 0.5 µM | 62,758 | +0.12 |  |
| H5 | [[Gallic acid (drug)]] | 0.5 µM | 109,234 | +0.92 |  |
| H6 | [[Lipoic acid (drug)]] | 0.5 µM | 87,314 | +0.59 |  |
| H7 | [[Amsacrine (drug)]] | 0.5 µM | 90,454 | +0.65 |  |
| H8 | [[Anethole trithione (drug)]] | 0.5 µM | 99,378 | +0.78 |  |
| H9 | [[Clonidine (hydrochloride) (drug)]] | 0.5 µM | 89,291 | +0.63 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 81,111 | +0.49 | ⚠ position not correctable |
| H11 | DMSO | — | 80,088 | +0.47 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 102,179 | +0.82 | ⚠ position not correctable · DMSO |
