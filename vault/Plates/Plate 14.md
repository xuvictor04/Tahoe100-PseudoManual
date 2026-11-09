---
plate: "plate14"
type: "plate"
number: 14
dose: "0.05 / 5"
unreliable: false
plate_factor: 1.0
n_wells: 95
dmso_wells: "H11, H12"
failed_wells: ["B11"]
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 14

`plate14` · dose 0.05 / 5 µM · 95 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): B11. Median cells per analysed well: 65,561. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 4 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[8-Hydroxyquinoline (drug)]] | 5 µM | 53,751 | -0.29 |  |
| A2 | [[Chlorhexidine (diacetate) (drug)]] | 5 µM | 76,471 | +0.22 |  |
| A3 | [[Trifluridine (drug)]] | 5 µM | 54,348 | -0.27 |  |
| A4 | [[Berbamine (drug)]] | 5 µM | 62,165 | -0.08 |  |
| A5 | [[Retinoic acid (drug)]] | 5 µM | 77,739 | +0.24 |  |
| A6 | [[Cysteamine (hydrochloride) (drug)]] | 5 µM | 68,361 | +0.06 |  |
| A7 | [[Vinblastine (sulfate) (drug)]] | 5 µM | 71,298 | +0.12 |  |
| A8 | [[Pasireotide (acetate) (drug)]] | 5 µM | 66,739 | +0.02 |  |
| A9 | [[Riluzole hydrochloride (drug)]] | 5 µM | 89,702 | +0.45 |  |
| A10 | [[Palmatine (chloride) (drug)]] | 5 µM | 71,901 | +0.13 |  |
| A11 | [[Isocorydine (drug)]] | 5 µM | 62,332 | -0.08 |  |
| A12 | [[Raltitrexed (drug)]] | 5 µM | 55,704 | -0.24 |  |
| B1 | [[Furosemide (drug)]] | 5 µM | 79,515 | +0.27 |  |
| B2 | [[Clotrimazole (drug)]] | 5 µM | 80,420 | +0.29 |  |
| B3 | [[Sodium Salicylate (drug)]] | 5 µM | 103,318 | +0.65 |  |
| B4 | [[Gallic acid (hydrate) (drug)]] | 5 µM | 72,529 | +0.14 |  |
| B5 | [[(R)-Verapamil (hydrochloride) (drug)]] | 5 µM | 81,100 | +0.30 |  |
| B6 | [[Pyridoxine (drug)]] | 5 µM | 70,974 | +0.11 |  |
| B7 | [[Acetohexamide (drug)]] | 5 µM | 70,623 | +0.10 |  |
| B8 | [[Temsirolimus (drug)]] | 5 µM | 81,451 | +0.31 |  |
| B9 | [[Megestrol (drug)]] | 5 µM | 91,432 | +0.48 |  |
| B10 | [[Diammonium Glycyrrhizinate (drug)]] | 5 µM | 70,973 | +0.11 |  |
| B11 | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] | 5 µM | 430 | — | ⚠ failed (excluded) |
| B12 | [[Ropivacaine (hydrochloride monohydrate) (drug)]] | 5 µM | 62,224 | -0.08 |  |
| C1 | [[Salicylic acid (drug)]] | 5 µM | 82,231 | +0.32 |  |
| C2 | [[Quinestrol (drug)]] | 5 µM | 86,796 | +0.40 |  |
| C3 | [[Tofacitinib (drug)]] | 5 µM | 58,046 | -0.18 |  |
| C4 | [[Trimetrexate (drug)]] | 5 µM | 63,768 | -0.04 |  |
| C5 | [[Gemfibrozil (drug)]] | 5 µM | 99,945 | +0.60 |  |
| C6 | [[18β-Glycyrrhetinic acid (drug)]] | 5 µM | 68,912 | +0.07 |  |
| C7 | [[Tolcapone (drug)]] | 5 µM | 68,106 | +0.05 |  |
| C8 | [[Terfenadine (drug)]] | 5 µM | 65,736 | +0.00 |  |
| C9 | [[Aliskiren (drug)]] | 5 µM | 81,546 | +0.31 |  |
| C10 | [[Fluvoxamine (maleate) (drug)]] | 5 µM | 61,834 | -0.09 |  |
| C11 | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] | 5 µM | 72,458 | +0.14 |  |
| C12 | [[Idarubicin (hydrochloride) (drug)]] | 5 µM | 34,772 | -0.92 |  |
| D1 | [[Elagolix sodium (drug)]] | 5 µM | 41,114 | -0.68 |  |
| D2 | [[Resveratrol (drug)]] | 5 µM | 43,392 | -0.60 |  |
| D3 | [[Rapamycin (drug)]] | 5 µM | 57,896 | -0.18 |  |
| D4 | [[Saquinavir (drug)]] | 5 µM | 42,754 | -0.62 |  |
| D5 | [[Tofacitinib (citrate) (drug)]] | 5 µM | 76,835 | +0.23 |  |
| D6 | [[Thymol (drug)]] | 5 µM | 65,561 | -0.00 |  |
| D7 | [[Almonertinib (hydrochloride) (drug)]] | 5 µM | 53,417 | -0.30 |  |
| D8 | [[Darinaparsin (drug)]] | 5 µM | 76,421 | +0.22 |  |
| D9 | [[Vilanterol (drug)]] | 5 µM | 73,313 | +0.16 |  |
| D10 | [[Lenalidomide (hemihydrate) (drug)]] | 5 µM | 54,866 | -0.26 |  |
| D11 | [[Azithromycin (hydrate) (drug)]] | 5 µM | 70,410 | +0.10 |  |
| D12 | [[Ritonavir (drug)]] | 5 µM | 65,126 | -0.01 |  |
| E1 | [[Pentamidine (isethionate) (drug)]] | 5 µM | 80,890 | +0.30 |  |
| E2 | [[Adenosine (drug)]] | 5 µM | 80,087 | +0.28 |  |
| E3 | [[Sulfisoxazole (drug)]] | 5 µM | 61,991 | -0.08 |  |
| E4 | [[Norepinephrine (hydrochloride) (drug)]] | 5 µM | 65,841 | +0.00 |  |
| E5 | [[Ciclopirox (drug)]] | 5 µM | 53,098 | -0.31 |  |
| E6 | [[Lidocaine (hydrochloride) (drug)]] | 5 µM | 63,720 | -0.04 |  |
| E7 | [[Demeclocycline (drug)]] | 5 µM | 70,017 | +0.09 |  |
| E8 | [[Mitoxantrone (dihydrochloride) (drug)]] | 5 µM | 69,156 | +0.07 |  |
| E9 | [[Larotrectinib (drug)]] | 5 µM | 61,576 | -0.09 |  |
| E10 | [[Busulfan (drug)]] | 5 µM | 56,504 | -0.22 |  |
| E11 | [[Cepharanthine (drug)]] | 5 µM | 70,520 | +0.10 |  |
| E12 | [[Radotinib (drug)]] | 5 µM | 64,148 | -0.04 |  |
| F1 | [[Docetaxel (drug)]] | 5 µM | 89,028 | +0.44 |  |
| F2 | [[Triclosan (drug)]] | 5 µM | 88,069 | +0.42 |  |
| F3 | [[Tucidinostat (drug)]] | 5 µM | 78,714 | +0.26 |  |
| F4 | [[Bergenin (drug)]] | 5 µM | 69,330 | +0.08 |  |
| F5 | [[Allantoin (drug)]] | 5 µM | 65,501 | -0.01 |  |
| F6 | [[Bimatoprost (drug)]] | 5 µM | 72,756 | +0.15 |  |
| F7 | [[Triamcinolone (drug)]] | 5 µM | 71,419 | +0.12 |  |
| F8 | [[Olanzapine (drug)]] | 5 µM | 61,902 | -0.09 |  |
| F9 | [[Rimonabant (drug)]] | 5 µM | 61,359 | -0.10 |  |
| F10 | [[Pentagastrin (drug)]] | 5 µM | 64,985 | -0.02 |  |
| F11 | [[Lumateperone (tosylate) (drug)]] | 5 µM | 63,676 | -0.05 |  |
| F12 | [[Relugolix (drug)]] | 5 µM | 58,509 | -0.17 |  |
| G1 | [[Homoharringtonine (drug)]] | 5 µM | 56,128 | -0.23 |  |
| G2 | [[Hexylresorcinol (drug)]] | 5 µM | 76,587 | +0.22 |  |
| G3 | [[Baicalin (drug)]] | 5 µM | 62,243 | -0.08 |  |
| G4 | [[Berberine (chloride hydrate) (drug)]] | 5 µM | 67,130 | +0.03 |  |
| G5 | [[Medroxyprogesterone acetate (drug)]] | 5 µM | 51,623 | -0.35 |  |
| G6 | [[Neratinib (maleate) (drug)]] | 5 µM | 51,667 | -0.35 |  |
| G7 | [[Sinomenine (drug)]] | 5 µM | 52,331 | -0.33 |  |
| G8 | [[Goserelin (acetate) (drug)]] | 5 µM | 55,344 | -0.25 |  |
| G9 | [[Fusidic acid (drug)]] | 5 µM | 68,627 | +0.06 |  |
| G10 | [[Balsalazide (sodium hydrate) (drug)]] | 5 µM | 66,288 | +0.01 |  |
| G11 | [[Cloxacillin (sodium) (drug)]] | 5 µM | 68,476 | +0.06 |  |
| G12 | [[Artesunate (drug)]] | 5 µM | 64,817 | -0.02 |  |
| H1 | [[Pyridoxine (hydrochloride) (drug)]] | 5 µM | 37,214 | -0.82 |  |
| H2 | [[Folic acid (drug)]] | 5 µM | 31,637 | -1.06 | low cells |
| H3 | [[Selinexor (drug)]] | 5 µM | 11,527 | -2.51 | low cells |
| H4 | [[Adenine (drug)]] | 5 µM | 44,522 | -0.56 |  |
| H5 | [[Gallic acid (drug)]] | 5 µM | 54,904 | -0.26 |  |
| H6 | [[Lipoic acid (drug)]] | 5 µM | 72,477 | +0.14 |  |
| H7 | [[Amsacrine (drug)]] | 5 µM | 56,183 | -0.23 |  |
| H8 | [[Anethole trithione (drug)]] | 5 µM | 55,572 | -0.24 |  |
| H9 | [[Clonidine (hydrochloride) (drug)]] | 5 µM | 63,945 | -0.04 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 52,712 | -0.32 | ⚠ position not correctable |
| H11 | DMSO | — | 40,140 | -0.71 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 55,432 | -0.25 | ⚠ position not correctable · DMSO |
