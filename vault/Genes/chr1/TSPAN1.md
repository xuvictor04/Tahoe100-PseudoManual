---
symbol: "TSPAN1"
type: "gene"
col: 3911
ensembl_id: "ENSG00000117472"
name: "tetraspanin 1"
location: "1p34.1"
module: 44
arm: "+"
pooled_cpm: 10.06
n_lines_expressing: 24
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 99
direction_downstream: 109
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# TSPAN1

*tetraspanin 1* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.31× (z +15.2, q 0e+00, up in 13 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +9.0, q 3e-17, up in 5 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 4.55×, MIA PaCa-2 7.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 4.78×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.683× (z -5.6, q 1e-05, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXYD3]] (+0.81, fdr 7e-06), [[CEACAM5]] (+0.81, fdr 7e-06), [[CEACAM6]] (+0.75, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 99 arrows point to it, the strongest [[SYTL5]] → it (grade B ⚠); 109 go from it, the strongest it → [[TMEM184A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3911.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 4.55×, MIA PaCa-2 7.11×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 4.78×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.31×** | +15.2 | 0e+00 | 13/16 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.52×** | +15.1 | 0e+00 | 9/11 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.48×** | +12.0 | 1e-30 | 10/13 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.0 | 3e-17 | 5/20 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.9 | 1e-04 | 4/18 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.3 | 0.002 | 7/18 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.009 | 3/20 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.37× | +3.1 | 0.11 | 6/21 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.35× | +3.1 | 0.11 | 4/20 (KATO III, NCI-H1573, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.69× | +3.1 | 0.11 | 1/20 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.683×** | -5.6 | 1e-05 | 16/21 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.595×** | -5.4 | 2e-05 | 18/21 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.606×** | -5.2 | 4e-05 | 16/20 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -4.7 | 4e-04 | 14/21 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.019 | 13/21 (LoVo, KATO III, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.702×** | -3.7 | 0.025 | 5/21 (HepG2/C3A, BT-474, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.705×** | -3.3 | 0.066 | 2/21 (BT-474, LS 180) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.708×** | -3.3 | 0.069 | 4/21 (SW1417, HepG2/C3A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.737× | -3.1 | 0.10 | 11/21 (SW48, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 97.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -25.1) |
| [[LS 180 (line)]] | wt | 42.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.55× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -20.3) |
| [[CFPAC-1 (line)]] | alt | 58.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.9) |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.3) |
| [[LoVo (line)]] | wt | 6.31 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0795× (z -11.3) |
| [[BT-474 (line)]] | alt | 45.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +9.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 5.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.11× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXYD3]] | +0.81 | +0.77 / +0.76 | both halves | 7e-06 | STRING 420 |
| [[CEACAM5]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM6]] | +0.75 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.75 | +0.82 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[TSPAN8]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 | same gene group |
| [[PROM2]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TM4SF4]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 | STRING 426 |
| [[UCA1]] | +0.70 | +0.68 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LINC01559]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MUC5B]] | +0.69 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[CLDN3]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[TMEM30B]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*99 arrows, 99 of them with an alert ⚠; grade A 0, B 5, C 94. Shown: the 12 strongest; 87 more arrows (87 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL5]] | B | SYTL5 activity raises TSPAN1's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without SYTL5 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[MANSC1]] | B | MANSC1 activity raises TSPAN1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without MANSC1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[LINC02985]] | B | LINC02985 activity lowers TSPAN1's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 3.76× higher at baseline in the lines without LINC02985 | 0.065 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |
| [[HDAC6]] | B | HDAC6 activity raises TSPAN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FUT2]] | B | FUT2 activity raises TSPAN1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without FUT2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[DPP4]] | C | DPP4 activity raises TSPAN1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 3.29× lower at baseline in the lines without DPP4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises TSPAN1's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 5.97× lower at baseline in the lines without CEACAM6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises TSPAN1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.98× lower at baseline in the lines without TMPRSS4 | 8e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises TSPAN1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 4.81× lower at baseline in the lines without SLC6A14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises TSPAN1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.55× lower at baseline in the lines without MPZL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises TSPAN1's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without P2RY2 | 0.001 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises TSPAN1's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 4.36× lower at baseline in the lines without RAB25 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |

### Downstream of this gene

*109 arrows, 109 of them with an alert ⚠; grade A 0, B 26, C 83. Shown: the 12 strongest; 97 more arrows (97 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM184A]] | B | TSPAN1 activity raises TMEM184A's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.73× lower at baseline in the lines without TSPAN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[TNFRSF21]] | B | TSPAN1 activity raises TNFRSF21's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.90× lower at baseline in the lines without TSPAN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[ABHD11]] | B | TSPAN1 activity raises ABHD11's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.63× lower at baseline in the lines without TSPAN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[MAPK13]] | B | TSPAN1 activity raises MAPK13's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.10× lower at baseline in the lines without TSPAN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[ELMO3]] | B | TSPAN1 activity raises ELMO3's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without TSPAN1 | 0.029 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[RGS6]] | B | TSPAN1 activity raises RGS6's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.74× lower at baseline in the lines without TSPAN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[FUT2]] | B | TSPAN1 activity raises FUT2's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without TSPAN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| cells under [[Trifluridine (drug)]] 5 µM | B | TSPAN1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express TSPAN1 (26) vs lines expressing it (22) | the lines without TSPAN1: 0.87× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[SYDE1]] | B | TSPAN1 activity lowers SYDE1's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.23× higher at baseline in the lines without TSPAN1 | 0.035 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | B | TSPAN1 activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express TSPAN1 (26) vs lines expressing it (22) | the lines without TSPAN1: 0.78× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | TSPAN1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TSPAN1 (26) vs lines expressing it (22) | the lines without TSPAN1: 1.18× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[EPB41L1]] | B | TSPAN1 activity raises EPB41L1's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without TSPAN1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 56.4); signed map (60.4, 7.2). **Vector** length 62.4, 19.0% of its response variance represented; |z| ≥ 3 in 483 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.53 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.53 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:46,175,073-46,185,962 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSPAN-1, NET-1 |
| Gene groups (HGNC) | Tetraspanin family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [O60635](https://www.uniprot.org/uniprotkb/O60635) (Tetraspanin-1):

> Structural component of specialized membrane microdomains known as tetraspanin-enriched microdomains (TERMs), which act as platforms for receptor clustering and signaling. Participates thereby in diverse biological functions such as cell signal transduction, adhesion, migration and protein trafficking. Regulates neuronal differentiation in response to NGF by facilitating NGF-mediated activation of NTRK1/TRKA receptor tyrosine kinase and subsequent downstream signaling pathways (By similarity). …

**Summary**, from NCBI Gene [10103](https://www.ncbi.nlm.nih.gov/gene/10103):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20657) · Entrez [10103](https://www.ncbi.nlm.nih.gov/gene/10103) · UniProt [O60635](https://www.uniprot.org/uniprotkb/O60635) · Ensembl [ENSG00000117472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117472)

## Data

Gene col 3911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3911); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3911]; `tensor/DDL_lfc|DDL_z.npy` [3911]; `embed/gene_vectors.npy` [3911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3911 or target_col == 3911). Every well: [[TSPAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
