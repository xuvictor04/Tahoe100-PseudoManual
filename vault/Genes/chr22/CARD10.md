---
symbol: "CARD10"
type: "gene"
col: 1857
ensembl_id: "ENSG00000100065"
name: "caspase recruitment domain family member 10"
location: "22q13.1"
module: 161
arm: "+"
pooled_cpm: 14.08
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 14
direction_downstream: 4
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# CARD10

*caspase recruitment domain family member 10* — 22q13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 6.41×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 3.36×; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 3.33×; ⚠ cell-cycle shift, explains ~10% of this change).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.608× (z -9.2, q 2e-17, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFNG]] (+0.65, fdr 7e-06, ⚠ same locus), [[WNT7A]] (+0.62, fdr 1e-05), [[SPNS2]] (+0.57, fdr 4e-05), [[WNT7B]] (+0.55, fdr 2e-05); moves opposite to [[SNX13]] (-0.48, fdr 6e-05), [[TMEM87A]] (-0.47, fdr 8e-05), [[AZI2]] (-0.46, fdr 3e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[PRAG1]] → it (grade B ⚠); 4 go from it, the strongest it → [[ELFN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1857.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 6.41×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 3.36×; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 3.33×; ⚠ cell-cycle shift, explains ~10% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.8 | 3e-06 | 5/40 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | 1.31× | +3.5 | 0.12 | 5/35 (Hs 766T, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.28 | 2/39 (SW480, A549) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -9.2 | 2e-17 | 28/36 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -8.0 | 2e-13 | 26/39 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.668×** | -7.5 | 1e-11 | 21/40 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.575×** | -7.3 | 5e-11 | 25/39 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.561×** | -7.2 | 9e-11 | 17/36 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -6.1 | 1e-07 | 17/37 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.674×** | -5.2 | 2e-05 | 19/39 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -4.6 | 3e-04 | 16/39 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.704×** | -4.6 | 3e-04 | 14/36 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.706×** | -4.4 | 6e-04 | 17/33 (PANC-1, HEC-1-A, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.718×** | -4.3 | 7e-04 | 17/39 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.721×** | -4.3 | 8e-04 | 17/39 (HepG2/C3A, A549, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.714×** | -4.3 | 9e-04 | 18/32 (NCI-H2347, HepG2/C3A, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.739×** | -3.8 | 0.005 | 14/37 (NCI-H2347, CFPAC-1, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.006 | 11/38 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.600×** | -3.5 | 0.015 | 11/34 (A-172, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.778×** | -3.3 | 0.028 | 10/36 (NCI-H2347, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **0.783×** | -3.2 | 0.036 | 3/40 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.041 | 10/40 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.787×** | -3.1 | 0.041 | 9/39 (NCI-H1573, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.2 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -18.4) |
| [[SW480 (line)]] | alt | 19.4 | 2 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0978× (z -15.7) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.131× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.22 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 9.92 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0857× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[CFPAC-1 (line)]] | alt | 26.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.1) |
| [[HS-578T (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -9.8) |
| [[J82 (line)]] | alt | 7.29 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[RKO (line)]] | wt | 6.53 | 0 | 1 | — | [[Thymol (drug)]] 5 µM 0.180× (z -8.7) |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.269× (z -8.6) |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.0) |
| [[A-427 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFNG]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | ⚠ same locus (4.0 kb, same strand: neighbours can correlate without regulation) |
| [[WNT7A]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SPNS2]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[WNT7B]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DRAP1]] | +0.55 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[SLC45A3]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[MYRF]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A25]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[HMGA1]] | +0.51 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CDC42BPG]] | +0.50 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[MAP2K3]] | +0.50 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SH3BP1]] | +0.49 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[STMN3]] | +0.49 | +0.53 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX13]] | -0.48 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[TMEM87A]] | -0.47 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[AZI2]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ALDH2]] | -0.45 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RIDA]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[METTL25]] | -0.43 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[PDHX]] | -0.42 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[PTRHD1]] ⚠ | -0.42 | -0.42 / -0.33 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MTREX]] | -0.42 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[EPM2AIP1]] | -0.41 | -0.53 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SMIM20]] | -0.41 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[RRAGB]] | -0.41 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[FAM172A]] | -0.41 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[USP47]] | -0.41 | -0.44 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRAG1]] | B | PRAG1 activity raises CARD10's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without PRAG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[SYT13]] | B | SYT13 activity raises CARD10's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.82× lower at baseline in the lines without SYT13 | 0.027 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[WNT7B]] | B | WNT7B activity raises CARD10's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.76× lower at baseline in the lines without WNT7B | 0.033 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[TMC6]] | B | TMC6 activity raises CARD10's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without TMC6 | 0.043 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[CCDC120]] | B | CCDC120 activity raises CARD10's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without CCDC120 | 0.047 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[TINAGL1]] | B | TINAGL1 activity raises CARD10's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without TINAGL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[BAIAP3]] | B | BAIAP3 activity raises CARD10's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without BAIAP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[PRR36]] | B | PRR36 activity raises CARD10's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without PRR36 | 0.065 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[CDC42BPG]] | B | CDC42BPG activity raises CARD10's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without CDC42BPG | 0.072 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises CARD10's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without TNFRSF11A | 0.075 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[TTC9]] | B | TTC9 activity raises CARD10's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.77× lower at baseline in the lines without TTC9 | 0.077 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[SPNS2]] | B | SPNS2 activity raises CARD10's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.86× lower at baseline in the lines without SPNS2 | 0.096 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN2]] | B | CARD10 activity raises ELFN2's level | lines that do not express CARD10 (8) vs lines expressing it (42) | 3.00× lower at baseline in the lines without CARD10 | 0.060 | ⚠ within organs, on part of the lines; also absent: MFNG, LRP5, SDC1; maybe low, not absent; its own permutation p |
| [[AHDC1]] | B | CARD10 activity raises AHDC1's level | lines that do not express CARD10 (8) vs lines expressing it (42) | 1.47× lower at baseline in the lines without CARD10 | 0.060 | ⚠ within organs, on part of the lines; also absent: MFNG, LRP5, SDC1; maybe low, not absent; its own permutation p |
| [[EPHB2]] | B | CARD10 activity raises EPHB2's level | lines that do not express CARD10 (8) vs lines expressing it (42) | 3.05× lower at baseline in the lines without CARD10 | 0.089 | ⚠ within organs, on part of the lines; also absent: MFNG, LRP5, SDC1; maybe low, not absent; its own permutation p |
| [[BAIAP3]] | B | CARD10 activity raises BAIAP3's level | lines that do not express CARD10 (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without CARD10 | 0.089 | ⚠ within organs, on part of the lines; also absent: MFNG, LRP5, SDC1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.0, 60.5); signed map (-1.3, 41.7). **Vector** length 79.6, 16.5% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.1 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.4 | +1.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.0 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | caspase recruitment domain family member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,490,362-37,519,542 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CARMA3, BIMP1 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; Caspase recruitment domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWT7](https://www.uniprot.org/uniprotkb/Q9BWT7) (Caspase recruitment domain-containing protein 10):

> Scaffold protein that plays an important role in mediating the activation of NF-kappa-B via BCL10 or EGFR.

**Summary**, from NCBI Gene [29775](https://www.ncbi.nlm.nih.gov/gene/29775):

> The caspase recruitment domain (CARD) is a protein module that consists of 6 or 7 antiparallel alpha helices. It participates in apoptosis signaling through highly specific protein-protein homophilic interactions. Like several other CARD proteins, CARD10 belongs to the membrane-associated guanylate kinase (MAGUK) family and activates NF-kappa-B (NFKB; see MIM 164011) through BCL10 (MIM 603517) (Wang et al., 2001 [PubMed 11259443]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16422) · Entrez [29775](https://www.ncbi.nlm.nih.gov/gene/29775) · UniProt [Q9BWT7](https://www.uniprot.org/uniprotkb/Q9BWT7) · Ensembl [ENSG00000100065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100065)

## Data

Gene col 1857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1857); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1857]; `tensor/DDL_lfc|DDL_z.npy` [1857]; `embed/gene_vectors.npy` [1857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1857 or target_col == 1857). Every well: [[CARD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
