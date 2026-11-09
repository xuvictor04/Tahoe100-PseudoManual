---
symbol: "MANEA"
type: "gene"
col: 10261
ensembl_id: "ENSG00000172469"
name: "mannosidase endo-alpha"
location: "6q16.1"
module: 25
arm: "+"
pooled_cpm: 15.11
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MANEA

*mannosidase endo-alpha* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.69× (z +14.1, q 2e-42, up in 25 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +6.8, q 2e-09, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -15.2, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBTPS2]] (+0.74, fdr 7e-06), [[ALG10]] (+0.72, fdr 9e-06), [[DCK]] (+0.72, fdr 7e-06); moves opposite to [[ELL]] (-0.67, fdr 1e-05), [[LINC00685]] (-0.66, fdr 1e-05), [[ZBTB7A]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[POGLUT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +14.1 | 2e-42 | 25/26 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +12.8 | 3e-35 | 36/40 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +6.8 | 2e-09 | 22/48 (SNU-423, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.2 | 3e-05 | 22/43 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.007 | 13/48 (RKO, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.007 | 14/48 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.022 | 9/43 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +3.4 | 0.050 | 14/32 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.23× | +3.0 | 0.15 | 10/48 (LS 180, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -15.2 | 0e+00 | 41/47 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -12.5 | 2e-33 | 34/46 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.432×** | -12.5 | 3e-33 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -10.1 | 1e-21 | 36/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -10.0 | 2e-21 | 32/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.535×** | -9.3 | 2e-18 | 33/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.538×** | -9.2 | 3e-18 | 31/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -8.7 | 3e-16 | 30/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.567×** | -8.0 | 1e-13 | 33/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.586×** | -7.9 | 1e-13 | 28/47 (LS 180, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.582×** | -7.7 | 6e-13 | 27/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -7.2 | 2e-11 | 25/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -6.6 | 2e-09 | 28/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -6.3 | 2e-08 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -5.9 | 1e-07 | 25/44 (RKO, SW1417, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -4.7 | 1e-04 | 19/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 9 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.7) |
| [[SW480 (line)]] | alt | 28.9 | 0 | 9 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -13.5) |
| [[PANC-1 (line)]] | alt | 17.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.5) |
| [[SNU-423 (line)]] | alt | 24.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.0) |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 19.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.5) |
| [[HOP62 (line)]] | alt | 13.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -12.1) |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.7) |
| [[KATO III (line)]] | alt | 29.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.3) |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0586× (z -9.9) |
| [[BT-474 (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0891× (z -9.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0860× (z -9.7) |
| [[J82 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0726× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 8.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -8.6) |
| [[RKO (line)]] | wt | 20.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.156× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0713× (z -9.6) |
| [[SW1417 (line)]] | alt | 8.17 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -9.6) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBTPS2]] | +0.74 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ALG10]] | +0.72 | +0.57 / +0.74 | both halves | 9e-06 | pathway: Asparagine N-linked glycosylation |
| [[DCK]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[TMEM237]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[DPY19L4]] | +0.67 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[SCCPDH]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.66 | +0.47 / +0.72 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[LANCL1]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RBBP9]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[NELFCD]] | +0.65 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[HADH]] | +0.64 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[POMK]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELL]] | -0.67 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[LINC00685]] | -0.66 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.63 | -0.56 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PLEKHN1]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 | STRING 448 |
| [[ATG2A]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[PLIN3]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[POLD4]] | -0.60 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[RABGEF1]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.59 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.59 | -0.52 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIDN]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CDC34]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[C11orf91]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POGLUT3]] | B | POGLUT3 activity raises MANEA's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without POGLUT3 | 0.028 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[C11orf91]] | B | C11orf91 activity lowers MANEA's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.48× higher at baseline in the lines without C11orf91 | 0.090 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.5, -18.6); signed map (-16.7, -39.9). **Vector** length 82.6, 17.0% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +12.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.9 | +1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -12.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -1.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -7.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase endo-alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:95,577,485-95,609,470 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12838, mandaselin |
| Gene groups (HGNC) | Mannosidases endo-alpha |
| Reactome | 3 pathways, smallest: N-glycan trimming and elongation in the cis-Golgi; Transport to the Golgi and subsequent modification; Asparagine N-linked glycosylation |
| Matched by | ensembl_id |

UniProt [Q5SRI9](https://www.uniprot.org/uniprotkb/Q5SRI9) carries no function annotation.

**Summary**, from NCBI Gene [79694](https://www.ncbi.nlm.nih.gov/gene/79694):

> N-glycosylation of proteins is initiated in the endoplasmic reticulum (ER) by the transfer of the preassembled oligosaccharide glucose-3-mannose-9-N-acetylglucosamine-2 from dolichyl pyrophosphate to acceptor sites on the target protein by an oligosaccharyltransferase complex. This core oligosaccharide is sequentially processed by several ER glycosidases and by an endomannosidase (E.C. 3.2.1.130), such as MANEA, in the Golgi. MANEA catalyzes the release of mono-, di-, and triglucosylmannose …

**Accessions** — [HGNC:21072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21072) · Entrez [79694](https://www.ncbi.nlm.nih.gov/gene/79694) · UniProt [Q5SRI9](https://www.uniprot.org/uniprotkb/Q5SRI9) · Ensembl [ENSG00000172469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172469)

## Data

Gene col 10261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10261); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10261]; `tensor/DDL_lfc|DDL_z.npy` [10261]; `embed/gene_vectors.npy` [10261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10261 or target_col == 10261). Every well: [[MANEA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MANEA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
