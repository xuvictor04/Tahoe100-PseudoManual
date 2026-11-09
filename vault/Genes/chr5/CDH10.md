---
symbol: "CDH10"
type: "gene"
col: 472
ensembl_id: "ENSG00000040731"
name: "cadherin 10"
location: "5p14.2-p14.1"
module: 9
arm: "+"
pooled_cpm: 12.86
n_lines_expressing: 13
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 26
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CDH10

*cadherin 10* — 5p14.2-p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.55× (z +10.9, q 8e-25, up in 1 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +7.2, q 1e-10, up in 1 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 3.00×; ⚠ position not correctable); [[Trametinib (drug)]] 5 µM in 1 line (A-427 6.43×; ⚠ cell-cycle shift, explains ~16% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.689× (z -4.5, q 0.003, down in 7 of 10 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02197]] (+0.80, fdr 7e-06), [[FGF14]] (+0.76, fdr 7e-06), [[CDH12]] (+0.73, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[ASCL1]] → it (grade C ⚠); 20 go from it, the strongest it → [[TRPC4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 3.00×; ⚠ position not correctable); [[Trametinib (drug)]] 5 µM in 1 line (A-427 6.43×; ⚠ cell-cycle shift, explains ~16% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +10.9 | 8e-25 | 1/8 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.65×** | +10.7 | 3e-24 | 1/6 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.2 | 1e-10 | 1/10 (LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +5.3 | 1e-05 | 3/10 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.1 | 3e-05 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.7 | 0.020 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.05× | +3.2 | 0.11 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.68× | +3.2 | 0.11 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 1.67× | +3.1 | 0.11 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.12 | 2/10 (J82, NCI-H2030) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.42× | +3.0 | 0.12 | 1/10 (J82) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.689×** | -4.5 | 0.003 | 7/10 (SHP-77, CHP-212, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.597×** | -4.3 | 0.006 | 4/10 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.633×** | -3.9 | 0.016 | 7/10 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.648×** | -3.7 | 0.027 | 4/10 (CHP-212, NCI-H23, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.657×** | -3.6 | 0.034 | 9/10 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -3.3 | 0.074 | 6/10 (SHP-77, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -3.3 | 0.074 | 7/10 (SHP-77, A-427, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.687×** | -3.2 | 0.081 | 8/10 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.688×** | -3.2 | 0.081 | 6/10 (SHP-77, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 120 | 0 | 18 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0219× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0771× (z -14.9) |
| [[CHP-212 (line)]] | wt | 860 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0564× (z -16.8) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -14.2) |
| [[A-427 (line)]] | wt | 57.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Trametinib (drug)]] 5 µM 6.43× (z +9.0) ⚠ cell-cycle shift, explains ~16% of this change | [[Auranofin (drug)]] 5 µM 0.108× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 3.00× (z +11.7) ⚠ position not correctable | — |
| [[NCI-H661 (line)]] | alt | 1,559 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -12.6) |
| [[A-172 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02197]] | +0.80 | +0.75 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[FGF14]] | +0.76 | +0.74 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CDH12]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 745 |
| [[SYT4]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[GRIA2]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[EPHA5]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[BMP5]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[NCAM2]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[SRRM4]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[EPHA5-AS1]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[CRISPLD1]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[KCNH5]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | C | ASCL1 activity raises CDH10's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 8.65× lower at baseline in the lines without ASCL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises CDH10's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.38× lower at baseline in the lines without TRPC4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises CDH10's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 4.21× lower at baseline in the lines without JAKMIP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises CDH10's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 10.82× lower at baseline in the lines without LINC01035 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[RAB3C]] | C | RAB3C activity raises CDH10's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 4.75× lower at baseline in the lines without RAB3C | 0.041 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises CDH10's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 5.82× lower at baseline in the lines without KCNH7 | 0.043 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | RMST activity raises CDH10's level | lines that do not express RMST (35) vs lines expressing it (15) | 3.85× lower at baseline in the lines without RMST | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises CDH10's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 9.95× lower at baseline in the lines without FUT9 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises CDH10's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 4.74× lower at baseline in the lines without CDH18 | 0.055 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises CDH10's level | lines that do not express BCHE (35) vs lines expressing it (15) | 4.86× lower at baseline in the lines without BCHE | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises CDH10's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 5.37× lower at baseline in the lines without CSMD3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises CDH10's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 6.64× lower at baseline in the lines without KCNH5 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPC4]] | C | CDH10 activity raises TRPC4's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 5.03× lower at baseline in the lines without CDH10 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[EPHA5]] | C | CDH10 activity raises EPHA5's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 6.75× lower at baseline in the lines without CDH10 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[BMP5]] | C | CDH10 activity raises BMP5's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 4.47× lower at baseline in the lines without CDH10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[EPHA5-AS1]] | C | CDH10 activity raises EPHA5-AS1's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.06× lower at baseline in the lines without CDH10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[SLITRK5]] | C | CDH10 activity raises SLITRK5's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 4.29× lower at baseline in the lines without CDH10 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[SCN3A]] | C | CDH10 activity raises SCN3A's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.25× lower at baseline in the lines without CDH10 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[CSMD3]] | C | CDH10 activity raises CSMD3's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.97× lower at baseline in the lines without CDH10 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[SCN2A]] | C | CDH10 activity raises SCN2A's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 2.57× lower at baseline in the lines without CDH10 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[ADGRL3]] | C | CDH10 activity raises ADGRL3's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 4.66× lower at baseline in the lines without CDH10 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[ASXL3]] | C | CDH10 activity raises ASXL3's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.69× lower at baseline in the lines without CDH10 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[ZFHX4]] | C | CDH10 activity raises ZFHX4's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 6.97× lower at baseline in the lines without CDH10 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[RAB3C]] | C | CDH10 activity raises RAB3C's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 2.55× lower at baseline in the lines without CDH10 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, 33.6); signed map (41.1, 35.4). **Vector** length 61.9, 27.2% of its response variance represented; |z| ≥ 3 in 370 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.53 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p14.2-p14.1 — chr5:24,487,100-24,644,978 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Type II classical cadherins |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6N8](https://www.uniprot.org/uniprotkb/Q9Y6N8) (Cadherin-10):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [1008](https://www.ncbi.nlm.nih.gov/gene/1008):

> This gene encodes a type II classical cadherin of the cadherin superfamily. Alternative splicing of this gene results in multiple transcript variants. At least one of these variants encodes a preproprotein that is proteolytically processed to generate the mature cadherin protein. These integral membrane proteins mediate calcium-dependent cell-cell adhesion and are composed of a large N-terminal extracellular domain, a single membrane-spanning domain, and a small, highly conserved C-terminal …

**Accessions** — [HGNC:1749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1749) · Entrez [1008](https://www.ncbi.nlm.nih.gov/gene/1008) · UniProt [Q9Y6N8](https://www.uniprot.org/uniprotkb/Q9Y6N8) · Ensembl [ENSG00000040731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040731)

## Data

Gene col 472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 472); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 472]; `tensor/DDL_lfc|DDL_z.npy` [472]; `embed/gene_vectors.npy` [472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 472 or target_col == 472). Every well: [[CDH10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
