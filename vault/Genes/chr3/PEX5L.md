---
symbol: "PEX5L"
type: "gene"
col: 3583
ensembl_id: "ENSG00000114757"
name: "peroxisomal biogenesis factor 5 like"
location: "3q26.33"
module: 9
arm: "+"
pooled_cpm: 13.62
n_lines_expressing: 18
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 33
direction_downstream: 29
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PEX5L

*peroxisomal biogenesis factor 5 like* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +15.5, q 0e+00, up in 4 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.337×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.319×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.238×); [[Peretinoin (drug)]] 0.5 µM in 1 line (H4 0.0534×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH8]] (+0.71, fdr 7e-06), [[MSR1]] (+0.68, fdr 7e-06), [[SNTG1]] (+0.68, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 29 go from it, the strongest it → [[SLC9A9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +15.5 | 0e+00 | 4/14 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +11.3 | 3e-27 | 2/11 (LOX-IMVI, H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +10.4 | 4e-23 | 6/14 (hTERT-HPNE, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +7.7 | 3e-12 | 4/11 (SK-MEL-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.5 | 7e-12 | 2/10 (H4, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.8 | 1e-09 | 4/15 (C-33 A, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +5.6 | 2e-06 | 2/15 (A-172, LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.0 | 5e-05 | 3/14 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.002 | 5/15 (C-33 A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 2/16 (A-172, LOX-IMVI) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.004 | 6/14 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.005 | 7/14 (NCI-H1573, A-172, …) | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.007 | 3/13 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.7 | 0.008 | 1/13 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.012 | 4/14 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.027 | 4/14 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.049 | 6/15 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.049 | 5/14 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.080 | 6/14 (SK-MEL-2, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3583.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.337×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.319×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.238×); [[Peretinoin (drug)]] 0.5 µM in 1 line (H4 0.0534×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.693× | -3.6 | 0.18 | 8/14 (H4, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.713× | -3.2 | 0.24 | 5/14 (SHP-77, H4, …) | top dose only |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.728× | -3.1 | 0.24 | 3/14 (HOP62, C-33 A, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.713× | -3.1 | 0.24 | 1/15 (A-172) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 417 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 159 | 2 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.57× (z +9.6) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[A-172 (line)]] | wt | 4.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.4) |
| [[H4 (line)]] | wt | 18.0 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0534× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +11.7) | — |
| [[A-427 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH8]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MSR1]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SNTG1]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CDH12]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[LINC01287]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[MAPK10]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[POU6F2]] | +0.64 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[NRXN1]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SLC9A9]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[EPHA6]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ST8SIA6-AS1]] | +0.60 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[TEX41]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 2, C 31. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PEX5L's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PLXDC2]] | B | PLXDC2 activity raises PEX5L's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without PLXDC2 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[LINC02405]] | C | LINC02405 activity raises PEX5L's level | lines that do not express LINC02405 (27) vs lines expressing it (23) | 2.64× lower at baseline in the lines without LINC02405 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000286016, ENSG00000278266, LINC02360; co-absent with the target |
| [[ST8SIA6-AS1]] | C | ST8SIA6-AS1 activity raises PEX5L's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 4.34× lower at baseline in the lines without ST8SIA6-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises PEX5L's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.79× lower at baseline in the lines without RIT2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises PEX5L's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 3.04× lower at baseline in the lines without F11-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises PEX5L's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 4.46× lower at baseline in the lines without LINC01320 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises PEX5L's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.71× lower at baseline in the lines without KCNB2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[WDR72]] | C | WDR72 activity raises PEX5L's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without WDR72 | 0.017 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[POU6F2]] | C | POU6F2 activity raises PEX5L's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 3.45× lower at baseline in the lines without POU6F2 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; co-absent with the target |
| [[CCDC152]] | C | CCDC152 activity raises PEX5L's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without CCDC152 | 0.021 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises PEX5L's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.25× lower at baseline in the lines without GTSF1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 5, C 24. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A9]] | B | PEX5L activity raises SLC9A9's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without PEX5L | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[MEIS1]] | B | PEX5L activity raises MEIS1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 3.16× lower at baseline in the lines without PEX5L | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[SNCAIP]] | B | PEX5L activity raises SNCAIP's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without PEX5L | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[OFCC1]] | B | PEX5L activity raises OFCC1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without PEX5L | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[GRIK2]] | B | PEX5L activity raises GRIK2's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without PEX5L | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[LINC02405]] | C | PEX5L activity raises LINC02405's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.81× lower at baseline in the lines without PEX5L | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[SLC4A4]] | C | PEX5L activity raises SLC4A4's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without PEX5L | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[LINC01885]] | C | PEX5L activity raises LINC01885's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 4.68× lower at baseline in the lines without PEX5L | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[KCNT2]] | C | PEX5L activity raises KCNT2's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.75× lower at baseline in the lines without PEX5L | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[LINC02882]] | C | PEX5L activity raises LINC02882's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 5.08× lower at baseline in the lines without PEX5L | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[AGTR1]] | C | PEX5L activity raises AGTR1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without PEX5L | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[MIR3171HG]] | C | PEX5L activity raises MIR3171HG's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 4.63× lower at baseline in the lines without PEX5L | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.7, 33.1); signed map (42.1, 32.8). **Vector** length 43.9, 13.0% of its response variance represented; |z| ≥ 3 in 322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +15.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | +1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -3.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:179,794,958-180,037,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEX5R, PXR2, TRIP8b |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYB4](https://www.uniprot.org/uniprotkb/Q8IYB4) (PEX5-related protein):

> Accessory subunit of hyperpolarization-activated cyclic nucleotide-gated (HCN) channels, regulating their cell-surface expression and cyclic nucleotide dependence.

**Summary**, from NCBI Gene [51555](https://www.ncbi.nlm.nih.gov/gene/51555):

> Enables peroxisome matrix targeting signal-1 binding activity and small GTPase binding activity. Predicted to be involved in protein import into peroxisome matrix, docking. Predicted to act upstream of or within maintenance of protein location and regulation of membrane potential. Located in cytosol. Part of signaling receptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30024) · Entrez [51555](https://www.ncbi.nlm.nih.gov/gene/51555) · UniProt [Q8IYB4](https://www.uniprot.org/uniprotkb/Q8IYB4) · Ensembl [ENSG00000114757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114757)

## Data

Gene col 3583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3583); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3583]; `tensor/DDL_lfc|DDL_z.npy` [3583]; `embed/gene_vectors.npy` [3583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3583 or target_col == 3583). Every well: [[PEX5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
