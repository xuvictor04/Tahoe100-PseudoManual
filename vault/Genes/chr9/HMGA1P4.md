---
symbol: "HMGA1P4"
type: "gene"
col: 13977
ensembl_id: "ENSG00000234705"
name: "high mobility group AT-hook 1 pseudogene 4"
location: "9q34.11"
module: 35
arm: "+"
pooled_cpm: 18.38
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# HMGA1P4

*high mobility group AT-hook 1 pseudogene 4* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +11.1, q 4e-26, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.368× (z -10.1, q 4e-21, down in 36 of 44 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.397× (z -9.2, q 9e-18, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL45P2]] (+0.68, fdr 7e-06), [[SLC16A1-AS1]] (+0.67, fdr 1e-05), [[RHBDD3]] (+0.64, fdr 9e-05); moves opposite to [[LIX1L]] (-0.62, fdr 3e-05), [[RAB3A]] (-0.62, fdr 2e-04), [[FOXO6]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[EIF5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +11.1 | 4e-26 | 33/43 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.6 | 9e-09 | 26/40 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.3 | 7e-08 | 31/45 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.005 | 16/43 (LS 180, COLO 205, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.008 | 19/45 (SW480, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.028 | 19/44 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.057 | 14/44 (HEC-1-A, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.13 | 12/45 (Hs 766T, A-427, …) | all doses, flat | position effect removed |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.42× | +3.0 | 0.16 | 8/44 (NCI-H460, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.368×** | -10.1 | 4e-21 | 36/44 (PANC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.397×** | -9.2 | 9e-18 | 35/44 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.397×** | -9.0 | 6e-17 | 32/41 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.441×** | -8.2 | 3e-14 | 32/44 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.574×** | -7.9 | 3e-13 | 28/43 (BT-474, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.476×** | -7.4 | 1e-11 | 32/44 (BT-474, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.492×** | -7.1 | 7e-11 | 30/44 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.530×** | -6.4 | 1e-08 | 28/42 (COLO 205, BT-474, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.534×** | -6.2 | 3e-08 | 28/44 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.686×** | -5.4 | 5e-06 | 27/45 (RKO, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.579×** | -5.3 | 6e-06 | 24/43 (COLO 205, Panc 03.27, …) | top dose only | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.634×** | -4.6 | 2e-04 | 26/44 (BT-474, SW1417, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.427×** | -4.5 | 3e-04 | 20/42 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -3.6 | 0.012 | 14/42 (SK-MEL-2, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.520×** | -3.4 | 0.022 | 12/21 (HEC-1-A, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.550×** | -3.1 | 0.052 | 16/43 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.731×** | -3.1 | 0.052 | 18/43 (RPMI-7951, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 47.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.257× (z -8.5) |
| [[LoVo (line)]] | wt | 19.9 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.156× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.235× (z -9.8) |
| [[BT-474 (line)]] | alt | 59.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 84.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -13.6) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 41.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -11.4) |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0671× (z -15.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.215× (z -9.3) |
| [[SW480 (line)]] | alt | 19.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -10.5) |
| [[A-427 (line)]] | wt | 19.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0822× (z -13.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 32.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 11.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 8.94× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.1) ⚠ cell-cycle shift, explains ~70% of this change |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.5) ⚠ cell-cycle shift, explains ~70% of this change |
| [[C32 (line)]] | wt | 7.16 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0857× (z -8.5) |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -8.8) |
| [[J82 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -9.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H23 (line)]] | alt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -9.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[RPMI-7951 (line)]] | alt | 7.93 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0671× (z -8.6) |
| [[SW48 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0649× (z -10.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL45P2]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SLC16A1-AS1]] | +0.67 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RHBDD3]] | +0.64 | +0.64 / +0.36 | both halves | 9e-05 |  |
| [[CDK12]] | +0.64 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ENOX2]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[WDR81]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MRM1]] | +0.63 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | +0.63 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[TLK2]] | +0.62 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SP2-AS1]] | +0.62 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[NINJ2]] | +0.62 | +0.54 / +0.23 | both halves | 5e-04 |  |
| [[SMG1-DT]] | +0.61 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIX1L]] | -0.62 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[RAB3A]] | -0.62 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[FOXO6]] | -0.59 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[ALAD]] | -0.59 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[GNAI2]] | -0.58 | -0.52 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[ARRB2]] | -0.56 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[FCHO1]] | -0.55 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[CEP131]] | -0.55 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[PLPPR2]] | -0.55 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[HLTF]] | -0.54 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[PJA2]] | -0.54 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[HMGN3]] | -0.54 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.54 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HMGA1P4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PAX8]] | B | PAX8 activity raises HMGA1P4's level | lines that do not express PAX8 (34) vs lines expressing it (16) | 1.83× lower at baseline in the lines without PAX8 | 0.044 | ⚠ within organs, on part of the lines; also absent: FGF19, RGPD2, BMP10 |
| [[TOP2B]] | B | TOP2B activity lowers HMGA1P4's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ENOX2]] | C | ENOX2's natural level strengthens HMGA1P4's drug response | ENOX2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.02; direction clear | 0.012 | ⚠ tissue can mimic it; precision caveat |
| [[RAB3A]] | C | RAB3A's natural level weakens HMGA1P4's drug response | RAB3A's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.12; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF5]] | C | HMGA1P4 activity raises EIF5's level | lines that do not express HMGA1P4 (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without HMGA1P4 | 0.088 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, CASP8, SP100 |
| cells under [[Pemigatinib (drug)]] 5 µM | C | HMGA1P4 activity raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | lines that do not express HMGA1P4 (3) vs lines expressing it (45) | the lines without HMGA1P4: 0.73× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, CASP8, SP100 |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-2.1, 9.0); signed map (26.0, -28.4). **Vector** length 100.0, 25.5% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.2 | -2.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group AT-hook 1 pseudogene 4 |
| Locus type | pseudogene |
| Location | 9q34.11 — chr9:128,663,129-128,684,493 (-) |
| Ensembl biotype | lncRNA |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39093) · Entrez [100506080](https://www.ncbi.nlm.nih.gov/gene/100506080) · Ensembl [ENSG00000234705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234705)

## Data

Gene col 13977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13977); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13977]; `tensor/DDL_lfc|DDL_z.npy` [13977]; `embed/gene_vectors.npy` [13977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13977 or target_col == 13977). Every well: [[HMGA1P4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGA1P4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
