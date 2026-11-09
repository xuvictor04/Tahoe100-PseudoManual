---
symbol: "ATAD3B"
type: "gene"
col: 8296
ensembl_id: "ENSG00000160072"
name: "ATPase family AAA domain containing 3B"
location: "1p36.33"
module: 36
arm: "+"
pooled_cpm: 17.39
n_lines_expressing: 48
n_dd_up: 35
n_dd_down: 14
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ATAD3B

*ATPase family AAA domain containing 3B* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.27× (z +10.9, q 7e-25, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.77× (z +7.6, q 5e-12, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.632× (z -8.7, q 1e-15, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD3A]] (+0.88, fdr 7e-06, ⚠ same locus), [[DPH7]] (+0.74, fdr 7e-06), [[ZNF276]] (+0.73, fdr 7e-06), [[TOMM40]] (+0.73, fdr 7e-06); moves opposite to [[IFNAR1]] (-0.63, fdr 1e-05), [[RAB21]] (-0.60, fdr 1e-05), [[CHMP2B]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.27×** | +10.9 | 7e-25 | 39/46 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.16×** | +10.3 | 3e-22 | 38/46 (SW480, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.16×** | +10.2 | 4e-22 | 40/46 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.91×** | +8.6 | 1e-15 | 38/45 (SW480, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +7.6 | 5e-12 | 34/44 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.61×** | +6.3 | 3e-08 | 25/46 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.54×** | +5.7 | 8e-07 | 23/43 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.56×** | +5.7 | 1e-06 | 23/42 (NCI-H460, NCI-H2030, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.55×** | +5.6 | 1e-06 | 15/28 (LoVo, RPMI-7951, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +5.5 | 2e-06 | 26/43 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +5.5 | 3e-06 | 24/45 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.0 | 3e-05 | 20/45 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.43×** | +4.7 | 9e-05 | 19/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.46×** | +4.6 | 2e-04 | 15/32 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.91×** | +4.5 | 3e-04 | 20/43 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.4 | 4e-04 | 20/46 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.005 | 15/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.006 | 15/43 (Panc 03.27, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.014 | 19/45 (CFPAC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.021 | 11/46 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.027 | 10/43 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.035 | 8/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.044 | 10/44 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.054 | 10/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.072 | 10/44 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.632×** | -8.7 | 1e-15 | 32/46 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.655×** | -5.5 | 1e-05 | 28/43 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -4.7 | 5e-04 | 21/46 (A498, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.705×** | -4.5 | 0.001 | 20/44 (AsPC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -4.1 | 0.004 | 7/46 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.750×** | -3.9 | 0.009 | 15/45 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.790×** | -3.7 | 0.020 | 14/46 (SW48, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.769×** | -3.6 | 0.026 | 19/46 (J82, NCI-H23, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.616×** | -3.4 | 0.040 | 13/43 (Hs 766T, RKO, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.775×** | -3.3 | 0.059 | 17/44 (KATO III, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.790×** | -3.2 | 0.071 | 12/46 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.816×** | -3.2 | 0.077 | 13/46 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.791×** | -3.1 | 0.089 | 10/44 (NCI-H23, C-33 A, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.790×** | -3.0 | 0.089 | 4/46 (HT-29, SHP-77, …) | two highest doses |  |
| [[Adenosine (drug)]] 5 µM |  | 0.855× | -3.0 | 0.089 | 15/46 (A-172, SW480, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.089 | 13/46 (MIA PaCa-2, C-33 A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.198× (z -14.0) |
| [[SW480 (line)]] | alt | 16.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.36× (z +9.3) | — |
| [[A-427 (line)]] | wt | 21.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -15.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.399× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.364× (z -8.7) |
| [[LoVo (line)]] | wt | 18.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.78× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Selinexor (drug)]] 5 µM 0.337× (z -10.7) |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0498× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.119× (z -9.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 28.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.407× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 12.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.93× (z +9.2) ⚠ unreliable plate only | — |
| [[A-172 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD3A]] | +0.88 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; STRING 640; ⚠ same locus (14.3 kb, same strand: neighbours can correlate without regulation) |
| [[DPH7]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ZNF276]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CTU2]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[TREX2]] | +0.72 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[E2F4]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SRM]] | +0.71 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TELO2]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TRAP1]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GNB1L]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNAR1]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[RAB21]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CHMP2B]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TCEAL1]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TET2]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SNX16]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ATAD3B's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-4.9, -27.5); signed map (-46.2, -17.2). **Vector** length 101, 24.8% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +10.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.9 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.5 | +10.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.2 | +8.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.2 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.5 | +2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.4 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ATPase family AAA domain containing 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,471,765-1,497,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TOB3, KIAA1273 |
| Gene groups (HGNC) | AAA ATPases; Mitochondrial nucleoid associated proteins |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T9A4](https://www.uniprot.org/uniprotkb/Q5T9A4) (ATPase family AAA domain-containing protein 3B):

> May play a role in a mitochondrial network organization typical for stem cells, characterized by reduced mitochondrial metabolism, low mtDNA copies and fragmentated mitochondrial network. May act by suppressing ATAD3A function, interfering with ATAD3A interaction with matrix nucleoid complexes.

**Summary**, from NCBI Gene [83858](https://www.ncbi.nlm.nih.gov/gene/83858):

> The protein encoded by this gene is localized to the mitochondrial inner membrane, where it can bind to a highly-related protein, ATAD3A. ATAD3A appears to interact with matrix nucleoid complexes, and the encoded protein negatively regulates that interaction. This gene is expressed almost exclusively in pluripotent embryonic stem cells and some cancer cells. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:24007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24007) · Entrez [83858](https://www.ncbi.nlm.nih.gov/gene/83858) · UniProt [Q5T9A4](https://www.uniprot.org/uniprotkb/Q5T9A4) · Ensembl [ENSG00000160072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160072)

## Data

Gene col 8296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8296); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8296]; `tensor/DDL_lfc|DDL_z.npy` [8296]; `embed/gene_vectors.npy` [8296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8296 or target_col == 8296). Every well: [[ATAD3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATAD3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
