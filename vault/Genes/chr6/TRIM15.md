---
symbol: "TRIM15"
type: "gene"
col: 12900
ensembl_id: "ENSG00000204610"
name: "tripartite motif containing 15"
location: "6p22.1"
module: 162
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 16
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 39
direction_downstream: 70
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# TRIM15

*tripartite motif containing 15* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.14× (z +12.6, q 2e-33, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Bimiralisib (drug)]] 5 µM: 0.399× (z -3.8, q 0.094, down in 4 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.134×, AsPC-1 0.0957×, LoVo 0.213×, HT-29 0.115×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.250×, KATO III 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HCT15 0.119×); [[Auranofin (drug)]] 5 µM in 1 line (CFPAC-1 0.102×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (SW48 0.0671×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRG1]] (+0.64, fdr 1e-05), [[SLC52A3]] (+0.64, fdr 1e-05), [[NTMT1]] (+0.64, fdr 1e-05); moves opposite to [[GLB1]] (-0.51, fdr 2e-05), [[AP3M1]] (-0.50, fdr 4e-05), [[VTI1B]] (-0.49, fdr 1e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); 70 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +12.6 | 2e-33 | 9/14 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.33×** | +9.3 | 5e-18 | 14/14 (LS 180, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +9.2 | 5e-18 | 2/8 (SW1417, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.79×** | +8.0 | 2e-13 | 9/14 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.27×** | +6.3 | 3e-08 | 14/14 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.33×** | +6.3 | 3e-08 | 14/14 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +5.9 | 3e-07 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.11×** | +5.8 | 5e-07 | 0/10 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.7 | 9e-07 | 2/14 (HepG2/C3A, AsPC-1) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.8 | 8e-05 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.76×** | +4.4 | 7e-04 | 2/12 (SW1417, CFPAC-1) | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.75×** | +4.3 | 1e-03 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.79×** | +4.2 | 0.001 | 1/6 (HCT15) | top dose only | noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.68×** | +4.0 | 0.003 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.9 | 0.003 | 3/14 (HepG2/C3A, LS 180, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +3.8 | 0.005 | 7/14 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.016 | 2/14 (AsPC-1, SW1417) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.27×** | +3.5 | 0.017 | 1/12 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.017 | 0/14 | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.018 | 1/14 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.031 | 1/14 (SW480) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.10×** | +3.1 | 0.043 | 1/14 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12900.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.134×, AsPC-1 0.0957×, LoVo 0.213×, HT-29 0.115×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.250×, KATO III 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HCT15 0.119×); [[Auranofin (drug)]] 5 µM in 1 line (CFPAC-1 0.102×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (SW48 0.0671×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | **0.399×** | -3.8 | 0.094 | 4/14 (HCT15, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.637×** | -3.6 | 0.096 | 0/14 | inconsistent across doses | position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.05 µM |  | **0.643×** | -3.5 | 0.096 | 0/14 | inconsistent across doses | position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 0.752× | -3.2 | 0.19 | 0/14 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 20.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.0957× (z -12.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 21.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 47.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 9.06 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.102× (z -9.0) |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -11.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0671× (z -8.9) |
| [[SW480 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.474 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRG1]] | +0.64 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[SLC52A3]] | +0.64 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[NTMT1]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TNFRSF1B]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SHH]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.57 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[LENG9]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ID1]] | +0.56 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[KCNH8]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MIDN]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ARHGEF38]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1]] | -0.51 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[AP3M1]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[VTI1B]] | -0.49 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[EIF3F]] | -0.48 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[TPGS2]] | -0.48 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[GFM2]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[CIZ1]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[THOC5]] | -0.47 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[STMP1]] | -0.46 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[GPN1]] | -0.46 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GHITM]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[UFD1]] | -0.45 | -0.43 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 2, C 37. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TRIM15's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.82× lower at baseline in the lines without ELF3-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[STON2]] | B | STON2 activity raises TRIM15's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without STON2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[TMEM45B]] | C | TMEM45B activity raises TRIM15's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 7.12× lower at baseline in the lines without TMEM45B | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[RNF39]] | C | RNF39 activity raises TRIM15's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 6.00× lower at baseline in the lines without RNF39 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises TRIM15's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.48× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises TRIM15's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.47× lower at baseline in the lines without C1orf116 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises TRIM15's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 5.54× lower at baseline in the lines without B3GNT3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[LINC02964]] | C | LINC02964 activity raises TRIM15's level | lines that do not express LINC02964 (38) vs lines expressing it (12) | 9.97× lower at baseline in the lines without LINC02964 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: CLRN3, GPA33, EPS8L3; co-absent with the target |
| [[CBLC]] | C | CBLC activity raises TRIM15's level | lines that do not express CBLC (31) vs lines expressing it (19) | 5.33× lower at baseline in the lines without CBLC | 5e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises TRIM15's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 6.92× lower at baseline in the lines without GCNT3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[SH2D3A]] | C | SH2D3A activity raises TRIM15's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.88× lower at baseline in the lines without SH2D3A | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[SGPP2]] | C | SGPP2 activity raises TRIM15's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 4.78× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4; co-absent with the target |

### Downstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 28, C 42. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | TRIM15 activity raises ELF3-AS1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 4.15× lower at baseline in the lines without TRIM15 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ITPKC]] | B | TRIM15 activity raises ITPKC's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.33× lower at baseline in the lines without TRIM15 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[GJB2]] | B | TRIM15 activity raises GJB2's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.88× lower at baseline in the lines without TRIM15 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[EPHA2-AS1]] | B | TRIM15 activity raises EPHA2-AS1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.87× lower at baseline in the lines without TRIM15 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[RDH13]] | B | TRIM15 activity raises RDH13's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.42× lower at baseline in the lines without TRIM15 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[STON2]] | B | TRIM15 activity raises STON2's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.86× lower at baseline in the lines without TRIM15 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[WWC1]] | B | TRIM15 activity raises WWC1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without TRIM15 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ABHD11]] | B | TRIM15 activity raises ABHD11's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.66× lower at baseline in the lines without TRIM15 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ZFP36L2]] | B | TRIM15 activity raises ZFP36L2's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.67× lower at baseline in the lines without TRIM15 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[MIDN]] | B | TRIM15 activity raises MIDN's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.49× lower at baseline in the lines without TRIM15 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[TRAF4]] | B | TRIM15 activity raises TRAF4's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.40× lower at baseline in the lines without TRIM15 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[MTHFR]] | B | TRIM15 activity raises MTHFR's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.58× lower at baseline in the lines without TRIM15 | 0.043 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, 46.8); signed map (7.7, 31.3). **Vector** length 49.5, 16.3% of its response variance represented; |z| ≥ 3 in 334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.8 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.5 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.3 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,163,206-30,172,693 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNFB7, RNF93; previously ZNF178 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C019](https://www.uniprot.org/uniprotkb/Q9C019) (E3 ubiquitin-protein ligase TRIM15):

> E3 ubiquitin-protein ligase that plays a role in several processes including innate antiviral immnity, cell migration and chemotaxis. Acts as a 'Lys-63'-specific ubiquitin ligase for MAPK1/ERK2 and MAPK3/ERK1, promoting their activation by facilitating their interaction with MAP2K1 and MAP2K2. Also plays a role in cell migration and chemotaxis by acting as a stable focal adhesion component upon recruitment by multi-adapter protein paxillin/PXN. Functions in the RIGI-mediated interferon …

**Summary**, from NCBI Gene [89870](https://www.ncbi.nlm.nih.gov/gene/89870):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to the cytoplasm. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16284) · Entrez [89870](https://www.ncbi.nlm.nih.gov/gene/89870) · UniProt [Q9C019](https://www.uniprot.org/uniprotkb/Q9C019) · Ensembl [ENSG00000204610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204610)

## Data

Gene col 12900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12900); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12900]; `tensor/DDL_lfc|DDL_z.npy` [12900]; `embed/gene_vectors.npy` [12900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12900 or target_col == 12900). Every well: [[TRIM15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
