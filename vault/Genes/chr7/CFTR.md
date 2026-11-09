---
symbol: "CFTR"
type: "gene"
col: 13
ensembl_id: "ENSG00000001626"
name: "CF transmembrane conductance regulator"
location: "7q31.2"
module: 44
arm: "+"
pooled_cpm: 10.2
n_lines_expressing: 11
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 51
direction_downstream: 57
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CFTR

*CF transmembrane conductance regulator* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.01× (z +19.8, q 0e+00, up in 4 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HT-29 0.0534×, LoVo 0.102×, LS 180 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LS 180 0.0510×, LoVo 0.0799×; ⚠ cell-cycle shift, explains ~30% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LS 180 0.0645×, LoVo 0.0691×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LS 180 0.0964×, LoVo 0.146×); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (LS 180 0.234×, HT-29 0.194×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.151×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM3D]] (+0.85, fdr 7e-06), [[GPA33]] (+0.83, fdr 7e-06), [[TSPAN8]] (+0.82, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 57 go from it, the strongest it → [[SLC12A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.01×** | +19.8 | 0e+00 | 4/8 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +14.1 | 2e-42 | 4/8 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.17×** | +12.4 | 5e-33 | 1/4 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.72×** | +11.0 | 7e-26 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.04×** | +9.7 | 5e-20 | 4/9 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +8.1 | 5e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.0 | 2e-07 | 2/9 (LoVo, C32) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.1 | 3e-05 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.5 | 4e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.5 | 4e-04 | 2/9 (NCI-H1573, C32) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 4/9 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +3.9 | 0.004 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.017 | 2/9 (C32, NCI-H23) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.023 | 4/9 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HT-29 0.0534×, LoVo 0.102×, LS 180 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LS 180 0.0510×, LoVo 0.0799×; ⚠ cell-cycle shift, explains ~30% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (LS 180 0.0645×, LoVo 0.0691×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LS 180 0.0964×, LoVo 0.146×); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (LS 180 0.234×, HT-29 0.194×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.151×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 0.673× | -3.4 | 0.36 | 5/9 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 118 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0510× (z -13.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.0) |
| [[LoVo (line)]] | wt | 74.3 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0691× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.124× (z -9.2) |
| [[HT-29 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0534× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.194× (z -8.9) |
| [[C32 (line)]] | wt | 3.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 3.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +9.6) | — |
| [[A-172 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM3D]] | +0.85 | +0.85 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.82 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02331]] | +0.82 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.80 | +0.82 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.80 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[HEPH]] | +0.79 | +0.87 / +0.69 | both halves | 7e-06 | pathway: Disorders of transmembrane transporters |
| [[CDH17]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.78 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[ST6GALNAC1]] | +0.78 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[PPP1R1B]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 1, C 50. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFTR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[REG4]] | C | REG4 activity raises CFTR's level | lines that do not express REG4 (43) vs lines expressing it (7) | 8.36× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises CFTR's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 4.80× lower at baseline in the lines without MUC2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[CTSE]] | C | CTSE activity raises CFTR's level | lines that do not express CTSE (42) vs lines expressing it (8) | 6.18× lower at baseline in the lines without CTSE | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises CFTR's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 6.45× lower at baseline in the lines without MUC17 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[FGFR2]] | C | FGFR2 activity raises CFTR's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 6.55× lower at baseline in the lines without FGFR2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises CFTR's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 6.38× lower at baseline in the lines without NPSR1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises CFTR's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.96× lower at baseline in the lines without SLC6A14 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises CFTR's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.03× lower at baseline in the lines without CEACAM5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[LINC00457]] | C | LINC00457 activity raises CFTR's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.78× lower at baseline in the lines without LINC00457 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises CFTR's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.39× lower at baseline in the lines without ST6GALNAC1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises CFTR's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.72× lower at baseline in the lines without CDH17 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 11, C 46. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A2]] | B | CFTR activity raises SLC12A2's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.24× lower at baseline in the lines without CFTR | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[TMEM229B]] | B | CFTR activity raises TMEM229B's level | lines that do not express CFTR (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without CFTR | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[MUC12]] | B | CFTR activity raises MUC12's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without CFTR | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[RSPH1]] | B | CFTR activity raises RSPH1's level | lines that do not express CFTR (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without CFTR | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[ABHD11]] | B | CFTR activity raises ABHD11's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.03× lower at baseline in the lines without CFTR | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[VILL]] | B | CFTR activity raises VILL's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.23× lower at baseline in the lines without CFTR | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[MANSC1]] | B | CFTR activity raises MANSC1's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.44× lower at baseline in the lines without CFTR | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[POU5F1B]] | B | CFTR activity raises POU5F1B's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.08× lower at baseline in the lines without CFTR | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[CCSER1]] | B | CFTR activity raises CCSER1's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.72× lower at baseline in the lines without CFTR | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[LINC02580]] | B | CFTR activity raises LINC02580's level | lines that do not express CFTR (39) vs lines expressing it (11) | 1.82× lower at baseline in the lines without CFTR | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[CMTM3]] | B | CFTR activity lowers CMTM3's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.29× higher at baseline in the lines without CFTR | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[FXYD3]] | C | CFTR activity raises FXYD3's level | lines that do not express CFTR (39) vs lines expressing it (11) | 5.81× lower at baseline in the lines without CFTR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 50.6); signed map (63.9, 6.2). **Vector** length 50.6, 21.9% of its response variance represented; |z| ≥ 3 in 292 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.64 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.64 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | +1.1 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.9 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.1 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | CF transmembrane conductance regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.2 — chr7:117,287,120-117,715,971 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP7, ABC35, TNR-CFTR, dJ760C5.1, CFTR/MRP; previously CF, ABCC7 |
| Gene groups (HGNC) | Chloride channels, ATP-gated CFTR; ATP binding cassette subfamily C |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 23 pathways, smallest: RHO GTPases regulate CFTR trafficking; Chaperone Mediated Autophagy; Late endosomal microautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [P13569](https://www.uniprot.org/uniprotkb/P13569) (Cystic fibrosis transmembrane conductance regulator):

> Epithelial ion channel that plays an important role in the regulation of epithelial ion and water transport and fluid homeostasis. Mediates the transport of chloride ions across the cell membrane. Possesses an intrinsic ATPase activity and utilizes ATP to gate its channel; the passive flow of anions through the channel is gated by cycles of ATP binding and hydrolysis by the ATP-binding domains. The ion channel is also permeable to HCO(3)(-); selectivity depends on the extracellular chloride …

**Summary**, from NCBI Gene [1080](https://www.ncbi.nlm.nih.gov/gene/1080):

> This gene encodes a member of the ATP-binding cassette (ABC) transporter superfamily. The encoded protein functions as a chloride channel, making it unique among members of this protein family, and controls ion and water secretion and absorption in epithelial tissues. Channel activation is mediated by cycles of regulatory domain phosphorylation, ATP-binding by the nucleotide-binding domains, and ATP hydrolysis. Mutations in this gene cause cystic fibrosis, the most common lethal genetic …

**Accessions** — [HGNC:1884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1884) · Entrez [1080](https://www.ncbi.nlm.nih.gov/gene/1080) · UniProt [P13569](https://www.uniprot.org/uniprotkb/P13569) · Ensembl [ENSG00000001626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001626)

## Data

Gene col 13: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13]; `tensor/DDL_lfc|DDL_z.npy` [13]; `embed/gene_vectors.npy` [13]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13 or target_col == 13). Every well: [[CFTR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFTR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
