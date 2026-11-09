---
symbol: "MATN2"
type: "gene"
col: 5338
ensembl_id: "ENSG00000132561"
name: "matrilin 2"
location: "8q22.1-q22.2"
module: 166
arm: "+"
pooled_cpm: 10.78
n_lines_expressing: 45
n_dd_up: 34
n_dd_down: 18
n_dd_up_clean: 26
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# MATN2

*matrilin 2* — 8q22.1-q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.24× (z +16.3, q 0e+00, up in 14 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +14.9, q 0e+00, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.546× (z -8.8, q 8e-16, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC80]] (+0.62, fdr 7e-06), [[PLXNC1]] (+0.62, fdr 2e-05), [[HDAC2-AS2]] (+0.62, fdr 1e-05); moves opposite to [[PHC2]] (-0.61, fdr 3e-05), [[MT2A]] (-0.60, fdr 1e-05), [[ANGPTL4]] (-0.58, fdr 3e-05).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC01151]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +16.3 | 0e+00 | 14/17 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +14.9 | 0e+00 | 29/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +12.6 | 3e-34 | 21/31 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +9.6 | 1e-19 | 16/25 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +8.8 | 1e-16 | 21/42 (A498, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.8 | 6e-13 | 20/42 (PANC-1, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.59×** | +6.7 | 2e-09 | 19/40 (C32, NCI-H460, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +6.1 | 8e-08 | 19/43 (KATO III, J82, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.8 | 5e-07 | 14/37 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 2e-06 | 15/41 (C32, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.5 | 2e-06 | 13/39 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.45×** | +5.3 | 5e-06 | 17/41 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +5.2 | 9e-06 | 17/43 (C32, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 1e-05 | 14/40 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.2 | 8e-04 | 20/40 (A-172, C32, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.36×** | +4.2 | 0.001 | 13/40 (Panc 03.27, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.001 | 12/38 (BT-474, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.001 | 16/41 (C32, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -8.8 | 8e-16 | 22/41 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.548×** | -8.7 | 8e-16 | 25/38 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -8.4 | 6e-15 | 23/41 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -8.1 | 8e-14 | 22/39 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.660×** | -6.0 | 2e-07 | 19/41 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.793×** | -4.8 | 2e-04 | 13/42 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.724×** | -4.7 | 2e-04 | 10/40 (J82, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -4.2 | 0.002 | 15/40 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.757×** | -4.1 | 0.003 | 16/41 (NCI-H1792, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.749×** | -4.0 | 0.003 | 17/39 (KATO III, J82, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.759×** | -4.0 | 0.003 | 15/41 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.768×** | -3.8 | 0.006 | 12/40 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.768×** | -3.7 | 0.010 | 2/41 (HS-578T, SW1417) | top dose only | plate-row cell shift; position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.029 | 5/41 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.792×** | -3.1 | 0.065 | 9/37 (A-172, SW48, …) | all doses, flat | low cells (technical?) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.076 | 2/41 (SHP-77, hTERT-HPNE) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.815×** | -3.0 | 0.088 | 9/39 (SW 900, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 23.4 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0970× (z -12.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.170× (z -9.3) |
| [[A498 (line)]] | wt | 13.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +14.2) | — |
| [[A549 (line)]] | wt | 9.25 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +10.3) | — |
| [[J82 (line)]] | alt | 88.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.270× (z -8.6) |
| [[BT-474 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.114× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.29× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0662× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC80]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PLXNC1]] | +0.62 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[HDAC2-AS2]] | +0.62 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CCDC3]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[COL24A1]] | +0.59 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[GRIK4]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SGCD]] | +0.56 | +0.45 / +0.47 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[HSPB8]] | +0.55 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[LINC01725]] | +0.55 | +0.48 / +0.30 | both halves | 2e-04 |  |
| [[LUZP2]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MRAS]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[STARD4-AS1]] | +0.54 | +0.43 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2]] | -0.61 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[MT2A]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ANGPTL4]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MT1X]] | -0.55 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[STX1A]] | -0.51 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[CKLF]] | -0.51 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[RPGR]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[GGA1]] | -0.51 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[ETV5]] | -0.50 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[RGS17]] | -0.50 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[RMND1]] | -0.49 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[ZFYVE28]] | -0.49 | -0.52 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[MHENCR]] | -0.48 | -0.51 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MATN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM149A]] | B | FAM149A activity raises MATN2's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 1.28× lower at baseline in the lines without FAM149A | 0.055 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[MOXD1]] | B | MOXD1 activity raises MATN2's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without MOXD1 | 0.081 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01151]] | B | MATN2 activity lowers LINC01151's level | lines that do not express MATN2 (5) vs lines expressing it (45) | 2.29× higher at baseline in the lines without MATN2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, NAT14, KIF17; maybe low, not absent |
| [[SSPN]] | B | MATN2 activity raises SSPN's level | lines that do not express MATN2 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without MATN2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, NAT14, KIF17; maybe low, not absent |

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.490). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.4, 20.0); signed map (40.5, 18.0). **Vector** length 90.7, 18.2% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.3 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +5.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.7 | -4.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.0 | -4.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | matrilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1-q22.2 — chr8:97,868,840-98,036,724 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Matrilins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [O00339](https://www.uniprot.org/uniprotkb/O00339) (Matrilin-2):

> Involved in matrix assembly.

**Summary**, from NCBI Gene [4147](https://www.ncbi.nlm.nih.gov/gene/4147):

> This gene encodes a member of the von Willebrand factor A domain containing protein family. This family of proteins is thought to be involved in the formation of filamentous networks in the extracellular matrices of various tissues. This protein contains five von Willebrand factor A domains. The specific function of this gene has not yet been determined. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6908) · Entrez [4147](https://www.ncbi.nlm.nih.gov/gene/4147) · UniProt [O00339](https://www.uniprot.org/uniprotkb/O00339) · Ensembl [ENSG00000132561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132561)

## Data

Gene col 5338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5338); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5338]; `tensor/DDL_lfc|DDL_z.npy` [5338]; `embed/gene_vectors.npy` [5338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5338 or target_col == 5338). Every well: [[MATN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MATN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
