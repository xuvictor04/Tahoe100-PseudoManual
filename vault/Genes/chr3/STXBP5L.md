---
symbol: "STXBP5L"
type: "gene"
col: 6955
ensembl_id: "ENSG00000145087"
name: "syntaxin binding protein 5L"
location: "3q13.33"
module: 61
arm: "+"
pooled_cpm: 18.74
n_lines_expressing: 15
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 17
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# STXBP5L

*syntaxin binding protein 5L* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 8.20× (z +22.0, q 0e+00, up in 10 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.203×, SW480 0.251×, SW1417 0.311×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.318×, SW1417 0.266×, SW480 0.354×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (HT-29 0.0454×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (BT-474 0.0664×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COLEC12]] (+0.64, fdr 1e-05), [[KCNH7]] (+0.62, fdr 3e-05), [[PCSK2]] (+0.60, fdr 9e-06); moves opposite to [[PDCD6P1]] (-0.47, fdr 8e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[SLC1A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **8.20×** | +22.0 | 0e+00 | 10/12 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.11×** | +20.9 | 0e+00 | 10/11 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.11×** | +20.9 | 0e+00 | 8/12 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.66×** | +18.1 | 0e+00 | 10/12 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.93×** | +16.7 | 0e+00 | 10/12 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.86×** | +15.5 | 0e+00 | 11/13 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +13.5 | 2e-39 | 4/11 (NCI-H1573, J82, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +11.4 | 5e-28 | 4/10 (BT-474, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.49×** | +9.1 | 4e-18 | 4/9 (J82, NCI-H460, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.37×** | +9.0 | 1e-17 | 6/12 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +8.8 | 9e-17 | 7/11 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +7.7 | 7e-13 | 10/12 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +7.3 | 1e-11 | 10/12 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +7.2 | 2e-11 | 3/11 (BT-474, HT-29, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.8 | 2e-07 | 4/13 (J82, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.8 | 3e-07 | 4/11 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.8 | 4e-05 | 4/11 (A-172, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 4e-04 | 9/11 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6955.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.203×, SW480 0.251×, SW1417 0.311×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.318×, SW1417 0.266×, SW480 0.354×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (HT-29 0.0454×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (BT-474 0.0664×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -3.7 | 0.14 | 2/13 (SK-MEL-2, NCI-H1573) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.05 µM |  | 0.740× | -3.1 | 0.35 | 2/12 (NCI-H460, SK-MEL-2) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.811× | -3.1 | 0.35 | 0/13 | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.731× | -3.0 | 0.35 | 1/12 (AN3 CA) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.0 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 6.42× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 11.3× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 6.85 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +15.9) | — |
| [[A-172 (line)]] | wt | 12.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.68× (z +10.3) | — |
| [[J82 (line)]] | alt | 4.87 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 21.3× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 7.43 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 10.9× (z +10.3) | [[Glycyrrhizic acid (drug)]] 5 µM 0.0454× (z -12.8) |
| [[SW480 (line)]] | alt | 66.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 9.65 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +11.2) | [[Pentoxifylline (drug)]] 0.5 µM 0.0664× (z -8.6) |
| [[SHP-77 (line)]] | alt | 404 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLEC12]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[KCNH7]] | +0.62 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[PCSK2]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[SH3GL2]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PPARGC1A]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PDLIM3]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TSHZ2]] | +0.56 | +0.37 / +0.59 | both halves | 7e-05 |  |
| [[SPTB]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 | same gene group |
| [[CNTNAP2]] | +0.53 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[KCNN2]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[NCALD]] | +0.53 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ADAMTS19]] | +0.53 | +0.36 / +0.59 | both halves | 9e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6P1]] | -0.47 | -0.37 / -0.38 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STXBP5L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLSTN2]] | C | CLSTN2 activity raises STXBP5L's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without CLSTN2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises STXBP5L's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without TSHZ2 | 0.022 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[LINC01287]] | C | LINC01287 activity raises STXBP5L's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.67× lower at baseline in the lines without LINC01287 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises STXBP5L's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.75× lower at baseline in the lines without RUNX1T1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises STXBP5L's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.35× lower at baseline in the lines without KCNH7 | 0.041 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[MAGEA10]] | C | MAGEA10 activity raises STXBP5L's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 2.65× lower at baseline in the lines without MAGEA10 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[ELAVL2]] | C | ELAVL2 activity raises STXBP5L's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without ELAVL2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10; co-absent with the target |
| [[FREM2]] | C | FREM2 activity raises STXBP5L's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without FREM2 | 0.080 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; co-absent with the target |
| [[RIMBP2]] | C | RIMBP2 activity raises STXBP5L's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without RIMBP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 8, C 9. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A2]] | B | STXBP5L activity raises SLC1A2's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.09× lower at baseline in the lines without STXBP5L | 0.026 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[SORCS1]] | B | STXBP5L activity raises SORCS1's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.79× lower at baseline in the lines without STXBP5L | 0.030 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[MIR325HG]] | B | STXBP5L activity raises MIR325HG's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.63× lower at baseline in the lines without STXBP5L | 0.031 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[PDLIM3]] | B | STXBP5L activity raises PDLIM3's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.88× lower at baseline in the lines without STXBP5L | 0.046 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[AGBL4]] | B | STXBP5L activity raises AGBL4's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.28× lower at baseline in the lines without STXBP5L | 0.060 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[UNC80]] | B | STXBP5L activity raises UNC80's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.52× lower at baseline in the lines without STXBP5L | 0.071 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[OFCC1]] | B | STXBP5L activity raises OFCC1's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without STXBP5L | 0.089 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[VENTXP1]] | B | STXBP5L activity raises VENTXP1's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.79× lower at baseline in the lines without STXBP5L | 0.091 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent |
| [[RMST]] | C | STXBP5L activity raises RMST's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 1.96× lower at baseline in the lines without STXBP5L | 0.019 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[RIMBP2]] | C | STXBP5L activity raises RIMBP2's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.06× lower at baseline in the lines without STXBP5L | 0.047 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[CLSTN2]] | C | STXBP5L activity raises CLSTN2's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.56× lower at baseline in the lines without STXBP5L | 0.048 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[PWWP3B]] | C | STXBP5L activity raises PWWP3B's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.04× lower at baseline in the lines without STXBP5L | 0.056 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 33.1); signed map (33.5, 25.4). **Vector** length 38.8, 10.6% of its response variance represented; |z| ≥ 3 in 345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +13.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.7 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +20.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | +0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin binding protein 5L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:120,908,072-121,424,761 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1006, LLGL4, tomosyn-2 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes; Syntaxin binding protein 5 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2K9](https://www.uniprot.org/uniprotkb/Q9Y2K9) (Syntaxin-binding protein 5-like):

> Plays a role in vesicle trafficking and exocytosis inhibition. In pancreatic beta-cells, inhibits insulin secretion probably by interacting with and regulating STX1A and STX4, key t-SNARE proteins involved in the fusion of insulin granules to the plasma membrane. Also plays a role in neurotransmitter release by inhibiting basal acetylcholine release from axon terminals and by preventing synaptic fatigue upon repetitive stimulation (By similarity). Promotes as well axonal outgrowth.

**Summary**, from NCBI Gene [9515](https://www.ncbi.nlm.nih.gov/gene/9515):

> The protein encoded by this gene is similar to syntaxin-binding protein 5 and contains ten N-terminal WD40 repeats, four variable region WD40 repeats, and a C-terminal R-SNARE domain. Studies of the orthologous proteins in mouse and rat have shown that the encoded protein may inhibit exocytosis in neurosecretory cells, and may negatively regulate the secretion of insulin. A missense variant in this gene is likely the cause of an infantile-onset neurodegenerative disorder diagnosed in two …

**Accessions** — [HGNC:30757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30757) · Entrez [9515](https://www.ncbi.nlm.nih.gov/gene/9515) · UniProt [Q9Y2K9](https://www.uniprot.org/uniprotkb/Q9Y2K9) · Ensembl [ENSG00000145087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145087)

## Data

Gene col 6955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6955); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6955]; `tensor/DDL_lfc|DDL_z.npy` [6955]; `embed/gene_vectors.npy` [6955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6955 or target_col == 6955). Every well: [[STXBP5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
