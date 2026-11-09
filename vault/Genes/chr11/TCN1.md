---
symbol: "TCN1"
type: "gene"
col: 5611
ensembl_id: "ENSG00000134827"
name: "transcobalamin 1"
location: "11q12.1"
module: 8
arm: "+"
pooled_cpm: 5.68
n_lines_expressing: 13
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 31
direction_downstream: 51
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TCN1

*transcobalamin 1* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.71× (z +12.0, q 1e-30, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.21× (z +7.1, q 2e-10, up in 10 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.144×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARSL]] (+0.66, fdr 1e-05), [[LRG1]] (+0.59, fdr 2e-05), [[RNF183]] (+0.57, fdr 1e-05); moves opposite to [[ZC3H8]] (-0.46, fdr 2e-04), [[FLII]] (-0.44, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 51 go from it, the strongest it → [[CARD14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.71×** | +12.0 | 1e-30 | 2/3 (BT-474, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.44×** | +10.3 | 2e-22 | 2/2 (BT-474, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.31×** | +8.5 | 3e-15 | 1/2 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +7.1 | 2e-10 | 10/11 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +7.0 | 3e-10 | 2/9 (BT-474, NCI-H460) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +5.3 | 9e-06 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.7 | 2e-04 | 5/11 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +4.4 | 7e-04 | 9/10 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.67×** | +4.3 | 0.001 | 2/3 (BT-474, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +3.8 | 0.009 | 3/10 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +3.7 | 0.010 | 0/10 | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +3.6 | 0.017 | 1/9 (BT-474) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +3.5 | 0.024 | 1/5 (BT-474) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.2 | 0.053 | 2/11 (SNU-423, Hs 766T) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.66×** | +3.2 | 0.053 | 1/11 (NCI-H460) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5611.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.163×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.613× | -3.1 | 0.94 | 8/10 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -11.4) |
| [[BT-474 (line)]] | alt | 122 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +9.7) | — |
| [[A-172 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.958 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.563 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARSL]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[LRG1]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[RNF183]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[WFDC2]] | +0.57 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[SMIM2-AS1]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PROM2]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HLA-DRB1]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[FXYD2]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC1]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[LYZ]] | +0.54 | +0.66 / +0.31 | both halves | 2e-04 |  |
| [[CARD14]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MUC5B]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H8]] | -0.46 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[FLII]] | -0.44 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 2, C 29. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TCN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLEKHS1]] | B | PLEKHS1 activity raises TCN1's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without PLEKHS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[ITIH2]] | C | ITIH2 activity raises TCN1's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.46× lower at baseline in the lines without ITIH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises TCN1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.03× lower at baseline in the lines without SMIM2-AS1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises TCN1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.62× lower at baseline in the lines without MUC5B | 0.005 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises TCN1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.58× lower at baseline in the lines without PIGR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[RNF183]] | C | RNF183 activity raises TCN1's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 1.65× lower at baseline in the lines without RNF183 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises TCN1's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 3.25× lower at baseline in the lines without SERPINA5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[SIDT1]] | C | SIDT1 activity raises TCN1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without SIDT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2; co-absent with the target |
| [[SLC34A2]] | C | SLC34A2 activity raises TCN1's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.63× lower at baseline in the lines without SLC34A2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises TCN1's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.78× lower at baseline in the lines without GABRP | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises TCN1's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without ANKRD22 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |

### Downstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 21, C 30. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD14]] | B | TCN1 activity raises CARD14's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.44× lower at baseline in the lines without TCN1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[PROM2]] | B | TCN1 activity raises PROM2's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.89× lower at baseline in the lines without TCN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[RBM47]] | B | TCN1 activity raises RBM47's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 4.51× lower at baseline in the lines without TCN1 | 0.006 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[PPP1R3B-DT]] | B | TCN1 activity raises PPP1R3B-DT's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.41× lower at baseline in the lines without TCN1 | 0.008 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[MANSC1]] | B | TCN1 activity raises MANSC1's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.42× lower at baseline in the lines without TCN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[STS]] | B | TCN1 activity raises STS's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.64× lower at baseline in the lines without TCN1 | 0.011 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[HNMT]] | B | TCN1 activity raises HNMT's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.81× lower at baseline in the lines without TCN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[PBX1]] | B | TCN1 activity raises PBX1's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without TCN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[B4GALT5]] | B | TCN1 activity raises B4GALT5's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without TCN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[ATP1B1]] | B | TCN1 activity raises ATP1B1's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.95× lower at baseline in the lines without TCN1 | 0.024 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[BCL2L15]] | B | TCN1 activity raises BCL2L15's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.13× lower at baseline in the lines without TCN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[XKRX]] | B | TCN1 activity raises XKRX's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.42× lower at baseline in the lines without TCN1 | 0.044 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, 54.8); signed map (61.2, -1.9). **Vector** length 28.1, 7.14% of its response variance represented; |z| ≥ 3 in 260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transcobalamin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,852,800-59,866,489 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TCI, TC1 |
| Reactome | 7 pathways, smallest: Uptake of dietary cobalamins into enterocytes; Transport of RCbl within the body; Cobalamin (Cbl, vitamin B12) transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P20061](https://www.uniprot.org/uniprotkb/P20061) (Transcobalamin-1):

> Binds vitamin B12 with femtomolar affinity and protects it from the acidic environment of the stomach.

**Summary**, from NCBI Gene [6947](https://www.ncbi.nlm.nih.gov/gene/6947):

> This gene encodes a member of the vitamin B12-binding protein family. This family of proteins, alternatively referred to as R binders, is expressed in various tissues and secretions. This protein is a major constituent of secondary granules in neutrophils and facilitates the transport of cobalamin into cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11652) · Entrez [6947](https://www.ncbi.nlm.nih.gov/gene/6947) · UniProt [P20061](https://www.uniprot.org/uniprotkb/P20061) · Ensembl [ENSG00000134827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134827)

## Data

Gene col 5611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5611); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5611]; `tensor/DDL_lfc|DDL_z.npy` [5611]; `embed/gene_vectors.npy` [5611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5611 or target_col == 5611). Every well: [[TCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
