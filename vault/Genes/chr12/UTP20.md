---
symbol: "UTP20"
type: "gene"
col: 4222
ensembl_id: "ENSG00000120800"
name: "UTP20 small subunit processome component"
location: "12q23.2"
module: 1
arm: "+"
pooled_cpm: 48.43
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 8
n_dd_up_clean: 28
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# UTP20

*UTP20 small subunit processome component* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.49× (z +21.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.631× (z -7.8, q 2e-12, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCE1]] (+0.84, fdr 7e-06), [[GPATCH4]] (+0.83, fdr 7e-06), [[DHX37]] (+0.83, fdr 7e-06); moves opposite to [[ANG]] (-0.75, fdr 7e-06), [[KMT5C]] (-0.75, fdr 7e-06), [[ARL3]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +21.8 | 0e+00 | 48/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +17.6 | 0e+00 | 46/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +15.9 | 0e+00 | 46/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.53×** | +15.7 | 0e+00 | 47/48 (NCI-H460, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.52×** | +15.0 | 0e+00 | 44/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.07×** | +12.2 | 2e-32 | 40/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +12.0 | 3e-31 | 42/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +11.5 | 7e-29 | 47/48 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +9.7 | 2e-20 | 40/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +9.1 | 3e-18 | 37/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.79×** | +9.1 | 4e-18 | 29/45 (A498, Hs 766T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.71×** | +9.0 | 1e-17 | 37/45 (A498, A549, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +9.0 | 1e-17 | 38/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.68×** | +8.5 | 1e-15 | 31/43 (A498, NCI-H1573, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +8.0 | 4e-14 | 33/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +8.0 | 5e-14 | 34/48 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.37×** | +7.6 | 8e-13 | 40/48 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +7.6 | 1e-12 | 37/49 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.21×** | +7.0 | 8e-11 | 39/48 (A498, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.8 | 2e-10 | 35/48 (BT-474, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.631×** | -7.8 | 2e-12 | 42/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -6.7 | 8e-09 | 31/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.502×** | -6.1 | 2e-07 | 30/48 (NCI-H23, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.713×** | -5.8 | 1e-06 | 28/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.725×** | -5.5 | 5e-06 | 27/48 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.732×** | -5.3 | 9e-06 | 27/47 (SW48, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.776×** | -4.3 | 0.001 | 27/48 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.855× | -3.8 | 0.010 | 16/48 (KATO III, LS 180, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.033 | 15/48 (Hs 766T, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.836× | -3.4 | 0.036 | 14/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.079 | 11/48 (MIA PaCa-2, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.838× | -3.0 | 0.11 | 15/49 (MIA PaCa-2, NCI-H23, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.839× | -3.0 | 0.11 | 16/47 (Hs 766T, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 42.2 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +18.6) | — |
| [[A498 (line)]] | wt | 32.6 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +19.8) | — |
| [[NCI-H1792 (line)]] | alt | 38.0 | 7 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.90× (z +15.2) | — |
| [[NCI-H460 (line)]] | wt | 71.9 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 70.6 | 5 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.51× (z +10.8) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.468× (z -9.0) |
| [[A549 (line)]] | wt | 46.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 59.5 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.73× (z +14.8) | — |
| [[SW480 (line)]] | alt | 68.6 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.364× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 25.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +13.6) | — |
| [[C32 (line)]] | wt | 50.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +13.6) | — |
| [[HOP62 (line)]] | alt | 30.6 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.91× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 24.3 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.6) | [[PF-06260933 (drug)]] 5 µM 0.0599× (z -9.3) |
| [[HS-578T (line)]] | alt | 25.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 23.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +15.0) | — |
| [[J82 (line)]] | alt | 49.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.0) | — |
| [[LoVo (line)]] | wt | 55.4 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 114 | 2 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 31.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +17.3) | — |
| [[SW 900 (line)]] | alt | 19.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 44.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 23.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +13.9) | — |
| [[H4 (line)]] | wt | 31.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 43.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 35.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +15.7) | — |
| [[A-172 (line)]] | wt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.9) | — |
| [[A-427 (line)]] | wt | 72.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 24.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +17.4) | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.45× (z +10.9) | — |
| [[RKO (line)]] | wt | 81.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 71.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 62.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-1 (line)]] | wt | 65.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCE1]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 | STRING 427 |
| [[GPATCH4]] | +0.83 | +0.84 / +0.78 | both halves | 7e-06 |  |
| [[DHX37]] | +0.83 | +0.82 / +0.79 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 975 |
| [[DNAJC11]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[TTC27]] | +0.78 | +0.80 / +0.70 | both halves | 7e-06 | STRING 610 |
| [[ZNF507]] | +0.78 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | STRING 522 |
| [[UTP15]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[METAP1D]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[NOL11]] | +0.75 | +0.79 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 979 |
| [[LTV1]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 805 |
| [[MAK16]] | +0.73 | +0.71 / +0.81 | both halves | 7e-06 | STRING 415 |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANG]] | -0.75 | -0.73 / -0.69 | both halves | 7e-06 |  |
| [[KMT5C]] | -0.75 | -0.71 / -0.71 | both halves | 7e-06 |  |
| [[ARL3]] | -0.74 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[ANKRD37]] | -0.74 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[PJA2]] | -0.74 | -0.75 / -0.59 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.72 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[PLEKHH3]] | -0.71 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[AHDC1]] | -0.70 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[MINDY2]] | -0.70 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.69 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[GUK1]] | -0.69 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[NDRG1]] | -0.69 | -0.65 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity lowers UTP20's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.49× higher at baseline in the lines without NR3C2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity lowers UTP20's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.86× higher at baseline in the lines without NDRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[TLR4]] | B | TLR4 activity lowers UTP20's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.42× higher at baseline in the lines without TLR4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |
| [[TNFRSF11A]] | B | TNFRSF11A activity lowers UTP20's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.29× higher at baseline in the lines without TNFRSF11A | 0.068 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[FHIP1A]] | B | FHIP1A activity lowers UTP20's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.38× higher at baseline in the lines without FHIP1A | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UTP20's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UTP20's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[YPEL3]] | B | YPEL3 activity lowers UTP20's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.45× higher at baseline in the lines without YPEL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[SLC9B2]] | C | SLC9B2 activity raises UTP20's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.39× lower at baseline in the lines without SLC9B2 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.812). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.9, -33.6); signed map (2.5, -41.6). **Vector** length 130, 44.7% of its response variance represented; |z| ≥ 3 in 1,580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.7 | +15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +8.4 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +7.6 | +9.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +7.4 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +17.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +8.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.2 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +5.2 | +6.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.7 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.5 | -7.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.0 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.6 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | UTP20 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:101,280,105-101,386,618 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRIM, 1A6/DRIM |
| Gene groups (HGNC) | SSU processome; Armadillo like helical domain containing |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O75691](https://www.uniprot.org/uniprotkb/O75691) (Small subunit processome component 20 homolog):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in 18S pre-rRNA processing. Associates with U3 snoRNA.

**Summary**, from NCBI Gene [27340](https://www.ncbi.nlm.nih.gov/gene/27340):

> UTP20 is a component of the U3 small nucleolar RNA (snoRNA) (SNORD3A; MIM 180710) protein complex (U3 snoRNP) and is involved in 18S rRNA processing (Wang et al., 2007 [PubMed 17498821]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:17897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17897) · Entrez [27340](https://www.ncbi.nlm.nih.gov/gene/27340) · UniProt [O75691](https://www.uniprot.org/uniprotkb/O75691) · Ensembl [ENSG00000120800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120800)

## Data

Gene col 4222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4222); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4222]; `tensor/DDL_lfc|DDL_z.npy` [4222]; `embed/gene_vectors.npy` [4222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4222 or target_col == 4222). Every well: [[UTP20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
