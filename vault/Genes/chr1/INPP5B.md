---
symbol: "INPP5B"
type: "gene"
col: 12810
ensembl_id: "ENSG00000204084"
name: "inositol polyphosphate-5-phosphatase B"
location: "1p34.3"
module: 30
arm: "+"
pooled_cpm: 33.22
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# INPP5B

*inositol polyphosphate-5-phosphatase B* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.17× (z +14.0, q 6e-42, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.384× (z -16.7, q 0e+00, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.494× (z -12.8, q 3e-35, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A6]] (+0.68, fdr 1e-05), [[SDHAP1]] (+0.67, fdr 7e-06), [[RNF41]] (+0.67, fdr 1e-05); moves opposite to [[HIVEP2]] (-0.67, fdr 1e-05), [[SKIL]] (-0.66, fdr 1e-05), [[LEKR1]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXCL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +14.0 | 6e-42 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +13.1 | 1e-36 | 38/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +11.1 | 4e-26 | 37/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +6.8 | 1e-09 | 33/48 (C-33 A, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.006 | 15/48 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.17× | +4.0 | 0.007 | 17/48 (C32, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.040 | 17/48 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.068 | 11/48 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.076 | 9/47 (NCI-H1792, AN3 CA, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.19× | +3.1 | 0.11 | 11/48 (SW480, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.38× | +3.0 | 0.12 | 9/47 (NCI-H2030, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 1.38× | +3.0 | 0.12 | 13/48 (SW1417, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.384×** | -16.7 | 0e+00 | 39/48 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.568×** | -14.5 | 3e-45 | 39/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.481×** | -13.3 | 4e-38 | 32/45 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -12.8 | 3e-35 | 40/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.566×** | -10.3 | 5e-23 | 36/48 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.597×** | -9.4 | 6e-19 | 31/46 (PANC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.635×** | -7.9 | 2e-13 | 23/38 (A498, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.628×** | -7.8 | 4e-13 | 26/43 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.681×** | -7.0 | 2e-10 | 30/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.711×** | -6.2 | 3e-08 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -5.5 | 2e-06 | 28/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.745×** | -5.4 | 4e-06 | 23/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -5.0 | 2e-05 | 24/48 (SW480, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.6 | 1e-04 | 22/48 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | **0.808×** | -3.9 | 0.004 | 18/46 (A-427, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.009 | 17/44 (SNU-423, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **0.817×** | -3.5 | 0.013 | 14/47 (SNU-1, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.086 | 13/47 (SNU-1, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.6 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -30.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.217× (z -18.0) |
| [[A498 (line)]] | wt | 55.8 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.400× (z -10.7) |
| [[C32 (line)]] | wt | 49.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.263× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 33.9 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 40.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.445× (z -8.7) |
| [[KATO III (line)]] | alt | 39.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[LoVo (line)]] | wt | 13.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.63× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.285× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 14.7 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.233× (z -11.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.336× (z -8.5) |
| [[SW480 (line)]] | alt | 41.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 33.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[COLO 205 (line)]] | alt | 42.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HOP62 (line)]] | alt | 16.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.59× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 39.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.5) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.370× (z -8.5) |
| [[J82 (line)]] | alt | 16.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +10.5) | — |
| [[A-427 (line)]] | wt | 42.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 38.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0489× (z -17.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.17× (z +9.7) | [[Homoharringtonine (drug)]] 0.05 µM 0.245× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0939× (z -9.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 25.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.2) ⚠ cell-cycle shift, explains ~56% of this change | [[Harringtonine (drug)]] 5 µM 0.236× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 35.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -13.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RPMI-7951 (line)]] | alt | 51.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 42.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0876× (z -12.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW48 (line)]] | wt | 46.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[AN3 CA (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 24.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.51× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[LOX-IMVI (line)]] | wt | 31.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 21.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | +0.68 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RNF41]] | +0.67 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CCZ1B]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MYPOP]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CDADC1]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.65 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MED23]] | +0.65 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CCZ1]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ALG9]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[CDK5RAP1]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2]] | -0.67 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[SKIL]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.66 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.64 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ST7L]] | -0.62 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[ARAP2]] | -0.62 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[LIG4]] | -0.61 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[TUG1]] | -0.61 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R1C]] | -0.60 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ZC3H11A]] | -0.60 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[ZNF702P]] | -0.60 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ZBED5]] | -0.59 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL1]] | B | CXCL1 activity lowers INPP5B's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 1.34× higher at baseline in the lines without CXCL1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[HDAC6]] | B | HDAC6 activity lowers INPP5B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.0, -14.1); signed map (-37.1, -0.0). **Vector** length 97.7, 24.0% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +11.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.3 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.4 | -16.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -6.9 | -14.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.8 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-5-phosphatase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,860,697-37,947,053 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 3 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P32019](https://www.uniprot.org/uniprotkb/P32019) (Type II inositol 1,4,5-trisphosphate 5-phosphatase):

> Regulates phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) cellular levels by cleaving the phosphate at the 5-position producing PtdIns(4)P. Also hydrolyzes the 5-position phosphate from inositol 1,4,5-trisphosphate (Ins(1,4,5)P3), thereby modulating cellular signaling events.

**Summary**, from NCBI Gene [3633](https://www.ncbi.nlm.nih.gov/gene/3633):

> This gene encodes a member of a family of inositol polyphosphate-5-phosphatases. These enzymes function in the regulation of calcium signaling by inactivating inositol phosphates. The encoded protein is localized to the cytosol and mitochondria, and associates with membranes through an isoprenyl modification near the C-terminus. Alternatively spliced transcript variants of this gene have been described. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:6077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6077) · Entrez [3633](https://www.ncbi.nlm.nih.gov/gene/3633) · UniProt [P32019](https://www.uniprot.org/uniprotkb/P32019) · Ensembl [ENSG00000204084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204084)

## Data

Gene col 12810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12810); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12810]; `tensor/DDL_lfc|DDL_z.npy` [12810]; `embed/gene_vectors.npy` [12810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12810 or target_col == 12810). Every well: [[INPP5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
