---
symbol: "EDIL3-DT"
type: "gene"
col: 14685
ensembl_id: "ENSG00000250320"
name: "EDIL3 divergent transcript"
location: "5q14.3"
module: 66
arm: "+"
pooled_cpm: 8.65
n_lines_expressing: 25
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# EDIL3-DT

*EDIL3 divergent transcript* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.78× (z +22.0, q 0e+00, up in 15 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.533× (z -5.6, q 1e-05, down in 11 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDIL3]] (+0.64, fdr 7e-06, ⚠ same locus), [[CCDC3]] (+0.63, fdr 1e-05), [[FYB1]] (+0.62, fdr 1e-05), [[KLRK1-AS1]] (+0.62, fdr 2e-05); moves opposite to [[MT1X]] (-0.56, fdr 8e-05), [[ZHX3]] (-0.53, fdr 2e-04), [[COPS8]] (-0.51, fdr 2e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[RPS6KA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.78×** | +22.0 | 0e+00 | 15/18 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.07×** | +15.4 | 0e+00 | 5/7 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.05×** | +14.4 | 1e-44 | 10/13 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.02×** | +13.2 | 7e-38 | 7/9 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +7.5 | 5e-12 | 15/22 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +7.4 | 2e-11 | 11/19 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +7.2 | 4e-11 | 11/22 (C32, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +7.1 | 6e-11 | 12/15 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +5.6 | 1e-06 | 5/14 (A-172, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +5.3 | 6e-06 | 9/21 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +5.1 | 1e-05 | 11/20 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.4 | 6e-04 | 12/22 (HOP62, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.1 | 0.001 | 2/13 (NCI-H460, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.012 | 6/21 (HOP62, C32, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.013 | 4/20 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.029 | 6/19 (A-172, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.046 | 7/22 (NCI-H2030, SNU-423, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.071 | 5/22 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.080 | 6/20 (HOP62, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.533×** | -5.6 | 1e-05 | 11/20 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.657×** | -3.7 | 0.049 | 8/20 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.651×** | -3.5 | 0.049 | 4/23 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.673×** | -3.5 | 0.049 | 7/23 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.673×** | -3.5 | 0.049 | 6/21 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.066 | 8/20 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.3 | 0.091 | 5/23 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.093 | 6/22 (NCI-H1573, SW 1271, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.700×** | -3.2 | 0.093 | 8/20 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.706× | -3.1 | 0.11 | 6/22 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.689× | -3.1 | 0.11 | 8/20 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 6.90 | 0 | 4 (1 ⚠) | — | [[Dexamethasone (drug)]] 5 µM 0.0693× (z -10.4) |
| [[HS-578T (line)]] | alt | 18.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.1× (z +10.6) | — |
| [[A-172 (line)]] | wt | 4.71 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 2.57 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.4× (z +15.3) | — |
| [[CFPAC-1 (line)]] | alt | 6.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 4.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +10.8) | — |
| [[A-427 (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.945 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.731 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDIL3]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CCDC3]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FYB1]] | +0.62 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[KLRK1-AS1]] | +0.62 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[NOVA1]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LRP1B]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MYPN]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[OLR1]] | +0.59 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[ATXN1-AS1]] | +0.58 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[KMO]] | +0.58 | +0.56 / +0.37 | both halves | 7e-05 |  |
| [[SYNPO2]] | +0.58 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[TMC1]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SLC16A2]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | -0.56 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[ZHX3]] | -0.53 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[COPS8]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ERGIC1]] | -0.50 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[PHKA2]] | -0.49 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[NUDCD3]] | -0.49 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[MT2A]] | -0.49 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EDIL3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGFBP7]] | B | IGFBP7 activity strengthens EDIL3-DT's drug response | lines that do not express IGFBP7 (7) vs lines expressing it (15) | the lines without IGFBP7 respond 0.38× as strongly (z diff +1.73); strongest at Idarubicin (hydrochloride) 5 µM: 2.11x vs 7.18x (z diff +4.6) | 0.069 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; target measured in part of the lines; artifact flags |
| [[EDIL3]] | C | EDIL3 activity raises EDIL3-DT's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 3.54× lower at baseline in the lines without EDIL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[CPA4]] | C | CPA4 activity raises EDIL3-DT's level | lines that do not express CPA4 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without CPA4 | 0.051 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6; co-absent with the target |
| [[DOCK10]] | C | DOCK10 activity raises EDIL3-DT's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 2.85× lower at baseline in the lines without DOCK10 | 0.088 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS6KA2]] | B | EDIL3-DT activity raises RPS6KA2's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.58× lower at baseline in the lines without EDIL3-DT | 0.004 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[LNCRNA-IUR]] | B | EDIL3-DT activity raises LNCRNA-IUR's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.23× lower at baseline in the lines without EDIL3-DT | 0.017 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[NPHS1]] | B | EDIL3-DT activity lowers NPHS1's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.27× higher at baseline in the lines without EDIL3-DT | 0.024 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[NHS]] | B | EDIL3-DT activity raises NHS's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 3.76× lower at baseline in the lines without EDIL3-DT | 0.024 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[HSD11B1-AS1]] | B | EDIL3-DT activity raises HSD11B1-AS1's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.33× lower at baseline in the lines without EDIL3-DT | 0.096 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[EDIL3]] | C | EDIL3-DT activity raises EDIL3's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 10.12× lower at baseline in the lines without EDIL3-DT | 0.003 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA; co-absent with the target |
| [[MOXD1]] | C | EDIL3-DT activity raises MOXD1's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 2.65× lower at baseline in the lines without EDIL3-DT | 0.086 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA; co-absent with the target |
| [[CPA4]] | C | EDIL3-DT activity raises CPA4's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without EDIL3-DT | 0.092 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.7, 22.4); signed map (41.0, 18.1). **Vector** length 60.8, 15.9% of its response variance represented; |z| ≥ 3 in 569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +22.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -5.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | EDIL3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.3 — chr5:84,382,424-84,490,765 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40204) · Entrez [105379057](https://www.ncbi.nlm.nih.gov/gene/105379057) · Ensembl [ENSG00000250320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250320)

## Data

Gene col 14685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14685); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14685]; `tensor/DDL_lfc|DDL_z.npy` [14685]; `embed/gene_vectors.npy` [14685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14685 or target_col == 14685). Every well: [[EDIL3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDIL3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
