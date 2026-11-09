---
symbol: "NPHP4"
type: "gene"
col: 5233
ensembl_id: "ENSG00000131697"
name: "nephrocystin 4"
location: "1p36.31"
module: 85
arm: "+"
pooled_cpm: 33.42
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# NPHP4

*nephrocystin 4* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.37× (z +17.2, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.477× (z -14.8, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1328]] (+0.71, fdr 1e-05), [[CHTF18]] (+0.67, fdr 1e-05), [[CEP131]] (+0.64, fdr 1e-04); moves opposite to [[MR1]] (-0.71, fdr 1e-05), [[ERCC6L2-AS1]] (-0.69, fdr 2e-04), [[HIKESHI]] (-0.67, fdr 2e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +17.2 | 0e+00 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +11.5 | 3e-28 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +11.2 | 1e-26 | 32/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.019 | 12/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.020 | 14/47 (LoVo, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains <1% of this change | **1.20×** | +3.7 | 0.022 | 15/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.071 | 3/48 (hTERT-HPNE, NCI-H23, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.11 | 7/47 (H4, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.17× | +3.1 | 0.13 | 12/48 (A-172, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.477×** | -14.8 | 0e+00 | 41/48 (A-427, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.508×** | -12.5 | 2e-33 | 33/42 (J82, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.540×** | -12.3 | 2e-32 | 33/47 (J82, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -12.1 | 1e-31 | 34/47 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -10.3 | 5e-23 | 22/35 (KATO III, J82, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.601×** | -10.1 | 3e-22 | 33/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.591×** | -10.1 | 5e-22 | 33/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.392×** | -9.8 | 1e-20 | 37/48 (HS-578T, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.709×** | -9.7 | 2e-20 | 33/48 (A498, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -8.1 | 3e-14 | 28/47 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.772×** | -7.3 | 2e-11 | 33/48 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.774×** | -7.2 | 3e-11 | 24/47 (HS-578T, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -6.4 | 7e-09 | 30/46 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -5.8 | 2e-07 | 28/48 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -5.8 | 2e-07 | 22/48 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.808×** | -4.3 | 7e-04 | 18/48 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.819×** | -4.0 | 0.002 | 15/48 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.720×** | -3.4 | 0.019 | 11/47 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.842× | -3.4 | 0.019 | 11/47 (LS 180, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.724×** | -3.4 | 0.020 | 16/48 (SNU-1, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.7 | 19 | 2 (2 ⚠) | [[Budesonide (drug)]] 0.5 µM 3.79× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 70.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -16.9) |
| [[PANC-1 (line)]] | alt | 35.2 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.76× (z +13.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -11.1) |
| [[HOP62 (line)]] | alt | 64.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.8) |
| [[A498 (line)]] | wt | 17.9 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 2.97× (z +8.5) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.369× (z -11.2) |
| [[C32 (line)]] | wt | 56.0 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.182× (z -13.9) |
| [[KATO III (line)]] | alt | 28.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -15.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 47.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -14.2) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.326× (z -9.4) |
| [[A549 (line)]] | wt | 30.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.393× (z -10.6) |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -10.5) |
| [[J82 (line)]] | alt | 51.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -18.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 20.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.04× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 38.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 43.3 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.287× (z -10.9) |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.313× (z -10.1) |
| [[SW1417 (line)]] | alt | 18.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.76× (z +11.9) | — |
| [[SW480 (line)]] | alt | 31.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +15.9) | — |
| [[A-427 (line)]] | wt | 34.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.181× (z -14.5) |
| [[H4 (line)]] | wt | 31.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -12.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 28.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.16× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 48.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -12.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.222× (z -9.7) |
| [[AN3 CA (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -10.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.359× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 20.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.344× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 13.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -12.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.201× (z -10.1) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1328]] | +0.71 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CHTF18]] | +0.67 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CEP131]] | +0.64 | +0.51 / +0.35 | both halves | 1e-04 | pathway: Anchoring of the basal body to the plasma membrane |
| [[TBCD]] | +0.63 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[IFT122]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 441 |
| [[WRN]] | +0.63 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[FN3KRP]] | +0.63 | +0.53 / +0.27 | both halves | 3e-04 |  |
| [[SFI1]] | +0.62 | +0.58 / +0.46 | both halves | 2e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[SIVA1]] | +0.62 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[GRK6]] | +0.62 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[SH2B2]] | +0.62 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[POLD2]] | +0.61 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MR1]] | -0.71 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[ERCC6L2-AS1]] | -0.69 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[HIKESHI]] | -0.67 | -0.66 / -0.30 | both halves | 2e-04 |  |
| [[ZNF407-AS1]] | -0.67 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[PATL2]] | -0.66 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.66 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[KRBA2]] | -0.65 | -0.67 / -0.27 | both halves | 3e-04 |  |
| [[FAM200A]] | -0.65 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[RNF6]] | -0.64 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[WAC-AS1]] | -0.64 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[MKLN1-AS]] | -0.64 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[METTL6]] | -0.64 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NPHP4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01836]] | B | LINC01836 activity lowers NPHP4's level | lines that do not express LINC01836 (16) vs lines expressing it (34) | 1.36× higher at baseline in the lines without LINC01836 | 0.047 | ⚠ within organs, on part of the lines; also absent: ANXA3, SLC9A2, SHROOM3 |
| [[HDAC6]] | B | HDAC6 activity lowers NPHP4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.5, 16.0); signed map (-48.6, -16.4). **Vector** length 103, 25.5% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +9.3 | +17.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.3 | +11.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.1 | +11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.4 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.5 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -12.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | nephrocystin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:5,862,811-5,992,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLSN4, KIAA0673, POC10 |
| Gene groups (HGNC) | NPHP complex |
| Reactome | 5 pathways, smallest: Signaling by Hippo; Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [O75161](https://www.uniprot.org/uniprotkb/O75161) (Nephrocystin-4):

> Involved in the organization of apical junctions; the function is proposed to implicate a NPHP1-4-8 module. Does not seem to be strictly required for ciliogenesis. Required for building functional cilia. Involved in the organization of the subapical actin network in multiciliated epithelial cells. Seems to recruit INT to basal bodies of motile cilia which subsequently interacts with actin-modifying proteins such as DAAM1 (By similarity). In cooperation with INVS may down-regulate the canonical …

**Summary**, from NCBI Gene [261734](https://www.ncbi.nlm.nih.gov/gene/261734):

> This gene encodes a protein involved in renal tubular development and function. This protein interacts with nephrocystin, and belongs to a multifunctional complex that is localized to actin- and microtubule-based structures. Mutations in this gene are associated with nephronophthisis type 4, a renal disease, and with Senior-Loken syndrome type 4, a combination of nephronophthisis and retinitis pigmentosa. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr …

**Accessions** — [HGNC:19104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19104) · Entrez [261734](https://www.ncbi.nlm.nih.gov/gene/261734) · UniProt [O75161](https://www.uniprot.org/uniprotkb/O75161) · Ensembl [ENSG00000131697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131697)

## Data

Gene col 5233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5233); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5233]; `tensor/DDL_lfc|DDL_z.npy` [5233]; `embed/gene_vectors.npy` [5233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5233 or target_col == 5233). Every well: [[NPHP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPHP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
