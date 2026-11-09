---
symbol: "CIB1"
type: "gene"
col: 11614
ensembl_id: "ENSG00000185043"
name: "calcium and integrin binding 1"
location: "15q26.1"
module: 154
arm: "+"
pooled_cpm: 78.38
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 14
direction_downstream: 12
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# CIB1

*calcium and integrin binding 1* — 15q26.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.288× (z -14.4, q 4e-44, down in 43 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPT1]] (+0.77, fdr 7e-06), [[CIAO2B]] (+0.75, fdr 7e-06), [[UBA6]] (+0.75, fdr 1e-05); moves opposite to [[ZMYND11]] (-0.77, fdr 7e-06), [[EWSR1]] (-0.69, fdr 2e-05), [[RCN1]] (-0.67, fdr 4e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[PLEK2]] → it (grade B ⚠); 12 go from it, the strongest it → [[NDRG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | 1.49× | +3.3 | 0.54 | 26/44 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.288×** | -14.4 | 4e-44 | 43/43 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -7.0 | 5e-10 | 38/43 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.473×** | -5.9 | 9e-07 | 37/44 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.247×** | -5.7 | 1e-06 | 41/44 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -5.7 | 2e-06 | 42/45 (AsPC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -4.7 | 3e-04 | 28/45 (CFPAC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.545×** | -4.3 | 0.001 | 32/46 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.598×** | -4.2 | 0.002 | 29/44 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -3.9 | 0.006 | 27/43 (hTERT-HPNE, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.597×** | -3.8 | 0.007 | 32/44 (LoVo, SW 1088, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.415×** | -3.6 | 0.016 | 32/46 (LoVo, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.036 | 28/44 (HOP62, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.735×** | -3.3 | 0.041 | 26/44 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.668×** | -3.3 | 0.044 | 25/44 (LoVo, BT-474, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.457×** | -3.2 | 0.051 | 27/44 (LoVo, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -3.1 | 0.066 | 28/44 (H4, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.073 | 24/44 (Panc 03.27, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 203 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -22.0) |
| [[CFPAC-1 (line)]] | alt | 280 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -19.3) |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -19.3) |
| [[Panc 03.27 (line)]] | alt | 70.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.9) |
| [[A498 (line)]] | wt | 106 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.7) |
| [[BT-474 (line)]] | alt | 44.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -13.3) |
| [[COLO 205 (line)]] | alt | 83.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.4) |
| [[HS-578T (line)]] | alt | 70.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 66.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.4) |
| [[SW 900 (line)]] | alt | 79.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.0) |
| [[A-172 (line)]] | wt | 69.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 90.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.4) |
| [[C32 (line)]] | wt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.4) |
| [[H4 (line)]] | wt | 66.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 81.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -18.8) |
| [[Hs 766T (line)]] | wt | 80.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.0) |
| [[HT-29 (line)]] | alt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.8) |
| [[J82 (line)]] | alt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.1) |
| [[KATO III (line)]] | alt | 87.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.9) |
| [[LoVo (line)]] | wt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.4) |
| [[LS 180 (line)]] | wt | 82.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 198 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.6) |
| [[PANC-1 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 55.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.1) |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 34.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.9) |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.7) |
| [[A-427 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPT1]] | +0.77 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.75 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[UBA6]] | +0.75 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.74 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SH3BGRL3]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[MPG]] | +0.72 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[POLD4]] | +0.71 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[NDRG1]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SEMA4B]] | +0.70 | +0.75 / +0.58 | both halves | 7e-06 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[ETHE1]] | +0.69 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[EPN2]] | +0.69 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ZNRD2]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.77 | -0.72 / -0.59 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.69 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[RCN1]] | -0.67 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[MRRF]] | -0.66 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | -0.65 | -0.70 / -0.34 | both halves | 1e-04 |  |
| [[FUBP1]] | -0.64 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ZFX]] | -0.64 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.63 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ADI1]] | -0.63 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[UTP20]] | -0.63 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.62 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[TRIM44]] | -0.62 | -0.55 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEK2]] | B | PLEK2 activity raises CIB1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.00× lower at baseline in the lines without PLEK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[IL1RAP]] | B | IL1RAP activity raises CIB1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without IL1RAP | 0.024 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises CIB1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.81× lower at baseline in the lines without TNFRSF11A | 0.024 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises CIB1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.59× lower at baseline in the lines without S100A16 | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[SERPINB1]] | B | SERPINB1 activity raises CIB1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without SERPINB1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[MARCHF3]] | B | MARCHF3 activity raises CIB1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without MARCHF3 | 0.041 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[WNT7B]] | B | WNT7B activity raises CIB1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without WNT7B | 0.048 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[ABHD17C]] | B | ABHD17C activity raises CIB1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without ABHD17C | 0.056 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[FAM107B]] | B | FAM107B activity raises CIB1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without FAM107B | 0.066 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[TMCC3]] | B | TMCC3 activity raises CIB1's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without TMCC3 | 0.070 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PLAUR]] | B | PLAUR activity raises CIB1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.41× lower at baseline in the lines without PLAUR | 0.079 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises CIB1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.25× lower at baseline in the lines without GPRC5A | 0.085 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | C | CIB1, [[SEMA4B]], [[SLC2A1]] activity raises NDRG1's level | lines that do not express CIB1, SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 8.44× lower at baseline in the lines without CIB1, SEMA4B, SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[LINC00887]] | C | CIB1, [[SEMA4B]] activity raises LINC00887's level | lines that do not express CIB1, SEMA4B (4) vs lines expressing them (46) | 3.28× lower at baseline in the lines without CIB1, SEMA4B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p; co-absent genes |
| [[GTF3C6]] | C | CIB1 activity lowers GTF3C6's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.82× higher at baseline in the lines without CIB1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[PRAF2]] | C | CIB1 activity raises PRAF2's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without CIB1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[ILF3]] | C | CIB1 activity lowers ILF3's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.52× higher at baseline in the lines without CIB1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[SDF2]] | C | CIB1 activity raises SDF2's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without CIB1 | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |
| [[PLEK2]] | C | CIB1, [[SEMA4B]] activity raises PLEK2's level | lines that do not express CIB1, SEMA4B (4) vs lines expressing them (46) | 4.98× lower at baseline in the lines without CIB1, SEMA4B | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[S100A16]] | C | CIB1 activity raises S100A16's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 7.70× lower at baseline in the lines without CIB1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[STK17A]] | C | CIB1 activity raises STK17A's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without CIB1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[FAIM]] | C | CIB1, [[SEMA4B]], [[SLC2A1]] activity lowers FAIM's level | lines that do not express CIB1, SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 1.66× higher at baseline in the lines without CIB1, SEMA4B, SLC2A1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p; co-absent genes |
| [[LARP1]] | C | CIB1 activity lowers LARP1's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without CIB1 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |
| [[MAD2L2]] | C | CIB1 activity lowers MAD2L2's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without CIB1 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.0, 2.7); signed map (-4.3, 47.1). **Vector** length 125, 46.8% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -1.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +2.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.4 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | +2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.4 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.1 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | calcium and integrin binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,229,975-90,234,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SIP2-28, CIB, KIP |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99828](https://www.uniprot.org/uniprotkb/Q99828) (Calcium and integrin-binding protein 1):

> Calcium-binding protein that plays a role in the regulation of numerous cellular processes, such as cell differentiation, cell division, cell proliferation, cell migration, thrombosis, angiogenesis, cardiac hypertrophy and apoptosis. Involved in bone marrow megakaryocyte differentiation by negatively regulating thrombopoietin-mediated signaling pathway. Participates in the endomitotic cell cycle of megakaryocyte, a form of mitosis in which both karyokinesis and cytokinesis are interrupted. …

**Summary**, from NCBI Gene [10519](https://www.ncbi.nlm.nih.gov/gene/10519):

> This gene encodes a member of the EF-hand domain-containing calcium-binding superfamily. The encoded protein interacts with many other proteins, including the platelet integrin alpha-IIb-beta-3, DNA-dependent protein kinase, presenilin-2, focal adhesion kinase, p21 activated kinase, and protein kinase D. The encoded protein may be involved in cell survival and proliferation, and is associated with several disease states including cancer and Alzheimer's disease. Alternative splicing results in …

**Accessions** — [HGNC:16920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16920) · Entrez [10519](https://www.ncbi.nlm.nih.gov/gene/10519) · UniProt [Q99828](https://www.uniprot.org/uniprotkb/Q99828) · Ensembl [ENSG00000185043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185043)

## Data

Gene col 11614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11614); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11614]; `tensor/DDL_lfc|DDL_z.npy` [11614]; `embed/gene_vectors.npy` [11614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11614 or target_col == 11614). Every well: [[CIB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
