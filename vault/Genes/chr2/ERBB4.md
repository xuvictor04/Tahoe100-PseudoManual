---
symbol: "ERBB4"
type: "gene"
col: 10938
ensembl_id: "ENSG00000178568"
name: "erb-b2 receptor tyrosine kinase 4"
location: "2q34"
module: 9
arm: "+"
pooled_cpm: 65.9
n_lines_expressing: 17
n_dd_up: 32
n_dd_down: 3
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ERBB4

*erb-b2 receptor tyrosine kinase 4* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.44× (z +24.6, q 0e+00, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.720× (z -3.8, q 0.068, down in 5 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.145×, NCI-H661 0.220×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.125×, A-427 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.116×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.201×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.221×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUT9]] (+0.68, fdr 7e-06), [[MMRN1]] (+0.67, fdr 3e-05), [[CDH18]] (+0.67, fdr 7e-06); moves opposite to [[KRBOX4]] (-0.47, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[FUT9]] → it (grade C ⚠); 9 go from it, the strongest it → [[ZFHX4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.44×** | +24.6 | 0e+00 | 12/15 (J82, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **5.51×** | +19.9 | 0e+00 | 12/15 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +18.4 | 0e+00 | 8/15 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.92×** | +15.9 | 0e+00 | 12/15 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.57×** | +14.8 | 0e+00 | 12/15 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.51×** | +14.6 | 0e+00 | 13/15 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +13.5 | 6e-40 | 10/15 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.16×** | +13.4 | 3e-39 | 12/15 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +10.2 | 8e-23 | 5/16 (NCI-H1573, A-172, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +7.9 | 2e-13 | 6/14 (C32, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.47×** | +7.6 | 2e-12 | 11/16 (J82, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +7.1 | 5e-11 | 4/14 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +7.1 | 8e-11 | 11/15 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.79×** | +6.8 | 4e-10 | 4/14 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.4 | 2e-06 | 2/17 (BT-474, C32) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +5.3 | 5e-06 | 6/15 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 1e-05 | 8/15 (A-427, BT-474, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 5e-04 | 4/15 (hTERT-HPNE, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.145×, NCI-H661 0.220×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.125×, A-427 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.116×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.201×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.221×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.720×** | -3.8 | 0.068 | 5/15 (NCI-H661, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.740×** | -3.5 | 0.085 | 8/15 (SHP-77, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.728×** | -3.5 | 0.085 | 0/15 | inconsistent across doses |  |
| [[Gallic acid (drug)]] 5 µM |  | 0.829× | -3.1 | 0.27 | 0/15 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.2 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 8.81× (z +14.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 19.1 | 9 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 10.7× (z +18.8) | — |
| [[A-172 (line)]] | wt | 34.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 163× (z +32.9) | — |
| [[C-33 A (line)]] | alt | 2,746 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -20.2) |
| [[NCI-H2030 (line)]] | alt | 34.9 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 7.73× (z +13.9) | — |
| [[C32 (line)]] | wt | 33.6 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 14.0× (z +18.6) | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 55.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 8.20× (z +11.4) | — |
| [[A-427 (line)]] | wt | 665 | 2 (1 ⚠) | 3 (2 ⚠) | [[Trametinib (drug)]] 5 µM 3.30× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.37× (z +8.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 52.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.23× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 18.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.24× (z +11.2) | — |
| [[NCI-H661 (line)]] | alt | 1,949 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -10.7) |
| [[SHP-77 (line)]] | alt | 128 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +11.3) | — |
| [[A549 (line)]] | wt | 5.45 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.95 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUT9]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MMRN1]] | +0.67 | +0.45 / +0.73 | both halves | 3e-05 | **novel candidate** |
| [[CDH18]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CTNNA2]] | +0.66 | +0.54 / +0.77 | both halves | 1e-05 | **novel candidate** |
| [[KLHL13]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SYT1]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 | same gene group; pathway: Neuronal System |
| [[CDH10]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[EPHA5]] | +0.64 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[CADM2]] | +0.63 | +0.63 / +0.71 | both halves | 7e-06 | same gene group |
| [[VAV3]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; STRING 426 |
| [[TMEM108]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX4]] | -0.47 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT9]] | C | FUT9 activity raises ERBB4's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 6.75× lower at baseline in the lines without FUT9 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[MIR2052HG]] | C | MIR2052HG activity raises ERBB4's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.88× lower at baseline in the lines without MIR2052HG | 0.018 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises ERBB4's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 4.35× lower at baseline in the lines without BRINP3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[GCG]] | C | GCG activity raises ERBB4's level | lines that do not express GCG (46) vs lines expressing it (4) | 19.01× lower at baseline in the lines without GCG | 0.026 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[MMRN1]] | C | MMRN1 activity raises ERBB4's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 14.21× lower at baseline in the lines without MMRN1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[FSTL5]] | C | FSTL5 activity raises ERBB4's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.38× lower at baseline in the lines without FSTL5 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises ERBB4's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 5.48× lower at baseline in the lines without KCNH7 | 0.033 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[LINC00993]] | C | LINC00993 activity raises ERBB4's level | lines that do not express LINC00993 (35) vs lines expressing it (15) | 5.39× lower at baseline in the lines without LINC00993 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANKRD30A, KCNH5, KCNB2; maybe low, not absent; co-absent with the target |
| [[ANKRD30A]] | C | ANKRD30A activity raises ERBB4's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without ANKRD30A | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises ERBB4's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 3.23× lower at baseline in the lines without MGAT4C | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[ZFHX4-AS1]] | C | ZFHX4-AS1 activity raises ERBB4's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 3.53× lower at baseline in the lines without ZFHX4-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFHX4]] | C | ERBB4 activity raises ZFHX4's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 6.40× lower at baseline in the lines without ERBB4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[MIR2052HG]] | C | ERBB4 activity raises MIR2052HG's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.24× lower at baseline in the lines without ERBB4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[MGAT4C]] | C | ERBB4 activity raises MGAT4C's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.41× lower at baseline in the lines without ERBB4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[DMD]] | C | ERBB4 activity raises DMD's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.17× lower at baseline in the lines without ERBB4 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[PPFIA2]] | C | ERBB4 activity raises PPFIA2's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 2.87× lower at baseline in the lines without ERBB4 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[OR3A2]] | C | ERBB4 activity raises OR3A2's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 2.02× lower at baseline in the lines without ERBB4 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[FMN2]] | C | ERBB4 activity raises FMN2's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 2.81× lower at baseline in the lines without ERBB4 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[PCDH10]] | C | ERBB4 activity raises PCDH10's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.28× lower at baseline in the lines without ERBB4 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[FUT9]] | C | ERBB4 activity raises FUT9's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.32× lower at baseline in the lines without ERBB4 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.2, 33.8); signed map (40.1, 35.4). **Vector** length 62.7, 19.5% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +24.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | erb-b2 receptor tyrosine kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:211,375,717-212,538,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALS19, HER4 |
| Gene groups (HGNC) | Erb-b2 receptor tyrosine kinases; MicroRNA protein coding host genes |
| Reactome | 37 pathways, smallest: Downregulation of ERBB4 signaling; PI3K events in ERBB4 signaling; ERBB2 Activates PTK6 Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15303](https://www.uniprot.org/uniprotkb/Q15303) (Receptor tyrosine-protein kinase erbB-4):

> Tyrosine-protein kinase that plays an essential role as cell surface receptor for neuregulins and EGF family members and regulates development of the heart, the central nervous system and the mammary gland, gene transcription, cell proliferation, differentiation, migration and apoptosis. Required for normal cardiac muscle differentiation during embryonic development, and for postnatal cardiomyocyte proliferation. Required for normal development of the embryonic central nervous system, …

**Summary**, from NCBI Gene [2066](https://www.ncbi.nlm.nih.gov/gene/2066):

> This gene is a member of the Tyr protein kinase family and the epidermal growth factor receptor subfamily. It encodes a single-pass type I membrane protein with multiple cysteine rich domains, a transmembrane domain, a tyrosine kinase domain, a phosphotidylinositol-3 kinase binding site and a PDZ domain binding motif. The protein binds to and is activated by neuregulins and other factors and induces a variety of cellular responses including mitogenesis and differentiation. Multiple proteolytic …

**Accessions** — [HGNC:3432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3432) · Entrez [2066](https://www.ncbi.nlm.nih.gov/gene/2066) · UniProt [Q15303](https://www.uniprot.org/uniprotkb/Q15303) · Ensembl [ENSG00000178568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178568)

## Data

Gene col 10938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10938); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10938]; `tensor/DDL_lfc|DDL_z.npy` [10938]; `embed/gene_vectors.npy` [10938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10938 or target_col == 10938). Every well: [[ERBB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERBB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
