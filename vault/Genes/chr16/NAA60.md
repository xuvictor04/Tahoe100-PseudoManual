---
symbol: "NAA60"
type: "gene"
col: 4333
ensembl_id: "ENSG00000122390"
name: "N-alpha-acetyltransferase 60, NatF catalytic subunit"
location: "16p13.3"
module: 149
arm: "+"
pooled_cpm: 44.12
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# NAA60

*N-alpha-acetyltransferase 60, NatF catalytic subunit* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +13.9, q 4e-41, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.599× (z -12.5, q 7e-33, down in 35 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 0.0917×, A-172 0.208×, SK-MEL-2 0.217×, LoVo 0.310×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.183×, C-33 A 0.164×, SW48 0.159×, NCI-H1573 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (KATO III 0.194×, HT-29 0.322×, HEC-1-A 0.392×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.282×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QRICH1]] (+0.66, fdr 1e-05), [[FBXO28]] (+0.65, fdr 1e-05), [[ZCCHC10]] (+0.65, fdr 1e-05); moves opposite to [[SPTBN1]] (-0.59, fdr 3e-05), [[PHF6]] (-0.58, fdr 3e-05), [[NONO]] (-0.57, fdr 5e-05).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +13.9 | 4e-41 | 37/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +11.6 | 2e-28 | 42/49 (LS 180, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +10.2 | 4e-22 | 31/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +10.1 | 1e-21 | 30/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +9.9 | 6e-21 | 36/48 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +8.3 | 9e-15 | 30/48 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +8.3 | 1e-14 | 33/48 (HEC-1-A, SW48, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +7.8 | 3e-13 | 35/48 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +6.9 | 3e-10 | 27/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +6.2 | 4e-08 | 28/46 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +6.1 | 5e-08 | 27/48 (A-172, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +5.2 | 1e-05 | 21/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.4 | 5e-04 | 18/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.002 | 18/48 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.009 | 13/48 (LoVo, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.033 | 6/48 (SNU-423, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.050 | 5/48 (C32, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.09× | +3.0 | 0.066 | 3/48 (NCI-H2030, SNU-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.086 | 8/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4333.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 0.0917×, A-172 0.208×, SK-MEL-2 0.217×, LoVo 0.310×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.183×, C-33 A 0.164×, SW48 0.159×, NCI-H1573 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (KATO III 0.194×, HT-29 0.322×, HEC-1-A 0.392×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.282×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -12.5 | 7e-33 | 35/46 (KATO III, HT-29, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -10.7 | 2e-24 | 25/42 (LS 180, A-172, …) | two highest doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.896× | -3.8 | 0.033 | 10/48 (J82, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.859× | -3.6 | 0.054 | 16/48 (SNU-1, SNU-423, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.873× | -3.3 | 0.11 | 10/48 (A-172, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.876× | -3.2 | 0.13 | 16/48 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Pimozide (drug)]] 5 µM |  | 0.881× | -3.1 | 0.17 | 4/48 (KATO III, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.9 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 44.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.87× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -16.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 49.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.44× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.0917× (z -25.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 54.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -17.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 44.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.241× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[LoVo (line)]] | wt | 42.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -13.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 62.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -16.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 51.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 53.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.2) | — |
| [[SW48 (line)]] | wt | 44.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 81.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.404× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[SNU-423 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.7) | — |
| [[A498 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH1]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[FBXO28]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.65 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[IP6K1]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[AKAP8L]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[APPBP2]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZNF791]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SMIM27]] | +0.61 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[ZBTB8OS]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ALKBH4]] | +0.60 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[YTHDF2]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZNF200]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN1]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[PHF6]] | -0.58 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[NONO]] | -0.57 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[TTLL12]] | -0.54 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ANXA2]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[SSX2IP]] | -0.53 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[IMPDH2]] | -0.52 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[PDHA1]] | -0.51 | -0.29 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.8, 5.0); signed map (-3.9, -10.3). **Vector** length 93.4, 20.3% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +10.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +0.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.6 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.5 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 60, NatF catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,443,649-3,486,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14154, HAT4, NatF, hNaa60; previously NAT15 |
| Gene groups (HGNC) | Lysine acetyltransferases; N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7X0](https://www.uniprot.org/uniprotkb/Q9H7X0) (N-alpha-acetyltransferase 60):

> N-alpha-acetyltransferase that specifically mediates the acetylation of N-terminal residues of the transmembrane proteins, with a strong preference for N-termini facing the cytosol. Displays N-terminal acetyltransferase activity towards a range of N-terminal sequences including those starting with Met-Lys, Met-Val, Met-Ala and Met-Met. Required for normal chromosomal segregation during anaphase. May also show histone acetyltransferase activity; such results are however unclear in vivo and would …

**Summary**, from NCBI Gene [79903](https://www.ncbi.nlm.nih.gov/gene/79903):

> This gene encodes an enzyme that localizes to the Golgi apparatus, where it transfers an acetyl group to the N-terminus of free proteins. This enzyme acts on histones, and its activity is important for chromatin assembly and chromosome integrity. Alternative splicing and the use of alternative promoters results in multiple transcript variants. The upstream promoter is located in a differentially methylated region (DMR) and undergoes imprinting; transcript variants originating from this position …

**Accessions** — [HGNC:25875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25875) · Entrez [79903](https://www.ncbi.nlm.nih.gov/gene/79903) · UniProt [Q9H7X0](https://www.uniprot.org/uniprotkb/Q9H7X0) · Ensembl [ENSG00000122390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122390)

## Data

Gene col 4333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4333); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4333]; `tensor/DDL_lfc|DDL_z.npy` [4333]; `embed/gene_vectors.npy` [4333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4333 or target_col == 4333). Every well: [[NAA60 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA60.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
