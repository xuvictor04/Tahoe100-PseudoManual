---
plate: "plate12"
type: "plate"
number: 12
dose: "0.05 / 5"
unreliable: false
plate_factor: 1.0
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 12

`plate12` · dose 0.05 / 5 µM · 96 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 100,272. Source: `tables/plates.parquet`, `tables/wells.parquet`.

## Layout

*Drug in each well (names cut to 10 characters; the table below has them in full). The per-gene plates notes use the same 8 × 12 layout.*

| |1|2|3|4|5|6|7|8|9|10|11|12|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|A|Bestatin (|Ataluren|Canagliflo|Brimonidin|Filgotinib|Esmolol (h|Omeprazole|Bicalutami|Drospireno|Belinostat|Ponatinib|Cabozantin|
|B|Benztropin|Indacatero|Tirabrutin|Loperamide|Econazole|Phenylephr|Entrectini|Vortioxeti|Omeprazole|Imiquimod|Fingolimod|Digitoxin|
|C|Vitamin K4|Aprepitant|Oxaprozin|Estrone su|L-Eflornit|Auranofin|Carbamazep|Flutamide|Zileuton|Osimertini|Sunitinib|Erythromyc|
|D|Abirateron|Asciminib|Allopurino|Clopidogre|Methyl ami|Captopril|Voriconazo|Lopinavir|Dexamethas|Ranolazine|Proglumide|Neratinib|
|E|Meloxicam|Piroxicam|Nafamostat|Idoxuridin|Atazanavir|Malotilate|Pioglitazo|Bexarotene|Tazarotene|Vandetanib|Delamanid|Ivermectin|
|F|Citalopram|Acetazolam|Fulvestran|Talc|Pentoxifyl|Artemether|Cyclospori|Crizotinib|Trametinib|Fedratinib|Darolutami|γ-Oryzanol|
|G|Clobetasol|Budesonide|Cinacalcet|Valdecoxib|Pimozide|Methotrexa|5-Fluorour|Ixazomib c|5-Azacytid|Aspirin|Vismodegib|Dihydroart|
|H|Lactate (c|Ouabain (O|Gefitinib|Methylthio|Binimetini|Perindopri|Dapagliflo|Panobinost|Uridine|Adagrasib|**DMSO**|**DMSO**|

## Wells

*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's median drug well. Every well of the plate is listed: 96, 3 with an alert ⚠ (on an unreliable plate, without a position correction, not used in its drug-dose or failed: what the run did with it is said, nothing is hidden).*

| Well | Drug | Dose | Cells | log2 vs plate | Flags |
|---|---|---|---|---|---|
| A1 | [[Bestatin (hydrochloride) (drug)]] | 5 µM | 107,041 | +0.09 |  |
| A2 | [[Ataluren (drug)]] | 5 µM | 178,892 | +0.83 |  |
| A3 | [[Canagliflozin (hemihydrate) (drug)]] | 5 µM | 209,642 | +1.06 |  |
| A4 | [[Brimonidine (drug)]] | 5 µM | 160,081 | +0.67 |  |
| A5 | [[Filgotinib (drug)]] | 5 µM | 180,642 | +0.85 |  |
| A6 | [[Esmolol (hydrochloride) (drug)]] | 5 µM | 158,002 | +0.65 |  |
| A7 | [[Omeprazole (drug)]] | 5 µM | 162,537 | +0.70 |  |
| A8 | [[Bicalutamide (drug)]] | 5 µM | 158,879 | +0.66 |  |
| A9 | [[Drospirenone (drug)]] | 5 µM | 157,936 | +0.65 |  |
| A10 | [[Belinostat (drug)]] | 5 µM | 91,519 | -0.13 |  |
| A11 | [[Ponatinib (drug)]] | 5 µM | 133,861 | +0.41 |  |
| A12 | [[Cabozantinib (S-malate) (drug)]] | 5 µM | 114,758 | +0.19 |  |
| B1 | [[Benztropine (mesylate) (drug)]] | 5 µM | 95,571 | -0.07 |  |
| B2 | [[Indacaterol (maleate) (drug)]] | 5 µM | 100,263 | -0.00 |  |
| B3 | [[Tirabrutinib (hydrochloride) (drug)]] | 5 µM | 108,668 | +0.11 |  |
| B4 | [[Loperamide (hydrochloride) (drug)]] | 5 µM | 91,142 | -0.14 |  |
| B5 | [[Econazole (drug)]] | 5 µM | 101,691 | +0.02 |  |
| B6 | [[Phenylephrine (hydrochloride) (drug)]] | 5 µM | 84,758 | -0.24 |  |
| B7 | [[Entrectinib (drug)]] | 5 µM | 56,863 | -0.82 |  |
| B8 | [[Vortioxetine (drug)]] | 5 µM | 41,138 | -1.29 | low cells |
| B9 | [[Omeprazole (sodium) (drug)]] | 5 µM | 82,520 | -0.28 |  |
| B10 | [[Imiquimod (hydrochloride) (drug)]] | 5 µM | 31,563 | -1.67 | low cells |
| B11 | [[Fingolimod (hydrochloride) (drug)]] | 5 µM | 46,013 | -1.13 | low cells |
| B12 | [[Digitoxin (drug)]] | 5 µM | 35,231 | -1.51 | low cells |
| C1 | [[Vitamin K4 (drug)]] | 5 µM | 97,835 | -0.04 |  |
| C2 | [[Aprepitant (drug)]] | 5 µM | 97,535 | -0.04 |  |
| C3 | [[Oxaprozin (drug)]] | 5 µM | 89,088 | -0.17 |  |
| C4 | [[Estrone sulfate (potassium) (drug)]] | 5 µM | 102,010 | +0.02 |  |
| C5 | [[L-Eflornithine (monohydrochloride) (drug)]] | 5 µM | 84,318 | -0.25 |  |
| C6 | [[Auranofin (drug)]] | 5 µM | 52,208 | -0.94 |  |
| C7 | [[Carbamazepine (drug)]] | 5 µM | 56,411 | -0.83 |  |
| C8 | [[Flutamide (drug)]] | 5 µM | 78,601 | -0.35 |  |
| C9 | [[Zileuton (drug)]] | 5 µM | 95,882 | -0.07 |  |
| C10 | [[Osimertinib (mesylate) (drug)]] | 5 µM | 65,405 | -0.62 |  |
| C11 | [[Sunitinib (drug)]] | 5 µM | 41,924 | -1.26 | low cells |
| C12 | [[Erythromycin (drug)]] | 5 µM | 66,893 | -0.59 |  |
| D1 | [[Abiraterone acetate (drug)]] | 5 µM | 97,184 | -0.05 |  |
| D2 | [[Asciminib (drug)]] | 5 µM | 74,778 | -0.43 |  |
| D3 | [[Allopurinol (drug)]] | 5 µM | 131,006 | +0.38 |  |
| D4 | [[Clopidogrel (drug)]] | 5 µM | 95,291 | -0.08 |  |
| D5 | [[Methyl aminolevulinate (hydrochloride) (drug)]] | 5 µM | 116,115 | +0.21 |  |
| D6 | [[Captopril (drug)]] | 5 µM | 104,693 | +0.06 |  |
| D7 | [[Voriconazole (drug)]] | 5 µM | 94,868 | -0.08 |  |
| D8 | [[Lopinavir (drug)]] | 5 µM | 65,815 | -0.61 |  |
| D9 | [[Dexamethasone (drug)]] | 5 µM | 82,767 | -0.28 |  |
| D10 | [[Ranolazine (drug)]] | 5 µM | 81,946 | -0.29 |  |
| D11 | [[Proglumide (drug)]] | 5 µM | 89,695 | -0.16 |  |
| D12 | [[Neratinib (drug)]] | 5 µM | 71,616 | -0.49 |  |
| E1 | [[Meloxicam (drug)]] | 5 µM | 71,502 | -0.49 |  |
| E2 | [[Piroxicam (drug)]] | 5 µM | 112,312 | +0.16 |  |
| E3 | [[Nafamostat (mesylate) (drug)]] | 5 µM | 118,546 | +0.24 |  |
| E4 | [[Idoxuridine (drug)]] | 5 µM | 122,037 | +0.28 |  |
| E5 | [[Atazanavir (sulfate) (drug)]] | 5 µM | 93,754 | -0.10 |  |
| E6 | [[Malotilate (drug)]] | 5 µM | 108,056 | +0.11 |  |
| E7 | [[Pioglitazone (drug)]] | 5 µM | 135,543 | +0.43 |  |
| E8 | [[Bexarotene (drug)]] | 5 µM | 109,339 | +0.12 |  |
| E9 | [[Tazarotene (drug)]] | 5 µM | 103,101 | +0.04 |  |
| E10 | [[Vandetanib (drug)]] | 5 µM | 104,501 | +0.06 |  |
| E11 | [[Delamanid (drug)]] | 5 µM | 126,302 | +0.33 |  |
| E12 | [[Ivermectin (drug)]] | 5 µM | 113,949 | +0.18 |  |
| F1 | [[Citalopram (hydrobromide) (drug)]] | 5 µM | 106,855 | +0.09 |  |
| F2 | [[Acetazolamide (drug)]] | 5 µM | 88,748 | -0.18 |  |
| F3 | [[Fulvestrant (drug)]] | 5 µM | 192,318 | +0.94 |  |
| F4 | [[Talc (drug)]] | 5 µM | 107,859 | +0.10 |  |
| F5 | [[Pentoxifylline (drug)]] | 5 µM | 135,185 | +0.43 |  |
| F6 | [[Artemether (drug)]] | 5 µM | 134,499 | +0.42 |  |
| F7 | [[Cyclosporin A (drug)]] | 5 µM | 100,281 | -0.00 |  |
| F8 | [[Crizotinib (hydrochloride) (drug)]] | 5 µM | 141,746 | +0.50 |  |
| F9 | [[Trametinib (drug)]] | 5 µM | 167,919 | +0.74 |  |
| F10 | [[Fedratinib (hydrochloride hydrate) (drug)]] | 5 µM | 106,855 | +0.09 |  |
| F11 | [[Darolutamide (drug)]] | 5 µM | 103,208 | +0.04 |  |
| F12 | [[γ-Oryzanol (drug)]] | 5 µM | 99,472 | -0.01 |  |
| G1 | [[Clobetasol propionate (drug)]] | 5 µM | 90,170 | -0.16 |  |
| G2 | [[Budesonide (drug)]] | 5 µM | 89,151 | -0.17 |  |
| G3 | [[Cinacalcet (drug)]] | 5 µM | 141,765 | +0.50 |  |
| G4 | [[Valdecoxib (drug)]] | 5 µM | 95,538 | -0.07 |  |
| G5 | [[Pimozide (drug)]] | 5 µM | 100,517 | +0.00 |  |
| G6 | [[Methotrexate (drug)]] | 5 µM | 134,187 | +0.42 |  |
| G7 | [[5-Fluorouracil (drug)]] | 5 µM | 107,647 | +0.10 |  |
| G8 | [[Ixazomib citrate (drug)]] | 5 µM | 63,168 | -0.67 |  |
| G9 | [[5-Azacytidine (drug)]] | 5 µM | 69,937 | -0.52 |  |
| G10 | [[Aspirin (drug)]] | 5 µM | 85,199 | -0.24 |  |
| G11 | [[Vismodegib (drug)]] | 5 µM | 74,037 | -0.44 |  |
| G12 | [[Dihydroartemisinin (drug)]] | 5 µM | 62,662 | -0.68 |  |
| H1 | [[Lactate (calcium) (drug)]] | 5 µM | 89,082 | -0.17 |  |
| H2 | [[Ouabain (Octahydrate) (drug)]] | 5 µM | 93,100 | -0.11 |  |
| H3 | [[Gefitinib (drug)]] | 5 µM | 178,000 | +0.83 |  |
| H4 | [[Methylthiouracil (drug)]] | 5 µM | 188,785 | +0.91 |  |
| H5 | [[Binimetinib (drug)]] | 5 µM | 175,760 | +0.81 |  |
| H6 | [[Perindopril (erbumine) (drug)]] | 5 µM | 125,883 | +0.33 |  |
| H7 | [[Dapagliflozin (drug)]] | 5 µM | 141,292 | +0.49 |  |
| H8 | [[Panobinostat (drug)]] | 5 µM | 77,802 | -0.37 |  |
| H9 | [[Uridine (drug)]] | 5 µM | 198,625 | +0.98 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 102,146 | +0.02 | ⚠ position not correctable |
| H11 | DMSO | — | 77,980 | -0.36 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 99,176 | -0.02 | ⚠ position not correctable · DMSO |
