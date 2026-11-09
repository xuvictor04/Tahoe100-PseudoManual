---
symbol: "SLC44A4"
type: "gene"
col: 12862
ensembl_id: "ENSG00000204385"
name: "solute carrier family 44 member 4"
location: "6p21.33"
module: 8
arm: "+"
pooled_cpm: 8.67
n_lines_expressing: 13
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 132
direction_downstream: 204
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC44A4

*solute carrier family 44 member 4* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.28× (z +12.5, q 7e-33, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.08× (z +6.5, q 1e-08, up in 0 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.563× (z -4.7, q 0.001, down in 0 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.82, fdr 7e-06), [[TC2N]] (+0.80, fdr 7e-06), [[TJP3]] (+0.77, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 132 arrows point to it, the strongest [[BDKRB2]] → it (grade B ⚠); 204 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.28×** | +12.5 | 7e-33 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +11.0 | 1e-25 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.28×** | +10.6 | 7e-24 | 1/9 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.08×** | +6.5 | 1e-08 | 0/11 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.92×** | +5.8 | 7e-07 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 0.001 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +4.3 | 0.001 | 1/11 (AsPC-1) | top dose only | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.97×** | +3.8 | 0.011 | 1/10 (KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +3.7 | 0.011 | 1/7 (KATO III) | rises with dose | noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.5 | 0.027 | 0/11 | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.029 | 6/11 (CFPAC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.029 | 5/11 (CFPAC-1, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.84×** | +3.4 | 0.032 | 0/11 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.46×** | +3.3 | 0.034 | 0/11 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.3 | 0.037 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.042 | 3/11 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Everolimus (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.088 | 0/11 | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.092 | 9/11 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.092 | 1/11 (HCT15) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.092 | 0/11 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.563×** | -4.7 | 0.001 | 0/11 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -3.9 | 0.022 | 10/11 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.649×** | -3.6 | 0.050 | 2/11 (COLO 205, NCI-H2347) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.649×** | -3.6 | 0.050 | 0/11 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.680×** | -3.4 | 0.064 | 6/11 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -3.4 | 0.070 | 8/11 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.674×** | -3.3 | 0.070 | 0/11 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.692×** | -3.3 | 0.070 | 7/11 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.100 | 2/11 (CFPAC-1, HT-29) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.714× | -3.0 | 0.15 | 1/11 (LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 49.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -20.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.4) |
| [[HT-29 (line)]] | alt | 99.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -19.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 44.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -13.5) |
| [[KATO III (line)]] | alt | 56.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -13.0) |
| [[LoVo (line)]] | wt | 6.43 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0740× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -9.2) |
| [[LS 180 (line)]] | wt | 45.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 37.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -12.0) |
| [[A-172 (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.670 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.80 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TJP3]] | +0.77 | +0.70 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[TRIM31]] | +0.77 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TMC4]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RNF183]] | +0.77 | +0.74 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.76 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[CLDN3]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MUC3A]] | +0.75 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[POF1B]] | +0.75 | +0.74 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*132 arrows, 132 of them with an alert ⚠; grade A 0, B 2, C 130. Shown: the 12 strongest; 120 more arrows (120 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BDKRB2]] | B | BDKRB2 activity raises SLC44A4's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without BDKRB2 | 0.050 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[EPS8L1]] | B | EPS8L1 activity raises SLC44A4's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.35× lower at baseline in the lines without EPS8L1 | 0.092 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises SLC44A4's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 7.87× lower at baseline in the lines without ST6GALNAC1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises SLC44A4's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.34× lower at baseline in the lines without CDH1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises SLC44A4's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 6.42× lower at baseline in the lines without MUC5B | 3e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises SLC44A4's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 5.95× lower at baseline in the lines without RAB25 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises SLC44A4's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 10.72× lower at baseline in the lines without AGR3 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises SLC44A4's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 5.09× lower at baseline in the lines without LINC03040 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises SLC44A4's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 7.15× lower at baseline in the lines without SLC6A14 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises SLC44A4's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 5.94× lower at baseline in the lines without ADGRF1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises SLC44A4's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 6.62× lower at baseline in the lines without DAPP1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises SLC44A4's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 6.33× lower at baseline in the lines without TMEM30B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |

### Downstream of this gene

*204 arrows, 204 of them with an alert ⚠; grade A 0, B 57, C 147. Shown: the 12 strongest; 192 more arrows (192 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | SLC44A4 activity raises FAM83E's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.33× lower at baseline in the lines without SLC44A4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[IL22RA1]] | B | SLC44A4 activity raises IL22RA1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.95× lower at baseline in the lines without SLC44A4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[FUT2]] | B | SLC44A4 activity raises FUT2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.09× lower at baseline in the lines without SLC44A4 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[MUC20]] | B | SLC44A4 activity raises MUC20's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.22× lower at baseline in the lines without SLC44A4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[ST3GAL3]] | B | SLC44A4 activity lowers ST3GAL3's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.65× higher at baseline in the lines without SLC44A4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[SDCBP2]] | B | SLC44A4 activity raises SDCBP2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 5.55× lower at baseline in the lines without SLC44A4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[ASS1]] | B | SLC44A4 activity raises ASS1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.52× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[FMO5]] | B | SLC44A4 activity raises FMO5's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.51× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[AMN]] | B | SLC44A4 activity raises AMN's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.73× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[CARD14]] | B | SLC44A4 activity raises CARD14's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without SLC44A4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[DNM2]] | B | SLC44A4 activity raises DNM2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 1.62× lower at baseline in the lines without SLC44A4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[FZD5]] | B | SLC44A4 activity raises FZD5's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.89× lower at baseline in the lines without SLC44A4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.847). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, 54.3); signed map (59.7, 5.1). **Vector** length 65.0, 32.2% of its response variance represented; |z| ≥ 3 in 315 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.58 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -4.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 44 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,863,192-31,879,046 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NG22, CTL4, FLJ14491, TPPT, DFNA72; previously C6orf29 |
| Gene groups (HGNC) | Solute carrier family 44 |
| Reactome | 8 pathways, smallest: SLC-mediated bile acid transport; SLC-mediated transport of organic anions; Synthesis of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GD3](https://www.uniprot.org/uniprotkb/Q53GD3) (Choline transporter-like protein 4):

> Choline transporter that plays a role in the choline-acetylcholine system and is required to the efferent innervation of hair cells in the olivocochlear bundle for the maintenance of physiological function of outer hair cells and the protection of hair cells from acoustic injury (By similarity). Also described as a thiamine pyrophosphate transporter in colon, may mediate the absorption of microbiota-generated thiamine pyrophosphate and contribute to host thiamine (vitamin B1) homeostasis.; …

**Summary**, from NCBI Gene [80736](https://www.ncbi.nlm.nih.gov/gene/80736):

> The protein encoded by this gene may be a sodium-dependent transmembrane transport protein involved in the uptake of choline by cholinergic neurons. Defects in this gene can cause sialidosis, a lysosomal storage disease. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:13941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13941) · Entrez [80736](https://www.ncbi.nlm.nih.gov/gene/80736) · UniProt [Q53GD3](https://www.uniprot.org/uniprotkb/Q53GD3) · Ensembl [ENSG00000204385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204385)

## Data

Gene col 12862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12862); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12862]; `tensor/DDL_lfc|DDL_z.npy` [12862]; `embed/gene_vectors.npy` [12862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12862 or target_col == 12862). Every well: [[SLC44A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC44A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
