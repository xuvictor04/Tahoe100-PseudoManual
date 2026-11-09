---
drug: "Triamcinolone"
type: "drug"
salt_base: "Triamcinolone"
targets: "NR3C1"
moa_fine: "Glucocorticoid receptor agonist"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 496
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Triamcinolone

*Glucocorticoid receptor agonist (unclear) · targets: NR3C1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 215 / 474 / 496; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.75 / 0.69.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F7 | 89 / 126 | — | -0.02 | +0.4/+0.0/-0.8 | — |
| 0.5 µM | [[Plate 05]]:F7 | 154 / 320 | — | -0.00 | -0.0/+0.1/-0.8 | — |
| 5 µM | [[Plate 14]]:F7 | 241 / 255 | 0.719 | -0.20 | -0.3/-1.3/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (89 genes, none with an alert; 12 shown): [[FKBP5]] 5.02× (z +24.3, 30/42 lines), [[CCND3]] 2.82× (z +14.1, 31/47 lines), [[KLF9]] 2.08× (z +12.3, 32/43 lines), [[NNMT]] 2.66× (z +8.9, 19/24 lines), [[MAOA]] 1.83× (z +8.3, 15/34 lines), [[FGD4]] 1.47× (z +8.0, 19/38 lines), [[DNER]] 1.84× (z +7.9, 15/16 lines), [[IRAK3]] 2.08× (z +7.6, 10/12 lines), [[TSC22D3]] 2.39× (z +7.3, 25/36 lines), [[SAA1]] 4.64× (z +6.9, 15/19 lines), [[ABLIM3]] 1.62× (z +6.9, 20/33 lines), [[JPH2]] 1.76× (z +6.6, 17/27 lines)

**0.5 µM** (154 genes, none with an alert; 12 shown): [[FKBP5]] 7.77× (z +30.9, 30/41 lines), [[CCND3]] 2.98× (z +14.8, 33/47 lines), [[KLF9]] 2.37× (z +14.5, 33/43 lines), [[NNMT]] 4.03× (z +12.7, 20/24 lines), [[MAOA]] 2.44× (z +12.3, 17/32 lines), [[IRAK3]] 2.54× (z +10.2, 10/12 lines), [[ITGA10]] 2.79× (z +9.5, 24/35 lines), [[JPH2]] 2.24× (z +9.5, 18/27 lines), [[SAA1]] 7.83× (z +9.3, 15/19 lines), [[B3GNT5]] 1.68× (z +8.5, 25/41 lines), [[ABLIM3]] 1.79× (z +8.4, 22/33 lines), [[TSC22D3]] 2.67× (z +8.2, 32/36 lines)

**5 µM** (241 genes, none with an alert; 12 shown): [[FKBP5]] 4.93× (z +32.1, 30/42 lines), [[KLF9]] 2.00× (z +16.4, 31/43 lines), [[CCND3]] 2.20× (z +15.2, 33/47 lines), [[MAOA]] 1.90× (z +11.7, 18/34 lines), [[NNMT]] 2.47× (z +11.6, 21/24 lines), [[IRAK3]] 1.96× (z +10.4, 10/12 lines), [[ITGA10]] 2.10× (z +9.7, 27/37 lines), [[JPH2]] 1.77× (z +9.5, 20/28 lines), [[TSC22D3]] 2.20× (z +9.3, 28/37 lines), [[SAA1]] 4.09× (z +9.0, 16/19 lines), [[ABLIM3]] 1.51× (z +8.4, 19/33 lines), [[TMTC1]] 1.46× (z +8.3, 13/23 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (126 genes, none with an alert; 12 shown): [[ADAMTS16]] 0.661× (z -6.9, 17/23 lines), [[PTHLH]] 0.518× (z -6.6, 18/25 lines), [[PKIA]] 0.695× (z -6.3, 18/26 lines), [[HMGN2P46]] 0.547× (z -6.2, 20/30 lines), [[ENSG00000259354]] 0.577× (z -6.1, 24/30 lines), [[KIAA1217]] 0.724× (z -5.9, 24/38 lines), [[ENSG00000239462]] 0.632× (z -5.7, 19/30 lines), [[NAV3]] 0.674× (z -5.5, 17/32 lines), [[E2F7]] 0.743× (z -5.5, 22/43 lines), [[GJA1]] 0.660× (z -5.5, 12/22 lines), [[IGFBP3]] 0.587× (z -5.4, 20/28 lines), [[SYNJ2]] 0.787× (z -5.2, 23/44 lines)

**0.5 µM** (320 genes, none with an alert; 12 shown): [[WNT7B]] 0.481× (z -9.6, 16/27 lines), [[ADAMTS16]] 0.572× (z -9.4, 18/23 lines), [[ENSG00000259354]] 0.514× (z -7.8, 26/30 lines), [[MYO10]] 0.717× (z -7.7, 24/43 lines), [[PTHLH]] 0.465× (z -7.7, 18/24 lines), [[PKIA]] 0.649× (z -7.5, 18/25 lines), [[KIAA1217]] 0.683× (z -7.0, 23/38 lines), [[NAV3]] 0.607× (z -7.0, 20/32 lines), [[HMGN2P46]] 0.515× (z -6.8, 24/30 lines), [[AFF3]] 0.637× (z -6.7, 19/26 lines), [[BMP2]] 0.597× (z -6.6, 15/26 lines), [[LIF]] 0.561× (z -6.6, 25/38 lines)

**5 µM** (255 genes, none with an alert; 12 shown): [[WNT7B]] 0.602× (z -9.4, 19/28 lines), [[ADAMTS16]] 0.679× (z -9.2, 18/23 lines), [[MYO10]] 0.767× (z -8.7, 23/43 lines), [[CD44]] 0.734× (z -8.7, 27/33 lines), [[KIAA1217]] 0.718× (z -8.6, 24/38 lines), [[ENSG00000259354]] 0.600× (z -8.4, 26/30 lines), [[AFF3]] 0.675× (z -8.2, 16/26 lines), [[IGFBP3]] 0.580× (z -7.9, 23/28 lines), [[NAV3]] 0.686× (z -7.5, 21/32 lines), [[PKIA]] 0.741× (z -7.3, 20/26 lines), [[ADAM19]] 0.555× (z -7.2, 28/35 lines), [[NHS]] 0.699× (z -7.1, 21/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 098]] (+3.9), [[Module 097]] (+2.4), [[Module 139]] (+2.4) | [[Module 112]] (-2.5) |
| 0.5 µM | [[Module 098]] (+4.8), [[Module 139]] (+3.2), [[Module 097]] (+3.1) | [[Module 112]] (-3.2), [[Module 228]] (-3.1), [[Module 081]] (-2.8) |
| 5 µM | [[Module 098]] (+4.9), [[Module 139]] (+3.2), [[Module 104]] (+3.1) | [[Module 112]] (-3.2), [[Module 224]] (-3.0), [[Module 081]] (-2.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[H4 (line)]] (2.23), [[NCI-H1573 (line)]] (2.09), [[HOP62 (line)]] (2.00), [[HS-578T (line)]] (1.96) · weakest: [[COLO 205 (line)]] (0.215), [[SW480 (line)]] (0.249), [[SW1417 (line)]] (0.251) |
| 0.5 µM | — | [[H4 (line)]] (2.10), [[NCI-H1792 (line)]] (1.87), [[HS-578T (line)]] (1.83), [[NCI-H1573 (line)]] (1.82) · weakest: [[KATO III (line)]] (0.229), [[SW480 (line)]] (0.296), [[RKO (line)]] (0.304) |
| 5 µM | — | [[H4 (line)]] (2.08), [[HOP62 (line)]] (1.90), [[HS-578T (line)]] (1.80), [[Hs 766T (line)]] (1.74) · weakest: [[SW480 (line)]] (0.341), [[LS 180 (line)]] (0.393), [[A-427 (line)]] (0.397) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Betamethasone dipropionate (drug)]] (+0.68, Glucocorticoid receptor agonist); [[Citalopram (hydrobromide) (drug)]] (+0.64, unclear); [[Budesonide (drug)]] (+0.64, Glucocorticoid receptor agonist); [[Medroxyprogesterone acetate (drug)]] (+0.64, unclear); [[Dexamethasone (drug)]] (+0.62, Glucocorticoid receptor agonist); [[Phenylephrine (hydrochloride) (drug)]] (+0.60, Adrenoceptor agonist); [[Clobetasol propionate (drug)]] (+0.60, unclear); [[Econazole (drug)]] (+0.58, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Triamcinolone"
- `tables/drugdoses.parquet` — dd in 1042, 1043, 1044
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
