---
symbol: "CTNND2"
type: "gene"
col: 9863
ensembl_id: "ENSG00000169862"
name: "catenin delta 2"
location: "5p15.2"
module: 19
arm: "+"
pooled_cpm: 24.23
n_lines_expressing: 10
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 35
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CTNND2

*catenin delta 2* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.80× (z +15.0, q 0e+00, up in 7 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (H4 0.0268×, NCI-H460 0.105×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0741×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0757×; ⚠ cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0786×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.110×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.118×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03000]] (+0.87, fdr 7e-06), [[SCARA5]] (+0.87, fdr 7e-06), [[ADGRD1]] (+0.83, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 35 go from it, the strongest it → [[LINC00922]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.80×** | +15.0 | 0e+00 | 7/8 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.73×** | +12.3 | 2e-32 | 3/6 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.34×** | +9.5 | 3e-19 | 5/8 (J82, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +9.3 | 2e-18 | 3/5 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +6.8 | 1e-09 | 1/5 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.79×** | +6.5 | 6e-09 | 4/7 (BT-474, SW 900, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.98×** | +5.4 | 5e-06 | 4/8 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +5.3 | 9e-06 | 5/7 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +4.8 | 1e-04 | 1/6 (J82) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +4.0 | 0.003 | 4/7 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.013 | 4/7 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.027 | 3/6 (BT-474, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.1 | 0.086 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.086 | 3/6 (SW 900, H4, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (H4 0.0268×, NCI-H460 0.105×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0741×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0757×; ⚠ cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0786×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.110×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.118×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 367 | 0 | 20 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0741× (z -18.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0786× (z -12.9) |
| [[J82 (line)]] | alt | 39.1 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 85.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.29× (z +8.5) | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0268× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 7.46 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.09× (z +8.8) | — |
| [[A-172 (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03000]] | +0.87 | +0.83 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.83 | +0.75 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.82 | +0.76 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.82 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GREM2]] | +0.80 | +0.77 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.80 | +0.72 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PAX7]] | +0.80 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[NCKAP5-AS2]] | +0.79 | +0.78 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[SPDYE10]] | +0.77 | +0.73 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CTNND2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises CTNND2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 3.04× lower at baseline in the lines without ZNF736P9Y | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises CTNND2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.07× lower at baseline in the lines without DPP10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises CTNND2's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 5.14× lower at baseline in the lines without GSG1L2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises CTNND2's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.66× lower at baseline in the lines without GTF2I-AS1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises CTNND2's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.99× lower at baseline in the lines without MARCOL, SPINK13 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[LINC03000]] | C | LINC03000 activity raises CTNND2's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 4.05× lower at baseline in the lines without LINC03000 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises CTNND2's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 2.48× lower at baseline in the lines without FENDRR | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises CTNND2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.03× lower at baseline in the lines without SCARA5 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises CTNND2's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 3.82× lower at baseline in the lines without SLC15A5 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises CTNND2's level | lines that do not express TBXT (47) vs lines expressing it (3) | 11.34× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[SERPINB11]] | C | SERPINB11 activity raises CTNND2's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 4.29× lower at baseline in the lines without SERPINB11 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 8, C 27. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00922]] | B | CTNND2 activity raises LINC00922's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.62× lower at baseline in the lines without CTNND2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[PLAC4]] | B | CTNND2 activity raises PLAC4's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.23× lower at baseline in the lines without CTNND2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[FSTL4]] | B | CTNND2 activity raises FSTL4's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.51× lower at baseline in the lines without CTNND2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[SLCO1C1]] | B | CTNND2 activity raises SLCO1C1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.76× lower at baseline in the lines without CTNND2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[PART1]] | B | CTNND2 activity raises PART1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.68× lower at baseline in the lines without CTNND2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[STEAP1B]] | B | CTNND2 activity raises STEAP1B's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.65× lower at baseline in the lines without CTNND2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[MN1]] | B | CTNND2 activity raises MN1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.47× lower at baseline in the lines without CTNND2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[SPDYE10]] | B | CTNND2 activity raises SPDYE10's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.59× lower at baseline in the lines without CTNND2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[CDH11]] | C | CTNND2 activity raises CDH11's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 5.45× lower at baseline in the lines without CTNND2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[FENDRR]] | C | CTNND2 activity raises FENDRR's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.05× lower at baseline in the lines without CTNND2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[LINC03000]] | C | CTNND2 activity raises LINC03000's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 3.33× lower at baseline in the lines without CTNND2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[TBXT]] | C | CTNND2 activity raises TBXT's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 3.01× lower at baseline in the lines without CTNND2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.832). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 36.2); signed map (42.8, 44.2). **Vector** length 45.2, 24.4% of its response variance represented; |z| ≥ 3 in 169 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | catenin delta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,971,836-11,904,446 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NPRAP, GT24 |
| Gene groups (HGNC) | Armadillo repeat containing; p120 catenin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQB3](https://www.uniprot.org/uniprotkb/Q9UQB3) (Catenin delta-2):

> Has a critical role in neuronal development, particularly in the formation and/or maintenance of dendritic spines and synapses. Involved in the regulation of Wnt signaling. It probably acts on beta-catenin turnover, facilitating beta-catenin interaction with GSK3B, phosphorylation, ubiquitination and degradation (By similarity). Functions as a transcriptional activator when bound to ZBTB33 (By similarity). May be involved in neuronal cell adhesion and tissue morphogenesis and integrity by …

**Summary**, from NCBI Gene [1501](https://www.ncbi.nlm.nih.gov/gene/1501):

> This gene encodes an adhesive junction associated protein of the armadillo/beta-catenin superfamily and is implicated in brain and eye development and cancer formation. The protein encoded by this gene promotes the disruption of E-cadherin based adherens junction to favor cell spreading upon stimulation by hepatocyte growth factor. This gene is overexpressed in prostate adenocarcinomas and is associated with decreased expression of tumor suppressor E-cadherin in this tissue. This gene resides …

**Accessions** — [HGNC:2516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2516) · Entrez [1501](https://www.ncbi.nlm.nih.gov/gene/1501) · UniProt [Q9UQB3](https://www.uniprot.org/uniprotkb/Q9UQB3) · Ensembl [ENSG00000169862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169862)

## Data

Gene col 9863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9863); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9863]; `tensor/DDL_lfc|DDL_z.npy` [9863]; `embed/gene_vectors.npy` [9863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9863 or target_col == 9863). Every well: [[CTNND2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNND2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
