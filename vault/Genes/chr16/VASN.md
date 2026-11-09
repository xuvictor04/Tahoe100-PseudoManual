---
symbol: "VASN"
type: "gene"
col: 9604
ensembl_id: "ENSG00000168140"
name: "vasorin"
location: "16p13.3"
module: 59
arm: "+"
pooled_cpm: 6.36
n_lines_expressing: 44
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# VASN

*vasorin* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.02× (z +20.6, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.596× (z -5.4, q 4e-05, down in 19 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.665× (z -4.3, q 0.006, down in 17 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.0520×); [[Verteporfin (drug)]] 5 µM in 1 line (RPMI-7951 0.134×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLIP]] (+0.71, fdr 7e-06), [[KDM5B]] (+0.64, fdr 1e-05), [[HOOK2]] (+0.63, fdr 7e-06); moves opposite to [[MTOR]] (-0.59, fdr 1e-05), [[SLC35B4]] (-0.57, fdr 2e-05), [[MAPKAPK5]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DLX2]] → it (grade B ⚠); 5 go from it, the strongest it → [[TNFAIP6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.02×** | +20.6 | 0e+00 | 32/32 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.73×** | +18.3 | 0e+00 | 39/41 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.31×** | +17.8 | 0e+00 | 29/34 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.90×** | +16.7 | 0e+00 | 39/40 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.96×** | +14.4 | 4e-45 | 39/41 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +8.0 | 1e-13 | 25/40 (HS-578T, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +7.2 | 5e-11 | 5/12 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +7.1 | 7e-11 | 19/41 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +6.9 | 4e-10 | 19/34 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.4 | 9e-09 | 15/32 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +6.3 | 2e-08 | 8/21 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.0 | 1e-07 | 11/41 (PANC-1, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +5.9 | 2e-07 | 16/41 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +5.8 | 2e-07 | 18/39 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.73×** | +5.7 | 4e-07 | 9/20 (HS-578T, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 9e-04 | 10/40 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.002 | 13/34 (hTERT-HPNE, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.002 | 6/40 (HS-578T, A-172, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.003 | 14/37 (SW480, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9604.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.0520×); [[Verteporfin (drug)]] 5 µM in 1 line (RPMI-7951 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.596×** | -5.4 | 4e-05 | 19/40 (A498, PANC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.665×** | -4.3 | 0.006 | 17/40 (A498, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.673×** | -4.0 | 0.014 | 15/38 (SW 900, SNU-423, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.738× | -3.2 | 0.19 | 15/38 (HT-29, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.732× | -3.1 | 0.19 | 11/36 (RPMI-7951, HT-29, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.568× | -3.1 | 0.19 | 9/33 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.748× | -3.0 | 0.20 | 6/41 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +14.6) | — |
| [[HS-578T (line)]] | alt | 24.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.11× (z +11.0) | — |
| [[A498 (line)]] | wt | 9.70 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 3.87 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.02× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +8.9) | [[Verteporfin (drug)]] 5 µM 0.134× (z -8.6) |
| [[SNU-423 (line)]] | alt | 20.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +10.0) | — |
| [[A-172 (line)]] | wt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 2.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +9.3) | — |
| [[H4 (line)]] | wt | 9.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +8.9) | — |
| [[KATO III (line)]] | alt | 5.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 6.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 4.62 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0520× (z -9.6) |
| [[SW480 (line)]] | alt | 5.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +8.9) | — |
| [[A-427 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLIP]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[KDM5B]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[HOOK2]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[DBP]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.60 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[BMF]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[IER5L]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CCNG2]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[GPRC5C]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ZMIZ1]] | +0.58 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[CBX4]] | +0.58 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[CBX8]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTOR]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[SLC35B4]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.55 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[MRPS27]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.55 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[CHCHD3]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NUDT5]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NUP155]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TIMM23B-AGAP6]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[EFTUD2]] | -0.52 | -0.51 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX2]] | B | DLX2 activity raises VASN's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without DLX2 | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[CXXC5]] | B | CXXC5 activity raises VASN's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without CXXC5 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[TENT5C]] | B | TENT5C activity raises VASN's level | lines that do not express TENT5C (5) vs lines expressing it (45) | 2.51× lower at baseline in the lines without TENT5C | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000258695, CTSD, BRME1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP6]] | B | VASN activity lowers TNFAIP6's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without VASN | 0.031 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[FAM117A]] | B | VASN activity raises FAM117A's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without VASN | 0.056 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[FAM222A]] | B | VASN activity raises FAM222A's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without VASN | 0.075 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[TUBB3]] | B | VASN activity raises TUBB3's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without VASN | 0.075 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[CBX4]] | B | VASN activity raises CBX4's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without VASN | 0.091 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (29.9, -29.9); signed map (-5.2, 13.7). **Vector** length 72.3, 13.5% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +17.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +20.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | vasorin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,371,848-4,383,538 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SLITL2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6EMK4](https://www.uniprot.org/uniprotkb/Q6EMK4) (Vasorin):

> May act as an inhibitor of TGF-beta signaling.

**Summary**, from NCBI Gene [114990](https://www.ncbi.nlm.nih.gov/gene/114990):

> Enables transforming growth factor beta binding activity. Involved in negative regulation of epithelial to mesenchymal transition and negative regulation of transforming growth factor beta receptor signaling pathway. Located in cell surface; extracellular exosome; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18517) · Entrez [114990](https://www.ncbi.nlm.nih.gov/gene/114990) · UniProt [Q6EMK4](https://www.uniprot.org/uniprotkb/Q6EMK4) · Ensembl [ENSG00000168140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168140)

## Data

Gene col 9604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9604); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9604]; `tensor/DDL_lfc|DDL_z.npy` [9604]; `embed/gene_vectors.npy` [9604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9604 or target_col == 9604). Every well: [[VASN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VASN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
