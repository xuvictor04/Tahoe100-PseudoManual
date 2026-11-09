---
symbol: "UCA1"
type: "gene"
col: 13167
ensembl_id: "ENSG00000214049"
name: "urothelial cancer associated 1"
location: "19p13.12"
module: 8
arm: "+"
pooled_cpm: 16.68
n_lines_expressing: 13
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 47
direction_downstream: 84
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# UCA1

*urothelial cancer associated 1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.04× (z +13.1, q 2e-36, up in 7 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.43× (z +4.1, q 0.005, up in 7 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.601× (z -4.2, q 0.018, down in 10 of 11 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.632× (z -3.7, q 0.033, down in 6 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (COLO 205 0.0594×, MIA PaCa-2 0.168×, BT-474 0.109×, Panc 03.27 0.319×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.0499×, LS 180 0.175×, SW1417 0.286×, HT-29 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW1417 0.217×, AsPC-1 0.0452×; ⚠ cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.133×); [[Digitoxin (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.189×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01559]] (+0.73, fdr 7e-06), [[TSPAN1]] (+0.70, fdr 7e-06), [[TMEM30B]] (+0.68, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[MUC20]] → it (grade B ⚠); 84 go from it, the strongest it → [[PSD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.04×** | +13.1 | 2e-36 | 7/11 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.68×** | +12.0 | 1e-30 | 7/9 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +8.3 | 2e-14 | 4/10 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.1 | 0.005 | 1/11 (A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.005 | 7/11 (HEC-1-A, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.008 | 6/11 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.016 | 6/11 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.71× | +3.1 | 0.14 | 3/11 (SW1417, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13167.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (COLO 205 0.0594×, MIA PaCa-2 0.168×, BT-474 0.109×, Panc 03.27 0.319×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.0499×, LS 180 0.175×, SW1417 0.286×, HT-29 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW1417 0.217×, AsPC-1 0.0452×; ⚠ cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.133×); [[Digitoxin (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.189×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.601×** | -4.2 | 0.018 | 10/11 (SW1417, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.614×** | -4.0 | 0.020 | 11/11 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.632×** | -3.7 | 0.033 | 6/11 (LS 180, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.685× | -3.1 | 0.22 | 9/11 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.666× | -3.1 | 0.22 | 0/11 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.689× | -3.0 | 0.22 | 9/11 (COLO 205, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 116 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0499× (z -22.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.2) |
| [[COLO 205 (line)]] | alt | 58.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -15.6) |
| [[LS 180 (line)]] | wt | 35.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.2) |
| [[SW1417 (line)]] | alt | 82.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 4.55 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0452× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -11.6) |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.6) |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.958 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01559]] | +0.73 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TSPAN1]] | +0.70 | +0.68 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[TMEM30B]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.65 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[CATSPERB]] | +0.64 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[FXYD3]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TACSTD2]] | +0.62 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[RAB25]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[MPZL2]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SAMD12-AS1]] | +0.60 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[PRR15]] | +0.59 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[IGFL2-AS1]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 3, C 44. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | MUC20 activity raises UCA1's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 3.01× lower at baseline in the lines without MUC20 | 0.033 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[PLCH1]] | B | PLCH1 activity raises UCA1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.63× lower at baseline in the lines without PLCH1 | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[INPP4B]] | B | INPP4B activity raises UCA1's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without INPP4B | 0.090 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[PDZK1IP1]] | C | PDZK1IP1 activity raises UCA1's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 5.92× lower at baseline in the lines without PDZK1IP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises UCA1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 6.26× lower at baseline in the lines without ARHGEF38 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises UCA1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 5.20× lower at baseline in the lines without ADGRF1 | 0.004 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises UCA1's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 4.77× lower at baseline in the lines without RAB25 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises UCA1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 3.85× lower at baseline in the lines without MAL2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises UCA1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.15× lower at baseline in the lines without TMPRSS4 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises UCA1's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.81× lower at baseline in the lines without ATP10B | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises UCA1's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without BSPRY | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises UCA1's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.45× lower at baseline in the lines without TMEM30B | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 18, C 66. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD4]] | B | UCA1 activity raises PSD4's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without UCA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[MUC20]] | B | UCA1 activity raises MUC20's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without UCA1 | 0.004 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[ABHD11]] | B | UCA1 activity raises ABHD11's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 2.85× lower at baseline in the lines without UCA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[FUT2]] | B | UCA1 activity raises FUT2's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 2.15× lower at baseline in the lines without UCA1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[MYH14]] | B | UCA1 activity raises MYH14's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 4.46× lower at baseline in the lines without UCA1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[INPP4B]] | B | UCA1 activity raises INPP4B's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 3.01× lower at baseline in the lines without UCA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[STS]] | B | UCA1 activity raises STS's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 4.02× lower at baseline in the lines without UCA1 | 0.014 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[LGALS9]] | B | UCA1 activity raises LGALS9's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 2.82× lower at baseline in the lines without UCA1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[EPS8L1]] | B | UCA1 activity raises EPS8L1's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 3.31× lower at baseline in the lines without UCA1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[PROM2]] | B | UCA1 activity raises PROM2's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 2.85× lower at baseline in the lines without UCA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[BCL2L15]] | B | UCA1 activity raises BCL2L15's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 2.36× lower at baseline in the lines without UCA1 | 0.028 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[TMEM184A]] | B | UCA1 activity raises TMEM184A's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without UCA1 | 0.039 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 56.5); signed map (60.7, 7.1). **Vector** length 46.5, 16.9% of its response variance represented; |z| ≥ 3 in 314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +12.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +3.9 |
| fall | [[Radotinib (drug)]] 5 µM |  | -0.9 | -3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.8 | -3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | urothelial cancer associated 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19p13.12 — chr19:15,828,206-15,836,328 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LINC00178, CUDR, UCAT1, onco-lncRNA-36 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Reactome | 9 pathways, smallest: Degradation of CDH1; Regulation of CDH1 Function; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [652995](https://www.ncbi.nlm.nih.gov/gene/652995):

> This gene produces a long non-coding RNA that was found to be upregulated in bladder cancer and plays a regulatory role in cell proliferation. This transcript regulates several genes, including CREB (cAMP responsive element binding protein). Expression of this transcript is regulated by CCAAT/enhancer-binding protein-alpha. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:37126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37126) · Entrez [652995](https://www.ncbi.nlm.nih.gov/gene/652995) · Ensembl [ENSG00000214049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214049)

## Data

Gene col 13167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13167); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13167]; `tensor/DDL_lfc|DDL_z.npy` [13167]; `embed/gene_vectors.npy` [13167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13167 or target_col == 13167). Every well: [[UCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
