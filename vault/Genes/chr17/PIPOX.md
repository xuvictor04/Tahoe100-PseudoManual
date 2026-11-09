---
symbol: "PIPOX"
type: "gene"
col: 11055
ensembl_id: "ENSG00000179761"
name: "pipecolic acid and sarcosine oxidase"
location: "17q11.2"
module: 26
arm: "+"
pooled_cpm: 7.95
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PIPOX

*pipecolic acid and sarcosine oxidase* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.55× (z +23.8, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.346× (z -11.8, q 4e-29, down in 30 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.392× (z -10.4, q 8e-23, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.75, fdr 1e-05), [[ZNF213-AS1]] (+0.73, fdr 7e-06), [[GPR137]] (+0.72, fdr 7e-06); moves opposite to [[COMMD2]] (-0.62, fdr 4e-05), [[RRP1B]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.55×** | +23.8 | 0e+00 | 42/42 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +12.2 | 5e-32 | 12/16 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +11.7 | 2e-29 | 34/39 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +11.5 | 2e-28 | 27/32 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +8.9 | 6e-17 | 30/43 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +8.3 | 1e-14 | 29/47 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +8.3 | 1e-14 | 15/24 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +6.1 | 8e-08 | 20/45 (HEC-1-A, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 7e-04 | 11/45 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.2 | 0.002 | 6/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.008 | 11/46 (HepG2/C3A, A549, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.079 | 7/40 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +3.1 | 0.079 | 3/45 (Hs 766T, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.346×** | -11.8 | 4e-29 | 30/42 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.392×** | -10.4 | 8e-23 | 31/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.512×** | -7.4 | 2e-11 | 30/46 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -7.2 | 1e-10 | 27/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.530×** | -6.8 | 1e-09 | 25/45 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.580×** | -6.0 | 2e-07 | 23/46 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -5.0 | 6e-05 | 20/47 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.436×** | -4.8 | 1e-04 | 13/42 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.684×** | -4.2 | 0.002 | 20/47 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.714×** | -3.7 | 0.011 | 11/47 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -3.7 | 0.011 | 14/45 (NCI-H1792, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.637×** | -3.6 | 0.017 | 10/48 (NCI-H460, SNU-1, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.020 | 11/47 (HS-578T, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.024 | 14/45 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.036 | 17/47 (NCI-H1792, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.755×** | -3.0 | 0.094 | 12/47 (HCT15, AsPC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0278× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0806× (z -12.4) |
| [[PANC-1 (line)]] | alt | 11.2 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -11.3) |
| [[HOP62 (line)]] | alt | 8.24 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.130× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 17.8 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +12.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -9.2) |
| [[SW1417 (line)]] | alt | 8.22 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +10.2) | — |
| [[SW480 (line)]] | alt | 5.34 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +14.8) | — |
| [[LoVo (line)]] | wt | 6.83 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.0858× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +12.6) | — |
| [[A498 (line)]] | wt | 6.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +13.7) | — |
| [[A549 (line)]] | wt | 7.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 9.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 9.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0431× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 7.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.58× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 5.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +10.4) | — |
| [[J82 (line)]] | alt | 8.70 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0933× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 8.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 2.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 3.91 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0544× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 3.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +14.4) | — |
| [[RKO (line)]] | wt | 4.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 6.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.02× (z +8.6) | — |
| [[SW48 (line)]] | wt | 6.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +9.1) | — |
| [[A-427 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.75 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[GPR137]] | +0.72 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.71 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[SIAH2-AS1]] | +0.71 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.70 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[FAM174B]] | +0.70 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SUMO2P17]] | +0.70 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SAXO1]] | +0.69 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.69 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[C2orf49-DT]] | +0.69 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[QRICH2]] | +0.68 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.62 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[RRP1B]] | -0.60 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIPOX's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ERRFI1-DT]] | B | ERRFI1-DT activity raises PIPOX's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without ERRFI1-DT | 0.054 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises PIPOX's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.8, 19.4); signed map (25.5, -2.7). **Vector** length 82.7, 16.5% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +23.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.3 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.7 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | +0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | pipecolic acid and sarcosine oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,950,513-29,057,216 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LPIPOX |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: Lysine catabolism; Peroxisomal protein import; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0Z9](https://www.uniprot.org/uniprotkb/Q9P0Z9) (Peroxisomal sarcosine oxidase):

> Metabolizes sarcosine and L-pipecolic acid.

**Summary**, from NCBI Gene [51268](https://www.ncbi.nlm.nih.gov/gene/51268):

> Enables L-pipecolate oxidase activity and sarcosine oxidase activity. Involved in obsolete L-lysine catabolic process to acetyl-CoA via L-pipecolate. Located in peroxisome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17804) · Entrez [51268](https://www.ncbi.nlm.nih.gov/gene/51268) · UniProt [Q9P0Z9](https://www.uniprot.org/uniprotkb/Q9P0Z9) · Ensembl [ENSG00000179761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179761)

## Data

Gene col 11055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11055); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11055]; `tensor/DDL_lfc|DDL_z.npy` [11055]; `embed/gene_vectors.npy` [11055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11055 or target_col == 11055). Every well: [[PIPOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIPOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
