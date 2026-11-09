---
symbol: "SLC29A2"
type: "gene"
col: 10512
ensembl_id: "ENSG00000174669"
name: "solute carrier family 29 member 2"
location: "11q13.2"
module: 18
arm: "+"
pooled_cpm: 7.96
n_lines_expressing: 36
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 7
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SLC29A2

*solute carrier family 29 member 2* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Cepharanthine (drug)]] 5 µM: 1.60× (z +7.9, q 1e-12, up in 23 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -20.8, q 0e+00, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3AP-AS1]] (+0.64, fdr 7e-06), [[CMTM8]] (+0.63, fdr 7e-06), [[GARNL3]] (+0.60, fdr 1e-05); moves opposite to [[USP11]] (-0.53, fdr 4e-05), [[PKN2-AS1]] (-0.52, fdr 4e-05), [[ERCC6L2-AS1]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); 7 go from it, the strongest it → [[GLB1L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **1.60×** | +7.9 | 1e-12 | 23/33 (LoVo, PANC-1, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.36×** | +5.2 | 4e-05 | 15/33 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.54×** | +5.2 | 4e-05 | 19/34 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.6 | 6e-04 | 10/31 (SW480, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.002 | 16/33 (NCI-H460, LoVo, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.004 | 6/33 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.010 | 7/32 (MIA PaCa-2, C-33 A, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.021 | 9/34 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.021 | 6/33 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.027 | 5/32 (HOP62, PANC-1, …) | top dose only | position effect removed |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.050 | 2/34 (HEC-1-A, PANC-1) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.050 | 5/34 (PANC-1, HOP62, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.294×** | -20.8 | 0e+00 | 28/31 (HCT15, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.350×** | -12.2 | 1e-31 | 24/33 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -11.2 | 6e-27 | 24/29 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.509×** | -8.1 | 6e-14 | 20/34 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -7.7 | 2e-12 | 23/30 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.572×** | -6.7 | 1e-09 | 17/34 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -6.4 | 1e-08 | 19/31 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -6.1 | 9e-08 | 17/30 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -5.7 | 1e-06 | 15/32 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.658×** | -5.1 | 2e-05 | 14/32 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -5.0 | 3e-05 | 17/31 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -4.3 | 8e-04 | 13/28 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.706×** | -4.2 | 0.001 | 13/33 (A-427, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.001 | 15/33 (NCI-H23, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.519×** | -4.1 | 0.001 | 12/30 (BT-474, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.724×** | -3.9 | 0.003 | 11/33 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -3.7 | 0.008 | 9/32 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 33.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.2) |
| [[A-427 (line)]] | wt | 28.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0981× (z -17.5) |
| [[PANC-1 (line)]] | alt | 9.60 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 8.97 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.0876× (z -11.3) |
| [[COLO 205 (line)]] | alt | 7.41 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -10.8) |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0552× (z -20.8) |
| [[KATO III (line)]] | alt | 16.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 4.74 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0411× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 4.08 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -11.7) |
| [[RKO (line)]] | wt | 9.95 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0942× (z -9.6) |
| [[SW48 (line)]] | wt | 11.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -8.9) |
| [[SW480 (line)]] | alt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 6.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.1) |
| [[LoVo (line)]] | wt | 7.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.2) |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 6.03 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.5) |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.6) |
| [[A-172 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP-AS1]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[CMTM8]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ARHGAP8]] | +0.59 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ACACA]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TMCO6]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MLXIPL]] | +0.56 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[CISD3]] | +0.56 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[SLC27A5]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[UCK2]] | +0.55 | +0.58 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ANKS6]] | +0.55 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[DHCR24]] | +0.55 | +0.58 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP11]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | -0.52 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ERCC6L2-AS1]] | -0.51 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[STAMBP]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[DECR1]] | -0.50 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[MAD2L1-DT]] | -0.49 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[CHD1-DT]] | -0.49 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[EFCAB6]] | -0.49 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[LINC01135]] | -0.49 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[UBE3B]] | -0.49 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[USP38-DT]] | -0.49 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[FAM120AOS]] | -0.49 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises SLC29A2's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without RASGEF1A | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[MCF2L]] | B | MCF2L activity raises SLC29A2's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without MCF2L | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[LHX6]] | B | LHX6 activity raises SLC29A2's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without LHX6 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity strengthens SLC29A2's drug response | lines that do not express ARHGAP44 (9) vs lines expressing it (25) | the lines without ARHGAP44 respond 0.56× as strongly (z diff +2.04); strongest at Homoharringtonine 5 µM: 0.35x vs 0.26x (z diff +3.1) | 0.058 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FGFR4]] | B | FGFR4 activity raises SLC29A2's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.58× lower at baseline in the lines without FGFR4 | 0.073 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[DMKN]] | B | DMKN activity raises SLC29A2's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.51× lower at baseline in the lines without DMKN | 0.077 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[RASAL1]] | B | RASAL1 activity raises SLC29A2's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without RASAL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[CKMT1B]] | C | CKMT1B activity raises SLC29A2's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 2.93× lower at baseline in the lines without CKMT1B | 0.036 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B; co-absent with the target |
| [[ARHGEF16]] | C | ARHGEF16 activity raises SLC29A2's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 3.11× lower at baseline in the lines without ARHGEF16 | 0.056 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP; co-absent with the target |
| [[LARGE2]] | C | LARGE2 activity raises SLC29A2's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 2.51× lower at baseline in the lines without LARGE2 | 0.077 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLB1L2]] | B | SLC29A2 activity raises GLB1L2's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 2.62× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[PTPN3]] | B | SLC29A2 activity raises PTPN3's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 2.27× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[NBEAL2]] | B | SLC29A2 activity raises NBEAL2's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[FGFR4]] | B | SLC29A2 activity raises FGFR4's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[CISD3]] | B | SLC29A2 activity raises CISD3's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without SLC29A2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN |
| [[MAP3K21]] | B | SLC29A2 activity raises MAP3K21's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 3.03× lower at baseline in the lines without SLC29A2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[CMTM8]] | B | SLC29A2 activity raises CMTM8's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without SLC29A2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.1, -38.5); signed map (-11.8, -54.7). **Vector** length 79.3, 19.4% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.0 | +5.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.9 | -3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 29 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,362,521-66,372,214 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DER12; previously ENT2, HNP36 |
| Gene groups (HGNC) | Solute carrier family 29 |
| Hallmark sets | MYC_TARGETS_V2, IL2_STAT5_SIGNALING |
| Reactome | 6 pathways, smallest: Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane; Azathioprine ADME; Transport of vitamins, nucleosides, and related molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14542](https://www.uniprot.org/uniprotkb/Q14542) (Equilibrative nucleoside transporter 2):

> Bidirectional uniporter involved in the facilitative transport of nucleosides and nucleobases, and contributes to maintaining their cellular homeostasis. Functions as a Na(+)-independent, passive transporter. Involved in the transport of nucleosides such as inosine, adenosine, uridine, thymidine, cytidine and guanosine. Also able to transport purine nucleobases (hypoxanthine, adenine, guanine) and pyrimidine nucleobases (thymine, uracil). Also mediates nicotinamide uptake supporting homeostasis …

**Summary**, from NCBI Gene [3177](https://www.ncbi.nlm.nih.gov/gene/3177):

> The uptake of nucleosides by transporters, such as SLC29A2, is essential for nucleotide synthesis by salvage pathways in cells that lack de novo biosynthetic pathways. Nucleoside transport also plays a key role in the regulation of many physiologic processes through its effect on adenosine concentration at the cell surface (Griffiths et al., 1997 [PubMed 9396714]).[supplied by OMIM, Nov 2008]

**Accessions** — [HGNC:11004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11004) · Entrez [3177](https://www.ncbi.nlm.nih.gov/gene/3177) · UniProt [Q14542](https://www.uniprot.org/uniprotkb/Q14542) · Ensembl [ENSG00000174669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174669)

## Data

Gene col 10512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10512); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10512]; `tensor/DDL_lfc|DDL_z.npy` [10512]; `embed/gene_vectors.npy` [10512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10512 or target_col == 10512). Every well: [[SLC29A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC29A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
