---
plate: "plate6"
type: "plate"
number: 6
dose: "0.05 / 5"
unreliable: false
plate_factor: 1.0
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 06

`plate6` · dose 0.05 / 5 µM · 96 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 71,906. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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
| A1 | [[8-Hydroxyquinoline (drug)]] | 5 µM | 105,834 | +0.58 |  |
| A2 | [[Chlorhexidine (diacetate) (drug)]] | 5 µM | 97,197 | +0.46 |  |
| A3 | [[Trifluridine (drug)]] | 5 µM | 68,787 | -0.04 |  |
| A4 | [[Berbamine (drug)]] | 5 µM | 106,317 | +0.59 |  |
| A5 | [[Retinoic acid (drug)]] | 5 µM | 90,873 | +0.36 |  |
| A6 | [[Cysteamine (hydrochloride) (drug)]] | 5 µM | 103,309 | +0.55 |  |
| A7 | [[Vinblastine (sulfate) (drug)]] | 5 µM | 47,200 | -0.58 |  |
| A8 | [[Pasireotide (acetate) (drug)]] | 5 µM | 87,206 | +0.30 |  |
| A9 | [[Riluzole hydrochloride (drug)]] | 5 µM | 88,347 | +0.32 |  |
| A10 | [[Palmatine (chloride) (drug)]] | 5 µM | 61,040 | -0.21 |  |
| A11 | [[Isocorydine (drug)]] | 5 µM | 77,471 | +0.13 |  |
| A12 | [[Raltitrexed (drug)]] | 5 µM | 144,418 | +1.03 |  |
| B1 | [[Furosemide (drug)]] | 5 µM | 55,485 | -0.35 |  |
| B2 | [[Clotrimazole (drug)]] | 5 µM | 55,132 | -0.36 |  |
| B3 | [[Sodium Salicylate (drug)]] | 5 µM | 52,597 | -0.43 |  |
| B4 | [[Gallic acid (hydrate) (drug)]] | 5 µM | 57,617 | -0.29 |  |
| B5 | [[(R)-Verapamil (hydrochloride) (drug)]] | 5 µM | 80,188 | +0.18 |  |
| B6 | [[Pyridoxine (drug)]] | 5 µM | 50,292 | -0.49 |  |
| B7 | [[Acetohexamide (drug)]] | 5 µM | 42,390 | -0.74 |  |
| B8 | [[Temsirolimus (drug)]] | 5 µM | 59,770 | -0.24 |  |
| B9 | [[Megestrol (drug)]] | 5 µM | 55,030 | -0.36 |  |
| B10 | [[Diammonium Glycyrrhizinate (drug)]] | 5 µM | 92,714 | +0.39 |  |
| B11 | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] | 5 µM | 95,841 | +0.44 |  |
| B12 | [[Ropivacaine (hydrochloride monohydrate) (drug)]] | 5 µM | 75,175 | +0.09 |  |
| C1 | [[Salicylic acid (drug)]] | 5 µM | 32,791 | -1.11 | low cells |
| C2 | [[Quinestrol (drug)]] | 5 µM | 87,281 | +0.30 |  |
| C3 | [[Tofacitinib (drug)]] | 5 µM | 73,101 | +0.05 |  |
| C4 | [[Trimetrexate (drug)]] | 5 µM | 63,904 | -0.15 |  |
| C5 | [[Gemfibrozil (drug)]] | 5 µM | 82,195 | +0.22 |  |
| C6 | [[18β-Glycyrrhetinic acid (drug)]] | 5 µM | 36,855 | -0.94 |  |
| C7 | [[Tolcapone (drug)]] | 5 µM | 104,222 | +0.56 |  |
| C8 | [[Terfenadine (drug)]] | 5 µM | 66,179 | -0.10 |  |
| C9 | [[Aliskiren (drug)]] | 5 µM | 58,665 | -0.27 |  |
| C10 | [[Fluvoxamine (maleate) (drug)]] | 5 µM | 70,661 | -0.00 |  |
| C11 | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] | 5 µM | 81,656 | +0.21 |  |
| C12 | [[Idarubicin (hydrochloride) (drug)]] | 5 µM | 42,711 | -0.73 |  |
| D1 | [[Elagolix sodium (drug)]] | 5 µM | 79,945 | +0.18 |  |
| D2 | [[Resveratrol (drug)]] | 5 µM | 109,926 | +0.64 |  |
| D3 | [[Rapamycin (drug)]] | 5 µM | 78,476 | +0.15 |  |
| D4 | [[Saquinavir (drug)]] | 5 µM | 37,548 | -0.91 |  |
| D5 | [[Tofacitinib (citrate) (drug)]] | 5 µM | 53,246 | -0.41 |  |
| D6 | [[Thymol (drug)]] | 5 µM | 44,964 | -0.65 |  |
| D7 | [[Almonertinib (hydrochloride) (drug)]] | 5 µM | 41,532 | -0.77 |  |
| D8 | [[Darinaparsin (drug)]] | 5 µM | 38,451 | -0.88 |  |
| D9 | [[Vilanterol (drug)]] | 5 µM | 54,165 | -0.38 |  |
| D10 | [[Lenalidomide (hemihydrate) (drug)]] | 5 µM | 62,126 | -0.19 |  |
| D11 | [[Azithromycin (hydrate) (drug)]] | 5 µM | 46,345 | -0.61 |  |
| D12 | [[Ritonavir (drug)]] | 5 µM | 58,168 | -0.28 |  |
| E1 | [[Pentamidine (isethionate) (drug)]] | 5 µM | 50,612 | -0.48 |  |
| E2 | [[Adenosine (drug)]] | 5 µM | 48,649 | -0.54 |  |
| E3 | [[Sulfisoxazole (drug)]] | 5 µM | 70,712 | +0.00 |  |
| E4 | [[Norepinephrine (hydrochloride) (drug)]] | 5 µM | 54,210 | -0.38 |  |
| E5 | [[Ciclopirox (drug)]] | 5 µM | 48,377 | -0.55 |  |
| E6 | [[Lidocaine (hydrochloride) (drug)]] | 5 µM | 34,509 | -1.03 | low cells |
| E7 | [[Demeclocycline (drug)]] | 5 µM | 41,592 | -0.77 |  |
| E8 | [[Mitoxantrone (dihydrochloride) (drug)]] | 5 µM | 31,041 | -1.19 | low cells |
| E9 | [[Larotrectinib (drug)]] | 5 µM | 22,420 | -1.66 | low cells |
| E10 | [[Busulfan (drug)]] | 5 µM | 58,719 | -0.27 |  |
| E11 | [[Cepharanthine (drug)]] | 5 µM | 19,026 | -1.89 | low cells |
| E12 | [[Radotinib (drug)]] | 5 µM | 52,513 | -0.43 |  |
| F1 | [[Docetaxel (drug)]] | 5 µM | 43,690 | -0.69 |  |
| F2 | [[Triclosan (drug)]] | 5 µM | 67,477 | -0.07 |  |
| F3 | [[Tucidinostat (drug)]] | 5 µM | 63,029 | -0.17 |  |
| F4 | [[Bergenin (drug)]] | 5 µM | 85,839 | +0.28 |  |
| F5 | [[Allantoin (drug)]] | 5 µM | 88,400 | +0.32 |  |
| F6 | [[Bimatoprost (drug)]] | 5 µM | 50,583 | -0.48 |  |
| F7 | [[Triamcinolone (drug)]] | 5 µM | 49,427 | -0.52 |  |
| F8 | [[Olanzapine (drug)]] | 5 µM | 60,204 | -0.23 |  |
| F9 | [[Rimonabant (drug)]] | 5 µM | 66,917 | -0.08 |  |
| F10 | [[Pentagastrin (drug)]] | 5 µM | 140,358 | +0.99 |  |
| F11 | [[Lumateperone (tosylate) (drug)]] | 5 µM | 90,340 | +0.35 |  |
| F12 | [[Relugolix (drug)]] | 5 µM | 121,355 | +0.78 |  |
| G1 | [[Homoharringtonine (drug)]] | 5 µM | 45,466 | -0.64 |  |
| G2 | [[Hexylresorcinol (drug)]] | 5 µM | 115,369 | +0.71 |  |
| G3 | [[Baicalin (drug)]] | 5 µM | 127,771 | +0.85 |  |
| G4 | [[Berberine (chloride hydrate) (drug)]] | 5 µM | 149,875 | +1.08 |  |
| G5 | [[Medroxyprogesterone acetate (drug)]] | 5 µM | 82,077 | +0.22 |  |
| G6 | [[Neratinib (maleate) (drug)]] | 5 µM | 122,439 | +0.79 |  |
| G7 | [[Sinomenine (drug)]] | 5 µM | 76,869 | +0.12 |  |
| G8 | [[Goserelin (acetate) (drug)]] | 5 µM | 116,294 | +0.72 |  |
| G9 | [[Fusidic acid (drug)]] | 5 µM | 87,789 | +0.31 |  |
| G10 | [[Balsalazide (sodium hydrate) (drug)]] | 5 µM | 104,347 | +0.56 |  |
| G11 | [[Cloxacillin (sodium) (drug)]] | 5 µM | 100,052 | +0.50 |  |
| G12 | [[Artesunate (drug)]] | 5 µM | 111,456 | +0.66 |  |
| H1 | [[Pyridoxine (hydrochloride) (drug)]] | 5 µM | 102,135 | +0.53 |  |
| H2 | [[Folic acid (drug)]] | 5 µM | 107,435 | +0.60 |  |
| H3 | [[Selinexor (drug)]] | 5 µM | 86,507 | +0.29 |  |
| H4 | [[Adenine (drug)]] | 5 µM | 118,063 | +0.74 |  |
| H5 | [[Gallic acid (drug)]] | 5 µM | 123,921 | +0.81 |  |
| H6 | [[Lipoic acid (drug)]] | 5 µM | 83,932 | +0.25 |  |
| H7 | [[Amsacrine (drug)]] | 5 µM | 50,419 | -0.49 |  |
| H8 | [[Anethole trithione (drug)]] | 5 µM | 73,891 | +0.06 |  |
| H9 | [[Clonidine (hydrochloride) (drug)]] | 5 µM | 158,706 | +1.17 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 117,264 | +0.73 | ⚠ position not correctable |
| H11 | DMSO | — | 95,563 | +0.44 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 112,874 | +0.68 | ⚠ position not correctable · DMSO |
