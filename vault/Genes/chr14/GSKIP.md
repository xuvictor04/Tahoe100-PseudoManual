---
symbol: "GSKIP"
type: "gene"
col: 2017
ensembl_id: "ENSG00000100744"
name: "GSK3B interacting protein"
location: "14q32.2"
module: 34
arm: "+"
pooled_cpm: 20.83
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# GSKIP

*GSK3B interacting protein* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.25× (z +31.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.709× (z -7.1, q 5e-10, down in 24 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.826× (z -4.1, q 0.005, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.242×, Panc 03.27 0.191×, LOX-IMVI 0.151×, LoVo 0.286×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H2030 0.109×, A549 0.121×, LS 180 0.301×, SW48 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.106×, LS 180 0.290×, LoVo 0.332×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35E4]] (+0.53, fdr 4e-05), [[CTTNBP2NL]] (+0.53, fdr 9e-05), [[AGPAT2]] (+0.53, fdr 1e-03, ⚠ one half only (not replicated)), [[ALAS1]] (+0.51, fdr 1e-04); moves opposite to [[ANKRD18CP]] (-0.51, fdr 1e-04), [[RBBP4]] (-0.48, fdr 1e-04), [[CCNL2]] (-0.48, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SGPP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.25×** | +31.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.03×** | +30.0 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.75×** | +28.4 | 0e+00 | 46/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +22.1 | 0e+00 | 40/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +20.6 | 0e+00 | 39/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +13.7 | 1e-40 | 41/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +12.7 | 6e-35 | 33/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +12.3 | 4e-33 | 28/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +11.0 | 2e-26 | 35/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +10.9 | 7e-26 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +8.1 | 2e-14 | 19/48 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.5 | 2e-12 | 24/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +7.2 | 3e-11 | 26/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +6.7 | 8e-10 | 21/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +6.3 | 1e-08 | 19/42 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +4.8 | 6e-05 | 15/47 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2017.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.242×, Panc 03.27 0.191×, LOX-IMVI 0.151×, LoVo 0.286×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H2030 0.109×, A549 0.121×, LS 180 0.301×, SW48 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.106×, LS 180 0.290×, LoVo 0.332×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -7.1 | 5e-10 | 24/33 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.765×** | -5.8 | 2e-06 | 16/38 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.804×** | -4.7 | 4e-04 | 18/46 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.826×** | -4.1 | 0.005 | 14/48 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.823×** | -3.9 | 0.011 | 17/36 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.4 | 0.061 | 11/47 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.063 | 9/43 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.7 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +18.5) | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.83× (z +17.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +14.2) | — |
| [[A549 (line)]] | wt | 16.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.73× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -13.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.68× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.85× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.47× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.52× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 27.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.48× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 27.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.83× (z +11.4) | — |
| [[A-172 (line)]] | wt | 12.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.14× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -13.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 9.17 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.29× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 31.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.2) | — |
| [[J82 (line)]] | alt | 14.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.55× (z +10.0) | — |
| [[LoVo (line)]] | wt | 66.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 51.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 21.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.11× (z +13.4) | — |
| [[RKO (line)]] | wt | 18.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.98× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 11.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +9.2) | — |
| [[SW48 (line)]] | wt | 38.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.24× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 29.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.80× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 15.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.49× (z +9.6) | — |
| [[KATO III (line)]] | alt | 28.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 10.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 19.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.78× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 18.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +9.0) | — |
| [[H4 (line)]] | wt | 10.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.3× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 12.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.51× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 24.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35E4]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[CTTNBP2NL]] | +0.53 | +0.42 / +0.37 | both halves | 9e-05 |  |
| [[AGPAT2]] | +0.53 | +0.18 / +0.52 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ALAS1]] | +0.51 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[MRPL10]] | +0.49 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[FA2H]] | +0.49 | +0.24 / +0.46 | both halves | 4e-04 |  |
| [[SERPINB1]] | +0.49 | +0.24 / +0.46 | both halves | 5e-04 |  |
| [[SLC45A4]] | +0.48 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[ETV3]] | +0.48 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[H3-3B]] | +0.48 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[BCL10]] | +0.48 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[CDKN2AIP]] | +0.48 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.47 | +0.25 / +0.45 | both halves | 4e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18CP]] | -0.51 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[RBBP4]] | -0.48 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[CCNL2]] | -0.48 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[PAXBP1]] | -0.47 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[GTF2I]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[LUC7L2]] | -0.46 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[MRPS25]] | -0.44 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[SNX5]] | -0.43 | -0.19 / -0.34 | ⚠ not reproduced | 9e-04 |  |
| [[STRN3]] | -0.43 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[LINC01341]] | -0.42 | -0.21 / -0.36 | both halves | 7e-04 |  |
| [[EIF2D]] | -0.42 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[SLC16A4-AS1]] | -0.42 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[MED24]] | -0.42 | -0.26 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGPP2]] | B | SGPP2 activity raises GSKIP's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 1.67× lower at baseline in the lines without SGPP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[KIAA0040]] | B | KIAA0040 activity raises GSKIP's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 1.52× lower at baseline in the lines without KIAA0040 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[DSG4]] | B | DSG4 activity raises GSKIP's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 1.99× lower at baseline in the lines without DSG4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[NECTIN1]] | B | NECTIN1 activity raises GSKIP's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without NECTIN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[HEPH]] | B | HEPH activity raises GSKIP's level | lines that do not express HEPH (41) vs lines expressing it (9) | 1.63× lower at baseline in the lines without HEPH | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[LGALS1]] | B | LGALS1 activity lowers GSKIP's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 1.54× higher at baseline in the lines without LGALS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[FA2H]] | B | FA2H activity raises GSKIP's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.58× lower at baseline in the lines without FA2H | 0.099 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.345). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.5, 30.5); signed map (-14.4, 39.6). **Vector** length 75.6, 14.9% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +22.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +31.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +7.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | GSK3B interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:96,363,452-96,387,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf129 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0R6](https://www.uniprot.org/uniprotkb/Q9P0R6) (GSK3B-interacting protein):

> A-kinase anchoring protein for GSK3B and PKA that regulates or facilitates their kinase activity towards their targets. The ternary complex enhances Wnt-induced signaling by facilitating the GSK3B- and PKA-induced phosphorylation of beta-catenin leading to beta-catenin degradation and stabilization respectively. Upon cAMP activation, the ternary complex contributes to neuroprotection against oxidative stress-induced apoptosis by facilitating the PKA-induced phosphorylation of DML1 and …

**Summary**, from NCBI Gene [51527](https://www.ncbi.nlm.nih.gov/gene/51527):

> This gene encodes a protein that is involved as a negative regulator of GSK3-beta in the Wnt signaling pathway. The encoded protein may play a role in the retinoic acid signaling pathway by regulating the functional interactions between GSK3-beta, beta-catenin and cyclin D1, and it regulates the beta-catenin/N-cadherin pool. The encoded protein contains a GSK3-beta interacting domain (GID) in its C-terminus, which is similar to the GID of Axin. The protein also contains an evolutionarily …

**Accessions** — [HGNC:20343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20343) · Entrez [51527](https://www.ncbi.nlm.nih.gov/gene/51527) · UniProt [Q9P0R6](https://www.uniprot.org/uniprotkb/Q9P0R6) · Ensembl [ENSG00000100744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100744)

## Data

Gene col 2017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2017); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2017]; `tensor/DDL_lfc|DDL_z.npy` [2017]; `embed/gene_vectors.npy` [2017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2017 or target_col == 2017). Every well: [[GSKIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSKIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
