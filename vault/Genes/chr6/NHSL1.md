---
symbol: "NHSL1"
type: "gene"
col: 5722
ensembl_id: "ENSG00000135540"
name: "NHS like 1"
location: "6q24.1"
module: 92
arm: "+"
pooled_cpm: 183.62
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 45
n_dd_up_clean: 3
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# NHSL1

*NHS like 1* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +10.9, q 8e-25, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.221× (z -28.0, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4-AS1]] (+0.69, fdr 7e-06), [[E2F3]] (+0.66, fdr 1e-05), [[NPAS2]] (+0.65, fdr 7e-06); moves opposite to [[MAPK3]] (-0.55, fdr 1e-04), [[POT1-AS1]] (-0.53, fdr 1e-05), [[TUFT1]] (-0.53, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +10.9 | 8e-25 | 28/48 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +10.0 | 6e-21 | 34/47 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.4 | 3e-08 | 30/49 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.1 | 5e-05 | 31/47 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +4.8 | 2e-04 | 25/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.022 | 19/47 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[Dabrafenib (drug)]] 5 µM |  | 1.46× | +3.2 | 0.11 | 15/48 (MIA PaCa-2, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.21× | +3.0 | 0.17 | 20/47 (HEC-1-A, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.221×** | -28.0 | 0e+00 | 47/47 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.232×** | -27.1 | 0e+00 | 47/47 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.283×** | -23.4 | 0e+00 | 47/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -14.0 | 2e-42 | 35/42 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.532×** | -10.8 | 4e-25 | 31/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.569×** | -10.4 | 2e-23 | 38/47 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.559×** | -9.3 | 9e-19 | 35/48 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.609×** | -9.2 | 3e-18 | 40/47 (C32, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -8.0 | 9e-14 | 27/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.652×** | -7.9 | 1e-13 | 31/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -7.4 | 9e-12 | 27/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.754×** | -7.1 | 4e-11 | 26/47 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.683×** | -7.0 | 1e-10 | 35/47 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.690×** | -6.9 | 3e-10 | 36/47 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.754×** | -6.8 | 5e-10 | 29/47 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.706×** | -6.7 | 9e-10 | 31/49 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.695×** | -5.8 | 2e-07 | 31/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.727×** | -5.7 | 4e-07 | 34/47 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -5.6 | 5e-07 | 31/47 (A-427, C32, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.757×** | -5.1 | 7e-06 | 27/47 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -5.0 | 1e-05 | 27/47 (NCI-H460, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.557×** | -4.9 | 2e-05 | 32/48 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 334 | 0 | 28 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0867× (z -23.2) |
| [[C32 (line)]] | wt | 613 | 0 | 23 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -26.5) |
| [[A-427 (line)]] | wt | 627 | 0 | 19 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 236 | 0 | 19 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.380× (z -27.1) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.0605× (z -23.6) |
| [[LOX-IMVI (line)]] | wt | 203 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 370 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -14.8) |
| [[HT-29 (line)]] | alt | 147 | 3 (2 ⚠) | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.155× (z -22.4) |
| [[LoVo (line)]] | wt | 196 | 1 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.126× (z -26.7) |
| [[LS 180 (line)]] | wt | 228 | 2 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.192× (z -19.6) |
| [[PANC-1 (line)]] | alt | 276 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -21.6) |
| [[HS-578T (line)]] | alt | 79.3 | 3 | 4 | [[Clobetasol propionate (drug)]] 5 µM 3.04× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.166× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 277 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0822× (z -25.3) |
| [[SK-MEL-2 (line)]] | alt | 210 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -20.8) |
| [[SW1417 (line)]] | alt | 301 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -20.4) |
| [[SW48 (line)]] | wt | 217 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -15.9) |
| [[SW480 (line)]] | alt | 291 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -20.7) |
| [[A498 (line)]] | wt | 85.6 | 3 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 70.5 | 3 (2 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.54× (z +9.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -19.4) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 68.0 | 3 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.184× (z -16.9) |
| [[A549 (line)]] | wt | 148 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -16.3) |
| [[COLO 205 (line)]] | alt | 89.4 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.9) ⚠ cell-cycle shift, explains ~81% of this change | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 66.3 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.308× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -16.2) |
| [[KATO III (line)]] | alt | 252 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -18.6) |
| [[RKO (line)]] | wt | 86.5 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.174× (z -14.3) |
| [[C-33 A (line)]] | alt | 93.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.217× (z -14.1) |
| [[HOP62 (line)]] | alt | 98.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -18.9) |
| [[Hs 766T (line)]] | wt | 98.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -16.0) |
| [[J82 (line)]] | alt | 91.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -19.1) |
| [[A-172 (line)]] | wt | 88.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -15.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H2347 (line)]] | alt | 64.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -14.0) |
| [[SHP-77 (line)]] | alt | 93.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -14.2) |
| [[SW 900 (line)]] | alt | 115 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -14.9) |
| [[BT-474 (line)]] | alt | 85.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 47.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -8.5) |
| [[H4 (line)]] | wt | 75.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 305 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 76.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -9.4) |
| [[SNU-1 (line)]] | wt | 55.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +11.1) | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0921× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.102× (z -9.5) |
| [[AN3 CA (line)]] | alt | 131 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -9.3) |
| [[HCT15 (line)]] | alt | 95.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 459 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -8.6) |
| [[SNU-423 (line)]] | alt | 56.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 33.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4-AS1]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[E2F3]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.65 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SIPA1L1]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[POC1B]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PITPNC1]] | +0.60 | +0.62 / +0.64 | both halves | 7e-06 | same gene group |
| [[B4GALT6]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GNG12-AS1]] | +0.58 | +0.43 / +0.49 | both halves | 4e-05 |  |
| [[NHSL1-AS1]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PRDM5]] | +0.57 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PYCR2]] | +0.57 | +0.40 / +0.46 | both halves | 5e-05 | same gene group |
| [[MSANTD2]] | +0.56 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK3]] | -0.55 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[POT1-AS1]] | -0.53 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[TUFT1]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 | same gene group |
| [[PLD3]] | -0.52 | -0.39 / -0.45 | both halves | 5e-05 | same gene group |
| [[PKIG]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[KIAA1522]] | -0.51 | -0.39 / -0.45 | both halves | 6e-05 | same gene group; STRING 585 |
| [[OSBPL9]] | -0.51 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[TOM1]] | -0.50 | -0.54 / -0.46 | both halves | 3e-05 | same gene group |
| [[GBP2]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CLIP3]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[THEMIS2]] | -0.50 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[RHOB]] | -0.50 | -0.47 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NHSL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[STAMBPL1]] | B | STAMBPL1 activity lowers NHSL1's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 1.67× higher at baseline in the lines without STAMBPL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[NHSL1-AS1]] | B | NHSL1-AS1 activity raises NHSL1's level | lines that do not express NHSL1-AS1 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without NHSL1-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: DLX2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, -7.9); signed map (13.4, 21.8). **Vector** length 135, 46.1% of its response variance represented; |z| ≥ 3 in 1,734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.6 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.8 | -6.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.7 | -7.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.6 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.5 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.5 | -5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.3 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | NHS like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:138,422,043-138,692,571 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA43P8.1, KIAA1357; previously C6orf63 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; NHS family |
| Matched by | ensembl_id |

UniProt [Q5SYE7](https://www.uniprot.org/uniprotkb/Q5SYE7) carries no function annotation.

**Summary**, from NCBI Gene [57224](https://www.ncbi.nlm.nih.gov/gene/57224):

> Predicted to be involved in cell differentiation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21021) · Entrez [57224](https://www.ncbi.nlm.nih.gov/gene/57224) · UniProt [Q5SYE7](https://www.uniprot.org/uniprotkb/Q5SYE7) · Ensembl [ENSG00000135540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135540)

## Data

Gene col 5722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5722); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5722]; `tensor/DDL_lfc|DDL_z.npy` [5722]; `embed/gene_vectors.npy` [5722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5722 or target_col == 5722). Every well: [[NHSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
