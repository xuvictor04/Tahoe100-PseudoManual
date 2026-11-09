---
symbol: "LYRM4"
type: "gene"
col: 13173
ensembl_id: "ENSG00000214113"
name: "LYR motif containing 4"
location: "6p25.1"
module: 5
arm: "+"
pooled_cpm: 54.71
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# LYRM4

*LYR motif containing 4* — 6p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.52× (z +19.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.727× (z -6.9, q 3e-09, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARS2]] (+0.76, fdr 7e-06), [[ATR]] (+0.69, fdr 7e-06), [[POLR3E]] (+0.69, fdr 7e-06); moves opposite to [[RAB30]] (-0.55, fdr 1e-05), [[KMT2E]] (-0.55, fdr 1e-05), [[ILK]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.52×** | +19.9 | 0e+00 | 44/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +16.3 | 0e+00 | 40/48 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.10×** | +16.0 | 0e+00 | 46/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +15.0 | 0e+00 | 39/47 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +14.7 | 0e+00 | 42/48 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.89×** | +13.7 | 1e-40 | 44/48 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.00×** | +10.7 | 1e-24 | 44/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +9.8 | 8e-21 | 33/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.37×** | +9.7 | 1e-20 | 37/43 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +9.4 | 2e-19 | 36/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.49×** | +8.5 | 8e-16 | 30/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.6 | 1e-12 | 31/48 (HOP62, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +6.7 | 9e-10 | 24/49 (J82, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.34×** | +6.2 | 2e-08 | 25/48 (HOP62, AsPC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +6.0 | 1e-07 | 29/48 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +5.8 | 3e-07 | 24/47 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.58×** | +5.7 | 3e-07 | 25/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 3e-05 | 23/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Penfluridol (drug)]] 5 µM |  | 1.19× | +3.6 | 0.007 | 15/47 (A498, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.010 | 13/47 (HEC-1-A, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.727×** | -6.9 | 3e-09 | 30/48 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.756×** | -6.1 | 3e-07 | 28/47 (SHP-77, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -6.0 | 4e-07 | 27/48 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.795×** | -5.0 | 8e-05 | 24/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **0.827×** | -4.1 | 0.004 | 18/48 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.843× | -3.7 | 0.016 | 19/48 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.837× | -3.7 | 0.016 | 20/43 (A-427, C-33 A, …) | two highest doses | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.850× | -3.5 | 0.026 | 16/47 (KATO III, HepG2/C3A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.845× | -3.5 | 0.026 | 15/47 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.896× | -3.4 | 0.037 | 10/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.861× | -3.3 | 0.056 | 8/47 (NCI-H2030, LoVo, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.780×** | -3.2 | 0.077 | 12/48 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 60.4 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.28× (z +17.5) | — |
| [[HEC-1-A (line)]] | alt | 54.5 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 63.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.88× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 55.6 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.231× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 27.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.60× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 101 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -16.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 71.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.19× (z +11.8) | — |
| [[H4 (line)]] | wt | 48.7 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 33.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +14.6) | — |
| [[J82 (line)]] | alt | 108 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.77× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 66.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.248× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 111 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 17.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 68.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 97.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 67.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 49.6 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 60.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.62× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 45.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +10.3) | — |
| [[A-172 (line)]] | wt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 35.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 42.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 65.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 96.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARS2]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ATR]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[POLR3E]] | +0.69 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[RPUSD4]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[RBM19]] | +0.67 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[MACROD1]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[NDUFAF2]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[PRDM15]] | +0.65 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[WDR4]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.63 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ANAPC1]] | +0.63 | +0.63 / +0.57 | both halves | 9e-06 | same gene group |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ILK]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[BPNT1]] | -0.54 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[RAB33B]] | -0.54 | -0.60 / -0.44 | both halves | 3e-05 | STRING 553 |
| [[COMMD3]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[LINC00888-1]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[TUFT1]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity lowers LYRM4's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.60× higher at baseline in the lines without MPZL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[ADCY3]] | B | ADCY3 activity raises LYRM4's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.54× lower at baseline in the lines without ADCY3 | 0.007 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[TOP2A]] | B | TOP2A activity lowers LYRM4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTC28]] | B | TTC28 activity raises LYRM4's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without TTC28 | 0.036 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[CDC42BPG]] | B | CDC42BPG activity lowers LYRM4's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.37× higher at baseline in the lines without CDC42BPG | 0.038 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[MTHFD1L]] | C | MTHFD1L activity raises LYRM4's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.49× lower at baseline in the lines without MTHFD1L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-11.6, -33.2); signed map (-0.9, -51.3). **Vector** length 120, 36.0% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +16.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +16.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.4 | +13.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +9.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +5.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.3 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.6 | -6.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LYR motif containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.1 — chr6:5,103,629-5,260,950 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-203, ISD11; previously C6orf149 |
| Gene groups (HGNC) | LYR motif containing; MicroRNA protein coding host genes; Mitochondrial iron-sulfur assembly components |
| Reactome | 6 pathways, smallest: Mitochondrial iron-sulfur cluster biogenesis; Maturation of TCA enzymes and regulation of TCA cycle; Complex III assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD34](https://www.uniprot.org/uniprotkb/Q9HD34) (LYR motif-containing protein 4):

> Stabilizing factor, of the core iron-sulfur cluster (ISC) assembly complex, that regulates, in association with NDUFAB1, the stability and the cysteine desulfurase activity of NFS1 and participates in the [2Fe-2S] clusters assembly on the scaffolding protein ISCU. The core iron-sulfur cluster (ISC) assembly complex is involved in the de novo synthesis of a [2Fe-2S] cluster, the first step of the mitochondrial iron-sulfur protein biogenesis. This process is initiated by the cysteine desulfurase …

**Summary**, from NCBI Gene [57128](https://www.ncbi.nlm.nih.gov/gene/57128):

> The protein encoded by this gene is found in both mitochondria and the nucleus, where it binds cysteine desulfurase and helps free inorganic sulfur for Fe/S clusters. Disruption of this gene negatively impacts mitochondrial and cytosolic iron homeostasis. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:21365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21365) · Entrez [57128](https://www.ncbi.nlm.nih.gov/gene/57128) · UniProt [Q9HD34](https://www.uniprot.org/uniprotkb/Q9HD34) · Ensembl [ENSG00000214113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214113)

## Data

Gene col 13173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13173); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13173]; `tensor/DDL_lfc|DDL_z.npy` [13173]; `embed/gene_vectors.npy` [13173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13173 or target_col == 13173). Every well: [[LYRM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYRM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
