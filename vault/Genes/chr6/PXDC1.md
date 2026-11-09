---
symbol: "PXDC1"
type: "gene"
col: 9734
ensembl_id: "ENSG00000168994"
name: "PX domain containing 1"
location: "6p25.2"
module: 46
arm: "+"
pooled_cpm: 12.1
n_lines_expressing: 41
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PXDC1

*PX domain containing 1* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.68× (z +6.1, q 7e-07, up in 21 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.215× (z -18.2, q 0e+00, down in 36 of 39 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.237× (z -17.0, q 0e+00, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELF4]] (+0.63, fdr 3e-05), [[IPO9-AS1]] (+0.58, fdr 4e-05), [[MAEA]] (+0.57, fdr 3e-05); moves opposite to [[SPATA6]] (-0.66, fdr 2e-05), [[RALGAPA2]] (-0.59, fdr 4e-05), [[ARL6]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF469]] → it (grade B ⚠); 4 go from it, the strongest it → [[TMEM186]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +6.1 | 7e-07 | 21/39 (MIA PaCa-2, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 0.001 | 17/34 (MIA PaCa-2, C32, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.020 | 15/36 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.088 | 17/37 (MIA PaCa-2, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.32× | +3.3 | 0.11 | 10/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.215×** | -18.2 | 0e+00 | 36/39 (A-172, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.237×** | -17.0 | 0e+00 | 36/39 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.244×** | -16.7 | 0e+00 | 37/39 (A-172, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.410×** | -10.5 | 1e-23 | 27/39 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.543×** | -6.9 | 5e-10 | 21/33 (HT-29, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.702×** | -5.9 | 3e-07 | 24/39 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.640×** | -5.3 | 1e-05 | 21/36 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **0.644×** | -5.0 | 4e-05 | 17/21 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.464×** | -4.7 | 1e-04 | 19/38 (A498, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.630×** | -4.6 | 2e-04 | 18/31 (hTERT-HPNE, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.038 | 12/39 (SW 1088, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.754×** | -3.3 | 0.038 | 12/38 (H4, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.087 | 12/35 (HepG2/C3A, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.64 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.0634× (z -15.3) |
| [[A498 (line)]] | wt | 16.8 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -14.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.148× (z -12.9) |
| [[A-172 (line)]] | wt | 20.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0657× (z -18.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.281× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0662× (z -14.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -10.6) |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.149× (z -11.2) |
| [[J82 (line)]] | alt | 26.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.249× (z -10.0) |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0808× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.132× (z -12.2) |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.227× (z -9.8) |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -14.2) |
| [[KATO III (line)]] | alt | 22.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.146× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0634× (z -14.2) |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -9.5) |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0597× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0988× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0739× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 18.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.170× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0922× (z -15.6) |
| [[C32 (line)]] | wt | 11.5 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.100× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 9.31 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0800× (z -13.1) |
| [[SW480 (line)]] | alt | 5.26 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -8.6) |
| [[A-427 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.967 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF4]] | +0.63 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[IPO9-AS1]] | +0.58 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[MAEA]] | +0.57 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[SETD1B]] | +0.57 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[ATXN1L]] | +0.57 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[GPR137]] | +0.56 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[ARHGEF17]] | +0.56 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ZBTB8A]] | +0.56 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[ZBTB2]] | +0.55 | +0.35 / +0.36 | both halves | 1e-04 |  |
| [[PTOV1-AS1]] | +0.55 | +0.26 / +0.50 | both halves | 4e-04 |  |
| [[GRK4]] | +0.55 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[ZNF621]] | +0.54 | +0.41 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA6]] | -0.66 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[RALGAPA2]] | -0.59 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ARL6]] | -0.56 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GUSBP1]] | -0.56 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[PGAP1]] | -0.53 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[FRRS1]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[BTBD3]] | -0.53 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[IMMP1L]] | -0.52 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.52 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[MRPS31P5-1]] | -0.52 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[PDK3]] | -0.52 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[PLA2G12A]] | -0.52 | -0.33 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF469]] | B | ZNF469 activity raises PXDC1's level | lines that do not express ZNF469 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without ZNF469 | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[RGS20]] | B | RGS20 activity raises PXDC1's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 2.67× lower at baseline in the lines without RGS20 | 0.078 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM186]] | B | PXDC1 activity lowers TMEM186's level | lines that do not express PXDC1 (9) vs lines expressing it (41) | 1.57× higher at baseline in the lines without PXDC1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TSPAN4, OSMR, VIM |
| [[GPR176]] | B | PXDC1 activity raises GPR176's level | lines that do not express PXDC1 (9) vs lines expressing it (41) | 5.04× lower at baseline in the lines without PXDC1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TSPAN4, OSMR, VIM |
| [[WNT5B]] | B | PXDC1 activity raises WNT5B's level | lines that do not express PXDC1 (9) vs lines expressing it (41) | 2.88× lower at baseline in the lines without PXDC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TSPAN4, OSMR, VIM |
| [[ARHGEF17]] | B | PXDC1 activity raises ARHGEF17's level | lines that do not express PXDC1 (9) vs lines expressing it (41) | 2.06× lower at baseline in the lines without PXDC1 | 0.086 | ⚠ within organs, on part of the lines; also absent: TSPAN4, OSMR, VIM |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.373). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (14.4, 7.3); signed map (20.0, -5.9). **Vector** length 76.6, 15.9% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | +2.8 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.2 | -16.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -17.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.0 | -18.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PX domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:3,722,614-3,751,713 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C6orf145 |
| Matched by | ensembl_id |

UniProt [Q5TGL8](https://www.uniprot.org/uniprotkb/Q5TGL8) carries no function annotation.

**Summary**, from NCBI Gene [221749](https://www.ncbi.nlm.nih.gov/gene/221749):

> Predicted to enable phosphatidylinositol binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21361) · Entrez [221749](https://www.ncbi.nlm.nih.gov/gene/221749) · UniProt [Q5TGL8](https://www.uniprot.org/uniprotkb/Q5TGL8) · Ensembl [ENSG00000168994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168994)

## Data

Gene col 9734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9734); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9734]; `tensor/DDL_lfc|DDL_z.npy` [9734]; `embed/gene_vectors.npy` [9734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9734 or target_col == 9734). Every well: [[PXDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
