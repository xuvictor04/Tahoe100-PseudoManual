---
symbol: "FNBP4"
type: "gene"
col: 3094
ensembl_id: "ENSG00000109920"
name: "formin binding protein 4"
location: "11p11.2"
module: 12
arm: "+"
pooled_cpm: 240.0
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# FNBP4

*formin binding protein 4* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +16.1, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.716× (z -8.7, q 2e-15, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.831× (z -6.8, q 2e-09, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC59]] (+0.69, fdr 1e-05), [[WHAMM]] (+0.69, fdr 1e-05), [[SNW1]] (+0.68, fdr 1e-05); moves opposite to [[FKBP1A]] (-0.66, fdr 1e-05), [[ITGB1]] (-0.61, fdr 3e-05), [[APMAP]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Hesperidin (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +16.1 | 0e+00 | 42/48 (BT-474, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +13.7 | 2e-40 | 45/48 (SW48, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +10.6 | 8e-24 | 46/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +9.9 | 5e-21 | 43/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +9.2 | 3e-18 | 39/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.6 | 3e-12 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +7.2 | 6e-11 | 33/48 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +6.8 | 5e-10 | 29/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +6.6 | 2e-09 | 37/48 (KATO III, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +6.5 | 4e-09 | 34/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 3e-07 | 26/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +5.0 | 3e-05 | 25/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 3e-05 | 33/45 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 2e-04 | 23/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 32/49 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.3 | 7e-04 | 21/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 9e-04 | 28/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.716×** | -8.7 | 2e-15 | 36/48 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.722×** | -8.5 | 8e-15 | 41/48 (H4, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.727×** | -8.3 | 2e-14 | 38/48 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -6.8 | 2e-09 | 26/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.772×** | -6.7 | 2e-09 | 35/49 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.769×** | -6.3 | 3e-08 | 28/49 (SNU-423, A498, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.788×** | -6.2 | 5e-08 | 34/48 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.782×** | -6.1 | 6e-08 | 24/44 (SNU-1, AN3 CA, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.799×** | -5.4 | 5e-06 | 26/45 (A-427, NCI-H23, …) | all doses, flat | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.874× | -3.5 | 0.027 | 12/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.796× | -3.1 | 0.10 | 20/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 172 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +12.7) | — |
| [[LoVo (line)]] | wt | 263 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +14.4) | [[Belinostat (drug)]] 5 µM 0.661× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 313 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.28× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.585× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 266 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 223 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 245 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.461× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 255 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.564× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 192 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 198 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +15.5) | — |
| [[RKO (line)]] | wt | 293 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.537× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 276 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.558× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 224 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.503× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 172 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.7) | — |
| [[H4 (line)]] | wt | 226 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.397× (z -11.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 175 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 194 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.466× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 312 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.626× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 276 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 2.70× (z +11.8) | — |
| [[A498 (line)]] | wt | 261 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.504× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 248 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 249 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.10× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 256 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.55× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 298 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.521× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 215 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 196 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.85× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.513× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 238 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.88× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.537× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 296 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 301 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.529× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 271 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.2) | — |
| [[AN3 CA (line)]] | alt | 261 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 290 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 1.70× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 309 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.638× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 373 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.71× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 227 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.524× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 166 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 291 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 1088 (line)]] | alt | 212 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.153× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 284 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 179 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 373 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC59]] | +0.69 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[WHAMM]] | +0.69 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[SNW1]] | +0.68 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.67 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.66 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[UPF3B]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[MPHOSPH8]] | +0.64 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[PPIG]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ATF5]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP1A]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[ITGB1]] | -0.61 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[APMAP]] | -0.61 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MED14]] | -0.61 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[USB1]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ABI2]] | -0.59 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ITM2C]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ACTB]] | -0.57 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[MDH2]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[BRK1]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[HPSE]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FNBP4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises FNBP4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Hesperidin (drug)]] 0.05 µM | C | FNBP4's natural level lowers the cells' numbers under Hesperidin 0.05 µM (makes them more sensitive) | FNBP4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.084 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.8, 2.6); signed map (1.4, -15.0). **Vector** length 119, 39.6% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +16.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +1.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.8 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +6.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.1 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.0 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -6.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -1.4 |
|  | [[Adenine (drug)]] 5 µM |  | -2.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | formin binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,716,494-47,767,443 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1014 |
| Matched by | ensembl_id |

UniProt [Q8N3X1](https://www.uniprot.org/uniprotkb/Q8N3X1) carries no function annotation.

**Summary**, from NCBI Gene [23360](https://www.ncbi.nlm.nih.gov/gene/23360):

> This gene encodes a protein containing two tryptophan-rich WW domains that binds the proline-rich formin homology 1 domains of formin family proteins, suggesting a role in the regulation of cytoskeletal dynamics during cell division and migration. It also binds intersectin family proteins suggesting a role in the maintenance of membrane curvature at sites of nascent vesicle formation. Naturally occurring mutations in this gene are associated with Waardenburg anophthalmia syndrome. [provided by …

**Accessions** — [HGNC:19752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19752) · Entrez [23360](https://www.ncbi.nlm.nih.gov/gene/23360) · UniProt [Q8N3X1](https://www.uniprot.org/uniprotkb/Q8N3X1) · Ensembl [ENSG00000109920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109920)

## Data

Gene col 3094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3094); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3094]; `tensor/DDL_lfc|DDL_z.npy` [3094]; `embed/gene_vectors.npy` [3094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3094 or target_col == 3094). Every well: [[FNBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
