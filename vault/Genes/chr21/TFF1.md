---
symbol: "TFF1"
type: "gene"
col: 8308
ensembl_id: "ENSG00000160182"
name: "trefoil factor 1"
location: "21q22.3"
module: 73
arm: "+"
pooled_cpm: 8.95
n_lines_expressing: 19
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 46
direction_downstream: 67
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# TFF1

*trefoil factor 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.02× (z +8.5, q 8e-15, up in 5 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vilanterol (drug)]] 0.5 µM: 2.02× (z +3.9, q 0.009, up in 9 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.430× (z -4.6, q 0.002, down in 15 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFF2]] (+0.79, fdr 7e-06, ⚠ same locus), [[KLK11]] (+0.68, fdr 7e-06), [[KLK10]] (+0.65, fdr 7e-06), [[RBP1]] (+0.65, fdr 9e-06); moves opposite to [[SH3BP4]] (-0.46, fdr 4e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[JUP]] → it (grade B ⚠); 67 go from it, the strongest it → [[ABHD17C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.02×** | +8.5 | 8e-15 | 5/10 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.02×** | +7.6 | 6e-12 | 6/12 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +5.3 | 2e-05 | 6/10 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.15×** | +4.2 | 0.004 | 6/12 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.10×** | +4.1 | 0.005 | 6/17 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.9 | 0.009 | 4/15 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **2.02×** | +3.9 | 0.009 | 9/16 (CFPAC-1, Hs 766T, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.79×** | +3.2 | 0.089 | 3/14 (HT-29, BT-474, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.93× | +3.1 | 0.12 | 4/16 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 0.05 µM |  | 1.74× | +3.0 | 0.13 | 7/17 (Panc 03.27, HOP62, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.430×** | -4.6 | 0.002 | 15/17 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.497×** | -3.8 | 0.027 | 13/17 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.602×** | -3.8 | 0.027 | 10/17 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.488×** | -3.5 | 0.062 | 11/17 (HepG2/C3A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); noisy plate (z scaled); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.537×** | -3.4 | 0.070 | 12/17 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.513×** | -3.4 | 0.070 | 8/17 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.563× | -3.1 | 0.14 | 11/17 (A549, AsPC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.327× | -3.1 | 0.14 | 11/17 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.577× | -3.0 | 0.17 | 10/17 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0131× (z -13.8) |
| [[LS 180 (line)]] | wt | 120 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 9.11 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0768× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 31.9 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0516× (z -9.6) |
| [[KATO III (line)]] | alt | 82.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -11.0) |
| [[A-172 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.864 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFF2]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | ⚠ same locus (11.3 kb, same strand: neighbours can correlate without regulation) |
| [[KLK11]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[KLK10]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RBP1]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 | **novel candidate** |
| [[CEACAM6]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SULT2B1]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[FA2H]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[FGFBP1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.58 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CA2]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[TMC7]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LCK]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MUC2]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 | STRING 622 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BP4]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 4, C 42. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | JUP activity raises TFF1's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without JUP | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[HDAC6]] | B | HDAC6 activity raises TFF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[XYLT1]] | B | XYLT1 activity raises TFF1's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without XYLT1 | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[ATP1B1]] | B | ATP1B1 activity raises TFF1's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without ATP1B1 | 0.093 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[MUC5AC]] | C | MUC5AC activity raises TFF1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 10.02× lower at baseline in the lines without MUC5AC | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises TFF1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 6.84× lower at baseline in the lines without LINC02582 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[CYP3A5]] | C | CYP3A5 activity raises TFF1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 3.99× lower at baseline in the lines without CYP3A5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[DHRS9]] | C | DHRS9 activity raises TFF1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 5.53× lower at baseline in the lines without DHRS9 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[IL33]] | C | IL33 activity raises TFF1's level | lines that do not express IL33 (35) vs lines expressing it (15) | 2.67× lower at baseline in the lines without IL33 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[PRSS3]] | C | PRSS3 activity raises TFF1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 3.11× lower at baseline in the lines without PRSS3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR; co-absent with the target |
| [[KCNK1]] | C | KCNK1 activity raises TFF1's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.99× lower at baseline in the lines without KCNK1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises TFF1's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 6.64× lower at baseline in the lines without MUC2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |

### Downstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 22, C 45. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | TFF1 activity raises ABHD17C's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.58× lower at baseline in the lines without TFF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[ATP1B1]] | B | TFF1 activity raises ATP1B1's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.75× lower at baseline in the lines without TFF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[SDCBP2]] | B | TFF1 activity raises SDCBP2's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.38× lower at baseline in the lines without TFF1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[PLEKHM1P1]] | B | TFF1 activity raises PLEKHM1P1's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 1.56× lower at baseline in the lines without TFF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[TTLL13]] | B | TFF1 activity raises TTLL13's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without TFF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[LYPD3]] | B | TFF1 activity raises LYPD3's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.43× lower at baseline in the lines without TFF1 | 0.022 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[FA2H]] | B | TFF1 activity weakens FA2H's drug response | lines that do not express TFF1 (8) vs lines expressing it (15) | the lines without TFF1 respond 4.22× as strongly (z diff -2.45); strongest at Panobinostat 5 µM: 2.21x vs 0.78x (z diff -7.2) | 0.046 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; target measured in part of the lines; artifact flags |
| [[NOSTRIN]] | B | TFF1 activity raises NOSTRIN's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.17× lower at baseline in the lines without TFF1 | 0.047 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[GPRC5D-AS1]] | B | TFF1 activity raises GPRC5D-AS1's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without TFF1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[JUP]] | B | TFF1 activity raises JUP's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.50× lower at baseline in the lines without TFF1 | 0.051 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[ARHGAP27]] | B | TFF1 activity raises ARHGAP27's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.02× lower at baseline in the lines without TFF1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[TNFRSF11A]] | B | TFF1 activity raises TNFRSF11A's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.15× lower at baseline in the lines without TFF1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.2, 53.7); signed map (68.4, 9.6). **Vector** length 55.0, 18.3% of its response variance represented; |z| ≥ 3 in 436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | trefoil factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,362,282-42,366,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D21S21, HPS2, pS2, pNR-2, HP1.A; previously BCEI |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Estrogen-dependent gene expression; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P04155](https://www.uniprot.org/uniprotkb/P04155) (Trefoil factor 1):

> Stabilizer of the mucous gel overlying the gastrointestinal mucosa that provides a physical barrier against various noxious agents. May inhibit the growth of calcium oxalate crystals in urine.

**Summary**, from NCBI Gene [7031](https://www.ncbi.nlm.nih.gov/gene/7031):

> Members of the trefoil family are characterized by having at least one copy of the trefoil motif, a 40-amino acid domain that contains three conserved disulfides. They are stable secretory proteins expressed in gastrointestinal mucosa. Their functions are not defined, but they may protect the mucosa from insults, stabilize the mucus layer, and affect healing of the epithelium. This gene, which is expressed in the gastric mucosa, has also been studied because of its expression in human tumors. …

**Accessions** — [HGNC:11755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11755) · Entrez [7031](https://www.ncbi.nlm.nih.gov/gene/7031) · UniProt [P04155](https://www.uniprot.org/uniprotkb/P04155) · Ensembl [ENSG00000160182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160182)

## Data

Gene col 8308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8308); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8308]; `tensor/DDL_lfc|DDL_z.npy` [8308]; `embed/gene_vectors.npy` [8308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8308 or target_col == 8308). Every well: [[TFF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
