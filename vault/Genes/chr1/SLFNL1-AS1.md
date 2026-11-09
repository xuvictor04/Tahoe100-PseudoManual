---
symbol: "SLFNL1-AS1"
type: "gene"
col: 15979
ensembl_id: "ENSG00000281207"
name: "SLFNL1 antisense RNA 1"
location: "1p34.2"
module: 5
arm: "+"
pooled_cpm: 8.64
n_lines_expressing: 46
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SLFNL1-AS1

*SLFNL1 antisense RNA 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +9.9, q 4e-20, up in 21 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.303× (z -5.5, q 2e-05, down in 24 of 33 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.713× (z -4.3, q 0.006, down in 18 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTPS1]] (+0.84, fdr 7e-06, ⚠ same locus), [[HNRNPAB]] (+0.76, fdr 7e-06), [[WDR4]] (+0.73, fdr 7e-06), [[LETM1]] (+0.71, fdr 7e-06); moves opposite to [[SECISBP2L]] (-0.67, fdr 7e-06), [[USP30]] (-0.66, fdr 1e-05), [[KBTBD3]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC02728]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +9.9 | 4e-20 | 21/39 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **2.52×** | +8.0 | 3e-13 | 25/43 (HOP62, HS-578T, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.47×** | +7.8 | 9e-13 | 36/42 (A498, SW480, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.87×** | +7.7 | 3e-12 | 24/38 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.26×** | +7.1 | 2e-10 | 29/43 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **2.15×** | +6.4 | 2e-08 | 19/31 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.12×** | +6.3 | 3e-08 | 19/36 (NCI-H460, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +6.2 | 3e-08 | 19/38 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **2.07×** | +6.1 | 8e-08 | 4/12 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.9 | 2e-07 | 25/44 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.93×** | +5.7 | 7e-07 | 18/43 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.88×** | +5.4 | 2e-06 | 19/42 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.87×** | +5.2 | 8e-06 | 20/40 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +4.7 | 9e-05 | 20/42 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.72×** | +4.7 | 1e-04 | 16/42 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.001 | 9/42 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.003 | 15/42 (MIA PaCa-2, H4, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.56×** | +3.9 | 0.003 | 14/42 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.006 | 9/43 (SW480, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.56×** | +3.6 | 0.008 | 8/41 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.008 | 17/42 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.020 | 10/42 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Finasteride (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.088 | 10/42 (Hs 766T, AN3 CA, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.303×** | -5.5 | 2e-05 | 24/33 (NCI-H23, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.713×** | -4.3 | 0.006 | 18/43 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.625×** | -4.2 | 0.006 | 21/42 (A498, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.741×** | -3.8 | 0.023 | 16/43 (A498, HEC-1-A, …) | rises with dose | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.686×** | -3.3 | 0.080 | 13/42 (C32, NCI-H1573, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.676×** | -3.3 | 0.080 | 16/41 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.784× | -3.1 | 0.16 | 16/42 (RKO, HEC-1-A, …) | top dose only |  |
| [[Daidzin (drug)]] 5 µM |  | 0.700× | -3.1 | 0.16 | 6/42 (SK-MEL-2, NCI-H661, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.712× | -3.0 | 0.16 | 15/42 (NCI-H2030, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.08 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[A-427 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.134× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 2.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 5.57 | 0 | 1 | — | [[Entrectinib (drug)]] 0.5 µM 0.0361× (z -8.6) |
| [[HOP62 (line)]] | alt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +10.8) | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[KATO III (line)]] | alt | 4.49 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0613× (z -8.8) |
| [[LoVo (line)]] | wt | 8.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 4.95 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.119× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0902× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 7.96 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.155× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 5.08 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0531× (z -9.6) |
| [[SW1417 (line)]] | alt | 5.26 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0854× (z -9.0) |
| [[A-172 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[HNRNPAB]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[WDR4]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[LETM1]] | +0.71 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[PUS1]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GBX2-AS1]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 | same gene group |
| [[XXYLT1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SPOPL-DT]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[GART]] | +0.65 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[ATR]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SECISBP2L]] | -0.67 | -0.67 / -0.68 | both halves | 7e-06 |  |
| [[USP30]] | -0.66 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.65 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SNX2]] | -0.64 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[OGA]] | -0.62 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[CFAP36]] | -0.62 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[MAPK3]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[ZCRB1]] | -0.61 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[DBP]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.61 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[CCNG2]] | -0.60 | -0.62 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises SLFNL1-AS1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without TERT | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[PLEKHA6]] | B | PLEKHA6 activity lowers SLFNL1-AS1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.48× higher at baseline in the lines without PLEKHA6 | 0.019 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[STK32A]] | B | STK32A activity lowers SLFNL1-AS1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.76× higher at baseline in the lines without STK32A | 0.029 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[TOP2A]] | B | TOP2A activity lowers SLFNL1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02728]] | C | SLFNL1-AS1 activity raises LINC02728's level | lines that do not express SLFNL1-AS1 (4) vs lines expressing it (46) | 1.23× lower at baseline in the lines without SLFNL1-AS1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FAM182B, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[EEF1AKMT1]] | C | SLFNL1-AS1 activity raises EEF1AKMT1's level | lines that do not express SLFNL1-AS1 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without SLFNL1-AS1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FAM182B, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[SCLY]] | C | SLFNL1-AS1 activity raises SCLY's level | lines that do not express SLFNL1-AS1 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without SLFNL1-AS1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FAM182B, ENSG00000287400; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.8, -35.2); signed map (2.7, -50.6). **Vector** length 92.2, 19.8% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.57 to 13); *ribosome biogenesis* (control, mean cos +0.56 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.3 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | +3.8 | +6.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.9 | -4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.8 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | SLFNL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.2 — chr1:41,014,590-41,043,890 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44126) · Entrez [100507178](https://www.ncbi.nlm.nih.gov/gene/100507178) · Ensembl [ENSG00000281207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281207)

## Data

Gene col 15979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15979); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15979]; `tensor/DDL_lfc|DDL_z.npy` [15979]; `embed/gene_vectors.npy` [15979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15979 or target_col == 15979). Every well: [[SLFNL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLFNL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
