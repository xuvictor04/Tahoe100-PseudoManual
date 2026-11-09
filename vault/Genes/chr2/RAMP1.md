---
symbol: "RAMP1"
type: "gene"
col: 5300
ensembl_id: "ENSG00000132329"
name: "receptor activity modifying protein 1"
location: "2q37.3"
module: 8
arm: "+"
pooled_cpm: 5.98
n_lines_expressing: 34
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 30
direction_downstream: 2
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RAMP1

*receptor activity modifying protein 1* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.27× (z +17.5, q 0e+00, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +7.6, q 4e-12, up in 11 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.438× (z -4.7, q 0.001, down in 12 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC20]] (+0.71, fdr 7e-06), [[MGAM2]] (+0.65, fdr 1e-05), [[SPATA6L]] (+0.63, fdr 1e-05); moves opposite to [[LYSMD4]] (-0.52, fdr 6e-05), [[SEMA4F]] (-0.51, fdr 2e-04), [[ABCC10]] (-0.51, fdr 8e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[SAMD12-AS1]] → it (grade B ⚠); 2 go from it, the strongest it → [[RPS4Y1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.27×** | +17.5 | 0e+00 | 2/7 (NCI-H2347, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +12.2 | 1e-31 | 7/13 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +12.1 | 3e-31 | 3/8 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +7.6 | 4e-12 | 11/28 (A-172, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +7.4 | 2e-11 | 10/25 (HOP62, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.7 | 3e-09 | 5/21 (A-172, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.4 | 4e-06 | 6/20 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +5.3 | 1e-05 | 11/28 (LS 180, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.8 | 1e-04 | 6/26 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.47×** | +4.0 | 0.004 | 7/27 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.006 | 11/28 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.016 | 7/27 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.026 | 3/24 (NCI-H2347, CFPAC-1, …) | two highest doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.026 | 10/24 (AsPC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.026 | 5/23 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.027 | 1/27 (SW480) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.040 | 3/27 (SW1417, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.089 | 2/28 (LS 180, AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -4.7 | 0.001 | 12/26 (LS 180, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.668×** | -4.1 | 0.009 | 2/28 (RKO, RPMI-7951) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 5 µM |  | **0.691×** | -4.1 | 0.009 | 6/28 (NCI-H23, LS 180, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.733× | -3.2 | 0.21 | 2/28 (LOX-IMVI, RPMI-7951) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.758× | -3.1 | 0.24 | 10/28 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.745× | -3.0 | 0.25 | 3/28 (SNU-423, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 43.0 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0626× (z -22.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -10.9) |
| [[LS 180 (line)]] | wt | 55.3 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 6.15 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Megestrol (drug)]] 0.5 µM 0.0677× (z -8.9) |
| [[HOP62 (line)]] | alt | 1.80 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC20]] | +0.71 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.65 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SAMD12-AS1]] | +0.61 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[HNF4G]] | +0.60 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[MTUS1]] | +0.60 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[PTPN22]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[LINC02889]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TM4SF4]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TOX3]] | +0.59 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[SYNPR-AS1]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYSMD4]] | -0.52 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[SEMA4F]] | -0.51 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[ABCC10]] | -0.51 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[ITGB1BP1]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[STEAP3]] | -0.49 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[SPRYD3]] | -0.49 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[ZFP28]] | -0.47 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CROCCP3]] | -0.47 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[MICAL1]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 30, C 0. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity raises RAMP1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without SAMD12-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[FAAH2]] | B | FAAH2 activity raises RAMP1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.38× lower at baseline in the lines without FAAH2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[TNFSF15]] | B | TNFSF15 activity raises RAMP1's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without TNFSF15 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[C11orf52]] | B | C11orf52 activity raises RAMP1's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without C11orf52 | 0.024 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[SYK]] | B | SYK activity raises RAMP1's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without SYK | 0.025 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[BCL2L15]] | B | BCL2L15 activity raises RAMP1's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 1.98× lower at baseline in the lines without BCL2L15 | 0.027 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises RAMP1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without SPINT1-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[SLC34A2]] | B | SLC34A2 activity raises RAMP1's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.81× lower at baseline in the lines without SLC34A2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[KCNE3]] | B | KCNE3 activity raises RAMP1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.82× lower at baseline in the lines without KCNE3 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[LINC02999]] | B | LINC02999 activity raises RAMP1's level | lines that do not express LINC02999 (43) vs lines expressing it (7) | 1.27× lower at baseline in the lines without LINC02999 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, GCG, SFTPA2 |
| [[ABO]] | B | ABO activity raises RAMP1's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without ABO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[HNF1B]] | B | HNF1B activity raises RAMP1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without HNF1B | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS4Y1]] | B | RAMP1 activity lowers RPS4Y1's level | lines that do not express RAMP1 (16) vs lines expressing it (34) | 3.13× higher at baseline in the lines without RAMP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: IGFBP6, TRHDE, SDCBP2; maybe low, not absent |
| [[SATB1]] | B | RAMP1 activity raises SATB1's level | lines that do not express RAMP1 (16) vs lines expressing it (34) | 1.96× lower at baseline in the lines without RAMP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: IGFBP6, TRHDE, SDCBP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 52.2); signed map (59.8, 1.1). **Vector** length 47.1, 7.34% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +17.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +7.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -1.2 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | receptor activity modifying protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,858,893-237,912,106 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor (G protein-coupled) activity modifying proteins |
| Reactome | 6 pathways, smallest: Calcitonin-like ligand receptors; Class B/2 (Secretin family receptors); G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [O60894](https://www.uniprot.org/uniprotkb/O60894) (Receptor activity-modifying protein 1):

> Accessory protein that interacts with and modulates the function of G protein-coupled receptors including calcitonin gene-related peptide type 1 receptor (CALCRL) and calcitonin receptor (CALCR). Required for the transport of CALCRL to the plasma membrane. Together with CALCRL, form the receptor complex for the calcitonin gene-related peptides CGRP1/CALCA and CGRP2/CALCB. Together with CALCR, form the AMYR1 receptor complex for amylin/IAPP and CGRP1/CALCA.

**Summary**, from NCBI Gene [10267](https://www.ncbi.nlm.nih.gov/gene/10267):

> The protein encoded by this gene is a member of the RAMP family of single-transmembrane-domain proteins, called receptor (calcitonin) activity modifying proteins (RAMPs). RAMPs are type I transmembrane proteins with an extracellular N terminus and a cytoplasmic C terminus. RAMPs are required to transport calcitonin-receptor-like receptor (CRLR) to the plasma membrane. CRLR, a receptor with seven transmembrane domains, can function as either a calcitonin-gene-related peptide (CGRP) receptor or …

**Accessions** — [HGNC:9843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9843) · Entrez [10267](https://www.ncbi.nlm.nih.gov/gene/10267) · UniProt [O60894](https://www.uniprot.org/uniprotkb/O60894) · Ensembl [ENSG00000132329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132329)

## Data

Gene col 5300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5300); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5300]; `tensor/DDL_lfc|DDL_z.npy` [5300]; `embed/gene_vectors.npy` [5300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5300 or target_col == 5300). Every well: [[RAMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
