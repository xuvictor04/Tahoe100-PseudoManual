---
symbol: "NKAIN1"
type: "gene"
col: 1402
ensembl_id: "ENSG00000084628"
name: "sodium/potassium transporting ATPase interacting 1"
location: "1p35.2"
module: 102
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 46
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 6
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# NKAIN1

*sodium/potassium transporting ATPase interacting 1* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.12× (z +15.8, q 0e+00, up in 18 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0752×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.151×); [[Orlistat (drug)]] 0.05 µM in 1 line (A-427 0.0902×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNQ4]] (+0.68, fdr 1e-05), [[DLGAP2]] (+0.67, fdr 1e-05), [[GPM6B]] (+0.66, fdr 7e-06).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[RET]] → it (grade B ⚠); 6 go from it, the strongest it → [[CELF5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +15.8 | 0e+00 | 18/23 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.59×** | +14.4 | 3e-44 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.83×** | +13.1 | 4e-37 | 19/32 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +10.1 | 6e-22 | 13/28 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +10.0 | 1e-21 | 4/9 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +9.2 | 3e-18 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +9.1 | 1e-17 | 18/41 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +9.0 | 2e-17 | 5/12 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.5 | 3e-06 | 16/34 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.55×** | +4.3 | 0.001 | 10/41 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +4.0 | 0.003 | 8/40 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.9 | 0.004 | 4/20 (NCI-H2347, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 5/26 (NCI-H460, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.004 | 1/16 (NCI-H1792) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.005 | 4/25 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.009 | 1/36 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.023 | 2/32 (HEC-1-A, A-427) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.035 | 1/35 (AN3 CA) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.053 | 3/17 (NCI-H23, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.061 | 1/29 (PANC-1) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.086 | 3/30 (NCI-H1792, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1402.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0752×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C-33 A 0.151×); [[Orlistat (drug)]] 0.05 µM in 1 line (A-427 0.0902×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.794× | -3.2 | 0.66 | 4/36 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.733× | -3.0 | 0.66 | 10/38 (C-33 A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 18.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0752× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -8.7) |
| [[A-427 (line)]] | wt | 5.44 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0902× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +9.0) | — |
| [[A-172 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.592 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.653 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.890 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.800 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNQ4]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[GPM6B]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[GNAL]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[KCND3]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CDH23]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | STRING 824 |
| [[RASGEF1C]] | +0.62 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[GSG1L]] | +0.62 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[FER1L6]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[GBX1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[MSI1]] | +0.60 | +0.46 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RET]] | B | RET activity raises NKAIN1's level | lines that do not express RET (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without RET | 0.018 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[CHD5]] | B | CHD5 activity raises NKAIN1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without CHD5 | 0.020 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[EBF4]] | B | EBF4 activity raises NKAIN1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without EBF4 | 0.029 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[ELFN1]] | B | ELFN1 activity raises NKAIN1's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.63× lower at baseline in the lines without ELFN1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[DUSP5-DT]] | B | DUSP5-DT activity lowers NKAIN1's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.46× higher at baseline in the lines without DUSP5-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[FER1L6]] | B | FER1L6 activity lowers NKAIN1's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without FER1L6 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[GNG4]] | B | GNG4 activity raises NKAIN1's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 1.40× lower at baseline in the lines without GNG4 | 0.058 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[WT1-AS]] | B | WT1-AS activity raises NKAIN1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.32× lower at baseline in the lines without WT1-AS | 0.064 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[LINC02643]] | B | LINC02643 activity raises NKAIN1's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 2.04× lower at baseline in the lines without LINC02643 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530 |
| [[EMID1]] | B | EMID1 activity raises NKAIN1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.62× lower at baseline in the lines without EMID1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[CBFA2T3]] | B | CBFA2T3 activity raises NKAIN1's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without CBFA2T3 | 0.087 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[BRSK2]] | B | BRSK2 activity raises NKAIN1's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without BRSK2 | 0.091 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELF5]] | C | NKAIN1 activity raises CELF5's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without NKAIN1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |
| [[WNT3]] | C | NKAIN1 activity raises WNT3's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without NKAIN1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; co-absent with the target |
| [[EMID1]] | C | NKAIN1 activity raises EMID1's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without NKAIN1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[OSBP2]] | C | NKAIN1 activity raises OSBP2's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without NKAIN1 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[TRAF3]] | C | NKAIN1 activity raises TRAF3's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without NKAIN1 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[RHBDL3]] | C | NKAIN1 activity raises RHBDL3's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without NKAIN1 | 0.0999 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.4, 35.1); signed map (28.0, 22.4). **Vector** length 45.4, 5.61% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Transmission across Chemical Synapses* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +14.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | sodium/potassium transporting ATPase interacting 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,179,745-31,239,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12650; previously FAM77C |
| Gene groups (HGNC) | Na+/K+ transporting ATPase interacting |
| Matched by | ensembl_id |

UniProt [Q4KMZ8](https://www.uniprot.org/uniprotkb/Q4KMZ8) carries no function annotation.

**Summary**, from NCBI Gene [79570](https://www.ncbi.nlm.nih.gov/gene/79570):

> NKAIN1 is a member of a family of mammalian proteins with similarity to Drosophila Nkain and interacts with the beta subunit of Na,K-ATPase (ATP1B1; MIM 182330) (Gorokhova et al., 2007 [PubMed 17606467]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:25743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25743) · Entrez [79570](https://www.ncbi.nlm.nih.gov/gene/79570) · UniProt [Q4KMZ8](https://www.uniprot.org/uniprotkb/Q4KMZ8) · Ensembl [ENSG00000084628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084628)

## Data

Gene col 1402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1402); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1402]; `tensor/DDL_lfc|DDL_z.npy` [1402]; `embed/gene_vectors.npy` [1402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1402 or target_col == 1402). Every well: [[NKAIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKAIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
