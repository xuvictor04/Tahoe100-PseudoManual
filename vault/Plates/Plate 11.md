---
plate: "plate11"
type: "plate"
number: 11
dose: "0.05 / 0.5"
unreliable: false
plate_factor: 1.0
n_wells: 96
dmso_wells: "H11, H12"
failed_wells: []
tags: ["plate"]
generated_by: "tahoemap"
---

# Plate 11

`plate11` · dose 0.05 / 0.5 µM · 96 wells analysed · plate factor 1.00 · reliable

The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other well (flag `unreliable plate only`). DMSO wells: H11, H12. Failed wells (excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): none. Median cells per analysed well: 70,799. Source: `tables/plates.parquet`, `tables/wells.parquet`.

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
| A1 | [[Bestatin (hydrochloride) (drug)]] | 0.5 µM | 101,258 | +0.54 |  |
| A2 | [[Ataluren (drug)]] | 0.5 µM | 63,290 | -0.14 |  |
| A3 | [[Canagliflozin (hemihydrate) (drug)]] | 0.5 µM | 31,426 | -1.15 | low cells |
| A4 | [[Brimonidine (drug)]] | 0.5 µM | 50,944 | -0.45 |  |
| A5 | [[Filgotinib (drug)]] | 0.5 µM | 57,853 | -0.27 |  |
| A6 | [[Esmolol (hydrochloride) (drug)]] | 0.5 µM | 57,693 | -0.27 |  |
| A7 | [[Omeprazole (drug)]] | 0.5 µM | 39,521 | -0.82 |  |
| A8 | [[Bicalutamide (drug)]] | 0.5 µM | 55,250 | -0.33 |  |
| A9 | [[Drospirenone (drug)]] | 0.5 µM | 49,285 | -0.50 |  |
| A10 | [[Belinostat (drug)]] | 0.5 µM | 36,913 | -0.92 |  |
| A11 | [[Ponatinib (drug)]] | 0.5 µM | 61,980 | -0.17 |  |
| A12 | [[Cabozantinib (S-malate) (drug)]] | 0.5 µM | 53,719 | -0.37 |  |
| B1 | [[Benztropine (mesylate) (drug)]] | 0.5 µM | 89,091 | +0.36 |  |
| B2 | [[Indacaterol (maleate) (drug)]] | 0.5 µM | 89,874 | +0.37 |  |
| B3 | [[Tirabrutinib (hydrochloride) (drug)]] | 0.5 µM | 94,754 | +0.44 |  |
| B4 | [[Loperamide (hydrochloride) (drug)]] | 0.5 µM | 107,737 | +0.63 |  |
| B5 | [[Econazole (drug)]] | 0.5 µM | 95,283 | +0.45 |  |
| B6 | [[Phenylephrine (hydrochloride) (drug)]] | 0.5 µM | 107,746 | +0.63 |  |
| B7 | [[Entrectinib (drug)]] | 0.5 µM | 114,416 | +0.72 |  |
| B8 | [[Vortioxetine (drug)]] | 0.5 µM | 102,288 | +0.55 |  |
| B9 | [[Omeprazole (sodium) (drug)]] | 0.5 µM | 104,934 | +0.59 |  |
| B10 | [[Imiquimod (hydrochloride) (drug)]] | 0.5 µM | 107,904 | +0.63 |  |
| B11 | [[Fingolimod (hydrochloride) (drug)]] | 0.5 µM | 99,753 | +0.52 |  |
| B12 | [[Digitoxin (drug)]] | 0.5 µM | 76,107 | +0.13 |  |
| C1 | [[Vitamin K4 (drug)]] | 0.5 µM | 64,100 | -0.12 |  |
| C2 | [[Aprepitant (drug)]] | 0.5 µM | 72,060 | +0.05 |  |
| C3 | [[Oxaprozin (drug)]] | 0.5 µM | 38,208 | -0.87 |  |
| C4 | [[Estrone sulfate (potassium) (drug)]] | 0.5 µM | 50,923 | -0.45 |  |
| C5 | [[L-Eflornithine (monohydrochloride) (drug)]] | 0.5 µM | 57,188 | -0.28 |  |
| C6 | [[Auranofin (drug)]] | 0.5 µM | 76,256 | +0.13 |  |
| C7 | [[Carbamazepine (drug)]] | 0.5 µM | 55,617 | -0.32 |  |
| C8 | [[Flutamide (drug)]] | 0.5 µM | 59,047 | -0.24 |  |
| C9 | [[Zileuton (drug)]] | 0.5 µM | 94,180 | +0.44 |  |
| C10 | [[Osimertinib (mesylate) (drug)]] | 0.5 µM | 88,235 | +0.34 |  |
| C11 | [[Sunitinib (drug)]] | 0.5 µM | 71,700 | +0.04 |  |
| C12 | [[Erythromycin (drug)]] | 0.5 µM | 58,984 | -0.24 |  |
| D1 | [[Abiraterone acetate (drug)]] | 0.5 µM | 97,739 | +0.49 |  |
| D2 | [[Asciminib (drug)]] | 0.5 µM | 107,023 | +0.62 |  |
| D3 | [[Allopurinol (drug)]] | 0.5 µM | 79,004 | +0.18 |  |
| D4 | [[Clopidogrel (drug)]] | 0.5 µM | 97,935 | +0.49 |  |
| D5 | [[Methyl aminolevulinate (hydrochloride) (drug)]] | 0.5 µM | 125,208 | +0.85 |  |
| D6 | [[Captopril (drug)]] | 0.5 µM | 91,443 | +0.39 |  |
| D7 | [[Voriconazole (drug)]] | 0.5 µM | 94,861 | +0.45 |  |
| D8 | [[Lopinavir (drug)]] | 0.5 µM | 107,615 | +0.63 |  |
| D9 | [[Dexamethasone (drug)]] | 0.5 µM | 83,112 | +0.26 |  |
| D10 | [[Ranolazine (drug)]] | 0.5 µM | 100,801 | +0.53 |  |
| D11 | [[Proglumide (drug)]] | 0.5 µM | 68,756 | -0.02 |  |
| D12 | [[Neratinib (drug)]] | 0.5 µM | 104,629 | +0.59 |  |
| E1 | [[Meloxicam (drug)]] | 0.5 µM | 62,077 | -0.17 |  |
| E2 | [[Piroxicam (drug)]] | 0.5 µM | 83,248 | +0.26 |  |
| E3 | [[Nafamostat (mesylate) (drug)]] | 0.5 µM | 62,388 | -0.16 |  |
| E4 | [[Idoxuridine (drug)]] | 0.5 µM | 59,515 | -0.23 |  |
| E5 | [[Atazanavir (sulfate) (drug)]] | 0.5 µM | 57,623 | -0.27 |  |
| E6 | [[Malotilate (drug)]] | 0.5 µM | 71,936 | +0.05 |  |
| E7 | [[Pioglitazone (drug)]] | 0.5 µM | 45,601 | -0.61 |  |
| E8 | [[Bexarotene (drug)]] | 0.5 µM | 81,063 | +0.22 |  |
| E9 | [[Tazarotene (drug)]] | 0.5 µM | 60,132 | -0.21 |  |
| E10 | [[Vandetanib (drug)]] | 0.5 µM | 52,677 | -0.40 |  |
| E11 | [[Delamanid (drug)]] | 0.5 µM | 70,528 | +0.02 |  |
| E12 | [[Ivermectin (drug)]] | 0.5 µM | 38,339 | -0.86 |  |
| F1 | [[Citalopram (hydrobromide) (drug)]] | 0.5 µM | 38,047 | -0.87 |  |
| F2 | [[Acetazolamide (drug)]] | 0.5 µM | 59,476 | -0.23 |  |
| F3 | [[Fulvestrant (drug)]] | 0.5 µM | 51,401 | -0.44 |  |
| F4 | [[Talc (drug)]] | 0.5 µM | 63,167 | -0.14 |  |
| F5 | [[Pentoxifylline (drug)]] | 0.5 µM | 62,839 | -0.15 |  |
| F6 | [[Artemether (drug)]] | 0.5 µM | 62,959 | -0.15 |  |
| F7 | [[Cyclosporin A (drug)]] | 0.5 µM | 55,880 | -0.32 |  |
| F8 | [[Crizotinib (hydrochloride) (drug)]] | 0.5 µM | 43,206 | -0.69 |  |
| F9 | [[Trametinib (drug)]] | 0.5 µM | 71,070 | +0.03 |  |
| F10 | [[Fedratinib (hydrochloride hydrate) (drug)]] | 0.5 µM | 74,064 | +0.09 |  |
| F11 | [[Darolutamide (drug)]] | 0.5 µM | 74,952 | +0.11 |  |
| F12 | [[γ-Oryzanol (drug)]] | 0.5 µM | 62,820 | -0.15 |  |
| G1 | [[Clobetasol propionate (drug)]] | 0.5 µM | 52,781 | -0.40 |  |
| G2 | [[Budesonide (drug)]] | 0.5 µM | 56,076 | -0.31 |  |
| G3 | [[Cinacalcet (drug)]] | 0.5 µM | 56,569 | -0.30 |  |
| G4 | [[Valdecoxib (drug)]] | 0.5 µM | 45,462 | -0.62 |  |
| G5 | [[Pimozide (drug)]] | 0.5 µM | 42,295 | -0.72 |  |
| G6 | [[Methotrexate (drug)]] | 0.5 µM | 82,665 | +0.25 |  |
| G7 | [[5-Fluorouracil (drug)]] | 0.5 µM | 74,841 | +0.10 |  |
| G8 | [[Ixazomib citrate (drug)]] | 0.5 µM | 55,962 | -0.32 |  |
| G9 | [[5-Azacytidine (drug)]] | 0.5 µM | 52,478 | -0.41 |  |
| G10 | [[Aspirin (drug)]] | 0.5 µM | 65,888 | -0.08 |  |
| G11 | [[Vismodegib (drug)]] | 0.5 µM | 56,438 | -0.30 |  |
| G12 | [[Dihydroartemisinin (drug)]] | 0.5 µM | 71,178 | +0.03 |  |
| H1 | [[Lactate (calcium) (drug)]] | 0.5 µM | 53,811 | -0.37 |  |
| H2 | [[Ouabain (Octahydrate) (drug)]] | 0.5 µM | 50,916 | -0.45 |  |
| H3 | [[Gefitinib (drug)]] | 0.5 µM | 92,835 | +0.41 |  |
| H4 | [[Methylthiouracil (drug)]] | 0.5 µM | 91,663 | +0.40 |  |
| H5 | [[Binimetinib (drug)]] | 0.5 µM | 89,614 | +0.36 |  |
| H6 | [[Perindopril (erbumine) (drug)]] | 0.5 µM | 121,218 | +0.80 |  |
| H7 | [[Dapagliflozin (drug)]] | 0.5 µM | 129,375 | +0.89 |  |
| H8 | [[Panobinostat (drug)]] | 0.5 µM | 79,133 | +0.18 |  |
| H9 | [[Uridine (drug)]] | 0.5 µM | 116,418 | +0.74 |  |
| H10 | [[Adagrasib (drug)]] | 0.05 µM | 86,481 | +0.31 | ⚠ position not correctable |
| H11 | DMSO | — | 84,649 | +0.28 | ⚠ position not correctable · DMSO |
| H12 | DMSO | — | 95,423 | +0.45 | ⚠ position not correctable · DMSO |
