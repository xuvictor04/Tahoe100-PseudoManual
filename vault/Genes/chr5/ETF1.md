---
symbol: "ETF1"
type: "gene"
col: 4211
ensembl_id: "ENSG00000120705"
name: "eukaryotic translation termination factor 1"
location: "5q31.2"
module: 198
arm: "+"
pooled_cpm: 165.03
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 11
n_dd_up_clean: 19
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# ETF1

*eukaryotic translation termination factor 1* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.08× (z +17.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.695× (z -6.8, q 8e-09, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYS1-DBNDD2]] (+0.61, fdr 1e-05), [[SMG1P6]] (+0.60, fdr 3e-05), [[HNRNPC]] (+0.58, fdr 7e-06); moves opposite to [[UBA3]] (-0.65, fdr 1e-05), [[MTFMT]] (-0.58, fdr 2e-05), [[RWDD3]] (-0.57, fdr 1e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.08×** | +17.5 | 0e+00 | 48/49 (LoVo, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.66×** | +14.9 | 0e+00 | 48/48 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +12.8 | 2e-35 | 45/48 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +12.6 | 3e-34 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +12.4 | 2e-33 | 36/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.69×** | +9.7 | 2e-20 | 44/49 (SW480, NCI-H23, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +9.0 | 3e-17 | 44/48 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.61×** | +8.2 | 1e-14 | 32/45 (SW480, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.55×** | +7.8 | 3e-13 | 34/44 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +7.6 | 2e-12 | 44/48 (Hs 766T, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.48×** | +7.3 | 2e-11 | 37/48 (NCI-H460, BT-474, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.9 | 2e-10 | 33/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 1e-09 | 32/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.39×** | +5.9 | 1e-07 | 35/47 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +5.1 | 1e-05 | 23/49 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.68×** | +5.0 | 2e-05 | 39/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +4.8 | 7e-05 | 35/48 (PANC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 1e-04 | 27/48 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 27/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +4.5 | 2e-04 | 30/48 (LOX-IMVI, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 9e-04 | 31/48 (LoVo, RKO, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.003 | 28/48 (LoVo, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.695×** | -6.8 | 8e-09 | 39/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.792×** | -6.1 | 3e-07 | 30/48 (AsPC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.737×** | -5.4 | 1e-05 | 33/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.835× | -4.6 | 6e-04 | 23/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.782×** | -4.6 | 6e-04 | 35/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.799×** | -4.2 | 0.002 | 25/49 (KATO III, CHP-212, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.800×** | -4.2 | 0.002 | 29/48 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.853× | -4.2 | 0.002 | 18/48 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.804×** | -3.9 | 0.006 | 26/48 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.824×** | -3.6 | 0.016 | 22/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.811×** | -3.6 | 0.016 | 27/48 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -3.6 | 0.016 | 13/48 (A498, CHP-212, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.016 | 21/49 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.838× | -3.3 | 0.039 | 22/47 (A-427, J82, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.840× | -3.2 | 0.044 | 16/48 (CHP-212, AN3 CA, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.799×** | -3.0 | 0.098 | 15/48 (A549, NCI-H1573, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 167 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +23.1) | — |
| [[SW480 (line)]] | alt | 146 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 154 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 220 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.64× (z +15.0) | — |
| [[SK-MEL-2 (line)]] | alt | 204 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 213 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.0) | [[Selinexor (drug)]] 5 µM 0.524× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 119 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.05× (z +10.8) | — |
| [[H4 (line)]] | wt | 174 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 170 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 6.87× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 123 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 266 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 140 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.87× (z +10.0) | — |
| [[LoVo (line)]] | wt | 201 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 9.26× (z +19.0) | — |
| [[LOX-IMVI (line)]] | wt | 137 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.52× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 123 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 8.07× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 208 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.66× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 149 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 9.54× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 168 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.45× (z +9.9) | — |
| [[A-172 (line)]] | wt | 87.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.32× (z +14.4) | — |
| [[A-427 (line)]] | wt | 237 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.60× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.587× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 161 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.64× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 186 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.49× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 144 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +11.5) | — |
| [[A549 (line)]] | wt | 157 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 190 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 24.8× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.4) | — |
| [[KATO III (line)]] | alt | 94.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.94× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 114 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 166 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.56× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.57× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 158 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.69× (z +13.3) | — |
| [[RKO (line)]] | wt | 171 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.83× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 225 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.40× (z +10.5) | — |
| [[A498 (line)]] | wt | 167 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.91× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 182 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.50× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 136 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +10.3) | — |
| [[C32 (line)]] | wt | 141 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 137 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.54× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 203 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.08× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 194 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.93× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 136 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.87× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 208 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 169 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYS1-DBNDD2]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SMG1P6]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[HNRNPC]] | +0.58 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PPIEL]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SMU1]] | +0.56 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[SSU72]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[FAM53A]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[HCG18]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.55 | +0.32 / +0.63 | both halves | 1e-04 |  |
| [[SEC16A]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ARPC4]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SECISBP2]] | +0.53 | +0.39 / +0.63 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA3]] | -0.65 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[MTFMT]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[RWDD3]] | -0.57 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[MBIP]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PAPOLG]] | -0.56 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[NDUFB4]] | -0.56 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[TRAF6]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MRPL39]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[FBXL3]] | -0.55 | -0.31 / -0.65 | both halves | 2e-04 |  |
| [[CNIH4]] | -0.55 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[XPA]] | -0.55 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[FBXO3]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction -0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.0, -24.2); signed map (16.2, -39.7). **Vector** length 116, 43.9% of its response variance represented; |z| ≥ 3 in 1,454 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +8.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +7.6 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +7.0 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +7.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +14.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.3 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.2 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -5.0 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation termination factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,506,095-138,543,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eRF1, TB3-1, RF1; previously SUP45L1, ERF1, ERF |
| Gene groups (HGNC) | SURF complex |
| Hallmark sets | APOPTOSIS, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation; Eukaryotic Translation Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [P62495](https://www.uniprot.org/uniprotkb/P62495) (Eukaryotic peptide chain release factor subunit 1):

> Component of the eRF1-eRF3-GTP ternary complex, a ternary complex that mediates translation termination in response to the termination codons. The eRF1-eRF3-GTP complex binds to a stop codon in the ribosomal A-site. ETF1/ERF1 is responsible for stop codon recognition and inducing hydrolysis of peptidyl-tRNA. Following GTP hydrolysis, eRF3 (GSPT1/ERF3A or GSPT2/ERF3B) dissociates, permitting ETF1/eRF1 to accommodate fully in the A-site and mediate hydrolysis of peptidyl-tRNA. Component of the …

**Summary**, from NCBI Gene [2107](https://www.ncbi.nlm.nih.gov/gene/2107):

> This gene encodes a class-1 polypeptide chain release factor. The encoded protein plays an essential role in directing termination of mRNA translation from the termination codons UAA, UAG and UGA. This protein is a component of the SURF complex which promotes degradation of prematurely terminated mRNAs via the mechanism of nonsense-mediated mRNA decay (NMD). Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 6, 7, and X. [provided by …

**Accessions** — [HGNC:3477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3477) · Entrez [2107](https://www.ncbi.nlm.nih.gov/gene/2107) · UniProt [P62495](https://www.uniprot.org/uniprotkb/P62495) · Ensembl [ENSG00000120705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120705)

## Data

Gene col 4211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4211); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4211]; `tensor/DDL_lfc|DDL_z.npy` [4211]; `embed/gene_vectors.npy` [4211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4211 or target_col == 4211). Every well: [[ETF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
