---
symbol: "GABPA"
type: "gene"
col: 7832
ensembl_id: "ENSG00000154727"
name: "GA binding protein transcription factor subunit alpha"
location: "21q21.3"
module: 15
arm: "+"
pooled_cpm: 47.58
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GABPA

*GA binding protein transcription factor subunit alpha* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +17.2, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.638× (z -10.0, q 8e-21, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM48]] (+0.68, fdr 2e-05), [[AHI1-DT]] (+0.65, fdr 4e-05), [[ZBED5-AS1]] (+0.61, fdr 5e-05); moves opposite to [[ZFYVE28]] (-0.58, fdr 1e-04), [[PBX4]] (-0.52, fdr 2e-04), [[CMIP]] (-0.52, fdr 9e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +17.2 | 0e+00 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +14.0 | 7e-42 | 36/48 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +13.9 | 1e-41 | 39/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +12.0 | 6e-31 | 43/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +9.8 | 2e-20 | 37/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +7.1 | 1e-10 | 28/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +6.8 | 7e-10 | 27/48 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +6.6 | 3e-09 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.34×** | +6.5 | 4e-09 | 27/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.8 | 3e-07 | 22/43 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.2 | 8e-06 | 24/43 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.25×** | +5.0 | 3e-05 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 9e-05 | 22/47 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.2 | 0.001 | 22/47 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.1 | 0.001 | 14/48 (A-172, RKO, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.004 | 19/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.5 | 0.013 | 19/48 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.016 | 11/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.061 | 5/48 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.064 | 7/48 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -10.0 | 8e-21 | 41/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.660×** | -9.2 | 7e-18 | 38/48 (SW1417, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.687×** | -8.4 | 1e-14 | 43/48 (LOX-IMVI, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -8.2 | 5e-14 | 35/48 (CHP-212, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.705×** | -7.8 | 8e-13 | 33/48 (LS 180, A-172, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.706×** | -7.7 | 1e-12 | 31/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -7.2 | 4e-11 | 34/48 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.637×** | -5.2 | 1e-05 | 24/48 (SNU-1, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.804×** | -4.9 | 8e-05 | 23/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.839× | -3.7 | 0.010 | 16/48 (SNU-423, Panc 03.27, …) | rises with dose | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.857× | -3.4 | 0.031 | 12/48 (SW1417, SNU-423, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.754×** | -3.3 | 0.050 | 15/48 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.826× | -3.0 | 0.10 | 10/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.2 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +16.0) | — |
| [[SW480 (line)]] | alt | 63.8 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +19.5) | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 46.0 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +20.3) | — |
| [[AsPC-1 (line)]] | alt | 43.7 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.48× (z +17.3) | — |
| [[BT-474 (line)]] | alt | 35.2 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 43.4 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.15× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 45.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.23× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 52.1 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.439× (z -8.7) |
| [[A-172 (line)]] | wt | 52.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.5) | — |
| [[A-427 (line)]] | wt | 60.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.61× (z +11.5) | — |
| [[A498 (line)]] | wt | 40.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +11.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[C-33 A (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -15.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.17× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 64.6 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.295× (z -8.7) |
| [[HCT15 (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 58.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 39.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.0) | — |
| [[KATO III (line)]] | alt | 32.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +10.9) | — |
| [[LoVo (line)]] | wt | 49.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.32× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 72.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.72× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 57.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 46.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 55.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 39.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.2) | — |
| [[SW48 (line)]] | wt | 47.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.11× (z +9.5) | — |
| [[A549 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM48]] | +0.68 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[AHI1-DT]] | +0.65 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[ZBED5-AS1]] | +0.61 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[CDNF]] | +0.61 | +0.29 / +0.51 | both halves | 3e-04 |  |
| [[DICER1-AS1]] | +0.61 | +0.42 / +0.36 | both halves | 9e-05 |  |
| [[IDNK]] | +0.60 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[HOXB7]] | +0.60 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | +0.59 | +0.34 / +0.39 | both halves | 1e-04 |  |
| [[USP38-DT]] | +0.59 | +0.41 / +0.31 | both halves | 2e-04 |  |
| [[UFC1]] | +0.58 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[C1D]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SEC24B-AS1]] | +0.58 | +0.35 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE28]] | -0.58 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[PBX4]] | -0.52 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[CMIP]] | -0.52 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[SH3PXD2B]] | -0.51 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[EHD4]] | -0.51 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[CLTCL1]] | -0.50 | -0.23 / -0.37 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises GABPA's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises GABPA's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.0, 18.8); signed map (29.0, -9.2). **Vector** length 91.1, 21.6% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.3 | +14.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.6 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -10.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.8 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | GA binding protein transcription factor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:25,734,570-25,772,460 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E4TF1A, NFT2, NRF2, E4TF1-60, NRF2A |
| Gene groups (HGNC) | ETS transcription factor family; GA binding protein transcription factor subunits |
| Reactome | 3 pathways, smallest: Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06546](https://www.uniprot.org/uniprotkb/Q06546) (GA-binding protein alpha chain):

> Transcription factor capable of interacting with purine rich repeats (GA repeats). Positively regulates transcription of transcriptional repressor RHIT/ZNF205.; (Microbial infection) Necessary for the expression of the Adenovirus E4 gene.

**Summary**, from NCBI Gene [2551](https://www.ncbi.nlm.nih.gov/gene/2551):

> This gene encodes one of three GA-binding protein transcription factor subunits which functions as a DNA-binding subunit. Since this subunit shares identity with a subunit encoding the nuclear respiratory factor 2 gene, it is likely involved in activation of cytochrome oxidase expression and nuclear control of mitochondrial function. This subunit also shares identity with a subunit constituting the transcription factor E4TF1, responsible for expression of the adenovirus E4 gene. Because of its …

**Accessions** — [HGNC:4071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4071) · Entrez [2551](https://www.ncbi.nlm.nih.gov/gene/2551) · UniProt [Q06546](https://www.uniprot.org/uniprotkb/Q06546) · Ensembl [ENSG00000154727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154727)

## Data

Gene col 7832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7832); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7832]; `tensor/DDL_lfc|DDL_z.npy` [7832]; `embed/gene_vectors.npy` [7832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7832 or target_col == 7832). Every well: [[GABPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
