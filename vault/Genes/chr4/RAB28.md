---
symbol: "RAB28"
type: "gene"
col: 8108
ensembl_id: "ENSG00000157869"
name: "RAB28, member RAS oncogene family"
location: "4p15.33"
module: 18
arm: "+"
pooled_cpm: 69.7
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RAB28

*RAB28, member RAS oncogene family* — 4p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.41× (z +6.2, q 3e-07, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.549× (z -10.8, q 1e-24, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO36]] (+0.65, fdr 1e-05), [[TRAPPC8]] (+0.59, fdr 2e-05), [[AP4E1]] (+0.59, fdr 1e-05); moves opposite to [[ZNF815P]] (-0.58, fdr 4e-05), [[RYBP]] (-0.54, fdr 1e-05), [[GADD45B]] (-0.54, fdr 8e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +6.2 | 3e-07 | 34/48 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 0.002 | 30/48 (AsPC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +4.1 | 0.009 | 25/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +4.0 | 0.009 | 24/48 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.16× | +3.8 | 0.018 | 21/49 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.018 | 23/48 (LS 180, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.023 | 19/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.20×** | +3.4 | 0.054 | 19/49 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.19× | +3.2 | 0.080 | 18/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.10 | 17/48 (J82, SW48, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.18× | +3.0 | 0.13 | 18/48 (AsPC-1, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.549×** | -10.8 | 1e-24 | 39/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.639×** | -8.1 | 2e-13 | 33/49 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.667×** | -6.8 | 2e-09 | 31/45 (C-33 A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -6.1 | 1e-07 | 31/44 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -5.9 | 4e-07 | 32/47 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.662×** | -3.9 | 0.009 | 26/48 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **0.809×** | -3.8 | 0.010 | 24/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.793×** | -3.6 | 0.020 | 23/48 (A-427, A498, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.6 | 0.023 | 13/48 (SW480, C-33 A, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.045 | 19/48 (J82, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 93.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.405× (z -10.7) |
| [[LoVo (line)]] | wt | 84.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.486× (z -9.0) |
| [[SW480 (line)]] | alt | 84.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -26.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -14.0) |
| [[C-33 A (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0718× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.333× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 55.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0828× (z -17.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 56.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.488× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-172 (line)]] | wt | 80.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.412× (z -9.9) |
| [[A549 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.362× (z -10.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 38.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 65.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.272× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.259× (z -9.8) ⚠ toxic |
| [[HCT15 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -18.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 81.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.449× (z -9.9) |
| [[J82 (line)]] | alt | 84.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[LS 180 (line)]] | wt | 61.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.402× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 72.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.213× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 93.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -28.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -17.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 86.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.302× (z -10.2) |
| [[SW 1271 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 75.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.311× (z -8.9) |
| [[A498 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO36]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[TRAPPC8]] | +0.59 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[AP4E1]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ATR]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LIN52]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.56 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[ARHGEF11]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PKD2]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ELP4]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[VPS45]] | +0.54 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[ANAPC7]] | +0.54 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[LSM6]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF815P]] | -0.58 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RYBP]] | -0.54 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[GADD45B]] | -0.54 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[PPP1CB]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[SYT11]] | -0.49 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[CD99P1]] | -0.48 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[STARD5]] | -0.48 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[SUGT1P4-STRA6LP]] | -0.48 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[LMBRD1]] | -0.47 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[PRKAR2B]] | -0.45 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[FXR1]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SUGT1]] | -0.45 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RAB28's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers RAB28's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PRKAR2B]] | B | PRKAR2B activity raises RAB28's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.24× lower at baseline in the lines without PRKAR2B | 0.068 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises RAB28's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.207). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-14.0, 4.9); signed map (-18.1, -26.2). **Vector** length 87.7, 21.7% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.6 | +0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | -1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB28, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.33 — chr4:13,361,354-13,484,365 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P51157](https://www.uniprot.org/uniprotkb/P51157) (Ras-related protein Rab-28):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB28 is required for shedding and phagocytosis of cone cell outer segments (OS) discs in the retina (By similarity). …

**Summary**, from NCBI Gene [9364](https://www.ncbi.nlm.nih.gov/gene/9364):

> This gene encodes a member of the Rab subfamily of Ras-related small GTPases. The encoded protein may be involved in regulating intracellular trafficking. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 9 and X. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:9768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9768) · Entrez [9364](https://www.ncbi.nlm.nih.gov/gene/9364) · UniProt [P51157](https://www.uniprot.org/uniprotkb/P51157) · Ensembl [ENSG00000157869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157869)

## Data

Gene col 8108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8108); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8108]; `tensor/DDL_lfc|DDL_z.npy` [8108]; `embed/gene_vectors.npy` [8108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8108 or target_col == 8108). Every well: [[RAB28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
