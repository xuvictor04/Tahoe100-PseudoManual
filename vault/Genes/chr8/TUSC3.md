---
symbol: "TUSC3"
type: "gene"
col: 2488
ensembl_id: "ENSG00000104723"
name: "tumor suppressor candidate 3"
location: "8p22"
module: 4
arm: "+"
pooled_cpm: 121.34
n_lines_expressing: 33
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TUSC3

*tumor suppressor candidate 3* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.17× (z +14.6, q 3e-45, up in 21 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.712× (z -9.0, q 8e-17, down in 21 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A498 0.325×, HEC-1-A 0.631×, SNU-423 0.511×, NCI-H460 0.518×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.331×, SK-MEL-2 0.453×, A498 0.451×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Menadione (drug)]] 0.05 µM in 1 line (SW 1271 0.0933×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL8]] (+0.59, fdr 1e-05), [[SACS]] (+0.58, fdr 1e-05), [[EIF4G3]] (+0.56, fdr 1e-05); moves opposite to [[MMUT]] (-0.57, fdr 1e-05), [[CRLS1]] (-0.54, fdr 1e-05), [[CCS]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ROR1-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[LOX]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.17×** | +14.6 | 3e-45 | 21/31 (HEC-1-A, A-172, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.98×** | +12.9 | 2e-35 | 21/31 (A-172, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +12.6 | 6e-34 | 29/31 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +12.1 | 1e-31 | 27/31 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +10.8 | 3e-25 | 25/31 (SHP-77, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.75×** | +9.9 | 3e-21 | 20/28 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +9.2 | 4e-18 | 27/31 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +8.9 | 6e-17 | 24/31 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +8.3 | 9e-15 | 20/31 (SNU-423, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +8.2 | 9e-15 | 18/30 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +8.2 | 1e-14 | 27/31 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.53×** | +8.0 | 7e-14 | 25/31 (SNU-423, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +7.7 | 8e-13 | 18/31 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +6.4 | 8e-09 | 18/31 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.3 | 9e-09 | 23/32 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +6.1 | 4e-08 | 20/31 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 3e-07 | 17/31 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.6 | 8e-07 | 17/31 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A498 0.325×, HEC-1-A 0.631×, SNU-423 0.511×, NCI-H460 0.518×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.331×, SK-MEL-2 0.453×, A498 0.451×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Menadione (drug)]] 0.05 µM in 1 line (SW 1271 0.0933×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -9.0 | 8e-17 | 21/32 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.808×** | -4.0 | 0.016 | 17/31 (H4, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.805×** | -3.9 | 0.016 | 15/30 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.826×** | -3.6 | 0.044 | 14/31 (SNU-423, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.850× | -3.1 | 0.25 | 10/31 (SNU-423, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 193 | 14 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +33.2) | — |
| [[SNU-423 (line)]] | alt | 185 | 12 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +21.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -10.6) |
| [[SW 900 (line)]] | alt | 176 | 13 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.47× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 169 | 12 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.74× (z +17.4) | — |
| [[NCI-H2347 (line)]] | alt | 160 | 12 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.17× (z +24.3) | — |
| [[CFPAC-1 (line)]] | alt | 52.9 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +15.1) | — |
| [[HEC-1-A (line)]] | alt | 324 | 8 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 4.07× (z +23.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 339 | 6 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -9.1) |
| [[A498 (line)]] | wt | 511 | 4 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 176 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.81× (z +22.3) | — |
| [[HOP62 (line)]] | alt | 138 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.36× (z +17.9) | — |
| [[NCI-H460 (line)]] | wt | 237 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 4.60× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 133 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.65× (z +13.6) | — |
| [[H4 (line)]] | wt | 164 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.25× (z +14.7) | — |
| [[SHP-77 (line)]] | alt | 438 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +11.7) | — |
| [[C32 (line)]] | wt | 43.7 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.71× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 160 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 73.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 133 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.8) |
| [[C-33 A (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 63.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +16.5) | — |
| [[SW 1271 (line)]] | alt | 82.1 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0933× (z -8.9) |
| [[A-427 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 156 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 151 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL8]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SACS]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[EIF4G3]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[MMP16]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NAV3]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ADAMTS1]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CHCHD3]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 | pathway: Protein localization |
| [[ROR1-AS1]] | +0.54 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[BICD1]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ARMC9]] | +0.53 | +0.53 / +0.49 | both halves | 2e-05 |  |
| [[ZFPM2-AS1]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[FAT1]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMUT]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CRLS1]] | -0.54 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CCS]] | -0.54 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TMEM134]] | -0.54 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[TRNAU1AP]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[GLT8D1]] | -0.53 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[LOX]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[MFSD8]] | -0.52 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[PEX13]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 | pathway: Protein localization |
| [[ZNF451]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[LNX2]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[BBOF1]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROR1-AS1]] | B | ROR1-AS1 activity strengthens TUSC3's drug response | lines that do not express ROR1-AS1 (10) vs lines expressing it (22) | the lines without ROR1-AS1 respond 0.48× as strongly (z diff +2.81); strongest at Auranofin 5 µM: 0.91x vs 1.77x (z diff +5.8) | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; target measured in part of the lines; artifact flags |
| [[ZFPM2-AS1]] | B | ZFPM2-AS1 activity strengthens TUSC3's drug response | lines that do not express ZFPM2-AS1 (8) vs lines expressing it (24) | the lines without ZFPM2-AS1 respond 0.31× as strongly (z diff +3.56); strongest at Auranofin 5 µM: 0.88x vs 1.70x (z diff +6.1) | 0.060 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6; target measured in part of the lines; artifact flags |
| [[ADAMTS1]] | C | ADAMTS1 activity raises TUSC3's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 4.71× lower at baseline in the lines without ADAMTS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises TUSC3's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 4.11× lower at baseline in the lines without ROR1-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | TUSC3 activity raises LOX's level | lines that do not express TUSC3 (17) vs lines expressing it (33) | 4.61× lower at baseline in the lines without TUSC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAP9, BVES-AS1, RNF150; its own permutation p |
| [[RABGAP1L]] | B | TUSC3 activity lowers RABGAP1L's level | lines that do not express TUSC3 (17) vs lines expressing it (33) | 1.27× higher at baseline in the lines without TUSC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAP9, BVES-AS1, RNF150; its own permutation p |
| [[TFPI2]] | C | TUSC3 activity raises TFPI2's level | lines that do not express TUSC3 (17) vs lines expressing it (33) | 6.18× lower at baseline in the lines without TUSC3 | 0.075 | ⚠ within organs, on part of the lines; also absent: MAP9, BVES-AS1, RNF150; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.7, 38.3); signed map (35.2, 26.4). **Vector** length 105, 30.3% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +14.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +12.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.6 | -3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tumor suppressor candidate 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:15,417,215-15,766,649 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13453, N33, OST3A, MRT7, MagT2, SLC58A2; previously MRT22 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits; Solute carrier family 58 |
| Reactome | 20 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Miscellaneous transport and binding events; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13454](https://www.uniprot.org/uniprotkb/Q13454) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit TUSC3):

> Acts as accessory component of the N-oligosaccharyl transferase (OST) complex which catalyzes the transfer of a high mannose oligosaccharide from a lipid-linked oligosaccharide donor to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains. Involved in N-glycosylation of STT3B-dependent substrates. Specifically required for the glycosylation of a subset of acceptor sites that are near cysteine residues; in this function seems to act redundantly with …

**Summary**, from NCBI Gene [7991](https://www.ncbi.nlm.nih.gov/gene/7991):

> This gene encodes a protein that has been associated with several biological functions including cellular magnesium uptake, protein glycosylation and embryonic development. This protein localizes to the endoplasmic reticulum and acts as a component of the oligosaccharyl transferase complex which is responsible for N-linked protein glycosylation. This gene is a candidate tumor suppressor gene. Homozygous mutations in this gene are associated with autosomal recessive nonsyndromic mental …

**Accessions** — [HGNC:30242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30242) · Entrez [7991](https://www.ncbi.nlm.nih.gov/gene/7991) · UniProt [Q13454](https://www.uniprot.org/uniprotkb/Q13454) · Ensembl [ENSG00000104723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104723)

## Data

Gene col 2488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2488); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2488]; `tensor/DDL_lfc|DDL_z.npy` [2488]; `embed/gene_vectors.npy` [2488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2488 or target_col == 2488). Every well: [[TUSC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUSC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
