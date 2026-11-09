---
symbol: "RBMS1"
type: "gene"
col: 7708
ensembl_id: "ENSG00000153250"
name: "RNA binding motif single stranded interacting protein 1"
location: "2q24.2"
module: 104
arm: "+"
pooled_cpm: 165.15
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# RBMS1

*RNA binding motif single stranded interacting protein 1* — 2q24.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 2.06×, MIA PaCa-2 2.81×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.46×; ⚠ position not correctable); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-172 2.11×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 1.93×); [[Tucidinostat (drug)]] 5 µM in 1 line (LoVo 1.57×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.414× (z -18.3, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2E3]] (+0.55, fdr 3e-05), [[VGLL3]] (+0.54, fdr 3e-05), [[IL1R1]] (+0.54, fdr 1e-04); moves opposite to [[RBCK1]] (-0.50, fdr 7e-05), [[DDIT3]] (-0.46, fdr 4e-05), [[RNMT]] (-0.44, fdr 3e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FN1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HK2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7708.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 2.06×, MIA PaCa-2 2.81×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.46×; ⚠ position not correctable); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-172 2.11×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 1.93×); [[Tucidinostat (drug)]] 5 µM in 1 line (LoVo 1.57×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.4 | 0.43 | 16/44 (LoVo, SW1417, …) | rises with dose |  |
| [[Econazole (drug)]] 5 µM |  | 1.16× | +3.1 | 0.57 | 15/44 (Hs 766T, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.414×** | -18.3 | 0e+00 | 43/44 (A498, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.444×** | -16.8 | 0e+00 | 40/44 (A498, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -16.1 | 0e+00 | 36/45 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.609×** | -14.5 | 1e-45 | 30/44 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -12.5 | 7e-34 | 38/44 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -8.1 | 7e-14 | 26/44 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -7.1 | 1e-10 | 29/46 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -6.2 | 4e-08 | 29/44 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.758×** | -5.5 | 2e-06 | 26/43 (CHP-212, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.792×** | -4.8 | 8e-05 | 25/45 (HOP62, J82, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.649×** | -4.7 | 2e-04 | 26/44 (HEC-1-A, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -4.6 | 2e-04 | 23/44 (Panc 03.27, SK-MEL-2, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.675×** | -4.2 | 9e-04 | 21/37 (LOX-IMVI, H4, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.819×** | -4.1 | 0.002 | 22/44 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **0.825×** | -3.8 | 0.005 | 20/44 (HOP62, H4, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.881× | -3.7 | 0.007 | 3/45 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.847× | -3.4 | 0.017 | 17/44 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.734×** | -3.4 | 0.023 | 17/44 (HOP62, J82, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 156 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -19.4) |
| [[A-172 (line)]] | wt | 262 | 4 (4 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.11× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -20.1) |
| [[C32 (line)]] | wt | 250 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -21.0) |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -23.2) |
| [[NCI-H1792 (line)]] | alt | 312 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -22.5) |
| [[HOP62 (line)]] | alt | 190 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -17.0) |
| [[Hs 766T (line)]] | wt | 228 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -18.2) |
| [[HS-578T (line)]] | alt | 236 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 61.3 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.254× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 239 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -14.9) |
| [[A498 (line)]] | wt | 377 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -27.0) |
| [[AsPC-1 (line)]] | alt | 276 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -20.4) |
| [[CHP-212 (line)]] | wt | 341 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -13.9) |
| [[HT-29 (line)]] | alt | 132 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -15.7) |
| [[J82 (line)]] | alt | 235 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -17.4) |
| [[LoVo (line)]] | wt | 74.4 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.57× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -22.1) |
| [[LOX-IMVI (line)]] | wt | 410 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 211 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -18.7) |
| [[BT-474 (line)]] | alt | 134 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.316× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 186 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 201 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.9) |
| [[SW 900 (line)]] | alt | 298 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -14.9) |
| [[A-427 (line)]] | wt | 126 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.486× (z -10.1) |
| [[A549 (line)]] | wt | 196 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -11.9) |
| [[COLO 205 (line)]] | alt | 65.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -15.1) |
| [[SW480 (line)]] | alt | 177 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -21.3) |
| [[H4 (line)]] | wt | 198 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -17.3) |
| [[PANC-1 (line)]] | alt | 107 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 1.84× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 98.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -11.3) |
| [[KATO III (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 91.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.6) |
| [[SW1417 (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 190 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2E3]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[VGLL3]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[IL1R1]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[PID1]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[HIF1A]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[FKBP5]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 | same gene group |
| [[LPP]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 | same gene group |
| [[TMTC1]] | +0.51 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[RDX]] | +0.51 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[HIPK2]] | +0.51 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TRPS1]] | +0.50 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[STXBP5]] | +0.49 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBCK1]] | -0.50 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[DDIT3]] | -0.46 | -0.43 / -0.41 | both halves | 4e-05 | same gene group |
| [[RNMT]] | -0.44 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[WDR45B]] | -0.44 | -0.19 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[ERO1A]] | -0.44 | -0.21 / -0.40 | both halves | 6e-04 |  |
| [[QPCTL]] | -0.43 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[BET1L]] | -0.43 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[GAL3ST1]] | -0.43 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[SLC7A5]] | -0.42 | -0.37 / -0.38 | both halves | 9e-05 | same gene group |
| [[LIPE-AS1]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[GOT1]] | -0.42 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[LINC02649]] | -0.42 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[PMS2P4-1]] | -0.41 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FN1]] | B | FN1 activity raises RBMS1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.46× lower at baseline in the lines without FN1 | 0.034 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[ABLIM3]] | B | ABLIM3 activity raises RBMS1's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without ABLIM3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[TGFBR2]] | B | TGFBR2 activity raises RBMS1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without TGFBR2 | 0.069 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[UBE2E2]] | B | UBE2E2 activity raises RBMS1's level | lines that do not express UBE2E2 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without UBE2E2 | 0.082 | ⚠ within organs, on part of the lines; also absent: PRDM5, AMOTL1, RAB31 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HK2]] | C | RBMS1 activity lowers HK2's level | lines that do not express RBMS1 (4) vs lines expressing it (46) | 1.26× higher at baseline in the lines without RBMS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with EP300, TGFBR2, BRCA2; also absent: ENSG00000285155, TBC1D9, TCEA2; its own permutation p |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.9, 17.4); signed map (19.7, 34.1). **Vector** length 106, 30.8% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.1 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.9 | +1.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -16.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -14.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | -2.8 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -18.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif single stranded interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:160,272,151-160,493,807 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCR2, MSSP-1, MSSP-2, MSSP-3, YC1, HCC-4, DKFZp564H0764; previously C2orf12 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P29558](https://www.uniprot.org/uniprotkb/P29558) (RNA-binding motif, single-stranded-interacting protein 1):

> Single-stranded DNA binding protein that interacts with the region upstream of the MYC gene. Binds specifically to the DNA sequence motif 5'-[AT]CT[AT][AT]T-3'. Probably has a role in DNA replication.

**Summary**, from NCBI Gene [5937](https://www.ncbi.nlm.nih.gov/gene/5937):

> This gene encodes a member of a small family of proteins which bind single stranded DNA/RNA. These proteins are characterized by the presence of two sets of ribonucleoprotein consensus sequence (RNP-CS) that contain conserved motifs, RNP1 and RNP2, originally described in RNA binding proteins, and required for DNA binding. These proteins have been implicated in such diverse functions as DNA replication, gene transcription, cell cycle progression and apoptosis. Several transcript variants, …

**Accessions** — [HGNC:9907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9907) · Entrez [5937](https://www.ncbi.nlm.nih.gov/gene/5937) · UniProt [P29558](https://www.uniprot.org/uniprotkb/P29558) · Ensembl [ENSG00000153250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153250)

## Data

Gene col 7708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7708); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7708]; `tensor/DDL_lfc|DDL_z.npy` [7708]; `embed/gene_vectors.npy` [7708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7708 or target_col == 7708). Every well: [[RBMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
