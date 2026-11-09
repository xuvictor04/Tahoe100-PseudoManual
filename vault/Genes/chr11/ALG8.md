---
symbol: "ALG8"
type: "gene"
col: 8211
ensembl_id: "ENSG00000159063"
name: "ALG8 alpha-1,3-glucosyltransferase"
location: "11q14.1"
module: 5
arm: "+"
pooled_cpm: 33.67
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ALG8

*ALG8 alpha-1,3-glucosyltransferase* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +5.2, q 1e-04, up in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.24× (z +4.2, q 0.005, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.44×; ⚠ cell-cycle shift, explains ~19% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.506× (z -9.4, q 2e-18, down in 34 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.521× (z -9.0, q 5e-17, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC11]] (+0.79, fdr 7e-06), [[TRNT1]] (+0.79, fdr 7e-06), [[WDR4]] (+0.77, fdr 7e-06); moves opposite to [[PLEKHH3]] (-0.71, fdr 7e-06), [[OAZ1]] (-0.69, fdr 4e-05), [[KBTBD3]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DENND3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8211.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.44×; ⚠ cell-cycle shift, explains ~19% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +5.2 | 1e-04 | 26/48 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.5 | 0.002 | 19/40 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.005 | 27/48 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.6 | 0.050 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -9.4 | 2e-18 | 34/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.521×** | -9.0 | 5e-17 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.685×** | -7.4 | 2e-11 | 31/47 (LoVo, PANC-1, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.601×** | -7.1 | 2e-10 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -6.9 | 7e-10 | 36/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -6.7 | 2e-09 | 31/47 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.632×** | -6.4 | 2e-08 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -5.4 | 4e-06 | 32/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.684×** | -5.1 | 3e-05 | 28/48 (PANC-1, A-427, …) | top dose only | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.725×** | -4.5 | 5e-04 | 23/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.727×** | -4.4 | 5e-04 | 23/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.732×** | -4.3 | 7e-04 | 22/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.745×** | -4.1 | 0.002 | 25/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -3.5 | 0.018 | 22/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Terfenadine (drug)]] 5 µM |  | 0.837× | -3.5 | 0.018 | 16/48 (SNU-1, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 73.5 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -9.7) |
| [[SW480 (line)]] | alt | 45.6 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.295× (z -12.1) |
| [[SHP-77 (line)]] | alt | 66.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[J82 (line)]] | alt | 40.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[KATO III (line)]] | alt | 48.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[NCI-H460 (line)]] | wt | 27.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[C-33 A (line)]] | alt | 64.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[C32 (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H23 (line)]] | alt | 99.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.282× (z -13.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.352× (z -9.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A549 (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.132× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.4) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -9.2) |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | +0.79 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[TRNT1]] | +0.79 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[WDR4]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[EMG1]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[E2F3]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DHX37]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.73 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[TSR1]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHH3]] | -0.71 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[OAZ1]] | -0.69 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[KBTBD3]] | -0.68 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.68 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.68 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[AHDC1]] | -0.67 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[SLC17A7]] | -0.67 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.66 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ARL3]] | -0.66 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[GRHL1]] | -0.64 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[FOXO6]] | -0.64 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RAB11FIP1]] | -0.63 | -0.55 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND3]] | B | DENND3 activity lowers ALG8's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.74× higher at baseline in the lines without DENND3 | 0.020 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity lowers ALG8's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.44× higher at baseline in the lines without NR3C2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity lowers ALG8's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.32× higher at baseline in the lines without IRF6 | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.842). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.8, -33.7); signed map (-0.5, -46.8). **Vector** length 109, 28.9% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.61 to 13); *rRNA processing* (reactome, mean cos +0.56 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -9.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -7.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ALG8 alpha-1,3-glucosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,095,244-78,139,660 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2840 |
| Gene groups (HGNC) | Alpha-1,3-glucosyltransferases |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVK2](https://www.uniprot.org/uniprotkb/Q9BVK2) (Dolichyl pyrophosphate Glc1Man9GlcNAc2 alpha-1,3-glucosyltransferase):

> Dolichyl pyrophosphate Glc1Man9GlcNAc2 alpha-1,3-glucosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, …

**Summary**, from NCBI Gene [79053](https://www.ncbi.nlm.nih.gov/gene/79053):

> This gene encodes a member of the ALG6/ALG8 glucosyltransferase family. The encoded protein catalyzes the addition of the second glucose residue to the lipid-linked oligosaccharide precursor for N-linked glycosylation of proteins. Mutations in this gene have been associated with congenital disorder of glycosylation type Ih (CDG-Ih). Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23161) · Entrez [79053](https://www.ncbi.nlm.nih.gov/gene/79053) · UniProt [Q9BVK2](https://www.uniprot.org/uniprotkb/Q9BVK2) · Ensembl [ENSG00000159063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159063)

## Data

Gene col 8211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8211); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8211]; `tensor/DDL_lfc|DDL_z.npy` [8211]; `embed/gene_vectors.npy` [8211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8211 or target_col == 8211). Every well: [[ALG8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
