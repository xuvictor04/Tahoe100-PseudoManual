---
symbol: "GASK1B"
type: "gene"
col: 8878
ensembl_id: "ENSG00000164125"
name: "golgi associated kinase 1B"
location: "4q32.1"
module: 19
arm: "+"
pooled_cpm: 13.13
n_lines_expressing: 16
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GASK1B

*golgi associated kinase 1B* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.25× (z +12.4, q 2e-32, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +8.7, q 5e-16, up in 3 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.594× (z -5.5, q 2e-05, down in 10 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.0858×, A-427 0.199×, CHP-212 0.106×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-427 0.202×, NCI-H460 0.124×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0900×; ⚠ cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.158×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.157×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GASK1B-AS1]] (+0.80, fdr 7e-06, ⚠ same locus), [[KCNK2]] (+0.73, fdr 1e-05), [[GLP2R]] (+0.70, fdr 7e-06), [[CHL1]] (+0.70, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[CRISPLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +12.4 | 2e-32 | 5/12 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.7 | 5e-24 | 1/8 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.7 | 5e-16 | 3/13 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +8.4 | 5e-15 | 3/8 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.7 | 2e-06 | 9/13 (A-172, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +5.2 | 2e-05 | 6/13 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.8 | 1e-04 | 1/13 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +4.8 | 1e-04 | 2/6 (A-172, A-427) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.6 | 2e-04 | 2/13 (KATO III, C32) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 4e-04 | 4/13 (A-172, hTERT-HPNE, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 5/14 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.9 | 0.004 | 1/10 (KATO III) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.7 | 0.009 | 0/8 | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.022 | 5/13 (A-172, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8878.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.0858×, A-427 0.199×, CHP-212 0.106×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-427 0.202×, NCI-H460 0.124×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0900×; ⚠ cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.158×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.157×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.594×** | -5.5 | 2e-05 | 10/13 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.663×** | -4.2 | 0.009 | 1/13 (NCI-H460) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.540× | -3.4 | 0.13 | 1/14 (LS 180) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.737× | -3.2 | 0.18 | 10/13 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.0 | 0 | 16 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -18.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0858× (z -13.4) |
| [[A-427 (line)]] | wt | 194 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.00× (z +9.2) ⚠ position not correctable | [[Celecoxib (drug)]] 0.5 µM 0.0459× (z -8.5) |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -10.3) |
| [[C32 (line)]] | wt | 3.79 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CHP-212 (line)]] | wt | 59.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -8.8) |
| [[LS 180 (line)]] | wt | 6.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.977 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GASK1B-AS1]] | +0.80 | +0.82 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[KCNK2]] | +0.73 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.70 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[CHL1]] | +0.70 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.70 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[LINC03000]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GREM2]] | +0.69 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[COL4A6]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CDH7]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PAX7]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[LIN7A]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[LINC01035]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GASK1B's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GASK1B-AS1]] | C | GASK1B-AS1 activity raises GASK1B's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 10.35× lower at baseline in the lines without GASK1B-AS1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |
| [[ALDH1A1]] | C | ALDH1A1 activity raises GASK1B's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 3.58× lower at baseline in the lines without ALDH1A1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises GASK1B's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 5.17× lower at baseline in the lines without MIR99AHG | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises GASK1B's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 3.00× lower at baseline in the lines without TTTY10 | 0.062 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 3, C 14. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRISPLD1]] | B | GASK1B activity raises CRISPLD1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without GASK1B | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054 |
| [[LINC02269]] | B | GASK1B activity raises LINC02269's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 1.74× lower at baseline in the lines without GASK1B | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054 |
| [[ADD3-AS1]] | B | GASK1B activity raises ADD3-AS1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 1.68× lower at baseline in the lines without GASK1B | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054 |
| [[GASK1B-AS1]] | C | GASK1B activity raises GASK1B-AS1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 4.72× lower at baseline in the lines without GASK1B | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[ALDH1A1]] | C | GASK1B activity raises ALDH1A1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 3.80× lower at baseline in the lines without GASK1B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[COL5A2]] | C | GASK1B activity raises COL5A2's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 4.85× lower at baseline in the lines without GASK1B | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[CHL1]] | C | GASK1B activity raises CHL1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without GASK1B | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[BCHE]] | C | GASK1B activity raises BCHE's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without GASK1B | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[LIN7A]] | C | GASK1B activity raises LIN7A's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without GASK1B | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[GREM2]] | C | GASK1B activity raises GREM2's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.82× lower at baseline in the lines without GASK1B | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[KCNK2]] | C | GASK1B activity raises KCNK2's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.01× lower at baseline in the lines without GASK1B | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[DCT]] | C | GASK1B activity raises DCT's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without GASK1B | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 36.3); signed map (43.5, 43.4). **Vector** length 51.3, 17.3% of its response variance represented; |z| ≥ 3 in 347 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +4.5 |
|  | [[Ixazomib (drug)]] 5 µM |  | +0.9 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.4 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +0.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | golgi associated kinase 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:158,124,474-158,173,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38155, DKFZp434L142, ENED; previously C4orf18, FAM198B |
| Gene groups (HGNC) | Golgi associated kinase family |
| Matched by | ensembl_id |

UniProt [Q6UWH4](https://www.uniprot.org/uniprotkb/Q6UWH4) carries no function annotation.

**Summary**, from NCBI Gene [51313](https://www.ncbi.nlm.nih.gov/gene/51313):

> Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25312) · Entrez [51313](https://www.ncbi.nlm.nih.gov/gene/51313) · UniProt [Q6UWH4](https://www.uniprot.org/uniprotkb/Q6UWH4) · Ensembl [ENSG00000164125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164125)

## Data

Gene col 8878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8878); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8878]; `tensor/DDL_lfc|DDL_z.npy` [8878]; `embed/gene_vectors.npy` [8878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8878 or target_col == 8878). Every well: [[GASK1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GASK1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
