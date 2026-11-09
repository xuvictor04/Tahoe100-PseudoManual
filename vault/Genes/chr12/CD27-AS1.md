---
symbol: "CD27-AS1"
type: "gene"
col: 13241
ensembl_id: "ENSG00000215039"
name: "CD27 antisense RNA 1"
location: "12p13.31"
module: 26
arm: "+"
pooled_cpm: 10.48
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CD27-AS1

*CD27 antisense RNA 1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.31× (z +24.6, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.589× (z -6.3, q 8e-08, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2E-AS1]] (+0.73, fdr 1e-05), [[SPATA1]] (+0.72, fdr 1e-05), [[RSRP1]] (+0.72, fdr 7e-06); moves opposite to [[COG2]] (-0.65, fdr 3e-04), [[NAA40]] (-0.64, fdr 3e-05), [[TMEM177]] (-0.63, fdr 6e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.31×** | +24.6 | 0e+00 | 44/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.51×** | +14.4 | 2e-44 | 39/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +8.9 | 1e-16 | 36/46 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.6 | 4e-12 | 29/47 (HOP62, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.5 | 6e-12 | 17/22 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.2 | 7e-08 | 24/31 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.7 | 1e-06 | 25/39 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +5.2 | 1e-05 | 22/46 (HOP62, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +5.1 | 2e-05 | 18/47 (C32, A498, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 13/47 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.006 | 21/48 (A549, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 13/46 (KATO III, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.007 | 16/48 (KATO III, A-427, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +3.8 | 0.007 | 10/41 (A498, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +3.7 | 0.009 | 11/26 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.018 | 8/46 (Panc 03.27, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.022 | 9/46 (SW480, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.064 | 9/47 (HOP62, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.098 | 6/44 (HOP62, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -6.3 | 8e-08 | 28/46 (SNU-423, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -6.3 | 8e-08 | 28/47 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.379×** | -6.1 | 3e-07 | 23/44 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.621×** | -5.7 | 2e-06 | 25/48 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.656×** | -5.1 | 5e-05 | 18/46 (NCI-H23, SW 1271, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.714×** | -4.0 | 0.005 | 17/45 (H4, SNU-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.741×** | -3.6 | 0.024 | 13/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.733×** | -3.6 | 0.024 | 19/47 (RKO, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.746×** | -3.5 | 0.028 | 16/45 (Panc 03.27, NCI-H23, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.752×** | -3.3 | 0.056 | 10/46 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.062 | 17/45 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.769×** | -3.1 | 0.082 | 13/45 (LS 180, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.833×** | -3.1 | 0.082 | 12/47 (CFPAC-1, BT-474, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.66 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +16.5) | — |
| [[SW480 (line)]] | alt | 23.6 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +16.6) | [[PH-797804 (drug)]] 5 µM 0.120× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 17.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +15.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[C32 (line)]] | wt | 9.28 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 9.13 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +11.6) | — |
| [[J82 (line)]] | alt | 9.19 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.162× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[LoVo (line)]] | wt | 6.36 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 3.85 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.16× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 9.00 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +12.0) | — |
| [[A549 (line)]] | wt | 3.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 4.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.30× (z +10.9) | — |
| [[H4 (line)]] | wt | 9.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.97× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 5.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 7.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 6.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 8.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 6.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +9.3) | — |
| [[A-172 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E-AS1]] | +0.73 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[SPATA1]] | +0.72 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.71 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MAP7D2]] | +0.71 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.69 | +0.65 / +0.57 | both halves | 1e-05 | same gene group |
| [[ADCY10]] | +0.68 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | +0.68 | +0.58 / +0.53 | both halves | 1e-05 | same gene group |
| [[ARID4B]] | +0.68 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[COLEC11]] | +0.67 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[IKZF4]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[STX17-DT]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG2]] | -0.65 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[NAA40]] | -0.64 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TMEM177]] | -0.63 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[RRP1B]] | -0.63 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[EIF2B3]] | -0.62 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[COMMD2]] | -0.61 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[COA1]] | -0.60 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[AGK]] | -0.60 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[WDR7]] | -0.60 | -0.22 / -0.52 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CD27-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MRC2]] | B | MRC2 activity raises CD27-AS1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without MRC2 | 0.029 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[PROCA1]] | C | PROCA1 activity strengthens CD27-AS1's drug response | lines that do not express PROCA1 (3) vs lines expressing it (45) | the lines without PROCA1 respond 0.49× as strongly (z diff +1.85); strongest at Idarubicin (hydrochloride) 5 µM: 1.31x vs 4.63x (z diff +6.2) | 0.030 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: LTBP3, NUAK1, BLVRA; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (24.8, -17.3); signed map (11.1, 3.0). **Vector** length 71.3, 12.7% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +24.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +14.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.8 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.1 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | CD27 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.31 — chr12:6,439,001-6,451,607 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43896) · Entrez [678655](https://www.ncbi.nlm.nih.gov/gene/678655) · Ensembl [ENSG00000215039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215039)

## Data

Gene col 13241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13241); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13241]; `tensor/DDL_lfc|DDL_z.npy` [13241]; `embed/gene_vectors.npy` [13241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13241 or target_col == 13241). Every well: [[CD27-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CD27-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
