---
symbol: "POU6F2"
type: "gene"
col: 2771
ensembl_id: "ENSG00000106536"
name: "POU class 6 homeobox 2"
location: "7p14.1"
module: 9
arm: "+"
pooled_cpm: 9.92
n_lines_expressing: 13
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 25
direction_downstream: 42
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# POU6F2

*POU class 6 homeobox 2* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.57× (z +20.6, q 0e+00, up in 2 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.171×, SHP-77 0.309×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0996×, SHP-77 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H1792 0.104×, SHP-77 0.209×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.106×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP25]] (+0.71, fdr 7e-06), [[PCSK1]] (+0.67, fdr 1e-05), [[GRIK1]] (+0.65, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 42 go from it, the strongest it → [[LSAMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.57×** | +20.6 | 0e+00 | 2/8 (C-33 A, NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.52×** | +12.5 | 1e-33 | 3/7 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.50×** | +12.0 | 6e-31 | 2/7 (SW480, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +10.8 | 7e-25 | 1/4 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.97×** | +10.4 | 2e-23 | 3/10 (NCI-H460, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +8.2 | 2e-14 | 2/7 (LOX-IMVI, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.05×** | +6.9 | 4e-10 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.5 | 2e-06 | 4/10 (C-33 A, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.7 | 2e-04 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.007 | 0/11 | top dose only | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.009 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.011 | 4/7 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.012 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.024 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.033 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.040 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.065 | 2/8 (SW480, HS-578T) | rises with dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2771.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.171×, SHP-77 0.309×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0996×, SHP-77 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H1792 0.104×, SHP-77 0.209×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.106×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.722× | -3.1 | 0.47 | 5/9 (NCI-H1792, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -20.7) |
| [[SHP-77 (line)]] | alt | 261 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -12.1) |
| [[A-172 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP25]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PCSK1]] | +0.67 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[GRIK1]] | +0.65 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[LRFN2]] | +0.65 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[RMST]] | +0.65 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[RUNX1T1]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PEX5L]] | +0.64 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CDH12]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SYT4]] | +0.63 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[MIR2052HG]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RIT2]] | +0.63 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[KCNB2]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 1, C 24. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POU6F2's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01287]] | C | LINC01287 activity raises POU6F2's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 4.69× lower at baseline in the lines without LINC01287 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |
| [[LINC00491]] | C | LINC00491 activity raises POU6F2's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without LINC00491 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises POU6F2's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 4.73× lower at baseline in the lines without SLC25A24P1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises POU6F2's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.11× lower at baseline in the lines without LINC01885 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[LINC02405]] | C | LINC02405 activity raises POU6F2's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without LINC02405 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360; co-absent with the target |
| [[MAGEA10]] | C | MAGEA10 activity raises POU6F2's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 5.27× lower at baseline in the lines without MAGEA10 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[LINC01611]] | C | LINC01611 activity raises POU6F2's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without LINC01611 | 0.025 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377; co-absent with the target |
| [[ST8SIA6-AS1]] | C | ST8SIA6-AS1 activity raises POU6F2's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 3.72× lower at baseline in the lines without ST8SIA6-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises POU6F2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.60× lower at baseline in the lines without PHYHIPL | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[ZNF208]] | C | ZNF208 activity raises POU6F2's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 3.43× lower at baseline in the lines without ZNF208 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises POU6F2's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.62× lower at baseline in the lines without PEX5L | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 14, C 28. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | POU6F2 activity raises LSAMP's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 3.35× lower at baseline in the lines without POU6F2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[LINC02466]] | B | POU6F2 activity raises LINC02466's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.84× lower at baseline in the lines without POU6F2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[NRG4]] | B | POU6F2 activity raises NRG4's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 3.01× lower at baseline in the lines without POU6F2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[CNTNAP2]] | B | POU6F2 activity raises CNTNAP2's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.57× lower at baseline in the lines without POU6F2 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[SLCO6A1]] | B | POU6F2 activity raises SLCO6A1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without POU6F2 | 0.041 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[GRM8]] | B | POU6F2 activity raises GRM8's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.88× lower at baseline in the lines without POU6F2 | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[GRIK2]] | B | POU6F2 activity raises GRIK2's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 3.43× lower at baseline in the lines without POU6F2 | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[PLCB1]] | B | POU6F2 activity raises PLCB1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.26× lower at baseline in the lines without POU6F2 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[COL21A1]] | B | POU6F2 activity raises COL21A1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.81× lower at baseline in the lines without POU6F2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[MYT1L]] | B | POU6F2 activity raises MYT1L's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.80× lower at baseline in the lines without POU6F2 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[VENTXP1]] | B | POU6F2 activity raises VENTXP1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without POU6F2 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[NRG4]] | B | POU6F2 activity weakens NRG4's drug response | lines that do not express POU6F2 (26) vs lines expressing it (9) | the lines without POU6F2 respond 13.83× as strongly (z diff -1.94); strongest at Homoharringtonine 5 µM: 2.82x vs 0.58x (z diff -8.5) | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.0, 37.5); signed map (46.1, 34.2). **Vector** length 35.6, 12.7% of its response variance represented; |z| ≥ 3 in 237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +20.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | POU class 6 homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:38,977,909-39,493,095 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPF-1 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [P78424](https://www.uniprot.org/uniprotkb/P78424) (POU domain, class 6, transcription factor 2):

> Probable transcription factor likely to be involved in early steps in the differentiation of amacrine and ganglion cells. Recognizes and binds to the DNA sequence 5'-ATGCAAAT-3'. Isoform 1 does not bind DNA.

**Summary**, from NCBI Gene [11281](https://www.ncbi.nlm.nih.gov/gene/11281):

> This gene encodes a member of the POU protein family characterized by the presence of a bipartite DNA binding domain, consisting of a POU-specific domain and a homeodomain, separated by a variable polylinker. The DNA binding domain may bind to DNA as monomers or as homo- and/or heterodimers, in a sequence-specific manner. The POU family members are transcriptional regulators, many of which are known to control cell type-specific differentiation pathways. This gene is a tumor suppressor involved …

**Accessions** — [HGNC:21694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21694) · Entrez [11281](https://www.ncbi.nlm.nih.gov/gene/11281) · UniProt [P78424](https://www.uniprot.org/uniprotkb/P78424) · Ensembl [ENSG00000106536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106536)

## Data

Gene col 2771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2771); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2771]; `tensor/DDL_lfc|DDL_z.npy` [2771]; `embed/gene_vectors.npy` [2771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2771 or target_col == 2771). Every well: [[POU6F2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU6F2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
