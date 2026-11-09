---
symbol: "STX1A"
type: "gene"
col: 2722
ensembl_id: "ENSG00000106089"
name: "syntaxin 1A"
location: "7q11.23"
module: 84
arm: "+"
pooled_cpm: 43.0
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 45
n_dd_up_clean: 8
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 21
direction_downstream: 29
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# STX1A

*syntaxin 1A* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.66× (z +6.4, q 9e-08, up in 23 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.38× (z +4.2, q 0.006, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.468× (z -14.0, q 9e-42, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNN4]] (+0.83, fdr 7e-06), [[RASA3]] (+0.78, fdr 7e-06), [[PHC2]] (+0.74, fdr 7e-06); moves opposite to [[GIPC2]] (-0.60, fdr 5e-05), [[DERA]] (-0.59, fdr 4e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TMEM158]] → it (grade B ⚠); 29 go from it, the strongest it → cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.4 | 9e-08 | 23/41 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.006 | 21/44 (LOX-IMVI, RKO, …) | two highest doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.014 | 23/44 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.014 | 17/45 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.058 | 17/45 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +3.4 | 0.058 | 16/45 (CFPAC-1, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.058 | 19/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.058 | 20/44 (LOX-IMVI, RKO, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.072 | 19/44 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.072 | 14/44 (SNU-423, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | 1.27× | +3.1 | 0.11 | 12/45 (CFPAC-1, SW480, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.468×** | -14.0 | 9e-42 | 33/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.564×** | -9.3 | 5e-18 | 34/45 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.481×** | -9.2 | 9e-18 | 29/44 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.508×** | -8.7 | 7e-16 | 31/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.506×** | -8.5 | 2e-15 | 32/45 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.579×** | -8.5 | 2e-15 | 34/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.521×** | -8.2 | 3e-14 | 31/45 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.541×** | -7.8 | 4e-13 | 31/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.555×** | -7.7 | 1e-12 | 33/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.563×** | -7.1 | 9e-11 | 30/44 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -6.9 | 3e-10 | 25/38 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -6.8 | 7e-10 | 32/46 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.604×** | -6.6 | 2e-09 | 32/44 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.717×** | -6.1 | 4e-08 | 27/45 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -6.1 | 5e-08 | 23/34 (NCI-H2347, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.723×** | -5.9 | 1e-07 | 31/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.649×** | -5.6 | 6e-07 | 29/45 (HT-29, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 25 (6 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.314× (z -34.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -26.5) |
| [[SK-MEL-2 (line)]] | alt | 56.4 | 0 | 20 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0429× (z -33.8) |
| [[C32 (line)]] | wt | 62.1 | 0 | 18 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0668× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 52.5 | 0 | 17 (2 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.203× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 40.7 | 0 | 11 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.473× (z -18.7) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -17.8) |
| [[H4 (line)]] | wt | 86.6 | 0 | 10 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0728× (z -14.6) |
| [[A-172 (line)]] | wt | 67.1 | 0 | 9 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.217× (z -12.3) |
| [[HS-578T (line)]] | alt | 79.8 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -15.2) |
| [[HOP62 (line)]] | alt | 63.1 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 93.2 | 0 | 8 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.432× (z -18.3) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -14.7) |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.324× (z -14.1) |
| [[SW 900 (line)]] | alt | 77.9 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -12.3) |
| [[A549 (line)]] | wt | 51.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.170× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 51.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -15.7) |
| [[LoVo (line)]] | wt | 19.0 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.18× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.663× (z -10.7) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 59.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.3) |
| [[SNU-423 (line)]] | alt | 64.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -15.7) |
| [[SW480 (line)]] | alt | 18.7 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.51× (z +9.8) | — |
| [[A498 (line)]] | wt | 45.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 38.7 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.325× (z -9.9) |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.116× (z -8.9) |
| [[HT-29 (line)]] | alt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -13.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -9.1) |
| [[PANC-1 (line)]] | alt | 46.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.0) |
| [[RKO (line)]] | wt | 66.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 40.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.9) |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 1 | — | [[Selinexor (drug)]] 0.5 µM 0.0518× (z -9.6) |
| [[A-427 (line)]] | wt | 9.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNN4]] | +0.83 | +0.83 / +0.79 | both halves | 7e-06 | pathway: Neuronal System |
| [[RASA3]] | +0.78 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[PHC2]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[RAC2]] | +0.73 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ARID3B]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.71 | +0.77 / +0.58 | both halves | 8e-06 |  |
| [[BMERB1]] | +0.70 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PDLIM7]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SH2B3]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SMOX]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TMEM255B]] | +0.66 | +0.64 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIPC2]] | -0.60 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[DERA]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM158]] | B | TMEM158 activity raises STX1A's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.48× lower at baseline in the lines without TMEM158 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[ANTXR2]] | B | ANTXR2 activity raises STX1A's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without ANTXR2 | 0.004 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[SMOX]] | B | SMOX activity raises STX1A's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without SMOX | 0.009 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[MIR100HG]] | B | MIR100HG activity raises STX1A's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without MIR100HG | 0.017 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[NPAS2]] | B | NPAS2 activity raises STX1A's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without NPAS2 | 0.018 | ⚠ within organs, on part of the lines |
| [[C13orf46]] | B | C13orf46 activity raises STX1A's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without C13orf46 | 0.019 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[PLAUR]] | B | PLAUR activity raises STX1A's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without PLAUR | 0.024 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises STX1A's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without S100A16 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[DUSP5]] | B | DUSP5 activity raises STX1A's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without DUSP5 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[CD82]] | B | CD82 activity raises STX1A's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without CD82 | 0.036 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[CDCP1]] | B | CDCP1 activity raises STX1A's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without CDCP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[TOR4A]] | B | TOR4A activity raises STX1A's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without TOR4A | 0.050 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 0, C 29. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM | C | STX1A activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.57× the cells of the other lines | 0.002 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | C | STX1A activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.19× the cells of the other lines | 0.003 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM | C | STX1A activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.47× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | STX1A activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.63× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[Everolimus (drug)]] 5 µM | C | STX1A activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 1.37× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[NIBAN2]] | C | STX1A activity raises NIBAN2's level | lines that do not express STX1A (3) vs lines expressing it (47) | 4.49× lower at baseline in the lines without STX1A | 0.007 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | C | STX1A activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 1.73× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[Infigratinib (drug)]] 5 µM | C | STX1A activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.52× the cells of the other lines | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[PLAUR]] | C | STX1A activity raises PLAUR's level | lines that do not express STX1A (3) vs lines expressing it (47) | 5.95× lower at baseline in the lines without STX1A | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[GSK1059615 (drug)]] 5 µM | C | STX1A activity raises the cells' numbers under GSK1059615 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.30× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[Tolcapone (drug)]] 5 µM | C | STX1A activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.75× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | STX1A activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.54× the cells of the other lines | 0.024 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.4, 2.2); signed map (1.5, 48.8). **Vector** length 152, 51.8% of its response variance represented; |z| ≥ 3 in 1,514 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.4 | +3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.3 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.0 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +2.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -10.1 | -8.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -9.9 | -9.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -9.3 | -9.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -9.2 | -7.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -9.1 | -8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.8 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,699,206-73,719,672 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPC-1, p35-1; previously STX1 |
| Gene groups (HGNC) | Syntaxins |
| Reactome | 27 pathways, smallest: Neurotoxicity of clostridium toxins; LGI-ADAM interactions; Acetylcholine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16623](https://www.uniprot.org/uniprotkb/Q16623) (Syntaxin-1A):

> Plays an essential role in hormone and neurotransmitter calcium-dependent exocytosis and endocytosis. Part of the SNARE (Soluble NSF Attachment Receptor) complex composed of SNAP25, STX1A and VAMP2 which mediates the fusion of synaptic vesicles with the presynaptic plasma membrane. STX1A and SNAP25 are localized on the plasma membrane while VAMP2 resides in synaptic vesicles. The pairing of the three SNAREs from the N-terminal SNARE motifs to the C-terminal anchors leads to the formation of the …

**Summary**, from NCBI Gene [6804](https://www.ncbi.nlm.nih.gov/gene/6804):

> This gene encodes a member of the syntaxin superfamily. Syntaxins are nervous system-specific proteins implicated in the docking of synaptic vesicles with the presynaptic plasma membrane. Syntaxins possess a single C-terminal transmembrane domain, a SNARE [Soluble NSF (N-ethylmaleimide-sensitive fusion protein)-Attachment protein REceptor] domain (known as H3), and an N-terminal regulatory domain (Habc). Syntaxins bind synaptotagmin in a calcium-dependent fashion and interact with voltage …

**Accessions** — [HGNC:11433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11433) · Entrez [6804](https://www.ncbi.nlm.nih.gov/gene/6804) · UniProt [Q16623](https://www.uniprot.org/uniprotkb/Q16623) · Ensembl [ENSG00000106089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106089)

## Data

Gene col 2722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2722); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2722]; `tensor/DDL_lfc|DDL_z.npy` [2722]; `embed/gene_vectors.npy` [2722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2722 or target_col == 2722). Every well: [[STX1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
