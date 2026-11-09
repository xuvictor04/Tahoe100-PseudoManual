---
plate: "plate10"
type: "plate"
number: 10
dose: "0.05"
unreliable: false
plate_factor: 1.0
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 10

`plate10` · dose 0.05 µM · 96 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 73,548. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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
| A1 | [[Bestatin (hydrochloride) (drug)]] | 0.05 µM | 56,037 | -0.39 |  |
| A2 | [[Ataluren (drug)]] | 0.05 µM | 102,120 | +0.47 |  |
| A3 | [[Canagliflozin (hemihydrate) (drug)]] | 0.05 µM | 68,981 | -0.09 |  |
| A4 | [[Brimonidine (drug)]] | 0.05 µM | 103,607 | +0.49 |  |
| A5 | [[Filgotinib (drug)]] | 0.05 µM | 77,323 | +0.07 |  |
| A6 | [[Esmolol (hydrochloride) (drug)]] | 0.05 µM | 124,717 | +0.76 |  |
| A7 | [[Omeprazole (drug)]] | 0.05 µM | 132,367 | +0.85 |  |
| A8 | [[Bicalutamide (drug)]] | 0.05 µM | 97,581 | +0.41 |  |
| A9 | [[Drospirenone (drug)]] | 0.05 µM | 69,847 | -0.07 |  |
| A10 | [[Belinostat (drug)]] | 0.05 µM | 72,440 | -0.02 |  |
| A11 | [[Ponatinib (drug)]] | 0.05 µM | 125,333 | +0.77 |  |
| A12 | [[Cabozantinib (S-malate) (drug)]] | 0.05 µM | 58,712 | -0.33 |  |
| B1 | [[Benztropine (mesylate) (drug)]] | 0.05 µM | 75,079 | +0.03 |  |
| B2 | [[Indacaterol (maleate) (drug)]] | 0.05 µM | 76,828 | +0.06 |  |
| B3 | [[Tirabrutinib (hydrochloride) (drug)]] | 0.05 µM | 117,877 | +0.68 |  |
| B4 | [[Loperamide (hydrochloride) (drug)]] | 0.05 µM | 60,082 | -0.29 |  |
| B5 | [[Econazole (drug)]] | 0.05 µM | 83,526 | +0.18 |  |
| B6 | [[Phenylephrine (hydrochloride) (drug)]] | 0.05 µM | 76,862 | +0.06 |  |
| B7 | [[Entrectinib (drug)]] | 0.05 µM | 78,922 | +0.10 |  |
| B8 | [[Vortioxetine (drug)]] | 0.05 µM | 74,021 | +0.01 |  |
| B9 | [[Omeprazole (sodium) (drug)]] | 0.05 µM | 89,652 | +0.29 |  |
| B10 | [[Imiquimod (hydrochloride) (drug)]] | 0.05 µM | 72,684 | -0.02 |  |
| B11 | [[Fingolimod (hydrochloride) (drug)]] | 0.05 µM | 82,769 | +0.17 |  |
| B12 | [[Digitoxin (drug)]] | 0.05 µM | 45,784 | -0.68 |  |
| C1 | [[Vitamin K4 (drug)]] | 0.05 µM | 79,484 | +0.11 |  |
| C2 | [[Aprepitant (drug)]] | 0.05 µM | 78,746 | +0.10 |  |
| C3 | [[Oxaprozin (drug)]] | 0.05 µM | 54,378 | -0.44 |  |
| C4 | [[Estrone sulfate (potassium) (drug)]] | 0.05 µM | 72,934 | -0.01 |  |
| C5 | [[L-Eflornithine (monohydrochloride) (drug)]] | 0.05 µM | 94,208 | +0.36 |  |
| C6 | [[Auranofin (drug)]] | 0.05 µM | 63,610 | -0.21 |  |
| C7 | [[Carbamazepine (drug)]] | 0.05 µM | 66,725 | -0.14 |  |
| C8 | [[Flutamide (drug)]] | 0.05 µM | 86,336 | +0.23 |  |
| C9 | [[Zileuton (drug)]] | 0.05 µM | 66,526 | -0.14 |  |
| C10 | [[Osimertinib (mesylate) (drug)]] | 0.05 µM | 63,646 | -0.21 |  |
| C11 | [[Sunitinib (drug)]] | 0.05 µM | 53,043 | -0.47 |  |
| C12 | [[Erythromycin (drug)]] | 0.05 µM | 63,667 | -0.21 |  |
| D1 | [[Abiraterone acetate (drug)]] | 0.05 µM | 98,300 | +0.42 |  |
| D2 | [[Asciminib (drug)]] | 0.05 µM | 62,294 | -0.24 |  |
| D3 | [[Allopurinol (drug)]] | 0.05 µM | 135,438 | +0.88 |  |
| D4 | [[Clopidogrel (drug)]] | 0.05 µM | 121,528 | +0.72 |  |
| D5 | [[Methyl aminolevulinate (hydrochloride) (drug)]] | 0.05 µM | 66,746 | -0.14 |  |
| D6 | [[Captopril (drug)]] | 0.05 µM | 50,051 | -0.56 |  |
| D7 | [[Voriconazole (drug)]] | 0.05 µM | 67,836 | -0.12 |  |
| D8 | [[Lopinavir (drug)]] | 0.05 µM | 64,068 | -0.20 |  |
| D9 | [[Dexamethasone (drug)]] | 0.05 µM | 65,500 | -0.17 |  |
| D10 | [[Ranolazine (drug)]] | 0.05 µM | 61,737 | -0.25 |  |
| D11 | [[Proglumide (drug)]] | 0.05 µM | 50,330 | -0.55 |  |
| D12 | [[Neratinib (drug)]] | 0.05 µM | 42,435 | -0.79 |  |
| E1 | [[Meloxicam (drug)]] | 0.05 µM | 73,240 | -0.01 |  |
| E2 | [[Piroxicam (drug)]] | 0.05 µM | 106,457 | +0.53 |  |
| E3 | [[Nafamostat (mesylate) (drug)]] | 0.05 µM | 61,286 | -0.26 |  |
| E4 | [[Idoxuridine (drug)]] | 0.05 µM | 70,286 | -0.07 |  |
| E5 | [[Atazanavir (sulfate) (drug)]] | 0.05 µM | 91,655 | +0.32 |  |
| E6 | [[Malotilate (drug)]] | 0.05 µM | 73,677 | +0.00 |  |
| E7 | [[Pioglitazone (drug)]] | 0.05 µM | 73,493 | -0.00 |  |
| E8 | [[Bexarotene (drug)]] | 0.05 µM | 74,241 | +0.01 |  |
| E9 | [[Tazarotene (drug)]] | 0.05 µM | 71,890 | -0.03 |  |
| E10 | [[Vandetanib (drug)]] | 0.05 µM | 64,619 | -0.19 |  |
| E11 | [[Delamanid (drug)]] | 0.05 µM | 70,256 | -0.07 |  |
| E12 | [[Ivermectin (drug)]] | 0.05 µM | 77,487 | +0.08 |  |
| F1 | [[Citalopram (hydrobromide) (drug)]] | 0.05 µM | 135,785 | +0.88 |  |
| F2 | [[Acetazolamide (drug)]] | 0.05 µM | 64,447 | -0.19 |  |
| F3 | [[Fulvestrant (drug)]] | 0.05 µM | 70,508 | -0.06 |  |
| F4 | [[Talc (drug)]] | 0.05 µM | 46,467 | -0.66 |  |
| F5 | [[Pentoxifylline (drug)]] | 0.05 µM | 78,335 | +0.09 |  |
| F6 | [[Artemether (drug)]] | 0.05 µM | 109,917 | +0.58 |  |
| F7 | [[Cyclosporin A (drug)]] | 0.05 µM | 119,582 | +0.70 |  |
| F8 | [[Crizotinib (hydrochloride) (drug)]] | 0.05 µM | 72,650 | -0.02 |  |
| F9 | [[Trametinib (drug)]] | 0.05 µM | 58,316 | -0.33 |  |
| F10 | [[Fedratinib (hydrochloride hydrate) (drug)]] | 0.05 µM | 73,602 | +0.00 |  |
| F11 | [[Darolutamide (drug)]] | 0.05 µM | 110,147 | +0.58 |  |
| F12 | [[γ-Oryzanol (drug)]] | 0.05 µM | 99,670 | +0.44 |  |
| G1 | [[Clobetasol propionate (drug)]] | 0.05 µM | 55,953 | -0.39 |  |
| G2 | [[Budesonide (drug)]] | 0.05 µM | 67,044 | -0.13 |  |
| G3 | [[Cinacalcet (drug)]] | 0.05 µM | 50,772 | -0.53 |  |
| G4 | [[Valdecoxib (drug)]] | 0.05 µM | 36,772 | -1.00 | low cells |
| G5 | [[Pimozide (drug)]] | 0.05 µM | 28,177 | -1.38 | low cells |
| G6 | [[Methotrexate (drug)]] | 0.05 µM | 36,365 | -1.02 | low cells |
| G7 | [[5-Fluorouracil (drug)]] | 0.05 µM | 66,560 | -0.14 |  |
| G8 | [[Ixazomib citrate (drug)]] | 0.05 µM | 68,696 | -0.10 |  |
| G9 | [[5-Azacytidine (drug)]] | 0.05 µM | 74,498 | +0.02 |  |
| G10 | [[Aspirin (drug)]] | 0.05 µM | 92,983 | +0.34 |  |
| G11 | [[Vismodegib (drug)]] | 0.05 µM | 48,524 | -0.60 |  |
| G12 | [[Dihydroartemisinin (drug)]] | 0.05 µM | 57,239 | -0.36 |  |
| H1 | [[Lactate (calcium) (drug)]] | 0.05 µM | 87,295 | +0.25 |  |
| H2 | [[Ouabain (Octahydrate) (drug)]] | 0.05 µM | 119,396 | +0.70 |  |
| H3 | [[Gefitinib (drug)]] | 0.05 µM | 104,283 | +0.50 |  |
| H4 | [[Methylthiouracil (drug)]] | 0.05 µM | 161,053 | +1.13 |  |
| H5 | [[Binimetinib (drug)]] | 0.05 µM | 135,899 | +0.89 |  |
| H6 | [[Perindopril (erbumine) (drug)]] | 0.05 µM | 140,339 | +0.93 |  |
| H7 | [[Dapagliflozin (drug)]] | 0.05 µM | 99,349 | +0.43 |  |
| H8 | [[Panobinostat (drug)]] | 0.05 µM | 95,507 | +0.38 |  |
| H9 | [[Uridine (drug)]] | 0.05 µM | 97,448 | +0.41 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 106,066 | +0.53 | ⚠ position not correctable |
| H11 | DMSO | — | 141,054 | +0.94 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 59,984 | -0.29 | ⚠ position not correctable · DMSO |
