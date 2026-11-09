---
plate: "plate4"
type: "plate"
number: 4
dose: "0.05"
unreliable: false
plate_factor: 1.0
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 04

`plate4` · dose 0.05 µM · 96 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 67,310. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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
| A1 | [[8-Hydroxyquinoline (drug)]] | 0.05 µM | 62,137 | -0.11 |  |
| A2 | [[Chlorhexidine (diacetate) (drug)]] | 0.05 µM | 73,128 | +0.12 |  |
| A3 | [[Trifluridine (drug)]] | 0.05 µM | 74,628 | +0.15 |  |
| A4 | [[Berbamine (drug)]] | 0.05 µM | 85,533 | +0.35 |  |
| A5 | [[Retinoic acid (drug)]] | 0.05 µM | 78,552 | +0.23 |  |
| A6 | [[Cysteamine (hydrochloride) (drug)]] | 0.05 µM | 66,536 | -0.01 |  |
| A7 | [[Vinblastine (sulfate) (drug)]] | 0.05 µM | 83,826 | +0.32 |  |
| A8 | [[Pasireotide (acetate) (drug)]] | 0.05 µM | 77,851 | +0.21 |  |
| A9 | [[Riluzole hydrochloride (drug)]] | 0.05 µM | 79,204 | +0.24 |  |
| A10 | [[Palmatine (chloride) (drug)]] | 0.05 µM | 96,406 | +0.52 |  |
| A11 | [[Isocorydine (drug)]] | 0.05 µM | 80,710 | +0.27 |  |
| A12 | [[Raltitrexed (drug)]] | 0.05 µM | 66,987 | -0.00 |  |
| B1 | [[Furosemide (drug)]] | 0.05 µM | 55,347 | -0.28 |  |
| B2 | [[Clotrimazole (drug)]] | 0.05 µM | 64,079 | -0.07 |  |
| B3 | [[Sodium Salicylate (drug)]] | 0.05 µM | 65,930 | -0.03 |  |
| B4 | [[Gallic acid (hydrate) (drug)]] | 0.05 µM | 67,398 | +0.01 |  |
| B5 | [[(R)-Verapamil (hydrochloride) (drug)]] | 0.05 µM | 84,838 | +0.34 |  |
| B6 | [[Pyridoxine (drug)]] | 0.05 µM | 70,237 | +0.07 |  |
| B7 | [[Acetohexamide (drug)]] | 0.05 µM | 61,164 | -0.13 |  |
| B8 | [[Temsirolimus (drug)]] | 0.05 µM | 80,915 | +0.27 |  |
| B9 | [[Megestrol (drug)]] | 0.05 µM | 70,009 | +0.06 |  |
| B10 | [[Diammonium Glycyrrhizinate (drug)]] | 0.05 µM | 69,231 | +0.04 |  |
| B11 | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] | 0.05 µM | 56,833 | -0.24 |  |
| B12 | [[Ropivacaine (hydrochloride monohydrate) (drug)]] | 0.05 µM | 65,450 | -0.04 |  |
| C1 | [[Salicylic acid (drug)]] | 0.05 µM | 77,115 | +0.20 |  |
| C2 | [[Quinestrol (drug)]] | 0.05 µM | 105,594 | +0.65 |  |
| C3 | [[Tofacitinib (drug)]] | 0.05 µM | 55,409 | -0.28 |  |
| C4 | [[Trimetrexate (drug)]] | 0.05 µM | 58,015 | -0.21 |  |
| C5 | [[Gemfibrozil (drug)]] | 0.05 µM | 60,227 | -0.16 |  |
| C6 | [[18β-Glycyrrhetinic acid (drug)]] | 0.05 µM | 54,105 | -0.31 |  |
| C7 | [[Tolcapone (drug)]] | 0.05 µM | 81,564 | +0.28 |  |
| C8 | [[Terfenadine (drug)]] | 0.05 µM | 87,982 | +0.39 |  |
| C9 | [[Aliskiren (drug)]] | 0.05 µM | 94,030 | +0.49 |  |
| C10 | [[Fluvoxamine (maleate) (drug)]] | 0.05 µM | 56,103 | -0.26 |  |
| C11 | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] | 0.05 µM | 66,489 | -0.01 |  |
| C12 | [[Idarubicin (hydrochloride) (drug)]] | 0.05 µM | 69,390 | +0.05 |  |
| D1 | [[Elagolix sodium (drug)]] | 0.05 µM | 64,893 | -0.05 |  |
| D2 | [[Resveratrol (drug)]] | 0.05 µM | 45,895 | -0.55 |  |
| D3 | [[Rapamycin (drug)]] | 0.05 µM | 59,853 | -0.16 |  |
| D4 | [[Saquinavir (drug)]] | 0.05 µM | 41,343 | -0.70 |  |
| D5 | [[Tofacitinib (citrate) (drug)]] | 0.05 µM | 56,339 | -0.25 |  |
| D6 | [[Thymol (drug)]] | 0.05 µM | 39,892 | -0.75 |  |
| D7 | [[Almonertinib (hydrochloride) (drug)]] | 0.05 µM | 52,412 | -0.36 |  |
| D8 | [[Darinaparsin (drug)]] | 0.05 µM | 54,578 | -0.30 |  |
| D9 | [[Vilanterol (drug)]] | 0.05 µM | 36,307 | -0.89 |  |
| D10 | [[Lenalidomide (hemihydrate) (drug)]] | 0.05 µM | 48,796 | -0.46 |  |
| D11 | [[Azithromycin (hydrate) (drug)]] | 0.05 µM | 60,858 | -0.14 |  |
| D12 | [[Ritonavir (drug)]] | 0.05 µM | 66,677 | -0.01 |  |
| E1 | [[Pentamidine (isethionate) (drug)]] | 0.05 µM | 56,337 | -0.25 |  |
| E2 | [[Adenosine (drug)]] | 0.05 µM | 59,102 | -0.18 |  |
| E3 | [[Sulfisoxazole (drug)]] | 0.05 µM | 63,035 | -0.09 |  |
| E4 | [[Norepinephrine (hydrochloride) (drug)]] | 0.05 µM | 62,326 | -0.11 |  |
| E5 | [[Ciclopirox (drug)]] | 0.05 µM | 60,491 | -0.15 |  |
| E6 | [[Lidocaine (hydrochloride) (drug)]] | 0.05 µM | 19,068 | -1.82 | low cells |
| E7 | [[Demeclocycline (drug)]] | 0.05 µM | 63,535 | -0.08 |  |
| E8 | [[Mitoxantrone (dihydrochloride) (drug)]] | 0.05 µM | 42,020 | -0.68 |  |
| E9 | [[Larotrectinib (drug)]] | 0.05 µM | 83,091 | +0.31 |  |
| E10 | [[Busulfan (drug)]] | 0.05 µM | 67,223 | +0.00 |  |
| E11 | [[Cepharanthine (drug)]] | 0.05 µM | 78,986 | +0.24 |  |
| E12 | [[Radotinib (drug)]] | 0.05 µM | 79,740 | +0.25 |  |
| F1 | [[Docetaxel (drug)]] | 0.05 µM | 21,018 | -1.67 | low cells |
| F2 | [[Triclosan (drug)]] | 0.05 µM | 65,040 | -0.05 |  |
| F3 | [[Tucidinostat (drug)]] | 0.05 µM | 77,894 | +0.22 |  |
| F4 | [[Bergenin (drug)]] | 0.05 µM | 82,189 | +0.29 |  |
| F5 | [[Allantoin (drug)]] | 0.05 µM | 52,242 | -0.36 |  |
| F6 | [[Bimatoprost (drug)]] | 0.05 µM | 66,774 | -0.01 |  |
| F7 | [[Triamcinolone (drug)]] | 0.05 µM | 66,250 | -0.02 |  |
| F8 | [[Olanzapine (drug)]] | 0.05 µM | 82,617 | +0.30 |  |
| F9 | [[Rimonabant (drug)]] | 0.05 µM | 89,711 | +0.42 |  |
| F10 | [[Pentagastrin (drug)]] | 0.05 µM | 48,152 | -0.48 |  |
| F11 | [[Lumateperone (tosylate) (drug)]] | 0.05 µM | 82,869 | +0.30 |  |
| F12 | [[Relugolix (drug)]] | 0.05 µM | 64,247 | -0.06 |  |
| G1 | [[Homoharringtonine (drug)]] | 0.05 µM | 68,475 | +0.03 |  |
| G2 | [[Hexylresorcinol (drug)]] | 0.05 µM | 77,476 | +0.21 |  |
| G3 | [[Baicalin (drug)]] | 0.05 µM | 76,590 | +0.19 |  |
| G4 | [[Berberine (chloride hydrate) (drug)]] | 0.05 µM | 63,379 | -0.08 |  |
| G5 | [[Medroxyprogesterone acetate (drug)]] | 0.05 µM | 64,692 | -0.05 |  |
| G6 | [[Neratinib (maleate) (drug)]] | 0.05 µM | 85,155 | +0.34 |  |
| G7 | [[Sinomenine (drug)]] | 0.05 µM | 50,207 | -0.42 |  |
| G8 | [[Goserelin (acetate) (drug)]] | 0.05 µM | 98,457 | +0.55 |  |
| G9 | [[Fusidic acid (drug)]] | 0.05 µM | 101,813 | +0.60 |  |
| G10 | [[Balsalazide (sodium hydrate) (drug)]] | 0.05 µM | 63,110 | -0.09 |  |
| G11 | [[Cloxacillin (sodium) (drug)]] | 0.05 µM | 82,897 | +0.30 |  |
| G12 | [[Artesunate (drug)]] | 0.05 µM | 87,419 | +0.38 |  |
| H1 | [[Pyridoxine (hydrochloride) (drug)]] | 0.05 µM | 74,764 | +0.16 |  |
| H2 | [[Folic acid (drug)]] | 0.05 µM | 76,264 | +0.18 |  |
| H3 | [[Selinexor (drug)]] | 0.05 µM | 104,901 | +0.64 |  |
| H4 | [[Adenine (drug)]] | 0.05 µM | 83,343 | +0.31 |  |
| H5 | [[Gallic acid (drug)]] | 0.05 µM | 42,675 | -0.65 |  |
| H6 | [[Lipoic acid (drug)]] | 0.05 µM | 83,876 | +0.32 |  |
| H7 | [[Amsacrine (drug)]] | 0.05 µM | 75,563 | +0.17 |  |
| H8 | [[Anethole trithione (drug)]] | 0.05 µM | 89,886 | +0.42 |  |
| H9 | [[Clonidine (hydrochloride) (drug)]] | 0.05 µM | 106,687 | +0.67 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 101,815 | +0.60 | ⚠ position not correctable |
| H11 | DMSO | — | 73,119 | +0.12 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 82,569 | +0.30 | ⚠ position not correctable · DMSO |
