---
symbol: "LRIG3-DT"
type: "gene"
col: 15041
ensembl_id: "ENSG00000257443"
name: "LRIG3 divergent transcript"
location: "12q14.1"
module: 10
arm: "+"
pooled_cpm: 3.52
n_lines_expressing: 44
n_dd_up: 28
n_dd_down: 29
n_dd_up_clean: 25
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LRIG3-DT

*LRIG3 divergent transcript* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.38× (z +22.9, q 0e+00, up in 26 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.308× (z -10.3, q 6e-22, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00466]] (+0.64, fdr 2e-05), [[KLRK1-AS1]] (+0.59, fdr 5e-05), [[LRRIQ3]] (+0.58, fdr 5e-05); moves opposite to [[PPIL2]] (-0.51, fdr 2e-04), [[DNAJC24]] (-0.50, fdr 2e-04), [[ASCC2]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ID2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.38×** | +22.9 | 0e+00 | 26/27 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.86×** | +8.8 | 3e-16 | 20/24 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +8.5 | 5e-15 | 24/38 (SHP-77, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +7.5 | 8e-12 | 21/31 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.17×** | +6.8 | 1e-09 | 23/40 (A498, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.5 | 8e-09 | 16/38 (A-172, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +6.5 | 8e-09 | 20/39 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +6.4 | 1e-08 | 16/30 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.06×** | +6.3 | 2e-08 | 18/35 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +6.0 | 1e-07 | 20/37 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.87×** | +5.5 | 2e-06 | 15/38 (LoVo, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +5.4 | 4e-06 | 12/32 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +5.1 | 1e-05 | 18/36 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +4.9 | 4e-05 | 0/5 | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.86×** | +4.8 | 6e-05 | 10/31 (LoVo, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.72×** | +4.7 | 8e-05 | 14/34 (KATO III, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.308×** | -10.3 | 6e-22 | 30/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.350×** | -9.1 | 2e-17 | 26/39 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -6.8 | 2e-09 | 23/35 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -6.2 | 9e-08 | 18/24 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.501×** | -6.0 | 2e-07 | 19/32 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.620×** | -5.9 | 4e-07 | 23/37 (LS 180, SNU-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.512×** | -5.8 | 5e-07 | 19/35 (HT-29, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.524×** | -5.6 | 1e-06 | 17/36 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.552×** | -5.2 | 2e-05 | 11/39 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.546×** | -5.1 | 2e-05 | 13/33 (LS 180, Hs 766T, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.449×** | -5.0 | 3e-05 | 16/39 (NCI-H2030, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.572×** | -4.9 | 6e-05 | 14/40 (LS 180, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -4.8 | 6e-05 | 13/32 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.589×** | -4.6 | 2e-04 | 13/33 (LS 180, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.594×** | -4.5 | 2e-04 | 11/40 (NCI-H2030, PANC-1, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -4.4 | 3e-04 | 15/27 (PANC-1, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -4.4 | 4e-04 | 18/35 (PANC-1, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.413×** | -4.0 | 0.002 | 14/29 (LS 180, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.634×** | -4.0 | 0.002 | 13/26 (PANC-1, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.92 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.0314× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0799× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 8.38 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0278× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 8.68 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0736× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0929× (z -9.5) |
| [[A498 (line)]] | wt | 5.48 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0164× (z -15.1) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 5.11 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0781× (z -10.1) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 8.68 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.83× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.0697× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 2.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +8.8) | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0922× (z -10.8) |
| [[Hs 766T (line)]] | wt | 7.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +9.5) | — |
| [[LoVo (line)]] | wt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.7× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 6.26 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0295× (z -12.7) |
| [[SNU-423 (line)]] | alt | 4.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 1.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +8.9) | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.453 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00466]] | +0.64 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[KLRK1-AS1]] | +0.59 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[LRRIQ3]] | +0.58 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[SPAG17]] | +0.58 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[LINC01122]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[FAM184A]] | +0.58 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[KATNAL2]] | +0.57 | +0.72 / +0.40 | both halves | 4e-05 |  |
| [[F8]] | +0.56 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[CRB1]] | +0.56 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[GALNT7-DT]] | +0.56 | +0.68 / +0.31 | both halves | 2e-04 | same gene group |
| [[ABCA17P]] | +0.55 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[LINC03036]] | +0.55 | +0.63 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL2]] | -0.51 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[DNAJC24]] | -0.50 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ASCC2]] | -0.49 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[MTG1]] | -0.48 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRIG3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers LRIG3-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | LRIG3-DT activity raises ID2-AS1's level | lines that do not express LRIG3-DT (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without LRIG3-DT | 0.082 | ⚠ within organs, on part of the lines; also absent: LRIG3, MID1, CPEB2; maybe low, not absent |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | LRIG3-DT's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | LRIG3-DT's natural level across 42 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.0, 32.1); signed map (34.4, -8.5). **Vector** length 54.0, 8.70% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +22.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +5.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -9.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | +6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | LRIG3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q14.1 — chr12:58,920,639-59,065,312 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55476) · Entrez [105369791](https://www.ncbi.nlm.nih.gov/gene/105369791) · Ensembl [ENSG00000257443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257443)

## Data

Gene col 15041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15041); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15041]; `tensor/DDL_lfc|DDL_z.npy` [15041]; `embed/gene_vectors.npy` [15041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15041 or target_col == 15041). Every well: [[LRIG3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRIG3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
