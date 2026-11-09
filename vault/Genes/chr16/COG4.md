---
symbol: "COG4"
type: "gene"
col: 2312
ensembl_id: "ENSG00000103051"
name: "component of oligomeric golgi complex 4"
location: "16q22.1"
module: 28
arm: "+"
pooled_cpm: 29.99
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# COG4

*component of oligomeric golgi complex 4* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.09× (z +6.6, q 2e-08, up in 5 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 1.30× (z +5.4, q 2e-05, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.614× (z -9.6, q 3e-19, down in 33 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.626× (z -9.6, q 3e-19, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD52]] (+0.65, fdr 1e-05), [[PHC3]] (+0.65, fdr 7e-06), [[ERMARD]] (+0.64, fdr 1e-05); moves opposite to [[CMTM8]] (-0.61, fdr 2e-05), [[DOCK9]] (-0.59, fdr 1e-05), [[EVI5]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KANK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.6 | 2e-08 | 5/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 2e-05 | 22/48 (BT-474, RKO, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.3 | 2e-05 | 19/47 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.8 | 2e-04 | 18/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.6 | 5e-04 | 17/48 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | **1.21×** | +3.8 | 0.012 | 15/46 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.7 | 0.018 | 14/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.020 | 17/47 (NCI-H2030, RKO, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.19× | +3.6 | 0.024 | 10/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.4 | 0.032 | 9/48 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.034 | 17/47 (NCI-H23, RKO, …) | all doses, flat | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.055 | 8/48 (SW480, SW48, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.077 | 7/48 (HOP62, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.095 | 6/47 (SW480, H4, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.095 | 17/45 (C-33 A, NCI-H2347, …) | all doses, flat | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -9.6 | 3e-19 | 33/47 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -9.6 | 3e-19 | 36/48 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -9.4 | 9e-19 | 32/48 (HCT15, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.681×** | -7.9 | 5e-13 | 30/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -7.1 | 1e-10 | 26/48 (SNU-423, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -6.6 | 4e-09 | 24/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.730×** | -6.1 | 1e-07 | 22/48 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.753×** | -5.8 | 5e-07 | 23/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -5.7 | 7e-07 | 25/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.854× | -4.6 | 3e-04 | 16/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.806×** | -4.4 | 6e-04 | 15/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.831×** | -3.8 | 0.007 | 15/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.8 | 0.007 | 16/48 (HCT15, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.008 | 13/47 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.834× | -3.7 | 0.008 | 16/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.827×** | -3.7 | 0.009 | 16/47 (C32, A-172, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.727×** | -3.4 | 0.020 | 16/48 (MIA PaCa-2, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.058 | 10/48 (Hs 766T, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.866× | -2.9 | 0.087 | 14/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.821×** | -2.9 | 0.099 | 12/48 (A-427, Panc 03.27, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 58.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.320× (z -13.6) |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.265× (z -9.0) |
| [[HOP62 (line)]] | alt | 35.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -11.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.286× (z -8.6) |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 2 | — | [[Sonidegib (drug)]] 5 µM 0.0923× (z -10.3) |
| [[SNU-423 (line)]] | alt | 27.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.267× (z -10.2) |
| [[SW48 (line)]] | wt | 16.3 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0806× (z -10.3) |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.189× (z -11.1) |
| [[H4 (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 39.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.379× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -9.8) ⚠ toxic |
| [[RKO (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -10.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD52]] | +0.65 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[PHC3]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ERMARD]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[LMBRD2]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[COQ9]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ZNF429]] | +0.60 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[COQ6]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[STAMBP]] | +0.58 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[NDUFS1]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.58 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[MKS1]] | +0.58 | +0.69 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTM8]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DOCK9]] | -0.59 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[EVI5]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TPST2]] | -0.58 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[LMBR1]] | -0.58 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[PRR5-ARHGAP8]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CDYL]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[PACC1]] | -0.55 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[PRR5]] | -0.55 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[TRABD]] | -0.54 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[LHX4]] | -0.54 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[ST6GALNAC6-1]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KANK1]] | B | KANK1 activity lowers COG4's level | lines that do not express KANK1 (12) vs lines expressing it (38) | 1.19× higher at baseline in the lines without KANK1 | 0.081 | ⚠ within organs, on part of the lines |
| [[TOP1]] | B | TOP1 activity lowers COG4's level | compounds that target TOP1: 2 of 3 raise it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.4, 5.0); signed map (10.3, -22.7). **Vector** length 86.5, 17.5% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -9.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.8 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,480,568-70,523,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COD1, DKFZP586E1519 |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Reactome | 9 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9E3](https://www.uniprot.org/uniprotkb/Q9H9E3) (Conserved oligomeric Golgi complex subunit 4):

> Required for normal Golgi function. Plays a role in SNARE-pin assembly and Golgi-to-ER retrograde transport via its interaction with SCFD1.

**Summary**, from NCBI Gene [25839](https://www.ncbi.nlm.nih.gov/gene/25839):

> The protein encoded by this gene is a component of an oligomeric protein complex involved in the structure and function of the Golgi apparatus. Defects in this gene may be a cause of congenital disorder of glycosylation type IIj. Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:18620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18620) · Entrez [25839](https://www.ncbi.nlm.nih.gov/gene/25839) · UniProt [Q9H9E3](https://www.uniprot.org/uniprotkb/Q9H9E3) · Ensembl [ENSG00000103051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103051)

## Data

Gene col 2312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2312); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2312]; `tensor/DDL_lfc|DDL_z.npy` [2312]; `embed/gene_vectors.npy` [2312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2312 or target_col == 2312). Every well: [[COG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
