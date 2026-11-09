---
symbol: "PTPN18"
type: "gene"
col: 1008
ensembl_id: "ENSG00000072135"
name: "protein tyrosine phosphatase non-receptor type 18"
location: "2q21.1"
module: 20
arm: "+"
pooled_cpm: 19.16
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PTPN18

*protein tyrosine phosphatase non-receptor type 18* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +8.7, q 3e-15, up in 28 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +7.1, q 4e-10, up in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 3.59×, HEC-1-A 2.60×, NCI-H1573 6.20×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -18.1, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIGMAR1]] (+0.71, fdr 1e-05), [[DPAGT1]] (+0.65, fdr 7e-06), [[AKT1]] (+0.65, fdr 7e-06); moves opposite to [[SUMO4]] (-0.68, fdr 7e-06), [[TRAPPC2B]] (-0.66, fdr 1e-05), [[PIGBOS1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VAX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1008.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 3.59×, HEC-1-A 2.60×, NCI-H1573 6.20×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +8.7 | 3e-15 | 28/40 (LS 180, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.1 | 4e-10 | 24/47 (A549, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.8 | 3e-09 | 16/29 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +6.6 | 7e-09 | 20/35 (Panc 03.27, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +3.7 | 0.023 | 8/47 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.098 | 13/46 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -18.1 | 0e+00 | 41/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -12.7 | 2e-34 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.448×** | -12.6 | 7e-34 | 36/46 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.444×** | -12.0 | 6e-31 | 41/47 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.495×** | -11.0 | 5e-26 | 37/47 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.529×** | -10.0 | 2e-21 | 36/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.534×** | -9.4 | 3e-19 | 37/47 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.549×** | -9.4 | 5e-19 | 35/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.555×** | -9.2 | 2e-18 | 30/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -8.1 | 4e-14 | 33/47 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.395×** | -7.6 | 2e-12 | 29/44 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.402×** | -7.5 | 4e-12 | 30/38 (NCI-H2030, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -7.1 | 7e-11 | 32/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -5.4 | 2e-06 | 23/48 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -4.9 | 3e-05 | 21/42 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -4.1 | 0.001 | 16/45 (HT-29, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.788×** | -3.7 | 0.006 | 15/48 (SNU-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.798×** | -3.3 | 0.024 | 15/47 (HEC-1-A, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.7) |
| [[PANC-1 (line)]] | alt | 19.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 26.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.7) |
| [[J82 (line)]] | alt | 14.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -19.6) |
| [[NCI-H460 (line)]] | wt | 22.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.4) |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0767× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.5) |
| [[LoVo (line)]] | wt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -13.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.1) |
| [[A-172 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.5) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0805× (z -9.2) |
| [[A498 (line)]] | wt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.6) |
| [[A549 (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.3) |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.189× (z -8.6) |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.7) |
| [[H4 (line)]] | wt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0988× (z -9.0) |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.8) |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.1) |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.230× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -10.9) |
| [[LS 180 (line)]] | wt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 6.91 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0760× (z -8.7) |
| [[RKO (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -18.0) |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIGMAR1]] | +0.71 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[DPAGT1]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[AKT1]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 | pathway: Downregulation of ERBB2 signaling |
| [[CCAR2]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CTSZ]] | +0.63 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CERS2]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[IPO4]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CA5BP1-1]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[IPO5]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO4]] | -0.68 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[TRAPPC2B]] | -0.66 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.61 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[DCP1A]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SEC62]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.59 | -0.60 / -0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DCTN6]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[PSMA7]] | -0.58 | -0.38 / -0.55 | both halves | 7e-05 | pathway: Interleukin-1 family signaling |
| [[NMT1]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[KLHL4]] | -0.57 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PI4KB]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PSMB1]] | -0.56 | -0.43 / -0.52 | both halves | 3e-05 | pathway: Interleukin-1 family signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAX2]] | B | VAX2 activity raises PTPN18's level | lines that do not express VAX2 (12) vs lines expressing it (38) | 1.09× lower at baseline in the lines without VAX2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with RNF43; also absent: ZNF512B, WHAMMP2, HLTF |
| [[TOP1]] | B | TOP1 activity lowers PTPN18's level | compounds that target TOP1: 2 of 3 raise it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.4, -25.6); signed map (-24.9, -42.2). **Vector** length 67.7, 12.1% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -12.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -9.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -18.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:130,356,045-130,375,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BDP1 |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type |
| Reactome | 7 pathways, smallest: Interleukin-37 signaling; Downregulation of ERBB2 signaling; Signaling by ERBB2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99952](https://www.uniprot.org/uniprotkb/Q99952) (Tyrosine-protein phosphatase non-receptor type 18):

> Differentially dephosphorylate autophosphorylated tyrosine kinases which are known to be overexpressed in tumor tissues.

**Summary**, from NCBI Gene [26469](https://www.ncbi.nlm.nih.gov/gene/26469):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, the mitotic cycle, and oncogenic transformation. This PTP contains a PEST motif, which often serves as a protein-protein interaction domain, and may be related to protein intracellular half-live. This protein can differentially dephosphorylate autophosphorylated tyrosine …

**Accessions** — [HGNC:9649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9649) · Entrez [26469](https://www.ncbi.nlm.nih.gov/gene/26469) · UniProt [Q99952](https://www.uniprot.org/uniprotkb/Q99952) · Ensembl [ENSG00000072135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072135)

## Data

Gene col 1008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1008); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1008]; `tensor/DDL_lfc|DDL_z.npy` [1008]; `embed/gene_vectors.npy` [1008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1008 or target_col == 1008). Every well: [[PTPN18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
