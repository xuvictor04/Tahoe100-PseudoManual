---
symbol: "EFCAB3P1"
type: "gene"
col: 15728
ensembl_id: "ENSG00000272601"
name: "EFCAB3 pseudogene 1"
location: "7q32.1"
module: 105
arm: "+"
pooled_cpm: 8.34
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# EFCAB3P1

*EFCAB3 pseudogene 1* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +6.1, q 5e-07, up in 26 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.245× (z -18.9, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUT11]] (+0.77, fdr 7e-06), [[C4orf47]] (+0.73, fdr 7e-06), [[FAM162A]] (+0.72, fdr 7e-06); moves opposite to [[PARVA]] (-0.51, fdr 3e-05), [[MCCC2]] (-0.49, fdr 3e-05), [[SGPL1]] (-0.48, fdr 5e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KDM2B-DT]] → it (grade B ⚠); 3 go from it, the strongest it → [[C4orf47]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.1 | 5e-07 | 26/44 (A498, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +5.5 | 1e-05 | 18/44 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.73×** | +5.2 | 3e-05 | 27/45 (H4, NCI-H1792, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +4.6 | 6e-04 | 19/42 (C-33 A, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 8e-04 | 16/44 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.043 | 11/44 (LoVo, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.069 | 12/44 (NCI-H460, NCI-H23, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.245×** | -18.9 | 0e+00 | 39/41 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.271×** | -11.9 | 3e-30 | 30/42 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.344×** | -10.1 | 8e-22 | 28/41 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.451×** | -7.3 | 5e-11 | 26/35 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -5.4 | 9e-06 | 24/43 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.675×** | -5.3 | 1e-05 | 15/44 (HT-29, HCT15, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.636×** | -4.1 | 0.004 | 21/42 (LOX-IMVI, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.0 | 0.004 | 18/44 (HEC-1-A, Hs 766T, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.658×** | -4.0 | 0.004 | 18/44 (NCI-H1792, SW48, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.668×** | -3.8 | 0.007 | 16/43 (HCT15, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.013 | 13/45 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.677×** | -3.6 | 0.018 | 14/18 (A498, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.689×** | -3.5 | 0.018 | 14/44 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.5 | 0.019 | 15/44 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.701×** | -3.4 | 0.028 | 19/43 (C32, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.702×** | -3.4 | 0.028 | 16/40 (SW48, J82, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.707×** | -3.1 | 0.062 | 12/44 (SW 1271, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 59.8 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0817× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -12.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.8) |
| [[C32 (line)]] | wt | 37.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0384× (z -27.8) |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0288× (z -14.2) |
| [[SW 900 (line)]] | alt | 6.89 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0756× (z -13.2) |
| [[SW480 (line)]] | alt | 7.00 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -14.6) |
| [[A-172 (line)]] | wt | 9.22 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.7) |
| [[A498 (line)]] | wt | 6.70 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.59× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0976× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[H4 (line)]] | wt | 14.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0356× (z -12.0) |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 5.58 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0444× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 9.48 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0706× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 7.70 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.3) |
| [[PANC-1 (line)]] | alt | 5.49 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0900× (z -11.7) |
| [[SW48 (line)]] | wt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.5) |
| [[BT-474 (line)]] | alt | 9.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -11.1) |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -9.6) |
| [[HOP62 (line)]] | alt | 8.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.6) |
| [[Hs 766T (line)]] | wt | 5.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -9.6) |
| [[HS-578T (line)]] | alt | 9.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0877× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.3) |
| [[SHP-77 (line)]] | alt | 5.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -11.4) |
| [[SNU-423 (line)]] | alt | 7.41 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0703× (z -9.2) |
| [[A-427 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUT11]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[C4orf47]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[FNTB]] | +0.69 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.68 | +0.69 / +0.70 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 8.1 kb 3′ of HILPDA on the same strand (can correlate by spillover, not regulation) |
| [[FAM210A]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RNMT]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[TMEM14B]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[PDK1]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[POM121C]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.63 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SLC2A1-DT]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARVA]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MCCC2]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SGPL1]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B-DT]] | B | KDM2B-DT activity raises EFCAB3P1's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without KDM2B-DT | 0.048 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[SYCP2L]] | B | SYCP2L activity raises EFCAB3P1's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without SYCP2L | 0.078 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf47]] | C | EFCAB3P1 activity raises C4orf47's level | lines that do not express EFCAB3P1 (3) vs lines expressing it (47) | 3.80× lower at baseline in the lines without EFCAB3P1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FRZB, ENSG00000273184, CLEC2D; maybe low, not absent; co-absent with the target; its own permutation p |
| [[FBXO42]] | C | EFCAB3P1 activity raises FBXO42's level | lines that do not express EFCAB3P1 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without EFCAB3P1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FRZB, ENSG00000273184, CLEC2D; maybe low, not absent; its own permutation p |
| [[FUT11]] | C | EFCAB3P1 activity raises FUT11's level | lines that do not express EFCAB3P1 (3) vs lines expressing it (47) | 1.52× lower at baseline in the lines without EFCAB3P1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FRZB, ENSG00000273184, CLEC2D; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -18.7); signed map (-34.0, 26.2). **Vector** length 97.5, 21.3% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -18.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | -3.4 | -2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -3.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -10.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | EFCAB3 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q32.1 — chr7:128,466,563-128,469,171 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56232) · Entrez [125775236](https://www.ncbi.nlm.nih.gov/gene/125775236) · Ensembl [ENSG00000272601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272601)

## Data

Gene col 15728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15728); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15728]; `tensor/DDL_lfc|DDL_z.npy` [15728]; `embed/gene_vectors.npy` [15728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15728 or target_col == 15728). Every well: [[EFCAB3P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB3P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
