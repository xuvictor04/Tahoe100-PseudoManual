---
symbol: "CDH19"
type: "gene"
col: 998
ensembl_id: "ENSG00000071991"
name: "cadherin 19"
location: "18q22.1"
module: 19
arm: "+"
pooled_cpm: 17.43
n_lines_expressing: 10
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 23
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CDH19

*cadherin 19* — 18q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.94× (z +10.7, q 9e-24, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.63× (z +3.5, q 0.055, up in 4 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.445× (z -5.4, q 3e-05, down in 7 of 8 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.463× (z -5.2, q 7e-05, down in 6 of 8 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL19A1]] (+0.69, fdr 7e-06), [[TBXT]] (+0.68, fdr 1e-05, ⚠ TBXT in the vector space only through flagged drug-doses), [[CHL1]] (+0.67, fdr 1e-05), [[LINC03000]] (+0.66, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 6 go from it, the strongest it → [[SLC16A4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.94×** | +10.7 | 9e-24 | 2/7 (A-427, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +7.7 | 5e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +6.3 | 4e-08 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.3 | 0.002 | 2/8 (A-427, C-33 A) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.055 | 4/8 (NCI-H460, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.066 | 4/8 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.066 | 3/8 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.06×** | +3.3 | 0.072 | 3/8 (A549, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.03×** | +3.2 | 0.072 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.072 | 0/8 | inconsistent across doses | position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.61×** | +3.2 | 0.072 | 0/8 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +3.1 | 0.072 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.60×** | +3.1 | 0.072 | 2/8 (SK-MEL-2, NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 998.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.445×** | -5.4 | 3e-05 | 7/8 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.463×** | -5.2 | 7e-05 | 6/8 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.513×** | -4.5 | 0.002 | 6/8 (SK-MEL-2, C32, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.568×** | -3.8 | 0.021 | 2/8 (NCI-H460, A549) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.574×** | -3.7 | 0.023 | 6/8 (SK-MEL-2, C32, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.601×** | -3.4 | 0.061 | 5/8 (SK-MEL-2, C32, …) | rises with dose | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.585×** | -3.3 | 0.074 | 0/8 | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.634× | -3.1 | 0.16 | 6/8 (NCI-H460, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.638× | -3.0 | 0.16 | 5/8 (NCI-H460, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 200 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0947× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 195 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -18.3) |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.6) |
| [[A-427 (line)]] | wt | 27.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.265× (z -9.2) |
| [[A-172 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL19A1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TBXT]] ⚠ | +0.68 | +0.57 / +0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHL1]] | +0.67 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LINC00461]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ADGRD1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GREM2]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GSG1L2]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 | **novel candidate** |
| [[CTNND2]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[DPP10]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SCARA5]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 1, C 22. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CDH19's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CHL1]] | C | CHL1 activity raises CDH19's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 8.56× lower at baseline in the lines without CHL1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises CDH19's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without TTTY10 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises CDH19's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 5.17× lower at baseline in the lines without GSG1L2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[UTY]] | C | UTY activity raises CDH19's level | lines that do not express UTY (31) vs lines expressing it (19) | 2.71× lower at baseline in the lines without UTY | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises CDH19's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 3.24× lower at baseline in the lines without LEF1-AS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises CDH19's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.56× lower at baseline in the lines without GTF2I-AS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises CDH19's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.77× lower at baseline in the lines without LINC03000 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises CDH19's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without LIN7A | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[ELOVL2]] | C | ELOVL2 activity raises CDH19's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 3.03× lower at baseline in the lines without ELOVL2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises CDH19's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without NCKAP5-AS2 | 0.040 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises CDH19's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without C10orf90 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A4]] | B | CDH19 activity raises SLC16A4's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 1.81× lower at baseline in the lines without CDH19 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425 |
| [[P3H2-AS1]] | C | CDH19 activity raises P3H2-AS1's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 2.09× lower at baseline in the lines without CDH19 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[HORMAD1]] | C | CDH19 activity raises HORMAD1's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 2.94× lower at baseline in the lines without CDH19 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[COL4A3]] | C | CDH19 activity raises COL4A3's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 3.84× lower at baseline in the lines without CDH19 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[TTTY10]] | C | CDH19 activity raises TTTY10's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without CDH19 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[UTY]] | C | CDH19 activity raises UTY's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 3.17× lower at baseline in the lines without CDH19 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, 36.1); signed map (43.2, 43.0). **Vector** length 49.6, 23.2% of its response variance represented; |z| ≥ 3 in 274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -5.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.1 — chr18:66,501,083-66,604,138 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDH7 |
| Gene groups (HGNC) | Type II classical cadherins |
| Reactome | 7 pathways, smallest: Regulation of CDH19 Expression and Function; Regulation of Expression and Function of Type II Classical Cadherins; Regulation of Homotypic Cell-Cell Adhesion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H159](https://www.uniprot.org/uniprotkb/Q9H159) (Cadherin-19):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [28513](https://www.ncbi.nlm.nih.gov/gene/28513):

> This gene is one of three related type II cadherin genes situated in a cluster on chromosome 18. The encoded protein is a calcium dependent cell-cell adhesion glycoprotein containing five extracellular cadherin repeats. Loss of cadherins may be associated with cancer formation. Alternative splicing results in multiple transcript variants for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:1758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1758) · Entrez [28513](https://www.ncbi.nlm.nih.gov/gene/28513) · UniProt [Q9H159](https://www.uniprot.org/uniprotkb/Q9H159) · Ensembl [ENSG00000071991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071991)

## Data

Gene col 998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 998); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 998]; `tensor/DDL_lfc|DDL_z.npy` [998]; `embed/gene_vectors.npy` [998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 998 or target_col == 998). Every well: [[CDH19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
