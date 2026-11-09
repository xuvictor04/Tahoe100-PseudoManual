---
symbol: "EFNB2"
type: "gene"
col: 4599
ensembl_id: "ENSG00000125266"
name: "ephrin B2"
location: "13q33.3"
module: 109
arm: "+"
pooled_cpm: 100.33
n_lines_expressing: 35
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 15
direction_downstream: 27
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# EFNB2

*ephrin B2* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.02× (z +20.2, q 0e+00, up in 28 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.622× (z -5.9, q 2e-06, down in 21 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB1]] (+0.67, fdr 7e-06), [[PTPRN2]] (+0.63, fdr 7e-06), [[LINC00460]] (+0.63, fdr 7e-06); moves opposite to [[NAPB]] (-0.55, fdr 1e-05), [[SEC61A2]] (-0.54, fdr 3e-05), [[FHIP2A]] (-0.51, fdr 2e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LINC00460]] → it (grade B ⚠); 27 go from it, the strongest it → [[STK17B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.02×** | +20.2 | 0e+00 | 28/33 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.51×** | +11.5 | 6e-28 | 24/33 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +11.0 | 7e-26 | 25/33 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.77×** | +7.4 | 2e-11 | 21/33 (A498, J82, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +5.7 | 1e-06 | 22/34 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.63×** | +5.0 | 6e-05 | 17/33 (A498, HS-578T, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 19/33 (C32, RPMI-7951, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.93×** | +4.5 | 6e-04 | 18/33 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.018 | 18/32 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +3.6 | 0.018 | 18/33 (Panc 03.27, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.046 | 14/33 (NCI-H1573, CHP-212, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.38×** | +3.3 | 0.046 | 16/33 (A498, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.622×** | -5.9 | 2e-06 | 21/32 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.564×** | -5.8 | 2e-06 | 27/33 (LS 180, RKO, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.660×** | -4.9 | 1e-04 | 22/33 (SW480, LS 180, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.766×** | -4.9 | 2e-04 | 23/33 (RKO, RPMI-7951, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.646×** | -4.8 | 2e-04 | 18/35 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.771×** | -4.7 | 3e-04 | 19/33 (SW480, COLO 205, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -4.6 | 3e-04 | 17/32 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.724×** | -4.2 | 0.002 | 20/32 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -4.1 | 0.003 | 18/30 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[MK-3903 (drug)]] 5 µM |  | **0.549×** | -4.0 | 0.003 | 22/33 (LoVo, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.718×** | -4.0 | 0.004 | 17/31 (LS 180, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.728×** | -3.9 | 0.004 | 18/33 (RKO, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.746×** | -3.8 | 0.007 | 17/34 (SW480, LoVo, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.013 | 16/33 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.824×** | -3.4 | 0.025 | 14/34 (SW480, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.807×** | -3.4 | 0.028 | 12/33 (SW480, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.722×** | -3.3 | 0.029 | 18/33 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -3.3 | 0.029 | 13/34 (RKO, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 319 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -10.3) |
| [[SW480 (line)]] | alt | 368 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.05 µM 0.487× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 278 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 35.6 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +26.6) | — |
| [[Hs 766T (line)]] | wt | 211 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 204 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.337× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 250 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.48× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 43.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +19.8) | — |
| [[LoVo (line)]] | wt | 251 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.384× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 70.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +20.6) | — |
| [[HS-578T (line)]] | alt | 28.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +19.2) | — |
| [[NCI-H1573 (line)]] | alt | 56.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +18.0) | — |
| [[NCI-H2347 (line)]] | alt | 60.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +16.0) | — |
| [[SW 900 (line)]] | alt | 43.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +18.5) | — |
| [[HT-29 (line)]] | alt | 135 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +18.2) | — |
| [[KATO III (line)]] | alt | 202 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -14.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 324 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 34.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 500 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 82.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.9) | — |
| [[J82 (line)]] | alt | 58.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 150 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.3) | — |
| [[SNU-423 (line)]] | alt | 52.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 21.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PTPRN2]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[LINC00460]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[BCL2L1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MCL1]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[EGR1]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[EGR3]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CASC19]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RGS2]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SGMS2]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[FOS]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPB]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.54 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[FHIP2A]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LINC00115]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PCMTD1]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CASC3]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[PI4K2B]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[COPS7B]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[DCUN1D4]] | -0.48 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[CDC23]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00460]] | B | LINC00460 activity raises EFNB2's level | lines that do not express LINC00460 (31) vs lines expressing it (19) | 3.57× lower at baseline in the lines without LINC00460 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02335, LINC01605, KISS1 |
| [[ANO1]] | B | ANO1 activity raises EFNB2's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.44× lower at baseline in the lines without ANO1 | 0.012 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[EPHA4]] | B | EPHA4 activity raises EFNB2's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without EPHA4 | 0.014 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |
| [[SERPINB5]] | B | SERPINB5 activity raises EFNB2's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without SERPINB5 | 0.029 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[SLC22A3]] | B | SLC22A3 activity raises EFNB2's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 3.39× lower at baseline in the lines without SLC22A3 | 0.050 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[MAP2K1]] | B | MAP2K1 activity raises EFNB2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[GJB3]] | B | GJB3 activity raises EFNB2's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.97× lower at baseline in the lines without GJB3 | 0.056 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[KLF5]] | B | KLF5 activity raises EFNB2's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without KLF5 | 0.058 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[SGPP2]] | B | SGPP2 activity raises EFNB2's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.39× lower at baseline in the lines without SGPP2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[KRT6A]] | B | KRT6A activity raises EFNB2's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 4.09× lower at baseline in the lines without KRT6A | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[MAML2]] | B | MAML2 activity raises EFNB2's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 2.45× lower at baseline in the lines without MAML2 | 0.087 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises EFNB2's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without ST3GAL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 25, C 2. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK17B]] | B | EFNB2 activity raises STK17B's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without EFNB2 | 0.001 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[EMP1]] | B | EFNB2 activity raises EMP1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 3.49× lower at baseline in the lines without EFNB2 | 0.001 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[RAPGEF6]] | B | EFNB2 activity lowers RAPGEF6's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.37× higher at baseline in the lines without EFNB2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[KLF5]] | B | EFNB2 activity raises KLF5's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without EFNB2 | 0.012 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[MAML2]] | B | EFNB2 activity raises MAML2's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.30× lower at baseline in the lines without EFNB2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[UTP14A]] | B | EFNB2 activity lowers UTP14A's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.51× higher at baseline in the lines without EFNB2 | 0.018 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[ANO1]] | B | EFNB2 activity raises ANO1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without EFNB2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[ST3GAL1]] | B | EFNB2 activity raises ST3GAL1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without EFNB2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[MAFB]] | B | EFNB2 activity raises MAFB's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without EFNB2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[GJB3]] | B | EFNB2 activity raises GJB3's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without EFNB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[SERBP1]] | B | EFNB2 activity lowers SERBP1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.29× higher at baseline in the lines without EFNB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[MAML2]] | B | EFNB2 activity strengthens MAML2's drug response | lines that do not express EFNB2 (10) vs lines expressing it (31) | the lines without EFNB2 respond 0.78× as strongly (z diff +1.65); strongest at Panobinostat 0.5 µM: 0.48x vs 0.31x (z diff +3.4) | 0.047 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.5, 2.0); signed map (7.6, 35.8). **Vector** length 133, 41.2% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +20.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +11.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.9 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.5 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ephrin B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.3 — chr13:106,489,745-106,535,662 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LERK5, Htk-L, HTKL, MGC126226, MGC126227, MGC126228; previously EPLG5 |
| Gene groups (HGNC) | Ephrins |
| Reactome | 6 pathways, smallest: Ephrin signaling; EPHB-mediated forward signaling; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P52799](https://www.uniprot.org/uniprotkb/P52799) (Ephrin-B2):

> Cell surface transmembrane ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binds promiscuously Eph receptors residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to …

**Summary**, from NCBI Gene [1948](https://www.ncbi.nlm.nih.gov/gene/1948):

> This gene encodes a member of the ephrin (EPH) family. The ephrins and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, especially in the nervous system and in erythropoiesis. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which …

**Accessions** — [HGNC:3227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3227) · Entrez [1948](https://www.ncbi.nlm.nih.gov/gene/1948) · UniProt [P52799](https://www.uniprot.org/uniprotkb/P52799) · Ensembl [ENSG00000125266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125266)

## Data

Gene col 4599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4599); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4599]; `tensor/DDL_lfc|DDL_z.npy` [4599]; `embed/gene_vectors.npy` [4599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4599 or target_col == 4599). Every well: [[EFNB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFNB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
