---
symbol: "AZGP1"
type: "gene"
col: 8388
ensembl_id: "ENSG00000160862"
name: "alpha-2-glycoprotein 1, zinc-binding"
location: "7q22.1"
module: 44
arm: "+"
pooled_cpm: 7.02
n_lines_expressing: 15
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 57
direction_downstream: 48
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# AZGP1

*alpha-2-glycoprotein 1, zinc-binding* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.48× (z +10.8, q 2e-24, up in 4 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +7.7, q 3e-12, up in 4 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.511× (z -5.1, q 2e-04, down in 12 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJB1]] (+0.73, fdr 7e-06), [[TFF3]] (+0.68, fdr 1e-05), [[CLRN3]] (+0.65, fdr 1e-05); moves opposite to [[CLIP1]] (-0.53, fdr 3e-05), [[RHBDD3]] (-0.48, fdr 5e-05), [[CPLANE1]] (-0.47, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 57 arrows point to it, the strongest [[MCF2L]] → it (grade B ⚠); 48 go from it, the strongest it → [[EPHB3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.48×** | +10.8 | 2e-24 | 4/8 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.95×** | +10.3 | 2e-22 | 5/11 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +7.7 | 3e-12 | 4/12 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +7.5 | 7e-12 | 8/13 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +7.2 | 6e-11 | 12/13 (SW1417, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +6.7 | 2e-09 | 11/13 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.12×** | +5.2 | 2e-05 | 4/10 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.92×** | +4.9 | 7e-05 | 7/13 (SW1417, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.005 | 4/13 (AsPC-1, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.005 | 6/12 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.66×** | +3.8 | 0.008 | 0/12 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.63×** | +3.5 | 0.021 | 2/12 (Panc 03.27, AsPC-1) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.57×** | +3.4 | 0.033 | 4/12 (KATO III, HepG2/C3A, …) | top dose only | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.058 | 1/12 (AsPC-1) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.071 | 1/12 (SK-MEL-2) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.0 | 0.077 | 7/13 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.00×** | +3.0 | 0.077 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8388.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.511×** | -5.1 | 2e-04 | 12/13 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.582×** | -4.1 | 0.013 | 12/12 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.609×** | -3.7 | 0.035 | 7/12 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.608×** | -3.6 | 0.043 | 11/13 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.614×** | -3.5 | 0.058 | 0/13 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.636×** | -3.4 | 0.060 | 9/13 (KATO III, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.649×** | -3.3 | 0.087 | 0/13 | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.627× | -3.2 | 0.11 | 7/13 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.643× | -3.1 | 0.13 | 4/13 (SW48, HT-29, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.465× | -3.0 | 0.13 | 2/13 (COLO 205, SK-MEL-2) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.671× | -3.0 | 0.13 | 1/13 (SW48) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 52.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -18.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -14.6) |
| [[SW480 (line)]] | alt | 22.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -9.3) |
| [[COLO 205 (line)]] | alt | 61.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 51.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 34.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0409× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 8.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 27.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.11× (z +9.0) | — |
| [[A-172 (line)]] | wt | 0.812 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.963 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJB1]] | +0.73 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[TFF3]] | +0.68 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[CLRN3]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[VIL1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NKD1]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FGFR4]] | +0.62 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[KLK7]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ENTPD2]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PCK1]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TMEM139]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[LINC01819]] | +0.60 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[KLK6]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIP1]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RHBDD3]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[CPLANE1]] | -0.47 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[CCT6P3]] | -0.47 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[ZSCAN29]] | -0.46 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[RAB30-DT]] | -0.46 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[N4BP2]] | -0.46 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[PEF1]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[TTC6]] | -0.46 | -0.39 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 2, C 55. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCF2L]] | B | MCF2L activity raises AZGP1's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without MCF2L | 0.021 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[CPLANE1]] | B | CPLANE1 activity lowers AZGP1's level | lines that do not express CPLANE1 (5) vs lines expressing it (45) | 11.00× higher at baseline in the lines without CPLANE1 | 0.079 | ⚠ within organs, on part of the lines; also absent: NKAIN1, SIX4, TPST1; maybe low, not absent |
| [[GJB1]] | C | GJB1 activity raises AZGP1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 10.88× lower at baseline in the lines without GJB1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises AZGP1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 9.23× lower at baseline in the lines without LYZ | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises AZGP1's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 5.43× lower at baseline in the lines without TMEM139 | 6e-04 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises AZGP1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 5.51× lower at baseline in the lines without TFF3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises AZGP1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 7.20× lower at baseline in the lines without CLRN3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises AZGP1's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 4.42× lower at baseline in the lines without LINC01819 | 0.001 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[KLK6]] | C | KLK6 activity raises AZGP1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 4.91× lower at baseline in the lines without KLK6 | 0.002 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises AZGP1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.95× lower at baseline in the lines without GPX2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[MOGAT3]] | C | MOGAT3 activity raises AZGP1's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 4.42× lower at baseline in the lines without MOGAT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises AZGP1's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 4.81× lower at baseline in the lines without HNF4A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 8, C 40. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB3]] | B | AZGP1 activity raises EPHB3's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.23× lower at baseline in the lines without AZGP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[EEPD1]] | B | AZGP1 activity raises EEPD1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.25× lower at baseline in the lines without AZGP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[CPLANE1]] | B | AZGP1 activity lowers CPLANE1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 2.85× higher at baseline in the lines without AZGP1 | 0.028 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[LMTK3]] | B | AZGP1 activity raises LMTK3's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 2.79× lower at baseline in the lines without AZGP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[RGS14]] | B | AZGP1 activity raises RGS14's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 1.57× lower at baseline in the lines without AZGP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[MROH7]] | B | AZGP1 activity raises MROH7's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 1.93× lower at baseline in the lines without AZGP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[MCF2L]] | B | AZGP1 activity raises MCF2L's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 2.15× lower at baseline in the lines without AZGP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[FGFR4]] | B | AZGP1 activity raises FGFR4's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 1.97× lower at baseline in the lines without AZGP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[LEMD1]] | C | AZGP1 activity raises LEMD1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 7.30× lower at baseline in the lines without AZGP1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[GJB1]] | C | AZGP1 activity raises GJB1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.95× lower at baseline in the lines without AZGP1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[RNF128]] | C | AZGP1 activity raises RNF128's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 6.98× lower at baseline in the lines without AZGP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[TMEM139]] | C | AZGP1 activity raises TMEM139's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.68× lower at baseline in the lines without AZGP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 46.2); signed map (63.8, 13.1). **Vector** length 45.2, 16.1% of its response variance represented; |z| ≥ 3 in 258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.7 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | alpha-2-glycoprotein 1, zinc-binding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,966,720-99,976,042 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZA2G, ZAG |
| Gene groups (HGNC) | C1-set domain containing |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P25311](https://www.uniprot.org/uniprotkb/P25311) (Zinc-alpha-2-glycoprotein):

> Stimulates lipid degradation in adipocytes and causes the extensive fat losses associated with some advanced cancers. May bind polyunsaturated fatty acids.

**Summary**, from NCBI Gene [563](https://www.ncbi.nlm.nih.gov/gene/563):

> Predicted to enable RNA nuclease activity and transmembrane protein transporter activity. Involved in cell adhesion and detection of chemical stimulus involved in sensory perception of bitter taste. Located in obsolete extracellular space. Implicated in prostate carcinoma. Biomarker of several diseases, including gastrointestinal system cancer (multiple); kidney failure (multiple); liver cirrhosis; lung adenocarcinoma; and obesity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:910) · Entrez [563](https://www.ncbi.nlm.nih.gov/gene/563) · UniProt [P25311](https://www.uniprot.org/uniprotkb/P25311) · Ensembl [ENSG00000160862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160862)

## Data

Gene col 8388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8388); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8388]; `tensor/DDL_lfc|DDL_z.npy` [8388]; `embed/gene_vectors.npy` [8388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8388 or target_col == 8388). Every well: [[AZGP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AZGP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
