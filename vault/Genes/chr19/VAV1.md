---
symbol: "VAV1"
type: "gene"
col: 6585
ensembl_id: "ENSG00000141968"
name: "vav guanine nucleotide exchange factor 1"
location: "19p13.3"
module: 191
arm: "+"
pooled_cpm: 5.09
n_lines_expressing: 27
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 20
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# VAV1

*vav guanine nucleotide exchange factor 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.50× (z +25.3, q 0e+00, up in 11 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.266×, CFPAC-1 0.397×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.0536×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.243×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC88B]] (+0.63, fdr 7e-06), [[BIK]] (+0.62, fdr 1e-05), [[COL26A1]] (+0.61, fdr 2e-05); moves opposite to [[PARN]] (-0.56, fdr 4e-05), [[MTOR]] (-0.53, fdr 4e-05), [[ADPGK]] (-0.51, fdr 2e-05).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[NCMAP]] → it (grade B ⚠); 20 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.50×** | +25.3 | 0e+00 | 11/19 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.03×** | +20.7 | 0e+00 | 13/19 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.16×** | +17.1 | 0e+00 | 17/24 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.15×** | +14.4 | 1e-44 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.34×** | +12.7 | 1e-34 | 4/9 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +12.0 | 2e-31 | 1/4 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +10.1 | 6e-22 | 9/20 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.34×** | +8.9 | 3e-17 | 16/22 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +8.4 | 3e-15 | 7/19 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +8.2 | 1e-14 | 11/24 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +6.5 | 4e-09 | 8/24 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +6.4 | 8e-09 | 8/23 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +6.1 | 5e-08 | 8/22 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.9 | 1e-07 | 1/10 (A498) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.40×** | +4.8 | 6e-05 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.2 | 8e-04 | 1/24 (A498) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.004 | 7/23 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.009 | 2/23 (CFPAC-1, A498) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.023 | 0/18 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.030 | 2/15 (CFPAC-1, A-427) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6585.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.266×, CFPAC-1 0.397×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.0536×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.243×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.750× | -3.0 | 0.74 | 3/22 (HT-29, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.44 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 45.0 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.54× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 24.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 63.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.7) |
| [[A549 (line)]] | wt | 5.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 7.95 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0536× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 2.15 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.6× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.0) | — |
| [[SW480 (line)]] | alt | 2.84 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.32× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.895 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.961 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC88B]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[BIK]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[COL26A1]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RAP1GAP]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PLB1]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[KCNN3]] | +0.60 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[SHF]] | +0.58 | +0.39 / +0.61 | both halves | 6e-05 | same gene group |
| [[SPTBN4]] | +0.58 | +0.39 / +0.63 | both halves | 5e-05 | same gene group |
| [[SULT2B1]] | +0.56 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[RASAL1]] | +0.56 | +0.30 / +0.60 | both halves | 2e-04 | same gene group |
| [[SLC15A1]] | +0.55 | +0.23 / +0.66 | both halves | 5e-04 |  |
| [[ZNF385C]] | +0.55 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARN]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MTOR]] | -0.53 | -0.40 / -0.50 | both halves | 4e-05 | pathway: Co-stimulation by CD28 |
| [[ADPGK]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ATR]] | -0.49 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[TIMM23B-AGAP6]] | -0.48 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[EHMT1]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCMAP]] | B | NCMAP activity raises VAV1's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without NCMAP | 0.029 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[BSPRY]] | B | BSPRY activity raises VAV1's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.94× lower at baseline in the lines without BSPRY | 0.047 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[CHST9]] | B | CHST9 activity raises VAV1's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.62× lower at baseline in the lines without CHST9 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[SUSD4]] | B | SUSD4 activity lowers VAV1's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.99× higher at baseline in the lines without SUSD4 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent |
| [[TJP3]] | B | TJP3 activity raises VAV1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without TJP3 | 0.093 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[PTAFR]] | C | PTAFR activity raises VAV1's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without PTAFR | 0.031 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent; co-absent with the target |
| [[GOLT1A]] | C | GOLT1A activity raises VAV1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without GOLT1A | 0.036 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent; co-absent with the target |
| [[SULT2B1]] | C | SULT2B1 activity raises VAV1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without SULT2B1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent; co-absent with the target |
| [[TSPAN2]] | C | TSPAN2 activity raises VAV1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without TSPAN2 | 0.041 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises VAV1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 1.94× lower at baseline in the lines without ATP2C2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises VAV1's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 1.94× lower at baseline in the lines without SLC5A1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |
| [[RASAL1]] | C | RASAL1 activity raises VAV1's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.81× lower at baseline in the lines without RASAL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | VAV1 activity raises LMTK3's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without VAV1 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[STYK1]] | B | VAV1 activity raises STYK1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without VAV1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[ZNF385C]] | B | VAV1 activity raises ZNF385C's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.47× lower at baseline in the lines without VAV1 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[CCDC148]] | B | VAV1 activity raises CCDC148's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without VAV1 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[PPL]] | B | VAV1 activity raises PPL's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without VAV1 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[SEMA4D]] | B | VAV1 activity raises SEMA4D's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without VAV1 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[CEACAM22P-1]] | B | VAV1 activity raises CEACAM22P-1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without VAV1 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[TJP3]] | B | VAV1 activity raises TJP3's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without VAV1 | 0.068 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[LPAR5]] | B | VAV1 activity raises LPAR5's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without VAV1 | 0.072 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[PLB1]] | B | VAV1 activity raises PLB1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without VAV1 | 0.073 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[JUP]] | B | VAV1 activity raises JUP's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without VAV1 | 0.080 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[YWHAEP7-1]] | B | VAV1 activity raises YWHAEP7-1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.40× lower at baseline in the lines without VAV1 | 0.080 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.0, 34.6); signed map (25.8, 17.5). **Vector** length 40.1, 7.01% of its response variance represented; |z| ≥ 3 in 555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +20.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +8.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | vav guanine nucleotide exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,772,708-6,857,366 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously VAV |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH2 domain containing; SH3 domain containing |
| Reactome | 58 pathways, smallest: CD28 dependent Vav1 pathway; Rituximab:MS4A1 (rituximab:CD20) targets B cells for antibody-dependent cellular cytotoxicity by NK cells; Erythropoietin activates RAS |
| Matched by | ensembl_id |

**Function**, from UniProt [P15498](https://www.uniprot.org/uniprotkb/P15498) (Proto-oncogene vav):

> Couples tyrosine kinase signals with the activation of the Rho/Rac GTPases, thus leading to cell differentiation and/or proliferation.

**Summary**, from NCBI Gene [7409](https://www.ncbi.nlm.nih.gov/gene/7409):

> This gene is a member of the VAV gene family. The VAV proteins are guanine nucleotide exchange factors (GEFs) for Rho family GTPases that activate pathways leading to actin cytoskeletal rearrangements and transcriptional alterations. The encoded protein is important in hematopoiesis, playing a role in T-cell and B-cell development and activation. The encoded protein has been identified as the specific binding partner of Nef proteins from HIV-1. Coexpression and binding of these partners …

**Accessions** — [HGNC:12657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12657) · Entrez [7409](https://www.ncbi.nlm.nih.gov/gene/7409) · UniProt [P15498](https://www.uniprot.org/uniprotkb/P15498) · Ensembl [ENSG00000141968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141968)

## Data

Gene col 6585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6585); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6585]; `tensor/DDL_lfc|DDL_z.npy` [6585]; `embed/gene_vectors.npy` [6585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6585 or target_col == 6585). Every well: [[VAV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
