---
symbol: "SLITRK4"
type: "gene"
col: 11041
ensembl_id: "ENSG00000179542"
name: "SLIT and NTRK like family member 4"
location: "Xq27.3"
module: 19
arm: "+"
pooled_cpm: 3.48
n_lines_expressing: 14
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 14
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLITRK4

*SLIT and NTRK like family member 4* — Xq27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.24× (z +9.7, q 2e-19, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.88× (z +5.1, q 5e-05, up in 8 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0824×, A498 0.120×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0631×, A498 0.0510×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.0623×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.385×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2I-AS1]] (+0.77, fdr 7e-06), [[NCKAP5-AS2]] (+0.75, fdr 7e-06), [[GREM2]] (+0.72, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01508]] → it (grade C ⚠); 14 go from it, the strongest it → [[PRSS23-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.24×** | +9.7 | 2e-19 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.42×** | +9.5 | 7e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.77×** | +7.2 | 2e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +5.1 | 5e-05 | 8/11 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.6 | 5e-04 | 0/7 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.5 | 7e-04 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.94×** | +4.3 | 0.001 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.76×** | +4.0 | 0.004 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.6 | 0.019 | 1/6 (LOX-IMVI) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +3.6 | 0.019 | 6/8 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.019 | 1/11 (NCI-H460) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.073 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +3.1 | 0.077 | 2/6 (LOX-IMVI, SHP-77) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +3.1 | 0.081 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +3.0 | 0.083 | 0/6 | top dose only | cell-cycle shift (explains ~23% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.15×** | +3.0 | 0.083 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.67×** | +3.0 | 0.092 | 1/6 (SHP-77) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11041.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0824×, A498 0.120×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0631×, A498 0.0510×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.0623×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.385×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.563× | -3.4 | 0.28 | 4/7 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.5 µM |  | 0.569× | -3.3 | 0.28 | 1/11 (CHP-212) | inconsistent across doses |  |
| [[Tucatinib (drug)]] 0.5 µM |  | 0.457× | -3.1 | 0.29 | 0/11 | inconsistent across doses | noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.568× | -3.1 | 0.29 | 0/11 | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.584× | -3.0 | 0.29 | 0/11 | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0824× (z -22.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0631× (z -17.6) |
| [[A498 (line)]] | wt | 6.24 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0510× (z -13.0) |
| [[A-172 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.329 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2I-AS1]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[NCKAP5-AS2]] | +0.75 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[GREM2]] | +0.72 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[CNTN1]] | +0.71 | +0.47 / +0.74 | both halves | 2e-05 | **novel candidate** |
| [[COL4A6]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[UNC5D]] | +0.70 | +0.52 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[ADGRD1]] | +0.69 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.69 | +0.52 / +0.81 | both halves | 1e-05 | pathway: Neuronal System |
| [[LINC01035]] | +0.69 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[DPP10]] | +0.69 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SCUBE1]] | +0.68 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01508]] | C | LINC01508 activity raises SLITRK4's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.22× lower at baseline in the lines without LINC01508 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises SLITRK4's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.81× lower at baseline in the lines without DPP10 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises SLITRK4's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without BCHE | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises SLITRK4's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 3.00× lower at baseline in the lines without LINC01035 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[NRCAM]] | C | NRCAM activity raises SLITRK4's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.01× lower at baseline in the lines without NRCAM | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[TENM1]] | C | TENM1 activity raises SLITRK4's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without TENM1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[ACSS3]] | C | ACSS3 activity raises SLITRK4's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 1.57× lower at baseline in the lines without ACSS3 | 0.095 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23-AS1]] | B | SLITRK4 activity raises PRSS23-AS1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 1.71× lower at baseline in the lines without SLITRK4 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R |
| [[SOX7]] | C | SLITRK4 activity raises SOX7's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 1.93× lower at baseline in the lines without SLITRK4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[TENM1]] | C | SLITRK4 activity raises TENM1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.93× lower at baseline in the lines without SLITRK4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[RTN1]] | C | SLITRK4 activity raises RTN1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.17× lower at baseline in the lines without SLITRK4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[ESM1]] | C | SLITRK4 activity raises ESM1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without SLITRK4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[PAK3]] | C | SLITRK4 activity raises PAK3's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.82× lower at baseline in the lines without SLITRK4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[LINC01508]] | C | SLITRK4 activity raises LINC01508's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 2.53× lower at baseline in the lines without SLITRK4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[PAX7]] | C | SLITRK4 activity raises PAX7's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 1.79× lower at baseline in the lines without SLITRK4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[SGIP1]] | C | SLITRK4 activity raises SGIP1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.59× lower at baseline in the lines without SLITRK4 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[LINC02742]] | C | SLITRK4 activity raises LINC02742's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without SLITRK4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[NRCAM]] | C | SLITRK4 activity raises NRCAM's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.16× lower at baseline in the lines without SLITRK4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[ADARB2]] | C | SLITRK4 activity raises ADARB2's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.13× lower at baseline in the lines without SLITRK4 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.4, 35.7); signed map (42.1, 44.9). **Vector** length 26.9, 7.26% of its response variance represented; |z| ≥ 3 in 260 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +0.3 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +0.7 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.0 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -0.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SLIT and NTRK like family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq27.3 — chrX:143,622,790-143,636,101 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp547M2010 |
| Gene groups (HGNC) | SLIT and NTRK like family |
| Reactome | 3 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW52](https://www.uniprot.org/uniprotkb/Q8IW52) (SLIT and NTRK-like protein 4):

> It is involved in synaptogenesis and promotes synapse differentiation. Suppresses neurite outgrowth (By similarity).

**Summary**, from NCBI Gene [139065](https://www.ncbi.nlm.nih.gov/gene/139065):

> This gene encodes a transmembrane protein belonging to the the SLITRK family. These family members include two N-terminal leucine-rich repeat domains similar to those found in the axonal growth-controlling protein SLIT, as well as C-terminal regions similar to neurotrophin receptors. Studies of an homologous protein in mouse suggest that this family member functions to suppress neurite outgrowth. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:23502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23502) · Entrez [139065](https://www.ncbi.nlm.nih.gov/gene/139065) · UniProt [Q8IW52](https://www.uniprot.org/uniprotkb/Q8IW52) · Ensembl [ENSG00000179542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179542)

## Data

Gene col 11041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11041); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11041]; `tensor/DDL_lfc|DDL_z.npy` [11041]; `embed/gene_vectors.npy` [11041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11041 or target_col == 11041). Every well: [[SLITRK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLITRK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
