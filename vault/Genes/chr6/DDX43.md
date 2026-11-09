---
symbol: "DDX43"
type: "gene"
col: 1272
ensembl_id: "ENSG00000080007"
name: "DEAD-box helicase 43"
location: "6q13"
module: 42
arm: "+"
pooled_cpm: 10.27
n_lines_expressing: 16
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# DDX43

*DEAD-box helicase 43* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.24× (z +16.1, q 0e+00, up in 14 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.639× (z -4.1, q 0.027, down in 1 of 14 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLA2G4C]] (+0.63, fdr 1e-05), [[EIF4EBP3]] (+0.60, fdr 3e-05), [[HDAC9]] (+0.57, fdr 6e-05); moves opposite to [[GRB2]] (-0.61, fdr 4e-05), [[GDAP2]] (-0.60, fdr 2e-05), [[RNF4]] (-0.57, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[STAP2]] → it (grade B ⚠); 7 go from it, the strongest it → [[DCAF8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.24×** | +16.1 | 0e+00 | 14/14 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +12.7 | 2e-34 | 3/12 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +12.1 | 2e-31 | 4/13 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +10.6 | 5e-24 | 4/14 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +10.2 | 2e-22 | 2/13 (KATO III, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.8 | 8e-13 | 13/14 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +6.4 | 1e-08 | 12/14 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +6.2 | 5e-08 | 10/14 (SW1417, SK-MEL-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.9 | 2e-07 | 10/14 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.72×** | +5.0 | 3e-05 | 13/14 (KATO III, NCI-H2347, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.8 | 8e-05 | 3/14 (SK-MEL-2, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +4.4 | 5e-04 | 12/14 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +4.3 | 7e-04 | 11/14 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.55×** | +4.3 | 8e-04 | 1/13 (NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.2 | 8e-04 | 8/14 (SW1417, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.2 | 8e-04 | 4/14 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 9e-04 | 1/14 (HOP62) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.6 | 0.009 | 1/13 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.009 | 4/14 (SW 900, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.068 | 5/14 (SK-MEL-2, PANC-1, …) | two highest doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.61×** | +3.0 | 0.068 | 2/14 (HOP62, LOX-IMVI) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +2.9 | 0.088 | 0/14 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +2.9 | 0.088 | 0/14 | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.639×** | -4.1 | 0.027 | 1/14 (HOP62) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.669×** | -3.7 | 0.074 | 0/14 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.733× | -3.1 | 0.42 | 8/14 (PANC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 41.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +17.3) | — |
| [[NCI-H2347 (line)]] | alt | 29.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +18.6) | — |
| [[LoVo (line)]] | wt | 14.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +15.1) | — |
| [[SW 900 (line)]] | alt | 26.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +17.9) | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 74.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 9.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.917 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.968 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.989 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.859 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G4C]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | +0.60 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[HDAC9]] | +0.57 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[BTN2A2]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[KANSL1L]] | +0.56 | +0.55 / +0.43 | both halves | 4e-05 |  |
| [[MSR1]] | +0.55 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[LINC02335]] | +0.55 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[CPEB1]] | +0.55 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[CDK3]] | +0.54 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[FLCN]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[COL28A1]] | +0.54 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[NPFFR2]] | +0.54 | +0.39 / +0.53 | both halves | 6e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB2]] | -0.61 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[GDAP2]] | -0.60 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RNF4]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[NOMO2]] | -0.57 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[EFCAB14]] | -0.55 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TAF5L]] | -0.54 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[POMGNT2]] | -0.54 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TSFM]] | -0.54 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[EDEM2]] | -0.53 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[SDHAP4]] | -0.52 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[LONP2]] | -0.52 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[SEC24C]] | -0.52 | -0.49 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAP2]] | B | STAP2 activity raises DDX43's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without STAP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |
| [[GPR176]] | B | GPR176 activity raises DDX43's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 2.00× lower at baseline in the lines without GPR176 | 0.093 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[UBBP4-1]] | C | UBBP4-1 activity raises DDX43's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.65× lower at baseline in the lines without UBBP4-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCAF8]] | B | DDX43 activity lowers DCAF8's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 1.20× higher at baseline in the lines without DDX43 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17 |
| [[UBBP4-1]] | C | DDX43 activity raises UBBP4-1's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 2.88× lower at baseline in the lines without DDX43 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[LINC02506]] | C | DDX43 activity raises LINC02506's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 4.30× lower at baseline in the lines without DDX43 | 0.035 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[PCDH17]] | C | DDX43 activity raises PCDH17's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without DDX43 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[MIR4307HG]] | C | DDX43 activity raises MIR4307HG's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without DDX43 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[NPFFR2]] | C | DDX43 activity raises NPFFR2's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 2.46× lower at baseline in the lines without DDX43 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[LINC02241]] | C | DDX43 activity raises LINC02241's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without DDX43 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction -0.416). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, -8.4); signed map (40.8, 16.7). **Vector** length 35.3, 8.90% of its response variance represented; |z| ≥ 3 in 277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:73,394,828-73,417,566 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HAGE, DKFZp434H2114, CT13 |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

UniProt [Q9NXZ2](https://www.uniprot.org/uniprotkb/Q9NXZ2) carries no function annotation.

**Summary**, from NCBI Gene [55510](https://www.ncbi.nlm.nih.gov/gene/55510):

> The protein encoded by this gene is an ATP-dependent RNA helicase in the DEAD-box family and displays tumor-specific expression. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18677) · Entrez [55510](https://www.ncbi.nlm.nih.gov/gene/55510) · UniProt [Q9NXZ2](https://www.uniprot.org/uniprotkb/Q9NXZ2) · Ensembl [ENSG00000080007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080007)

## Data

Gene col 1272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1272); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1272]; `tensor/DDL_lfc|DDL_z.npy` [1272]; `embed/gene_vectors.npy` [1272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1272 or target_col == 1272). Every well: [[DDX43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
