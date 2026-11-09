---
symbol: "TAPT1-AS1"
type: "gene"
col: 15413
ensembl_id: "ENSG00000263327"
name: "TAPT1 antisense RNA 1"
location: "4p15.32"
module: 10
arm: "+"
pooled_cpm: 13.82
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TAPT1-AS1

*TAPT1 antisense RNA 1* — 4p15.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.84×, HCT15 11.7×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 9.62×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 9.98×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.177× (z -11.3, q 7e-27, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEKR1]] (+0.75, fdr 7e-06), [[SDCBP2-AS1]] (+0.70, fdr 1e-05), [[CAPN3]] (+0.69, fdr 7e-06); moves opposite to [[ABCD4]] (-0.56, fdr 1e-05), [[RNF149]] (-0.56, fdr 3e-05), [[AZIN2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15413.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.84×, HCT15 11.7×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 9.62×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 9.98×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.72× | +3.5 | 0.17 | 20/46 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.70× | +3.3 | 0.17 | 20/45 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.73× | +3.3 | 0.17 | 13/31 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.177×** | -11.3 | 7e-27 | 45/47 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.236×** | -9.4 | 1e-18 | 37/45 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.260×** | -8.8 | 3e-16 | 41/47 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.264×** | -8.7 | 6e-16 | 42/47 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.298×** | -7.5 | 1e-11 | 39/45 (PANC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.353×** | -6.8 | 1e-09 | 34/46 (NCI-H1792, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.361×** | -6.6 | 2e-09 | 37/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.410×** | -5.6 | 2e-06 | 31/42 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.472×** | -4.9 | 6e-05 | 32/47 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.458×** | -3.9 | 0.004 | 27/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.339×** | -3.7 | 0.012 | 23/35 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -3.6 | 0.015 | 23/46 (SW 900, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.350×** | -3.6 | 0.015 | 21/42 (SW 900, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.578×** | -3.4 | 0.024 | 18/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -3.4 | 0.027 | 21/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.604×** | -3.2 | 0.053 | 20/47 (RPMI-7951, SW48, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 18.7 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 9.62× (z +11.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0851× (z -12.7) |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0929× (z -11.3) |
| [[H4 (line)]] | wt | 51.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0318× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 24.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.108× (z -10.6) |
| [[A-427 (line)]] | wt | 6.37 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0620× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Rosiglitazone (drug)]] 5 µM 0.0657× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.111× (z -11.5) |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.136× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0299× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -9.5) |
| [[A498 (line)]] | wt | 25.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0941× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0495× (z -10.4) |
| [[J82 (line)]] | alt | 10.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0507× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0677× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0908× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 9.17 | 0 | 2 (2 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0470× (z -12.0) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0816× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0968× (z -9.0) |
| [[SW 900 (line)]] | alt | 42.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -9.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -8.7) |
| [[C32 (line)]] | wt | 6.33 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0537× (z -8.9) |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0817× (z -8.8) |
| [[HCT15 (line)]] | alt | 6.20 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 8.74 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0898× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 6.04 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0277× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 5.08 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.98× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 7.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0825× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 5.89 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0671× (z -8.5) |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0378× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEKR1]] | +0.75 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[SDCBP2-AS1]] | +0.70 | +0.73 / +0.56 | both halves | 1e-05 | same gene group |
| [[CAPN3]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[KLHDC1]] | +0.68 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[RAP2C-AS1]] | +0.67 | +0.77 / +0.50 | both halves | 1e-05 | same gene group |
| [[LINC00886]] | +0.66 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[TMEM232]] | +0.65 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[LINC02340]] | +0.65 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[KRCC1]] | +0.64 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[LINC00667]] | +0.64 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[PDCL3P4]] | +0.63 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[STAC3]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCD4]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RNF149]] | -0.56 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[AZIN2]] | -0.56 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | -0.55 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.54 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[NTAN1]] | -0.54 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[ABHD3]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NQO2]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ECI2]] | -0.54 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[AP1S1]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ZNF823]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[GPR89A]] | -0.53 | -0.54 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises TAPT1-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without FSIP2-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity strengthens TAPT1-AS1's drug response | lines that do not express FSIP2-AS1 (6) vs lines expressing it (42) | the lines without FSIP2-AS1 respond 0.50× as strongly (z diff +2.19); strongest at Digitoxin 5 µM: 0.66x vs 0.22x (z diff +4.8) | 0.099 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.4, 15.1); signed map (28.7, -11.7). **Vector** length 88.9, 22.9% of its response variance represented; |z| ≥ 3 in 1,166 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.6 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.0 | -4.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.6 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | TAPT1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p15.32 — chr4:16,226,685-16,320,140 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ39653 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26832) · Entrez [202020](https://www.ncbi.nlm.nih.gov/gene/202020) · Ensembl [ENSG00000263327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263327)

## Data

Gene col 15413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15413); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15413]; `tensor/DDL_lfc|DDL_z.npy` [15413]; `embed/gene_vectors.npy` [15413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15413 or target_col == 15413). Every well: [[TAPT1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAPT1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
