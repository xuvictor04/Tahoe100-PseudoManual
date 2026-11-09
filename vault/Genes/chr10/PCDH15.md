---
symbol: "PCDH15"
type: "gene"
col: 7427
ensembl_id: "ENSG00000150275"
name: "protocadherin related 15"
location: "10q21.1"
module: 19
arm: "+"
pooled_cpm: 15.5
n_lines_expressing: 41
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PCDH15

*protocadherin related 15* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.49× (z +23.0, q 0e+00, up in 31 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.174×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.197×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.215×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0850×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCM]] (+0.81, fdr 7e-06), [[NKAIN2]] (+0.77, fdr 7e-06), [[KCNMB2]] (+0.77, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[PDE1A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[STEAP1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.49×** | +23.0 | 0e+00 | 31/36 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +11.8 | 1e-29 | 18/24 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +11.5 | 2e-28 | 25/33 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +11.5 | 3e-28 | 27/38 (C32, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.71×** | +10.8 | 4e-25 | 27/36 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.4 | 2e-23 | 7/13 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +6.7 | 2e-09 | 19/38 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +6.2 | 4e-08 | 9/17 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.9 | 2e-07 | 14/32 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.3 | 6e-06 | 11/31 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.2 | 1e-05 | 20/36 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 4e-04 | 13/36 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.001 | 12/35 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.002 | 13/36 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.006 | 7/37 (NCI-H23, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.006 | 12/36 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.009 | 11/38 (NCI-H460, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.024 | 15/38 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.174×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.197×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.215×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0850×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.730× | -3.4 | 0.37 | 7/37 (A-427, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 67.8 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 4.12× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 8.11 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 8.38× (z +10.6) | — |
| [[C32 (line)]] | wt | 4.03 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 17.6× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 3.88 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.6) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0850× (z -8.6) |
| [[A-172 (line)]] | wt | 9.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.87× (z +9.2) | — |
| [[A498 (line)]] | wt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 4.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 4.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +10.4) | — |
| [[J82 (line)]] | alt | 3.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +8.8) | — |
| [[LoVo (line)]] | wt | 4.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.58× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 9.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 4.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +13.3) | — |
| [[RKO (line)]] | wt | 4.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +10.1) | — |
| [[A-427 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCM]] | +0.81 | +0.68 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[NKAIN2]] | +0.77 | +0.70 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[KCNMB2]] | +0.77 | +0.63 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[KCNJ6]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LINC02755]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[LSAMP]] | +0.73 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[AGBL1]] | +0.71 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[LINC00922]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[RIMS1]] | +0.69 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ANO3]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[AQP4-AS1]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CDH7]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 | STRING 438 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE1A]] | B | PDE1A activity raises PCDH15's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without PDE1A | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PCDH15's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GSG1L2]] | B | GSG1L2 activity raises PCDH15's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 3.09× lower at baseline in the lines without GSG1L2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[LINC03000]] | B | LINC03000 activity raises PCDH15's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 4.42× lower at baseline in the lines without LINC03000 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |
| [[NKAIN2]] | B | NKAIN2 activity raises PCDH15's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.23× lower at baseline in the lines without NKAIN2 | 0.048 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent |
| [[MIR99AHG]] | B | MIR99AHG activity raises PCDH15's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 2.73× lower at baseline in the lines without MIR99AHG | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[LINC02945]] | B | LINC02945 activity raises PCDH15's level | lines that do not express LINC02945 (38) vs lines expressing it (12) | 2.26× lower at baseline in the lines without LINC02945 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02211, ENSG00000285751, ENSG00000275016 |
| [[LINC01257]] | B | LINC01257 activity raises PCDH15's level | lines that do not express LINC01257 (31) vs lines expressing it (19) | 1.50× lower at baseline in the lines without LINC01257 | 0.074 | ⚠ within organs, on part of the lines; also absent: MIR3667HG, LINC01446, NAA11; maybe low, not absent |
| [[GREM2]] | B | GREM2 activity raises PCDH15's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.60× lower at baseline in the lines without GREM2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PCDH15's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[CHL1]] | B | CHL1 activity raises PCDH15's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.72× lower at baseline in the lines without CHL1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[SLC15A5]] | B | SLC15A5 activity raises PCDH15's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.50× lower at baseline in the lines without SLC15A5 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP1B]] | B | PCDH15 activity raises STEAP1B's level | lines that do not express PCDH15 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without PCDH15 | 0.097 | ⚠ within organs, on part of the lines; also absent: ANKRD7, ENSG00000236230, NR2F1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.4, 34.5); signed map (42.6, 39.1). **Vector** length 68.9, 13.1% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +23.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin related 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:53,802,771-55,627,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDHR15; previously USH1F, DFNB23 |
| Gene groups (HGNC) | Cadherin related; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QU1](https://www.uniprot.org/uniprotkb/Q96QU1) (Protocadherin-15):

> Calcium-dependent cell-adhesion protein. Essential for maintenance of normal retinal and cochlear function.

**Summary**, from NCBI Gene [65217](https://www.ncbi.nlm.nih.gov/gene/65217):

> This gene is a member of the cadherin superfamily. Family members encode integral membrane proteins that mediate calcium-dependent cell-cell adhesion. It plays an essential role in maintenance of normal retinal and cochlear function. Mutations in this gene result in hearing loss and Usher Syndrome Type IF (USH1F). Extensive alternative splicing resulting in multiple isoforms has been observed in the mouse ortholog. Similar alternatively spliced transcripts are inferred to occur in human, and …

**Accessions** — [HGNC:14674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14674) · Entrez [65217](https://www.ncbi.nlm.nih.gov/gene/65217) · UniProt [Q96QU1](https://www.uniprot.org/uniprotkb/Q96QU1) · Ensembl [ENSG00000150275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150275)

## Data

Gene col 7427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7427); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7427]; `tensor/DDL_lfc|DDL_z.npy` [7427]; `embed/gene_vectors.npy` [7427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7427 or target_col == 7427). Every well: [[PCDH15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
