---
symbol: "UTP4"
type: "gene"
col: 6487
ensembl_id: "ENSG00000141076"
name: "UTP4 small subunit processome component"
location: "16q22.1"
module: 5
arm: "+"
pooled_cpm: 58.83
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# UTP4

*UTP4 small subunit processome component* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.72× (z +10.8, q 2e-24, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.776× (z -5.2, q 9e-05, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~19% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.313×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.153×); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.171×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.78, fdr 7e-06), [[POLR1A]] (+0.74, fdr 7e-06), [[URB2]] (+0.74, fdr 7e-06); moves opposite to [[UBE2B]] (-0.63, fdr 1e-05), [[PJA2]] (-0.61, fdr 1e-05), [[TMEM167B]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[USP31]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +10.8 | 2e-24 | 41/49 (PANC-1, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +9.9 | 9e-21 | 44/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +9.8 | 2e-20 | 41/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +8.6 | 1e-15 | 32/48 (NCI-H460, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +7.9 | 3e-13 | 32/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.48×** | +7.8 | 6e-13 | 33/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +6.1 | 1e-07 | 35/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.33×** | +5.9 | 3e-07 | 26/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 1e-06 | 27/48 (HT-29, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +4.9 | 4e-05 | 24/48 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +4.8 | 8e-05 | 24/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +4.7 | 1e-04 | 24/48 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.25×** | +4.5 | 3e-04 | 20/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.5 | 3e-04 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.4 | 3e-04 | 16/36 (A498, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 22/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.003 | 18/48 (NCI-H460, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.008 | 16/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.016 | 13/48 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.019 | 12/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.15× | +2.9 | 0.074 | 9/48 (NCI-H1573, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6487.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.313×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.153×); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.171×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.776×** | -5.2 | 9e-05 | 25/48 (SW1417, SW480, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.843× | -4.1 | 0.011 | 19/48 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -3.9 | 0.018 | 18/48 (SW480, SW1417, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.841× | -3.8 | 0.018 | 20/48 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.024 | 14/49 (SK-MEL-2, SW480, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.21 | 16/48 (SW480, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 82.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +16.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 35.8 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CHP-212 (line)]] | wt | 60.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.171× (z -8.9) |
| [[HT-29 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.03× (z +9.1) ⚠ toxic; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 89.7 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.82× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 41.9 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.91× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 | same gene group; STRING 429 |
| [[POLR1A]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 | STRING 879 |
| [[URB2]] | +0.74 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[NOP2]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 753 |
| [[DHX37]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 952 |
| [[ARMC6]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[TBRG4]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[NOL9]] | +0.70 | +0.58 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 622 |
| [[MRTO4]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 | STRING 889 |
| [[DHX33]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | STRING 497 |
| [[EIF2S1]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2B]] | -0.63 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[PJA2]] | -0.61 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[TMEM167B]] | -0.61 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[OAZ1]] | -0.61 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[SARAF]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[LCA5]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[WBP1]] | -0.57 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[CCDC186]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[DNAJB2]] | -0.56 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[AKAP9]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MXD1]] | -0.56 | -0.55 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP31]] | C | USP31 activity raises UTP4's level | lines that do not express USP31 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.3, -35.4); signed map (-3.0, -47.5). **Vector** length 112, 29.4% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.61 to 13); *ribosome biogenesis* (control, mean cos +0.55 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.4 | +9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +6.0 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.1 | +6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +10.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.5 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.9 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.8 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | UTP4 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,131,291-69,231,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAIC, FLJ14728, KIAA1988, TEX292, CIRHIN; previously CIRH1A |
| Gene groups (HGNC) | WD repeat domain containing; UTPa subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969X6](https://www.uniprot.org/uniprotkb/Q969X6) (U3 small nucleolar RNA-associated protein 4 homolog):

> Ribosome biogenesis factor. Involved in nucleolar processing of pre-18S ribosomal RNA. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted d Involved in SSU pre-rRNA …

**Summary**, from NCBI Gene [84916](https://www.ncbi.nlm.nih.gov/gene/84916):

> This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:1983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1983) · Entrez [84916](https://www.ncbi.nlm.nih.gov/gene/84916) · UniProt [Q969X6](https://www.uniprot.org/uniprotkb/Q969X6) · Ensembl [ENSG00000141076](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141076)

## Data

Gene col 6487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6487); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6487]; `tensor/DDL_lfc|DDL_z.npy` [6487]; `embed/gene_vectors.npy` [6487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6487 or target_col == 6487). Every well: [[UTP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
