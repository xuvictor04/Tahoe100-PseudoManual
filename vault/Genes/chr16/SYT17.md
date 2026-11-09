---
symbol: "SYT17"
type: "gene"
col: 2379
ensembl_id: "ENSG00000103528"
name: "synaptotagmin 17"
location: "16p12.3"
module: 128
arm: "+"
pooled_cpm: 19.87
n_lines_expressing: 37
n_dd_up: 2
n_dd_down: 41
n_dd_up_clean: 2
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# SYT17

*synaptotagmin 17* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.29× (z +4.0, q 0.036, up in 15 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.15×, NCI-H460 2.83×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.217× (z -33.1, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (65 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 35 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP20DC-AS1]] (+0.51, fdr 2e-04), [[KANSL1]] (+0.50, fdr 5e-05), [[TLE2]] (+0.49, fdr 1e-05); moves opposite to [[IPO9]] (-0.48, fdr 1e-04), [[INTS7]] (-0.44, fdr 3e-04), [[FAM106A]] (-0.44, fdr 2e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CELSR1]] → it (grade B ⚠); 2 go from it, the strongest it → [[CELSR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2379.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 2.15×, NCI-H460 2.83×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.036 | 15/35 (SW480, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.036 | 17/34 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.055 | 11/34 (A-427, KATO III, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.091 | 7/35 (PANC-1, A549, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.25× | +3.2 | 0.14 | 9/35 (Hs 766T, BT-474, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.14 | 9/35 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.22× | +3.0 | 0.21 | 3/33 (SW480, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.217×** | -33.1 | 0e+00 | 33/34 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.204×** | -23.4 | 0e+00 | 34/35 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.251×** | -21.1 | 0e+00 | 32/35 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.252×** | -21.1 | 0e+00 | 33/35 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.268×** | -20.2 | 0e+00 | 31/34 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.303×** | -18.3 | 0e+00 | 29/34 (AsPC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.303×** | -18.3 | 0e+00 | 27/35 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.315×** | -17.7 | 0e+00 | 33/34 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.328×** | -17.1 | 0e+00 | 32/32 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.359×** | -15.7 | 0e+00 | 30/34 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.446×** | -11.9 | 8e-31 | 25/31 (LoVo, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.503×** | -10.5 | 4e-24 | 25/34 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.273×** | -10.4 | 1e-23 | 27/35 (NCI-H1573, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -8.9 | 3e-17 | 29/34 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.583×** | -8.2 | 6e-15 | 25/33 (AsPC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -7.4 | 3e-12 | 22/34 (C32, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.627×** | -7.1 | 3e-11 | 22/34 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -6.1 | 3e-08 | 21/33 (A-172, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.664×** | -5.9 | 9e-08 | 20/34 (NCI-H1792, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 68.2 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0512× (z -38.6) |
| [[LoVo (line)]] | wt | 31.2 | 1 (1 ⚠) | 11 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.100× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -21.5) |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -20.4) |
| [[AsPC-1 (line)]] | alt | 50.0 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -34.6) |
| [[BT-474 (line)]] | alt | 101 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0648× (z -32.5) |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0914× (z -19.6) |
| [[A549 (line)]] | wt | 42.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -27.2) |
| [[CFPAC-1 (line)]] | alt | 39.2 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -25.4) |
| [[SW480 (line)]] | alt | 16.6 | 0 | 9 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0726× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.128× (z -16.4) |
| [[A-172 (line)]] | wt | 22.4 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0550× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -16.4) |
| [[J82 (line)]] | alt | 33.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -24.7) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 33.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -21.5) |
| [[C32 (line)]] | wt | 26.3 | 0 | 7 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0976× (z -11.9) |
| [[KATO III (line)]] | alt | 30.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.1) |
| [[HCT15 (line)]] | alt | 42.4 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0747× (z -15.5) |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -26.8) |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -10.9) |
| [[A-427 (line)]] | wt | 25.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.4) |
| [[HOP62 (line)]] | alt | 9.77 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.2) |
| [[SW48 (line)]] | wt | 23.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 6.35 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0463× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 12.2 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.223× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0411× (z -14.5) |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 34 of them with an alert (⚠; 34 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP20DC-AS1]] | +0.51 | +0.29 / +0.54 | both halves | 2e-04 |  |
| [[KANSL1]] | +0.50 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[TLE2]] | +0.49 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ZMAT5]] | +0.48 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[ADAP2]] | +0.48 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[DNASE1]] | +0.47 | +0.19 / +0.48 | ⚠ not reproduced | 8e-04 |  |
| [[PACRG]] | +0.47 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[ACP6]] | +0.47 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[L3MBTL1]] | +0.47 | +0.31 / +0.47 | both halves | 2e-04 |  |
| [[ST6GALNAC2]] | +0.46 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[CASKIN1]] | +0.46 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[ST8SIA6-AS1]] | +0.45 | +0.35 / +0.32 | both halves | 2e-04 |  |
| [[TBX1]] | +0.45 | +0.33 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.48 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[INTS7]] | -0.44 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[FAM106A]] | -0.44 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[MTG1]] | -0.43 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[POLM]] | -0.42 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[EFR3A]] | -0.41 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[FARSB]] | -0.41 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[ZNF22]] | -0.41 | -0.25 / -0.41 | both halves | 4e-04 |  |
| [[YEATS4]] | -0.41 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[MRPL42]] | -0.41 | -0.24 / -0.44 | both halves | 4e-04 |  |
| [[SPTLC3]] | -0.40 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[AGK]] | -0.40 | -0.20 / -0.50 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR1]] | B | CELSR1 activity raises SYT17's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 3.18× lower at baseline in the lines without CELSR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR1]] | B | SYT17 activity raises CELSR1's level | lines that do not express SYT17 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without SYT17 | 0.002 | ⚠ within organs, on part of the lines; also absent: SEPTIN3, STOX2, ULK2; maybe low, not absent |
| cells under [[Neratinib (drug)]] 5 µM | B | SYT17 activity raises the cells' numbers under Neratinib 5 µM (protects the cells) | lines that do not express SYT17 (13) vs lines expressing it (35) | the lines without SYT17: 0.91× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SEPTIN3, STOX2, ULK2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.398). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.5, 27.4); signed map (34.5, 1.4). **Vector** length 80.6, 18.5% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.6 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | -0.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -15.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -21.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -23.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,167,971-19,268,332 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Syt-17 |
| Gene groups (HGNC) | Synaptotagmins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSW7](https://www.uniprot.org/uniprotkb/Q9BSW7) (Synaptotagmin-17):

> Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [51760](https://www.ncbi.nlm.nih.gov/gene/51760):

> Predicted to enable SNARE binding activity; calcium ion sensor activity; and calcium-dependent phospholipid binding activity. Involved in positive regulation of dendrite extension and regulation of postsynaptic neurotransmitter receptor internalization. Is active in glutamatergic synapse and postsynapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24119) · Entrez [51760](https://www.ncbi.nlm.nih.gov/gene/51760) · UniProt [Q9BSW7](https://www.uniprot.org/uniprotkb/Q9BSW7) · Ensembl [ENSG00000103528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103528)

## Data

Gene col 2379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2379); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2379]; `tensor/DDL_lfc|DDL_z.npy` [2379]; `embed/gene_vectors.npy` [2379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2379 or target_col == 2379). Every well: [[SYT17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
