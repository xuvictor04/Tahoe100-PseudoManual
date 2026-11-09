---
symbol: "MCAM"
type: "gene"
col: 1161
ensembl_id: "ENSG00000076706"
name: "melanoma cell adhesion molecule"
location: "11q23.3"
module: 132
arm: "+"
pooled_cpm: 8.46
n_lines_expressing: 29
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# MCAM

*melanoma cell adhesion molecule* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.50× (z +12.6, q 1e-33, up in 15 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.77× (z +8.1, q 7e-14, up in 18 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cepharanthine (drug)]] 5 µM: 0.732× (z -4.5, q 0.004, down in 10 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.129×, SK-MEL-2 0.271×, NCI-H23 0.247×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0904×; ⚠ toxic).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGSF3]] (+0.59, fdr 2e-05), [[TRIM58]] (+0.57, fdr 6e-05), [[RETREG1]] (+0.57, fdr 4e-05); moves opposite to [[IKZF4]] (-0.50, fdr 5e-05), [[KIAA0753]] (-0.48, fdr 1e-04), [[LINS1]] (-0.46, fdr 2e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SCN9A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CFD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.50×** | +12.6 | 1e-33 | 15/20 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.55×** | +11.9 | 4e-30 | 14/16 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.62×** | +9.0 | 6e-17 | 14/16 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +8.1 | 7e-14 | 18/26 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.96×** | +6.8 | 1e-09 | 15/26 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.96×** | +6.8 | 1e-09 | 14/26 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.93×** | +6.6 | 4e-09 | 17/26 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +6.4 | 1e-08 | 16/26 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.55×** | +6.2 | 4e-08 | 16/26 (BT-474, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +6.1 | 5e-08 | 18/26 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +6.0 | 1e-07 | 10/26 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.5 | 2e-06 | 8/20 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.58×** | +5.3 | 7e-06 | 11/24 (SW 900, C32, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.73×** | +5.1 | 1e-05 | 13/24 (C32, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.9 | 3e-05 | 15/26 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.65×** | +4.7 | 9e-05 | 12/26 (BT-474, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.59×** | +4.7 | 1e-04 | 14/25 (SW 900, BT-474, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **2.33×** | +4.4 | 3e-04 | 9/21 (SW 900, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.4 | 3e-04 | 12/26 (NCI-H460, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +3.5 | 0.010 | 6/26 (PANC-1, HepG2/C3A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +3.1 | 0.036 | 2/21 (PANC-1, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.036 | 12/26 (BT-474, C32, …) | all doses, stronger at high dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.35×** | +2.8 | 0.096 | 3/26 (A-172, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1161.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.129×, SK-MEL-2 0.271×, NCI-H23 0.247×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0904×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **0.732×** | -4.5 | 0.004 | 10/26 (NCI-H2347, NCI-H661, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.547× | -3.2 | 0.29 | 7/26 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.736× | -3.1 | 0.29 | 4/27 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.558× | -3.1 | 0.29 | 4/27 (HS-578T, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 61.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.56× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0904× (z -9.8) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 19.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -17.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 9.29 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 5.58 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 7.25 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.886 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF3]] | +0.59 | +0.47 / +0.50 | both halves | 2e-05 | same gene group |
| [[TRIM58]] | +0.57 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[RETREG1]] | +0.57 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[TMOD2]] | +0.55 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[SDC3]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[GNAZ]] | +0.51 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[PRKAG2]] | +0.51 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[VPS13A]] | +0.51 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[ARHGAP17]] | +0.50 | +0.47 / +0.40 | both halves | 4e-05 | pathway: RAC1 GTPase cycle |
| [[FSD1]] | +0.49 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[KCTD17]] | +0.49 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[KRAS]] | +0.48 | +0.35 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKZF4]] | -0.50 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[KIAA0753]] | -0.48 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[LINS1]] | -0.46 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[KRBOX4]] | -0.44 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[RECQL5]] | -0.42 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[ACAD9]] | -0.42 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[SYNRG]] | -0.42 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[LINC00310]] | -0.42 | -0.44 / -0.26 | both halves | 3e-04 |  |
| [[PTH2R]] | -0.41 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[MAP3K7]] | -0.40 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[ZCWPW2]] | -0.40 | -0.30 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCN9A]] | B | SCN9A activity raises MCAM's level | lines that do not express SCN9A (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without SCN9A | 0.060 | ⚠ within organs, on part of the lines; also absent: PTPRM, RPS6KA6, UCHL1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFD]] | B | MCAM activity lowers CFD's level | lines that do not express MCAM (21) vs lines expressing it (29) | 1.89× higher at baseline in the lines without MCAM | 0.062 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SMIM10, PPP2R2B, SLC16A6 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.7, 35.1); signed map (-14.5, 37.2). **Vector** length 53.6, 11.5% of its response variance represented; |z| ≥ 3 in 589 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.3 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.0 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.8 | +11.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | -0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -0.9 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | melanoma cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,308,529-119,321,521 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MUC18, CD146, MelCAM, METCAM, HEMCAM |
| Gene groups (HGNC) | CD molecules; V-set domain containing; C2-set domain containing; Ig-like cell adhesion molecule family; MicroRNA protein coding host genes |
| Reactome | 12 pathways, smallest: RHOF GTPase cycle; RHOD GTPase cycle; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P43121](https://www.uniprot.org/uniprotkb/P43121) (Cell surface glycoprotein MUC18):

> Plays a role in cell adhesion, and in cohesion of the endothelial monolayer at intercellular junctions in vascular tissue. Its expression may allow melanoma cells to interact with cellular elements of the vascular system, thereby enhancing hematogeneous tumor spread. Could be an adhesion molecule active in neural crest cells during embryonic development. Acts as a surface receptor that triggers tyrosine phosphorylation of FYN and PTK2/FAK1, and a transient increase in the intracellular calcium …

**Summary**, from NCBI Gene [4162](https://www.ncbi.nlm.nih.gov/gene/4162):

> Involved in glomerular filtration and vascular wound healing. Acts upstream of or within angiogenesis. Located in external side of plasma membrane. Biomarker of chronic obstructive pulmonary disease and uveal melanoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6934) · Entrez [4162](https://www.ncbi.nlm.nih.gov/gene/4162) · UniProt [P43121](https://www.uniprot.org/uniprotkb/P43121) · Ensembl [ENSG00000076706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076706)

## Data

Gene col 1161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1161); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1161]; `tensor/DDL_lfc|DDL_z.npy` [1161]; `embed/gene_vectors.npy` [1161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1161 or target_col == 1161). Every well: [[MCAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
