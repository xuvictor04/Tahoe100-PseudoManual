---
symbol: "ADAT2"
type: "gene"
col: 12076
ensembl_id: "ENSG00000189007"
name: "adenosine deaminase tRNA specific 2"
location: "6q24.2"
module: 18
arm: "+"
pooled_cpm: 14.34
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ADAT2

*adenosine deaminase tRNA specific 2* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.39× (z +11.9, q 5e-30, up in 15 of 21 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.85× (z +9.8, q 1e-20, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.597× (z -11.7, q 6e-29, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1E1]] (+0.83, fdr 7e-06), [[MDN1]] (+0.75, fdr 7e-06), [[TUBGCP4]] (+0.74, fdr 7e-06); moves opposite to [[GOLGB1]] (-0.67, fdr 7e-06), [[KMT2A]] (-0.63, fdr 9e-06), [[DNAL4]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DUXAP9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.39×** | +11.9 | 5e-30 | 15/21 (LS 180, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +11.9 | 5e-30 | 23/28 (LS 180, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.02×** | +11.2 | 6e-27 | 39/46 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +10.9 | 1e-25 | 30/41 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +9.8 | 1e-20 | 33/45 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.79×** | +9.2 | 3e-18 | 26/46 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.67×** | +8.2 | 2e-14 | 24/38 (LoVo, NCI-H1792, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.47×** | +6.1 | 7e-08 | 21/45 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 1e-07 | 22/45 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.9 | 3e-07 | 22/46 (NCI-H1792, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 5e-07 | 20/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.40×** | +5.4 | 4e-06 | 21/46 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.3 | 5e-06 | 16/46 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.87×** | +5.2 | 8e-06 | 16/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.37×** | +5.0 | 3e-05 | 17/46 (PANC-1, J82, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.80×** | +4.9 | 4e-05 | 10/45 (LOX-IMVI, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.77×** | +4.8 | 6e-05 | 14/44 (A498, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.70×** | +4.4 | 3e-04 | 14/42 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 5e-04 | 12/47 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.002 | 9/45 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.003 | 12/45 (SNU-1, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.003 | 2/44 (NCI-H460, AsPC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.016 | 7/45 (COLO 205, NCI-H1792, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.033 | 6/40 (NCI-H23, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.597×** | -11.7 | 6e-29 | 33/45 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.582×** | -4.5 | 0.002 | 13/46 (LoVo, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.801×** | -4.1 | 0.009 | 12/47 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.707×** | -4.0 | 0.009 | 12/44 (LoVo, RPMI-7951, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.009 | 15/46 (C32, LoVo, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.766×** | -3.7 | 0.023 | 12/45 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.857× | -3.5 | 0.030 | 11/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.657×** | -3.5 | 0.030 | 8/45 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.813×** | -3.3 | 0.051 | 7/45 (A498, LoVo, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.862× | -3.3 | 0.055 | 12/46 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.816×** | -3.2 | 0.062 | 11/46 (LoVo, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.871× | -3.2 | 0.075 | 7/46 (KATO III, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.2) |
| [[PANC-1 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.7) |
| [[RKO (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0960× (z -15.8) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.0) |
| [[A-427 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.120× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 7.40 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -10.0) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H2030 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.57× (z +8.8) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -13.1) |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0694× (z -12.4) |
| [[SW48 (line)]] | wt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.3) |
| [[SW480 (line)]] | alt | 40.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.1) |
| [[A-172 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1E1]] | +0.83 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[MDN1]] | +0.75 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[TUBGCP4]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[UCK2]] | +0.73 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[DTD2]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 | pathway: tRNA processing |
| [[DHX33]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[GART]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[WDR12]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[SORD]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[CAD]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | -0.67 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[KMT2A]] | -0.63 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[DNAL4]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[YIPF3]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZRANB1]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP9]] | B | DUXAP9 activity raises ADAT2's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without DUXAP9 | 0.025 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[NT5M]] | B | NT5M activity raises ADAT2's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without NT5M | 0.029 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[DUXAP8]] | B | DUXAP8 activity raises ADAT2's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without DUXAP8 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[PROCR]] | B | PROCR activity lowers ADAT2's level | lines that do not express PROCR (8) vs lines expressing it (42) | 1.94× higher at baseline in the lines without PROCR | 0.058 | ⚠ within organs, on part of the lines; also absent: ATP2B4, RNF135, LAMB1; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises ADAT2's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.14× lower at baseline in the lines without MCOLN2 | 0.064 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[NCS1]] | B | NCS1 activity raises ADAT2's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without NCS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[MEX3A]] | B | MEX3A activity raises ADAT2's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without MEX3A | 0.097 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.9, -37.2); signed map (-4.0, -51.9). **Vector** length 95.6, 21.7% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.7 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.4 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +9.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.1 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -3.9 | -1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | adenosine deaminase tRNA specific 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:143,422,832-143,450,695 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ20N2.1, TAD2; previously DEADC1 |
| Gene groups (HGNC) | Adenosine deaminases acting on RNA |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6V5](https://www.uniprot.org/uniprotkb/Q7Z6V5) (tRNA-specific adenosine-34 deaminase catalytic subunit ADAT2):

> Catalytic subunit of the tRNA-specific adenosine-34 deaminase complex, composed of the ADAT2 catalytic subunit and the ADAT3 regulatory subunit, which deaminates adenosine-34 (the first, also called wobble position of the anticodon) to inosine in many tRNAs. Inosine-34 allows the decoding of 3 different nucleotides at the third position of mRNA codons, as inosine is able to pair with U, C, and A. Binding of the ADAT2-ADAT3 complex to tRNA is mediated by the N-terminus of ADAT3 which rotates …

**Summary**, from NCBI Gene [134637](https://www.ncbi.nlm.nih.gov/gene/134637):

> Predicted to enable tRNA-specific adenosine-34 deaminase activity. Predicted to be involved in tRNA wobble adenosine to inosine editing. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21172) · Entrez [134637](https://www.ncbi.nlm.nih.gov/gene/134637) · UniProt [Q7Z6V5](https://www.uniprot.org/uniprotkb/Q7Z6V5) · Ensembl [ENSG00000189007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189007)

## Data

Gene col 12076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12076); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12076]; `tensor/DDL_lfc|DDL_z.npy` [12076]; `embed/gene_vectors.npy` [12076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12076 or target_col == 12076). Every well: [[ADAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
