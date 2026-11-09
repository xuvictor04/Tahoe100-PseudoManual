---
symbol: "POLR3B"
type: "gene"
col: 274
ensembl_id: "ENSG00000013503"
name: "RNA polymerase III subunit B"
location: "12q23.3"
module: 33
arm: "+"
pooled_cpm: 22.53
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# POLR3B

*RNA polymerase III subunit B* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.63× (z +7.3, q 1e-10, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.544× (z -12.8, q 8e-35, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.460× (z -11.5, q 2e-28, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1B]] (+0.73, fdr 7e-06), [[POLR3H]] (+0.71, fdr 7e-06), [[CHCHD6]] (+0.70, fdr 7e-06); moves opposite to [[FAM117A]] (-0.64, fdr 2e-05), [[UPK2]] (-0.62, fdr 2e-05), [[HCG27]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +7.3 | 1e-10 | 36/48 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.9 | 8e-07 | 28/48 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.9 | 8e-07 | 28/48 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +5.4 | 1e-05 | 27/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.003 | 19/47 (SW480, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.32×** | +4.2 | 0.003 | 21/47 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +3.9 | 0.008 | 19/47 (LOX-IMVI, AsPC-1, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.6 | 0.026 | 12/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.036 | 10/48 (C32, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.544×** | -12.8 | 8e-35 | 35/47 (PANC-1, J82, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.460×** | -11.5 | 2e-28 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -11.3 | 4e-27 | 38/46 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -8.3 | 2e-14 | 36/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.561×** | -8.3 | 2e-14 | 30/47 (PANC-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.639×** | -6.6 | 3e-09 | 28/43 (LoVo, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -6.0 | 1e-07 | 27/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.679×** | -5.3 | 8e-06 | 22/38 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -5.1 | 3e-05 | 29/47 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -4.4 | 7e-04 | 17/33 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -4.3 | 9e-04 | 22/45 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.2 | 0.001 | 19/46 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -12.9) |
| [[PANC-1 (line)]] | alt | 26.7 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -24.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -18.5) |
| [[LoVo (line)]] | wt | 41.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -15.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -10.0) |
| [[A498 (line)]] | wt | 25.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 16.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -11.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 24.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 20.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -10.5) |
| [[SW1417 (line)]] | alt | 22.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0881× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -11.7) |
| [[SW480 (line)]] | alt | 26.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 26.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Silodosin (drug)]] 5 µM 0.142× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 26.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 37.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.3) |
| [[RKO (line)]] | wt | 23.7 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0938× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -9.3) |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 8.25 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0784× (z -11.5) |
| [[A-427 (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.258× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0672× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.202× (z -11.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.106× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0809× (z -18.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0795× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1B]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 | same gene group; STRING 913 |
| [[POLR3H]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 | same gene group; pathway: Cytosolic sensors of pathogen-associated DNA; STRING 999 |
| [[CHCHD6]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[VWA8]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[FXN]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[WDR3]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 | STRING 830 |
| [[MRPL3]] | +0.67 | +0.76 / +0.54 | both halves | 1e-05 | STRING 778 |
| [[TMEM177]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[HEATR3]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HMBS]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.64 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[UPK2]] | -0.62 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[HCG27]] | -0.62 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[HLA-A]] | -0.62 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CDK19]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[NDUFV2-AS1]] | -0.60 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[ZNF821]] | -0.59 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[CERT1]] | -0.58 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[YPEL5]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.57 | -0.70 / -0.48 | both halves | 2e-05 |  |
| [[RNASEK]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[LINC01090]] | -0.57 | -0.38 / -0.52 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises POLR3B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.7, -40.0); signed map (-11.3, -50.8). **Vector** length 91.5, 20.3% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.6 | -12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,357,748-106,510,198 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPC2, FLJ10388, C128 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NW08](https://www.uniprot.org/uniprotkb/Q9NW08) (DNA-directed RNA polymerase III subunit RPC2):

> Catalytic core component of RNA polymerase III (Pol III), a DNA-dependent RNA polymerase which synthesizes small non-coding RNAs using the four ribonucleoside triphosphates as substrates. Synthesizes 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. Pol III-mediated transcription cycle proceeds through transcription initiation, transcription elongation and transcription termination stages. During transcription initiation, Pol III is recruited to DNA promoters type I, II …

**Summary**, from NCBI Gene [55703](https://www.ncbi.nlm.nih.gov/gene/55703):

> This gene encodes the second largest subunit of RNA polymerase III, the polymerase responsible for synthesizing transfer and small ribosomal RNAs in eukaryotes. The largest subunit and the encoded protein form the catalytic center of RNA polymerase III. Mutations in this gene are a cause of hypomyelinating leukodystrophy. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:30348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30348) · Entrez [55703](https://www.ncbi.nlm.nih.gov/gene/55703) · UniProt [Q9NW08](https://www.uniprot.org/uniprotkb/Q9NW08) · Ensembl [ENSG00000013503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013503)

## Data

Gene col 274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 274); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 274]; `tensor/DDL_lfc|DDL_z.npy` [274]; `embed/gene_vectors.npy` [274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 274 or target_col == 274). Every well: [[POLR3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
