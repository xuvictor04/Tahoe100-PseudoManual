---
symbol: "ENTPD6"
type: "gene"
col: 12426
ensembl_id: "ENSG00000197586"
name: "ectonucleoside triphosphate diphosphohydrolase 6"
location: "20p11.21"
module: 4
arm: "+"
pooled_cpm: 28.68
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ENTPD6

*ectonucleoside triphosphate diphosphohydrolase 6* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.30× (z +4.1, q 0.015, up in 14 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.29× (z +4.0, q 0.015, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.398× (z -20.7, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYGB]] (+0.73, fdr 7e-06, ⚠ same locus), [[NBEAL2]] (+0.63, fdr 1e-05), [[MAPKAPK3]] (+0.62, fdr 1e-05), [[TTLL12]] (+0.62, fdr 1e-05); moves opposite to [[ARID4B]] (-0.58, fdr 3e-05), [[LINC02608]] (-0.54, fdr 3e-05), [[NIFK-AS1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.1 | 0.015 | 14/34 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.015 | 22/47 (SNU-423, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.13 | 17/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.23× | +3.3 | 0.13 | 15/48 (A498, NCI-H2030, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.398×** | -20.7 | 0e+00 | 43/46 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.529×** | -14.3 | 4e-44 | 41/47 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.594×** | -8.3 | 2e-14 | 35/46 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.655×** | -6.7 | 2e-09 | 28/46 (KATO III, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -6.7 | 2e-09 | 33/48 (HOP62, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.678×** | -6.2 | 6e-08 | 31/48 (LoVo, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.675×** | -6.0 | 2e-07 | 27/47 (A-427, LoVo, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.689×** | -5.9 | 2e-07 | 25/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.698×** | -5.7 | 7e-07 | 27/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.714×** | -5.4 | 5e-06 | 22/48 (LoVo, COLO 205, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -5.3 | 5e-06 | 24/44 (SW 900, SNU-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -4.8 | 8e-05 | 22/48 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.761×** | -4.3 | 6e-04 | 22/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.766×** | -4.2 | 9e-04 | 23/48 (LoVo, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.762×** | -4.2 | 0.001 | 19/46 (SW480, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.771×** | -4.1 | 0.001 | 22/48 (SNU-423, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.652×** | -3.6 | 0.012 | 16/45 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -3.3 | 0.024 | 14/48 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -3.2 | 0.036 | 15/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.042 | 17/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 43.4 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -19.7) |
| [[SNU-1 (line)]] | wt | 184 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -22.0) |
| [[KATO III (line)]] | alt | 45.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.9) |
| [[COLO 205 (line)]] | alt | 41.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.7) |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.7) |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0699× (z -15.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -9.7) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.4) |
| [[H4 (line)]] | wt | 19.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.8) |
| [[HOP62 (line)]] | alt | 28.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.1) |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.9) |
| [[HT-29 (line)]] | alt | 36.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -12.2) |
| [[LS 180 (line)]] | wt | 43.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 50.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -15.7) |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.7) |
| [[SW1417 (line)]] | alt | 44.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -15.5) |
| [[SW480 (line)]] | alt | 23.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -18.0) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.201× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 28.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.7) |
| [[A549 (line)]] | wt | 32.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -9.7) |
| [[C32 (line)]] | wt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -9.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.4) |
| [[PANC-1 (line)]] | alt | 26.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -15.0) |
| [[RKO (line)]] | wt | 23.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -9.7) |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGB]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 | STRING 425; ⚠ same locus (20.0 kb, same strand: neighbours can correlate without regulation) |
| [[NBEAL2]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | +0.62 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TTLL12]] | +0.62 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[APEH]] | +0.60 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[STK25]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[BOP1]] | +0.56 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[APMAP]] | +0.56 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[NOC2L]] | +0.55 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[POFUT1]] | +0.55 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[INF2]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NOP9]] | +0.55 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[PRPF19]] | +0.55 | +0.34 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | -0.58 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[LINC02608]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NIFK-AS1]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MARCKS]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[SAMD4A-AS1]] | -0.53 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[ASH1L]] | -0.52 | -0.63 / -0.27 | both halves | 3e-04 |  |
| [[PCF11-AS1]] | -0.52 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[NDUFC1]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MIR181A2HG]] | -0.52 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[ARL17B]] | -0.51 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[GTF2IRD2B]] | -0.51 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[DSE]] | -0.50 | -0.55 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ENTPD6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DENND3]] | B | DENND3 activity lowers ENTPD6's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.08× higher at baseline in the lines without DENND3 | 0.079 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[PYGB]] | C | PYGB's natural level strengthens ENTPD6's drug response | PYGB's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.08; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.0, -27.9); signed map (-27.4, -45.3). **Vector** length 75.9, 14.4% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.9 | +0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -20.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -14.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleoside triphosphate diphosphohydrolase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:25,195,693-25,228,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTPDase-6, dJ738P15.3; previously CD39L2, IL6ST2 |
| Gene groups (HGNC) | Ectonucleoside triphosphate diphosphohydrolase family |
| Reactome | 3 pathways, smallest: Phosphate bond hydrolysis by NTPDase proteins; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [O75354](https://www.uniprot.org/uniprotkb/O75354) (Ectonucleoside triphosphate diphosphohydrolase 6):

> Catalyzes the hydrolysis of nucleoside triphosphates and diphosphates in a calcium- or magnesium-dependent manner. Has a strong preference for nucleoside diphosphates, preferentially hydrolyzes GDP, IDP, and UDP, with slower hydrolysis of CDP, ITP, GTP, CTP, ADP, and UTP and virtually no hydrolysis of ATP. The membrane bound form might support glycosylation reactions in the Golgi apparatus and, when released from cells, might catalyze the hydrolysis of extracellular nucleotides.

**Summary**, from NCBI Gene [955](https://www.ncbi.nlm.nih.gov/gene/955):

> ENTPD6 is similar to E-type nucleotidases (NTPases). NTPases, such as CD39, mediate catabolism of extracellular nucleotides. ENTPD6 contains 4 apyrase-conserved regions which are characteristic of NTPases. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:3368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3368) · Entrez [955](https://www.ncbi.nlm.nih.gov/gene/955) · UniProt [O75354](https://www.uniprot.org/uniprotkb/O75354) · Ensembl [ENSG00000197586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197586)

## Data

Gene col 12426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12426); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12426]; `tensor/DDL_lfc|DDL_z.npy` [12426]; `embed/gene_vectors.npy` [12426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12426 or target_col == 12426). Every well: [[ENTPD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
